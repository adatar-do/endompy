"""Validated period and weighting contracts for member-level ENCFT data."""

import numbers
import numpy as np
import pandas as pd


def require_columns(tbl, columns):
    if not isinstance(tbl, pd.DataFrame):
        raise TypeError("A local pandas DataFrame is required.")
    if tbl.columns.has_duplicates:
        raise ValueError("Duplicate column names are not allowed.")
    missing = [name for name in columns if name not in tbl.columns]
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))


def quarter_parts(tbl):
    require_columns(tbl, ["TRIMESTRE"])
    q = pd.to_numeric(tbl["TRIMESTRE"], errors="coerce").astype(float)
    encoded = q >= 10001
    year = (q // 10).where(encoded)
    quarter = (q % 10).where(encoded, q)
    if "ANO" in tbl:
        supplied = pd.to_numeric(tbl["ANO"], errors="coerce").astype(float)
        if (encoded & (supplied.isna() | year.ne(supplied))).any():
            raise ValueError("ANO and TRIMESTRE disagree.")
        year = year.where(encoded, supplied)
    if (year.isna() | ~np.isfinite(year) | (year != np.trunc(year)) |
        ~year.between(1000, 9999) | ~quarter.isin([1, 2, 3, 4]) |
        q.isna() | ~np.isfinite(q) | (q != np.trunc(q))).any():
        raise ValueError("TRIMESTRE must be YYYYQ, or 1:4 with ANO; missing periods are not allowed.")
    return year, quarter


def _expansion(tbl, periods, semester):
    require_columns(tbl, ["FACTOR_EXPANSION"])
    weights = tbl["FACTOR_EXPANSION"]
    if not pd.api.types.is_numeric_dtype(weights) or pd.api.types.is_bool_dtype(weights):
        raise ValueError("FACTOR_EXPANSION must be numeric, finite and nonnegative (missing is allowed).")
    if ((~np.isfinite(weights) | (weights < 0)) & weights.notna()).any():
        raise ValueError("FACTOR_EXPANSION must be numeric, finite and nonnegative (missing is allowed).")
    maximum = 2 if semester else 4
    if periods is not None:
        if isinstance(periods, bool) or not isinstance(periods, numbers.Real) or not np.isfinite(periods) or periods != int(periods) or not 1 <= periods <= maximum:
            raise ValueError(f"periods must be an integer between 1 and {maximum}.")
        divisor = periods
    else:
        year, quarter = quarter_parts(tbl)
        keys = [year, (quarter - 1) // 2] if semester else year
        divisor = quarter.groupby(keys, sort=False).transform("nunique")
    result = tbl.copy(deep=True)
    result["factor_expansion_semestre" if semester else "factor_expansion_anual"] = weights / divisor
    return result


def factor_expansion_anual(tbl, periods=None):
    """Average quarterly weights over observed quarters within each year.

    Supply ``periods=4`` for a known four-quarter extract without quarter fields.
    Otherwise TRIMESTRE (YYYYQ), or TRIMESTRE (1:4) plus ANO, is required.
    Calculate before filtering persons. Partial coverage does not represent a full year.
    Returns a copy with factor_expansion_anual and the original row order/index.
    """
    return _expansion(tbl, periods, semester=False)


def factor_expansion_semestre(tbl, periods=None):
    """Average weights over observed quarters within each year and semester.

    Supply periods=2 to declare known two-quarter coverage explicitly.
    Missing weights stay missing; invalid weights and ambiguous periods raise ValueError.
    """
    return _expansion(tbl, periods, semester=True)
