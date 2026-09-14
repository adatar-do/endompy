"""Historical ICV SIUBEN, integrated from encftr0 0.0.2.9002.

The bundled closed pipelines preserve R coefficients and recode precedence.
This is not a claim about the currently adopted SIUBEN methodology. No R runtime,
eval, exec, arbitrary function calls or user-provided rule files are used.
"""
import copy
import json
from pathlib import Path

import numpy as np
import pandas as pd

from .core import require_columns as _require, quarter_parts as _quarters
from .rules import expression as _expression, _selection, _vector

_MODEL = json.loads((Path(__file__).parent / "resources/icv-siuben-rules.json").read_text(encoding="utf-8"))


def variables_icv_siuben():
    """Return required, optional, output and component names as detached lists."""
    return copy.deepcopy(_MODEL["variables"])


def _keys(df, dwelling=False):
    return (["ANO"] if "ANO" in df else []) + ["TRIMESTRE", "VIVIENDA"] + ([] if dwelling else ["HOGAR"])


def _icv_expression(op, args, df, env):
    values = [_expression(arg, df, env) for arg in args]
    if op == "encft_icv_n":
        return len(df)
    if op == "encft_icv_first":
        return values[0].iloc[0]
    if op == "encft_icv_mean":
        return values[0].mean(skipna=bool(values[1]) if len(values) > 1 else False)
    if op == "encft_icv_head_value":
        selected = values[0].loc[values[1].fillna(False)]
        if len(selected) != 1:
            raise ValueError("Exactly one household head is required.")
        return selected.iloc[0]
    raise ValueError("Unsupported bundled ICV expression: " + op)


def _run(name, df, groups=None):
    for step in _MODEL["functions"][name]:
        op = step["op"]
        if op == "invoke":
            df, groups = _run(step["function_name"], df, groups)
        elif op == "group_by":
            groups = _keys(df, dwelling=step["dwelling"])
        elif op == "ungroup":
            groups = None
        elif op == "mutate":
            for node, column in zip(step["args"], step["names"]):
                if groups:
                    result = pd.Series(pd.NA, index=df.index, dtype="Float64")
                    for rows in df.groupby(groups, sort=False, dropna=False).indices.values():
                        part = df.iloc[rows]
                        value = _vector(_expression(node, part), part)
                        result.loc[part.index] = value
                    df[column] = result
                else:
                    df[column] = _expression(node, df)
        elif op == "select":
            for node in step["args"]:
                if node.get("call") != "-":
                    raise ValueError("Unsupported ICV selector")
                columns = _selection(node["args"][0], df, {})
                df = df.drop(columns=columns)
        else:
            raise ValueError("Unsupported bundled ICV step: " + op)
    return df, groups


def icv_siuben(tbl, include_details=True, method="encftr0-0.0.2.9002"):
    """Calculate historical ICV category, score and methodology identifier.

    Supply complete member-level households with one PARENTESCO == 1 per key.
    TRIMESTRE is YYYYQ, or 1:4 together with ANO. Year is included in group keys;
    crowding retains the original dwelling-level aggregation across households.
    Historical missing-score and age-boundary rules are preserved. Inputs must
    use numeric survey codes, not display-label categories. Data, original index
    (including duplicates), metadata and row order are preserved in the copy.
    Existing calculated components are refreshed even if include_details=False.
    """
    spec = variables_icv_siuben()
    _require(tbl, spec["required"])
    if not isinstance(include_details, bool):
        raise ValueError("include_details must be bool.")
    if not isinstance(method, str) or method != _MODEL["method"]:
        raise ValueError("Unknown ICV method; use encftr0-0.0.2.9002.")
    _quarters(tbl)
    keys = _keys(tbl)
    if tbl[keys].isna().any().any():
        raise ValueError("Period, dwelling and household identifiers cannot be missing.")
    keep = spec["required"] + [name for name in spec["optional"] if name in tbl]
    work = pd.DataFrame(tbl[keep]).reset_index(drop=True)
    for name in set(spec["required"]) - {"TRIMESTRE", "VIVIENDA", "HOGAR"}:
        value = work[name]
        if (not pd.api.types.is_numeric_dtype(value) or pd.api.types.is_bool_dtype(value)
            or ((~np.isfinite(value) | (value != np.trunc(value))) & value.notna()).any()):
            raise ValueError(name + " must contain finite integer numeric codes or missing values.")
    if work[["ZONA", "ID_PROVINCIA", "ID_MUNICIPIO"]].isna().any().any() or not work["ZONA"].isin([1, 2]).all():
        raise ValueError("ZONA (1/2), ID_PROVINCIA and ID_MUNICIPIO cannot be missing.")
    if work["PARENTESCO"].isna().any():
        raise ValueError("PARENTESCO cannot be missing when identifying the household head.")
    if "MATERIAL_PARED_EXTERIOR_ESP" not in work:
        work["MATERIAL_PARED_EXTERIOR_ESP"] = ""
    if not work["MATERIAL_PARED_EXTERIOR_ESP"].dropna().map(lambda value: isinstance(value, str)).all():
        raise ValueError("MATERIAL_PARED_EXTERIOR_ESP must contain text.")
    output = spec["output"] + [name for name in spec["details"] if include_details or name in tbl]
    result = tbl.copy(deep=True)
    if not len(work):
        for name in output:
            result[name] = pd.Series(index=tbl.index, dtype="string" if name == "icv_metodo" else "Float64")
        return result
    for rows in work.groupby(keys, sort=False, dropna=False).indices.values():
        group = work.iloc[rows]
        if group["PARENTESCO"].eq(1).sum() != 1:
            raise ValueError("Each household and period requires exactly one household head (PARENTESCO == 1).")
        if any(group[name].nunique() != 1 for name in ("ZONA", "ID_PROVINCIA", "ID_MUNICIPIO")):
            raise ValueError("Inconsistent location within household.")
    computed, _ = _run("encft_icv_legacy_compute_icv_siuben", work)
    computed["icv_puntaje"] = computed["icv_nuevo"]
    computed["icv_metodo"] = method
    for name in output:
        result[name] = pd.array(computed[name], dtype="string" if name == "icv_metodo" else "Float64")
    return result


def compute_icv_siuben(tbl, include_details=True, method="encftr0-0.0.2.9002"):
    """Alias for icv_siuben matching the R compute entry point."""
    return icv_siuben(tbl, include_details=include_details, method=method)


def dict_icv_siuben():
    """Return ICV result labels without modifying the frozen ENCFT questionnaire."""
    from labelerpy import Dict
    return Dict(metadata={"name": "encft-icv-siuben", "method": _MODEL["method"]}, variables={
        "icv_global": {"label": "ICV SIUBEN historico", "labels": {f"ICV {i}": i for i in range(1, 5)}},
        "icv_puntaje": {"label": "Puntaje ICV SIUBEN historico"},
        "icv_metodo": {"label": "Implementacion ICV SIUBEN"},
    })


def set_labels_icv_siuben(tbl, vars=None):
    """Apply ICV value labels to the requested columns, preserving numeric codes."""
    from labelerpy.labeling import set_dict
    return set_dict(tbl, dict_icv_siuben(), subset=vars, dtypes=False)


def use_labels_icv_siuben(tbl, vars=None):
    """Convert ICV numeric codes to labeled categories without renaming columns."""
    from labelerpy.labeling import with_dict
    return with_dict(tbl, dict_icv_siuben(), subset=vars, use_label=False, use_labels=True)
