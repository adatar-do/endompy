"""Local-table, semester and structure contracts for the traditional ENFT."""
import numbers
import re
import numpy as np
import pandas as pd


def _require(tbl, columns=()):
    if not isinstance(tbl, pd.DataFrame): raise TypeError('A local pandas DataFrame is required.')
    if tbl.columns.has_duplicates or any(not isinstance(c, str) or not c for c in tbl.columns):
        raise ValueError('Column names must be unique, nonempty strings.')
    missing = [c for c in columns if c not in tbl]
    if missing: raise ValueError('Missing required columns: '+', '.join(missing))


def version(tbl):
    """Identify column structure: 1 PERIALFA, 2 EFT_PERIODO; reject ambiguity.

    This is not a questionnaire revision or a poverty methodology selector.
    """
    _require(tbl)
    cols = [c for c in ('PERIALFA','EFT_PERIODO') if c in tbl]
    if len(cols) != 1: raise ValueError('Exactly one period column, PERIALFA or EFT_PERIODO, is required.')
    return 1 if cols[0] == 'PERIALFA' else 2


def _parts(tbl):
    column = 'PERIALFA' if version(tbl) == 1 else 'EFT_PERIODO'
    years, semesters = [], []
    for v in tbl[column]:
        if pd.isna(v) or isinstance(v, (bool, np.bool_)): raise ValueError('Invalid period; expected S/YYYY, YYYY/S or YYYYS.')
        if isinstance(v, numbers.Real) and np.isfinite(v) and v == int(v): v = str(int(v))
        text = re.sub(r'\s+', '', str(v)).strip("'\"")
        first, last, code = re.fullmatch(r'([12])/([0-9]{4})',text), re.fullmatch(r'([0-9]{4})/([12])',text), re.fullmatch(r'([0-9]{4})([12])',text)
        if first: semester, year = map(int,first.groups())
        elif last or code: year, semester = map(int,(last or code).groups())
        else: raise ValueError('Invalid period; expected S/YYYY, YYYY/S or YYYYS.')
        if year < 1000: raise ValueError('Year must contain four digits.')
        years.append(year); semesters.append(semester)
    return column, np.array(years,dtype=int), np.array(semesters,dtype=int)


def peri_vars(tbl, rm=False, ano=True, semestre=True, periodo=True):
    """Add requested year, semester and YYYYS columns without altering other columns."""
    if any(not isinstance(v, (bool,np.bool_)) for v in (rm,ano,semestre,periodo)): raise ValueError('Flags must be bool.')
    column, year, half = _parts(tbl)
    out = tbl.copy(deep=True)
    if ano: out['ano'] = year
    if semestre: out['semestre'] = half
    if periodo: out['periodo'] = year*10+half
    if rm: out = out.drop(columns=[column])
    return out


def zona(tbl):
    """Map ENFT zone codes 0/1 to zona 1/2, preserving missing values."""
    column = 'S1_P4' if version(tbl) == 1 else 'EFT_ZONA'
    _numeric(tbl,[column])
    if (~tbl[column].dropna().isin([0,1])).any(): raise ValueError('Zone must use numeric 0/1 or missing.')
    out = tbl.copy(deep=True); out['zona'] = tbl[column]+1
    return out


def _numeric(tbl, columns):
    _require(tbl,columns)
    for c in columns:
        if not pd.api.types.is_numeric_dtype(tbl[c]) or pd.api.types.is_bool_dtype(tbl[c]) or np.isinf(tbl[c].dropna()).any():
            raise ValueError('Finite numbers or missing values required: '+c)


def _age(value):
    if isinstance(value,bool) or not isinstance(value,numbers.Real) or not np.isfinite(value) or value < 0 or value != int(value):
        raise ValueError('min_edad must be a nonnegative integer.')
