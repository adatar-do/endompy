"""Local ENHOGAR 2018/2022 contracts with edition-specific questionnaire codes."""
from contextvars import ContextVar
from numbers import Real
from pathlib import Path
import json
import numpy as np
import pandas as pd

_edition_option = ContextVar('ENHOGAR_EDITION', default=None)


def _table(tbl):
    if not isinstance(tbl, pd.DataFrame):
        raise TypeError('tbl must be a local pandas DataFrame')
    if not tbl.columns.is_unique or any(not isinstance(n,str) or not n for n in tbl.columns):
        raise ValueError('Column names must be unique and nonempty strings')
    return tbl


def _numeric(tbl, name, codes=None):
    if name not in tbl.columns:
        raise ValueError('Missing required column: '+name)
    x = tbl[name]
    if (not pd.api.types.is_numeric_dtype(x.dtype) or pd.api.types.is_bool_dtype(x.dtype)) and not x.isna().all():
        raise TypeError(name+' must contain numeric codes')
    values = x.to_numpy(dtype=float,na_value=np.nan)
    valid = ~np.isnan(values)
    if not np.all(np.isfinite(values[valid])) or not np.all(values[valid] == np.floor(values[valid])):
        raise ValueError(name+' must contain finite integer codes')
    if codes is not None and not np.isin(values[valid],codes).all():
        raise ValueError('Unsupported codes in '+name)
    return pd.Series(values,index=tbl.index)


def _year(year):
    if isinstance(year,bool) or not isinstance(year,Real) or year not in (2018,2022):
        raise ValueError('Supported ENHOGAR editions: 2018 and 2022')
    return int(year)


_SCHEMAS=json.loads((Path(__file__).parent/'resources/editions.json').read_text(encoding='utf-8'))


def _schema(edition): return _SCHEMAS[str(_year(edition))]


def _evidence(tbl):
    _table(tbl)
    old=any(n in tbl for n in ['H203']+['H50'+str(i) for i in range(1,8)])
    new=any(n in tbl for n in ['P203']+['P50'+str(i) for i in range(1,9)])
    if old and new: raise ValueError('Mixed questionnaire columns from 2018 and 2022')
    if old: return 2018
    if new: return 2022
    if 'HANO' in tbl and len(tbl):
        years=_numeric(tbl,'HANO')
        if years.isna().any(): raise ValueError('HANO contains missing interview years')
        if years.eq(2018).all(): return 2018
        if years.isin([2021,2022]).all() and years.eq(2022).any(): return 2022
        if not years.eq(2021).all(): raise ValueError('HANO conflicts with supported survey editions')
    return None


def _edition(tbl=None,edition=None):
    observed=_evidence(tbl) if tbl is not None else None
    configured=_edition_option.get()
    requested=_year(edition) if edition is not None else _year(configured) if configured is not None else None
    if requested is not None and observed is not None and requested != observed:
        raise ValueError('Conflicting survey edition and questionnaire columns')
    selected=requested if requested is not None else observed if observed is not None else 2018
    if tbl is not None and 'HANO' in tbl and len(tbl):
        years=_numeric(tbl,'HANO')
        if requested is None and observed is None:
            raise ValueError('Interview year alone is ambiguous; specify edition')
        if years.isna().any() or not years.isin(_schema(selected)['interview_years']).all():
            raise ValueError('HANO contains missing or incompatible interview years')
    return selected


def enhogar_edition(year):
    """Set the context-local edition, or reset with None. Return the previous value."""
    value = None if year is None else _year(year)
    old = _edition_option.get(); _edition_option.set(value)
    return old


def get_enhogar_edition(tbl=None):
    """Resolve edition without changing configuration; supports 2018 and 2022."""
    return _edition(tbl)


def guess_enhogar_edition(tbl):
    """Infer 2018/2022 from questionnaire columns or unambiguous interview years."""
    observed=_evidence(tbl)
    if observed is None: raise ValueError('Cannot infer edition; supply questionnaire columns or specify edition')
    return _edition(tbl,observed)


