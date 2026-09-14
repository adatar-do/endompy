"""Household income index using the same fixed models and definitions as encftr.

This is a model-based index. It is distinct from observed monetary poverty.
Models, coefficients and reviewed expressions are bundled; R is not required.
"""
import json
import re
import unicodedata

import numpy as np
import pandas as pd

from .core import require_columns
from .rules import RESOURCES, expression, case_when, _vector

_MODELS = json.loads((RESOURCES / "iih-models.json").read_text(encoding="utf-8"))
_RULES = json.loads((RESOURCES / "iih-rules.json").read_text(encoding="utf-8"))


def variables_iih(include_details=False):
    """Return detached lists of required inputs, optional inputs and output names."""
    return {"required": list(_MODELS["required"]), "optional": list(_MODELS["optional"]),
            "output": list(_MODELS["details" if include_details else "output"])}


def _normalize_text(value):
    value = "" if pd.isna(value) else str(value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().upper()
    return " ".join(value.split())


def _wall(raw, text):
    raw = pd.to_numeric(raw, errors="coerce").copy()
    text = text.map(_normalize_text)
    raw = raw.mask(raw.eq(14), 4)
    other = raw.eq(99)
    mapped = text.map(_MODELS["walls"])
    prefab = text.str.contains("PLAQUET|PREFABRIC|MAYA REB|MAYA REV|CHIRROT|PLAYWOOD|PLYWOOD|TABLA|PALMA|MADERA|PIEDRA Y CEMENTO")
    concrete = text.str.contains("VACIAD|VACEAD|VACED|CONCRETO|CEMENTO|MEZCLA|ARENA|VARILLA|ALAMBRE|BLOCK")
    mapped = mapped.mask(mapped.isna() & prefab, 7).mask(mapped.isna() & concrete & ~prefab, 4)
    return raw.mask(other & mapped.notna(), mapped)


def _format_keys(value):
    return pd.to_numeric(value, errors="coerce").map(lambda x: None if pd.isna(x) else format(x, ".15g"))


def _calc_id(df):
    period, household = _format_keys(df["PERIODO"]), _format_keys(df["ID_HOGAR"])
    if period.isna().any() or household.isna().any():
        raise ValueError("PERIODO and ID_HOGAR must be present to identify households.")
    return period + "__" + household


def _iih_expression(op, args, df, env):
    if op == "encft_iih_apply_model_spec":
        name = args[1]["args"][1]["symbol"]
        spec = _MODELS["models"][name]
        columns = {re.sub("[^a-z0-9]+", "_", col.strip().lower()): col for col in df}
        score = pd.Series(spec["alpha"], index=df.index, dtype=float)
        for variable, coefficients in spec["coefficients"].items():
            score = score + _format_keys(df[columns[variable]]).map(coefficients)
        return score
    values = [expression(arg, df, env) for arg in args]
    if op == "encft_iih_to_numeric":
        return pd.to_numeric(values[0], errors="coerce")
    if op == "encft_iih_normalize_wall_material":
        return _wall(*values)
    if op == "encft_iih_years_of_education":
        level, grade, age, base = [pd.to_numeric(x, errors="coerce") for x in values]
        return case_when(df, [(age <= 2, 0), (level == 99, np.nan), (level.isin([1, 9, 10]), 0),
            (level == 2, grade), (level.isin([3, 4]), base + grade), (level == 5, 12 + grade),
            (level.isin([6, 7, 8]), 16 + grade)])
    if op == "encft_iih_entropy":
        probs = pd.concat([_vector(v, df) for v in values], axis=1).fillna(0).astype(float)
        with np.errstate(divide="ignore", invalid="ignore"):
            return -(probs * np.log(probs.where(probs > 0, 1))).sum(axis=1)
    raise ValueError("Unsupported bundled IIH operation: " + op)


def _mutate(df, stage):
    for name, node in _RULES[stage]:
        df[name] = expression(node, df)
    return df


def _prepare(df):
    year = np.floor(pd.to_numeric(df["PERIODO"], errors="coerce") / 100)
    level = pd.to_numeric(df["NIVEL_ULTIMO_ANO_APROBADO"], errors="coerce")
    grade = pd.to_numeric(df["ULTIMO_ANO_APROBADO"], errors="coerce")
    primary = grade.where(level == 2).groupby(year).transform("max")
    df["secondary_base"] = pd.Series(np.where(primary >= 8, 8, 6), index=df.index)
    df["calc_id"] = _calc_id(df)
    return _mutate(df, "persons").drop(columns="secondary_base")


def _aggregate(df):
    grouping = df["calc_id"]
    result = pd.DataFrame(index=pd.Index(sorted(grouping.unique()), name="calc_id"))
    for name, node in _RULES["aggregate"]:
        op = node["call"].split("::")[-1]
        if op == "suppressWarnings":
            node = node["args"][0]
            op = node["call"].split("::")[-1]
        if op == "n":
            value = df.groupby("calc_id").size()
        else:
            value = expression(node["args"][0], df)
            grouped = value.groupby(grouping)
            if op == "first":
                # R first includes a missing first observation.
                value = pd.Series(value.loc[~grouping.duplicated()].to_numpy(), index=grouping.loc[~grouping.duplicated()])
            else:
                value = getattr(grouped, op)()
        result[name] = value
    return result.reset_index().replace([np.inf, -np.inf], np.nan)


def iih(tbl, vivienda_tbl=None, return_households=False, include_details=False, filter_valid_households=False):
    """Calculate the household income index, optionally returning one row per household.

    Accept a DataFrame or a mapping with miembros/members/personas/data and optional
    vivienda/viviendas. Household keys combine PERIODO and ID_HOGAR. Invalid model
    inputs produce IIH=9; filter_valid_households filters household output, while
    person output keeps all original rows and leaves filtered household scores missing.
    """
    if isinstance(tbl, dict):
        if vivienda_tbl is None:
            vivienda_tbl = next((tbl[key] for key in ("vivienda", "viviendas") if key in tbl), None)
        tbl = next((tbl[key] for key in ("miembros", "members", "personas", "data") if key in tbl), None)
    require_columns(tbl, _MODELS["required"])
    df = pd.DataFrame(tbl).copy().reset_index(drop=True)
    for col in _MODELS["optional"]:
        if col not in df:
            df[col] = pd.NA
    col = "MATERIAL_PARED_EXTERIOR_ESP"
    if vivienda_tbl is not None and all(c in vivienda_tbl for c in ("PERIODO", "VIVIENDA", col)):
        dwelling = vivienda_tbl[["PERIODO", "VIVIENDA", col]].drop_duplicates(["PERIODO", "VIVIENDA"])
        df = df.merge(dwelling.rename(columns={col: "_wall_text"}), on=["PERIODO", "VIVIENDA"], how="left", sort=False, validate="many_to_one")
        df[col] = df[col].fillna(df.pop("_wall_text"))
    households = _mutate(_mutate(_aggregate(_prepare(df)), "classify"), "models")
    invalid = households["hconmissing"].eq(1).fillna(False)
    households.loc[invalid, _RULES["model_columns"]] = np.nan
    for col in _RULES["model_columns"]:
        if col.startswith("pobofizona_"):
            households.loc[invalid, col] = 9
    households["IIH"] = households["pobofizona_ingresopc_oficial_NCRO_calc_C37_d1010_C939"]
    if filter_valid_households:
        households = households.loc[households["hconmissing"] == 0]
    columns = _MODELS["details" if include_details else "output"]
    if return_households:
        return households[columns].reset_index(drop=True)
    result = pd.DataFrame(tbl).copy()
    result["calc_id"] = _calc_id(result)
    added = [c for c in columns if c not in ("calc_id", "PERIODO", "ID_HOGAR")]
    result = result.drop(columns=added, errors="ignore")
    result = result.merge(households[["calc_id"] + added], on="calc_id", how="left", sort=False, validate="many_to_one").drop(columns="calc_id")
    result.index = tbl.index
    return result
