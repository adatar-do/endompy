"""Preserve original ENGIH codes; convert only explicitly mapped presentation fields."""
import math
import numbers
import numpy as np
import pandas as pd
from pandas.api.types import is_bool_dtype, is_numeric_dtype, is_complex_dtype
from labelerpy.labeling import set_dict as _set_dict
from .dictionaries import _resolve


def _table(tbl, vars):
    if not isinstance(tbl, pd.DataFrame):
        raise TypeError("tbl must be a local pandas DataFrame")
    if not tbl.columns.is_unique or any(not isinstance(c, str) or not c for c in tbl.columns):
        raise ValueError("Column names must be unique and nonempty strings")
    if vars is not None:
        if (not isinstance(vars, (list, tuple, pd.Index)) or any(not isinstance(c, str) for c in vars)
                or len(set(vars)) != len(vars) or any(c not in tbl.columns for c in vars)):
            raise ValueError("vars must select unique existing columns")


def _selected(tbl, dictionary, vars):
    return [name for name in (tbl.columns if vars is None else vars) if name in dictionary]


def _codes(series, codes):
    sample = next(iter(codes.values())) if codes else None
    categorical = isinstance(series.dtype, pd.CategoricalDtype)
    if categorical:
        compatible = False
    elif series.isna().all():
        compatible = True
    elif isinstance(sample, bool):
        compatible = is_bool_dtype(series.dtype)
    elif isinstance(sample, numbers.Real):
        compatible = is_numeric_dtype(series.dtype) and not is_bool_dtype(series.dtype) and not is_complex_dtype(series.dtype)
    else:
        compatible = all(isinstance(v, str) for v in series[series.notna()])
    unknown = series.notna() & ~series.isin(list(codes.values()))
    return compatible, unknown


def _display(value):
    if isinstance(value, (bool, np.bool_)):
        return "TRUE" if value else "FALSE"
    if isinstance(value, numbers.Real):
        if math.isinf(value):
            return "Inf" if value > 0 else "-Inf"
        return format(value, ".15g")
    return str(value)


def set_labels(tbl, dictionary=None, vars=None, module="personas", edition=2018,
               version=None, at=None, con=None, strict=False):
    """Attach labels/provenance while preserving values, dtypes, columns and index.

    Type mismatches always fail. strict=True also rejects unknown codes; the
    default preserves them. Only selected documented fields receive labels.
    """
    _table(tbl, vars)
    if not isinstance(strict, (bool, np.bool_)):
        raise ValueError("strict must be True or False")
    dictionary = _resolve(dictionary, module, edition, version, at, con)
    selected = _selected(tbl, dictionary, vars)
    for name in selected:
        codes = dictionary[name].labels
        if not codes:
            continue
        compatible, unknown = _codes(tbl[name], codes)
        if not compatible:
            raise ValueError("Incompatible code type in " + name + "; retain original numeric/string codes")
        if strict and unknown.any():
            raise ValueError("Unknown codes in " + name)
    result = _set_dict(tbl, dictionary, subset=selected, dtypes=False, at=at)
    result.attrs["engihr_module"] = module
    return result


def use_labels(tbl, dictionary=None, vars=None, module="personas", edition=2018,
               version=None, at=None, con=None, strict=False):
    """Return categorical presentation columns, retaining missing and unknown values.

    Label-only fields remain numeric. Unknown codes that equal a known display
    label receive [unlabelled code: ...]. Input and duplicate row indices survive.
    """
    _table(tbl, vars)
    resolved = _resolve(dictionary, module, edition, version, at, con)
    result = set_labels(tbl, resolved, vars, module, edition, at=at, strict=strict)
    # Delay whole-frame metadata propagation while replacing presentation columns.
    frame_attrs = result.attrs
    result.attrs = {}
    for name in _selected(tbl, resolved, vars):
        codes = resolved[name].labels
        if not codes:
            continue
        lookup = {}
        for label, code in codes.items():
            lookup.setdefault(code, label)  # R match() takes the first repeated code.
        display = []
        for value in tbl[name]:
            if pd.isna(value):
                display.append(None)
            elif value in lookup:
                display.append(lookup[value])
            else:
                text = _display(value)
                display.append("[unlabelled code: " + text + "]" if text in codes else text)
        levels = list(dict.fromkeys(list(codes) + [v for v in display if v is not None]))
        result[name] = pd.Categorical(display, categories=levels, ordered=False)
        result[name].attrs["label"] = resolved[name].label
    result.attrs = frame_attrs
    return result


def validate(tbl, dictionary=None, vars=None, module="personas", edition=2018,
             version=None, at=None, con=None):
    """Report field, status, n, missing and unknown without changing the table.

    Status: unmapped, label_only, ok, unknown_codes or type_mismatch. This checks
    metadata/code coverage; it does not certify survey consistency or estimates.
    """
    _table(tbl, vars)
    dictionary = _resolve(dictionary, module, edition, version, at, con)
    rows = []
    for name in tbl.columns if vars is None else vars:
        variable = dictionary.get(name)
        codes = None if variable is None else variable.labels
        status = "unmapped" if variable is None else "label_only" if not codes else "ok"
        unknown = None
        if codes:
            compatible, mask = _codes(tbl[name], codes)
            unknown = int(mask.sum()) if compatible else None
            status = "type_mismatch" if not compatible else "unknown_codes" if unknown else "ok"
        rows.append({"field": name, "status": status, "n": len(tbl),
            "missing": int(tbl[name].isna().sum()), "unknown": unknown})
    return pd.DataFrame(rows, columns=["field", "status", "n", "missing", "unknown"])