def enhogar_example(edition=2018):
    """Return 12 invented cases for 2018 or 2022; never use for population estimates."""
    _year(edition)
    file='synthetic.json' if edition==2018 else 'synthetic-2022.json'
    return pd.DataFrame(json.loads((Path(__file__).parent/'resources'/file).read_text(encoding='utf-8')))


def _response(tbl,name,edition):
    schema=_schema(edition)
    x=_numeric(tbl,name,schema['response_codes']).astype('Float64')
    x=x.mask(x.isin(schema['response_missing']),pd.NA)
    return x.eq(1)


def _mask(value,pet):
    return value.astype('boolean').where(pet.eq(1).fillna(False),pd.NA).astype('Int64')


def pet(tbl,min_edad=15,max_edad=float('inf'),edition=None):
    """Compute PET: H203=99 is missing in 2018; P203=99 is a valid age in 2022."""
    _table(tbl); edition=_edition(tbl,edition)
    if isinstance(min_edad,bool) or not isinstance(min_edad,Real) or not np.isfinite(min_edad) or min_edad < 10 or min_edad != np.floor(min_edad):
        raise ValueError('min_edad must be an integer of at least 10')
    if isinstance(max_edad,bool) or not isinstance(max_edad,Real) or np.isnan(max_edad) or max_edad < min_edad or max_edad != np.floor(max_edad):
        raise ValueError('max_edad must be an integer >= min_edad or Inf')
    schema=_schema(edition)
    age = _numeric(tbl,schema['age'],range(121)).astype('Float64')
    age = age.mask(age.isin(schema['age_missing']),pd.NA)
    out=tbl.copy(deep=True); out['pet']=(age.ge(min_edad)&age.le(max_edad)).astype('Int64')
    return out


def ocupado(tbl,min_edad=15,max_edad=float('inf'),edition=None):
    """Any affirmative employment answer establishes occupation: H501:H506 or P501:P506."""
    edition=_edition(tbl,edition)
    out=pet(tbl,min_edad,max_edad,edition)
    columns=_schema(edition)['employed']
    value=_response(out,columns[0],edition)
    for name in columns[1:]: value=value|_response(out,name,edition)
    out['ocupado']=_mask(value,out['pet']); return out


def desocupado(tbl,min_edad=15,max_edad=float('inf'),edition=None):
    """Known nonworkers with H507=1 (2018 proxy) or P508=1 (2022 four-week search)."""
    edition=_edition(tbl,edition)
    out=ocupado(tbl,min_edad,max_edad,edition)
    out['desocupado']=_mask(out['ocupado'].eq(0)&_response(out,_schema(edition)['search'],edition),out['pet']); return out


def pea(tbl,min_edad=15,max_edad=float('inf'),edition=None):
    """Union of employment and edition-specific unemployment, preserving unknowns."""
    out=desocupado(tbl,min_edad,max_edad,edition)
    out['pea']=_mask(out['ocupado'].eq(1)|out['desocupado'].eq(1),out['pet']); return out


def inactivo(tbl,min_edad=15,max_edad=float('inf'),edition=None):
    """Complement of known labour force, restricted to working-age population."""
    edition=_edition(tbl,edition)
    out=pea(tbl,min_edad,max_edad,edition)
    out['inactivo']=_mask(out['pea'].eq(0),out['pet']); return out


def fuerza_trabajo_potencial(tbl,min_edad=15,max_edad=float('inf'),edition=None):
    """Availability proxy outside PEA: H509/H510 in 2018 or P510/P511 in 2022."""
    edition=_edition(tbl,edition)
    out=pea(tbl,min_edad,max_edad,edition)
    out['fuerza_trabajo_potencial']=_mask(out['pea'].eq(0)&(_response(out,_schema(edition)['available_offer'],edition)|_response(out,_schema(edition)['available_now'],edition)),out['pet'])
    return out
