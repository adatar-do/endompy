"""Education and household indicators, preserving explicit survey universes."""
import numpy as np
import pandas as pd

from .core import require_columns, quarter_parts
from .rules import case_when, _column


def _age_range(min_edad, max_edad):
    if not np.isscalar(min_edad) or not np.isscalar(max_edad) or pd.isna(min_edad) or pd.isna(max_edad) or min_edad > max_edad:
        raise ValueError("Minimum age cannot exceed maximum age.")


def _cut(values, breaks, labels):
    if callable(breaks):
        breaks = breaks(values)
    return pd.cut(values.astype(float), bins=breaks, labels=labels, right=True)


def alfabetizacion(tbl, min_edad=0, max_edad=np.inf):
    """Literacy (1/0) within the inclusive age range; outside the range is missing."""
    require_columns(tbl, ["EDAD", "SABE_LEER_ESCRIBIR"])
    _age_range(min_edad, max_edad)
    df = tbl.copy()
    eligible = _column(df, "EDAD").between(min_edad, max_edad)
    df["alfabetizacion"] = case_when(df, [(eligible & _column(df, "SABE_LEER_ESCRIBIR").eq(1), 1), (eligible, 0)])
    return df


def anos_educacion(tbl, breaks=None, labels=None, secundaria_base="armonizada_6_6", anio_corte=2022):
    """Years completed under harmonized 6+6, legacy 8+4, or year-specific schooling.

    secundaria_base is armonizada_6_6, legacy_8_4 or historica_por_ano.
    The historical option requires ANO and changes the secondary offset at anio_corte.
    """
    require_columns(tbl, ["NIVEL_ULTIMO_ANO_APROBADO", "ULTIMO_ANO_APROBADO"])
    if secundaria_base not in ("armonizada_6_6", "legacy_8_4", "historica_por_ano"):
        raise ValueError("Unknown secundaria_base.")
    df = tbl.copy()
    level, grade = _column(df, "NIVEL_ULTIMO_ANO_APROBADO"), np.trunc(_column(df, "ULTIMO_ANO_APROBADO"))
    offset = 8 if secundaria_base == "legacy_8_4" else 6
    if secundaria_base == "historica_por_ano":
        year = _column(df, "ANO")
        offset = pd.Series(np.where(year.ge(anio_corte).fillna(False), 6, 8), index=df.index).mask(year.isna())
    df["anos_educacion"] = case_when(df, [(level.isin([0, 1, 9, 10]), 0),
        (level.eq(2), grade), (level.isin([3, 4]), offset + grade),
        (level.eq(5), 12 + grade), (level.isin([6, 7, 8]), 16 + grade)])
    if breaks is not None:
        df["anos_educacion"] = _cut(df["anos_educacion"], breaks, labels)
    return df


def _school(tbl, min_edad, max_edad, summer_fix, attendance):
    source = "TANDA_ASISTE" if attendance else "NIVEL_SE_MATRICULO"
    require_columns(tbl, ["EDAD", source, "MES", "PORQUE_NO_ESTUDIA"])
    _age_range(min_edad, max_edad)
    df = tbl.copy()
    eligible = _column(df, "EDAD").between(min_edad, max_edad)
    enrolled = _column(df, source).ne(7) if attendance else _column(df, source).between(1, 8)
    waiting = _column(df, "MES").between(6, 8) & _column(df, "PORQUE_NO_ESTUDIA").eq(1)
    df["asistencia_escolar" if attendance else "matriculacion_escolar"] = case_when(df,
        [(eligible & enrolled, 1), (eligible & waiting, 1 if summer_fix else 0), (eligible, 0)])
    return df


def matriculacion_escolar(tbl, min_edad=6, max_edad=17, summer_fix=False):
    """Enrollment for the selected ages; optionally include summer waiting periods."""
    return _school(tbl, min_edad, max_edad, summer_fix, attendance=False)


def asistencia_escolar(tbl, min_edad=6, max_edad=17, summer_fix=False):
    """Attendance for the selected ages; optionally include summer waiting periods."""
    return _school(tbl, min_edad, max_edad, summer_fix, attendance=True)


def sobreedad_escolar(tbl, nrezagos=2):
    """Overage among students in levels 2 to 4 using completed schooling plus six."""
    df = anos_educacion(tbl)
    eligible = _column(df, "NIVEL_SE_MATRICULO").between(2, 4)
    df["sobreedad_escolar"] = case_when(df, [(eligible & (_column(df, "EDAD") >= df["anos_educacion"] + 6 + nrezagos), 1), (eligible, 0)])
    return df


