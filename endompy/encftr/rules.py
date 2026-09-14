"""Small, closed expression evaluator for the bundled ENCFT calculation rules.

Only enumerated arithmetic, predicates, selectors and survey operations are accepted.
No eval, exec, imported code, arbitrary calls, or user-supplied rule files are used.
"""
import json
from functools import lru_cache
from pathlib import Path
import operator

import numpy as np
import pandas as pd

from .core import require_columns

RESOURCES = Path(__file__).parent / "resources"
RULES = json.loads((RESOURCES / "survey-rules.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=None)
def _table(name):
    return pd.DataFrame(json.loads((RESOURCES / (name + ".json")).read_text(encoding="utf-8")))


def _vector(value, df):
    if isinstance(value, pd.Series):
        return value
    return pd.Series(value, index=df.index)


def _column(df, name):
    if name not in df:
        raise ValueError("Missing required column: " + name)
    value = df[name]
    if pd.api.types.is_numeric_dtype(value):
        return value.astype("Float64")
    return value.astype("string")


def case_when(df, pairs, default=np.nan):
    def nullable(value):
        value = _vector(value, df)
        if pd.api.types.is_numeric_dtype(value.dtype) or value.isna().all():
            return value.astype("Float64")
        return value.astype("string") if all(isinstance(x, str) for x in value.dropna()) else value
    result = nullable(default).copy()
    for condition, value in reversed(pairs):
        mask = _vector(condition, df).astype("boolean").fillna(False)
        # Series.where handles nullable numbers and strings without NumPy coercion.
        current = nullable(value)
        if str(current.dtype) == "string" and str(result.dtype) != "string":
            result = result.astype("string")
        result = current.where(mask, result)
    return result


def _op(node):
    return node.get("call", "").split("::")[-1]


def expression(node, df, env=None):
    env = {} if env is None else env
    if node == []:
        return None
    if "value" in node:
        return np.nan if node["value"] is None else node["value"]
    if "symbol" in node:
        name = node["symbol"]
        constants = {"NA_real_": np.nan, "NA_integer_": np.nan, "NA": np.nan,
                     "NA_character_": pd.NA, "Inf": np.inf, "T": True, "F": False}
        if name in constants:
            return constants[name]
        if name in env:
            return env[name]
        return _column(df, name)
    op, args = _op(node), node.get("args", [])
    names = node.get("names", [""] * len(args))
    if op.startswith("encft_iih_"):
        from .iih import _iih_expression
        return _iih_expression(op, args, df, env)
    if op.startswith("encft_icv_"):
        from .icv import _icv_expression
        return _icv_expression(op, args, df, env)
    if op in ("$", "[["):
        name = args[1].get("symbol") if op == "$" else expression(args[1], df, env)
        return _column(df, name)
    if op == "case_when":
        pairs = [(expression(x["args"][0], df, env), expression(x["args"][1], df, env))
                 for x, key in zip(args, names) if key != ".default"]
        default = next((expression(x, df, env) for x, key in zip(args, names) if key == ".default"), np.nan)
        return case_when(df, pairs, default)
    if op == "ftc_pm22_row_sums":
        columns = expression(args[1], df, env)
        return df[[col for col in columns if col in df]].sum(axis=1, skipna=True)
    values = [expression(x, df, env) for x in args]
    binary = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv,
              "^": operator.pow, "%%": operator.mod, "%/%": operator.floordiv,
              "==": operator.eq, "!=": operator.ne, "<": operator.lt, "<=": operator.le,
              ">": operator.gt, ">=": operator.ge, "&": operator.and_, "|": operator.or_}
    if op in binary:
        if len(values) == 1:
            return -values[0] if op == "-" else values[0]
        return binary[op](*values)
    if op == "!":
        return ~values[0] if isinstance(values[0], pd.Series) else not values[0]
    if op == "(":
        return values[0]
    if op == "[":
        return values[0].where(values[1].fillna(False))
    if op in ("exp", "log", "floor"):
        return {"exp": np.exp, "log": np.log, "floor": np.floor}[op](values[0])
    if op == "is.na":
        return pd.isna(values[0])
    if op == "is.finite":
        return np.isfinite(values[0])
    if op == "between":
        return (values[0] >= values[1]) & (values[0] <= values[2])
    if op == "%in%":
        return values[0].isin(np.atleast_1d(values[1])) if isinstance(values[0], pd.Series) else values[0] in values[1]
    if op == ":":
        return list(range(int(values[0]), int(values[1]) + 1))
    if op == "c":
        return [item for value in values for item in (value if isinstance(value, list) else [value])]
    if op == "paste0":
        size = max((len(x) if isinstance(x, list) else 1) for x in values)
        result = ["".join(str(x[i % len(x)] if isinstance(x, list) else x) for x in values) for i in range(size)]
        return result if size > 1 else result[0]
    if op in ("as.double", "as.numeric", "as.integer"):
        value = pd.to_numeric(values[0], errors="coerce")
        return np.trunc(value) if op == "as.integer" else value
    if op == "as.character":
        return values[0].astype("string") if isinstance(values[0], pd.Series) else str(values[0])
    if op in ("ifelse", "if_else"):
        condition = _vector(values[0], df).astype("boolean")
        return _vector(values[1], df).where(condition.fillna(False), _vector(values[2], df)).mask(condition.isna())
    if op in ("lead", "lag"):
        return values[0].shift((-1 if op == "lead" else 1) * (int(values[1]) if len(values) > 1 else 1))
    if op == "replace_na":
        return values[0].fillna(values[1])
    if op == "str_detect":
        return values[0].astype("string").str.contains(values[1], regex=True)
    if op == "sum":
        return values[0].sum(skipna=dict(zip(names, values)).get("na.rm", False))
    if op == "ftc_pm22_row_sums":
        return df[[col for col in values[1] if col in df]].sum(axis=1, skipna=True)
    raise ValueError("Unsupported bundled expression: " + op)


def _selection(node, df, env):
    if "symbol" in node:
        name = node["symbol"]
        return env.get(name, [name])
    if "value" in node:
        return [node["value"]]
    op, args = _op(node), node.get("args", [])
    if op in ("c", "all_of", "any_of"):
        return [name for arg in args for name in _selection(arg, df, env)]
    if op in ("starts_with", "contains"):
        value = args[0]["value"].lower()
        return [name for name in df if name.lower().startswith(value) if op == "starts_with"] if op == "starts_with" else [name for name in df if value in name.lower()]
    if op == "everything":
        return list(df)
    raise ValueError("Unsupported bundled selector: " + op)


def join_table(df, table, on):
    columns = [name for name in table if name in on or name not in df]
    result = df.merge(table[columns], on=on, how="left", sort=False, validate="many_to_one")
    result.index = df.index
    return result


def apply_steps(df, steps, env):
    for step in steps:
        op, args, names = step["op"], step.get("args", []), step.get("names", [])
        if op == "mutate":
            for node, name in zip(args, names):
                if not name and _op(node) == "across":
                    columns = _selection(node["args"][0], df, env)
                    for column in columns:
                        df[column] = df[column].astype("string")
                else:
                    df[name] = expression(node, df, env)
        elif op == "select":
            for node in args:
                if _op(node) == "-":
                    df = df.drop(columns=_selection(node["args"][0], df, env), errors="ignore")
                else:
                    df = df[_selection(node, df, env)]
        elif op == "left_join_tipo_cambio":
            from .poverty import normalize_currency
            for column in df:
                if column.endswith("_MONEDA"):
                    df[column] = normalize_currency(df[column]).replace("REAL", "BRL")
            rates = _table("tipo_cambio").sort_values("PERIODO").copy()
            columns = rates.columns.difference(["PERIODO"])
            rates[columns] = rates[columns].shift(1)
            df = join_table(df, rates, ["PERIODO"])
        elif op == "left_join":
            table = _table(args[0]["symbol"])
            on = expression(args[names.index("by")], df, env)
            df = join_table(df, table, on)
        elif op == "deflate":
            if env.get("deflactar", True):
                df = apply_steps(df, step["steps"], env)
        elif op.startswith("ftc_"):
            df = run_rule(df, op[4:])
        else:
            raise ValueError("Unsupported bundled operation: " + op)
    return df


def run_rule(tbl, name, **kwargs):
    require_columns(tbl, [])
    spec = RULES[name]
    df = tbl.copy(deep=True)
    env = {key: value.get("value") for key, value in spec["parameters"].items() if key != "tbl"}
    env.update({("." + key if key in ("keep", "reuse") else key): value for key, value in kwargs.items()})
    dependencies = spec["dependencies"]
    reuse, keep = env.get(".reuse", False), env.get(".keep", False)
    if not isinstance(reuse, (bool, list, tuple)) or not isinstance(keep, (bool, list, tuple)):
        raise ValueError("keep and reuse must be bool or lists of component names.")
    computed = []
    for component in dependencies:
        retained = component in df if reuse is True else component in reuse if reuse is not False else False
        if not retained:
            if component == "ing_remesas_ext":
                from .poverty import ing_remesas_ext
                df = ing_remesas_ext(df)
            else:
                df = run_rule(df, component)
            computed.append(component)
        elif component not in df:
            raise ValueError("Requested reusable component is absent: " + component)
    env["ingresos"] = [] if keep is True else [name for name in computed if keep is False or name not in keep]
    return apply_steps(df, spec["steps"], env)