def trabajo_infantil(tbl, summer_fix=False):
    """Four work/attendance groups among ages 5–14; outside the universe is missing."""
    df = asistencia_escolar(tbl, min_edad=5, max_edad=14, summer_fix=summer_fix)
    eligible, occupied = _column(df, "EDAD").between(5, 14), _column(df, "OCUPADO")
    school = df["asistencia_escolar"]
    df["trabajo_infantil"] = case_when(df, [(eligible & occupied.eq(1) & school.eq(1), 1),
        (eligible & occupied.eq(1), 2), (eligible & school.eq(1), 3),
        (eligible & occupied.eq(0) & school.eq(0), 4)])
    return df


def grupos_edad(tbl, breaks=10, labels=None):
    """Group age using right-closed intervals, matching R cut boundaries."""
    require_columns(tbl, ["EDAD"])
    df = tbl.copy()
    df["grupos_edad"] = _cut(df["EDAD"], breaks, labels)
    return df


def _household_keys(df, dwelling=False):
    keys = ["TRIMESTRE", "VIVIENDA"] + ([] if dwelling else ["HOGAR"])
    if "ANO" in df:
        keys.insert(0, "ANO")
    require_columns(df, keys)
    if df[keys].isna().any().any():
        raise ValueError("Household and period identifiers cannot be missing.")
    return keys


def tasa_alfabetizacion_hogar(tbl, min_edad=0, max_edad=np.inf):
    """Percentage literate among eligible household members; no denominator gives NA."""
    df = alfabetizacion(tbl, min_edad, max_edad)
    keys = _household_keys(df)
    grouping = [df[key] for key in keys]
    yes = df["alfabetizacion"].eq(1).groupby(grouping, sort=False).transform("sum")
    total = df["alfabetizacion"].notna().groupby(grouping, sort=False).transform("sum")
    df["tasa_alfabetizacion_hogar"] = (yes / total * 100).where(total > 0)
    return df.drop(columns="alfabetizacion")


def tasa_dependencia(tbl, min_edad=15, max_edad=64, limit="both", breaks=None, labels=None):
    """Dependents per 100 working-age members; households with none return NA."""
    _age_range(min_edad, max_edad)
    limit = {"a": "above", "b": "below"}.get(limit, limit)
    if limit not in ("both", "above", "below"):
        raise ValueError("limit must be both, above or below.")
    df = tbl.copy()
    keys = _household_keys(df)
    age = _column(df, "EDAD")
    independent = age.between(min_edad, max_edad)
    dependent = ~age.between(min_edad if limit != "above" else -np.inf, max_edad if limit != "below" else np.inf)
    grouping = [df[key] for key in keys]
    denom = independent.groupby(grouping, sort=False).transform(lambda x: x.sum(skipna=False))
    numer = dependent.groupby(grouping, sort=False).transform(lambda x: x.sum(skipna=False))
    df["tasa_dependencia"] = (numer / denom * 100).where(denom.ne(0))
    if breaks is not None:
        df["tasa_dependencia"] = _cut(df["tasa_dependencia"], breaks, labels)
    return df


def hacinamiento(tbl, breaks=None, labels=None):
    """Persons per bedroom at dwelling level; zero bedrooms yield infinity."""
    df = tbl.copy()
    keys = _household_keys(df, dwelling=True)
    count = df.groupby(keys, sort=False)["VIVIENDA"].transform("size")
    df["hacinamiento"] = count / _column(df, "CANT_DORMITORIOS_VIVIENDA")
    if breaks is not None:
        df["hacinamiento"] = _cut(df["hacinamiento"], breaks, labels)
    return df


def sexo_jefe(tbl):
    """Sex of the household head, attached to each member of the household."""
    df = tbl.copy()
    keys = ["PERIODO", "VIVIENDA", "HOGAR"]
    require_columns(df, keys + ["PARENTESCO", "SEXO"])
    if df[keys].isna().any().any():
        raise ValueError("Household and period identifiers cannot be missing.")
    heads = df.loc[_column(df, "PARENTESCO").eq(1).fillna(False), keys + ["SEXO"]]
    if heads.duplicated(keys).any():
        raise ValueError("More than one household head for the same household.")
    result = df.drop(columns="sexo_jefe", errors="ignore").merge(heads.rename(columns={"SEXO": "sexo_jefe"}), on=keys, how="left", sort=False, validate="many_to_one")
    result.index = df.index
    return result
