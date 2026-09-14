"""ENCFT monetary poverty: explicit 2012 and 2022 methodology entry points."""
import json
import numpy as np
import pandas as pd

from .core import require_columns, quarter_parts
from .rules import RESOURCES, _table, _column, expression, case_when, join_table

PM22 = json.loads((RESOURCES / "poverty-2022-rules.json").read_text(encoding="utf-8"))
CURRENCIES = {str(i): c for i, c in enumerate(
    ["DOP", "EUR", "USD", "REAL", "CAD", "CHF", "CNY", "DEG", "DKK", "GBP", "LESC", "JPY", "NOK", "SEK", "VEF", "ARS"], 1)}


def normalize_currency(series):
    if pd.api.types.is_numeric_dtype(series):
        text = series.astype("Float64").astype("string").str.replace(r"\.0$", "", regex=True)
    else:
        text = series.astype("string")
    text = text.str.strip().str.upper().replace({"": pd.NA, "NA": pd.NA, "BRL": "REAL"})
    return text.replace(CURRENCIES)


def ing_remesas_ext(tbl):
    """Monthly mean of the preceding six months of foreign remittances.

    Each of three remittance streams uses the exchange rate of its reported month.
    Missing components contribute zero, following the official reference code.
    """
    require_columns(tbl, ["PERIODO"])
    rates = _table("tipo_cambio_pm22")
    amounts = []
    for j in range(1, 4):
        for i in range(1, 7):
            prefix = f"MES{i}_{j}_EXT"
            require_columns(tbl, [prefix + "_MONTO", prefix + "_MONEDA"])
            frame = pd.DataFrame({"periodo": tbl["PERIODO"].to_numpy(),
                "moneda": normalize_currency(tbl[prefix + "_MONEDA"]).to_numpy()})
            rate = frame.merge(rates[["periodo", "moneda", f"tasa_a_pesos_mes{i}"]],
                on=["periodo", "moneda"], how="left", sort=False, validate="many_to_one")[f"tasa_a_pesos_mes{i}"]
            amounts.append(pd.to_numeric(tbl[prefix + "_MONTO"], errors="coerce").reset_index(drop=True) * rate)
    df = tbl.copy()
    total = pd.concat(amounts, axis=1).sum(axis=1, skipna=True) / 6
    df["ing_remesas_ext"] = total.to_numpy()
    return df


def _assignments(df, assignments):
    for name, formula in assignments:
        df[name] = expression(formula, df)
    return df.copy()


def _macro_region(df):
    regions = {"Gran Santo Domingo": "Ozama", "Norte o Cibao": "Norte", "Sur": "Sur", "Este": "Este"}
    result = df["grupo_region"].map(regions)
    provinces = {"Ozama": [1, 32], "Este": [8, 11, 12, 23, 29, 30],
                 "Sur": [2, 3, 4, 7, 10, 16, 17, 21, 22, 31],
                 "Norte": [5, 6, 9, 13, 14, 15, 18, 19, 20, 24, 25, 26, 27, 28]}
    for region, codes in provinces.items():
        result = result.mask(result.isna() & df["id_provincia"].isin(codes), region)
    return result.astype("string")


def _pobreza_monetaria(tbl, keep=False, reuse=False, methodology="2022"):
    """Calculate 2022 monetary poverty using member-level data and regional lines.

    Returns the original rows plus household income, per-capita income, poverty
    lines, category (1 extreme, 2 general, 3 nonpoor), pobre and indigente.
    Missing income/lines remain unclassified. Monetary outputs are DOP per month.
    keep=True retains intermediate components; a list retains named components.
    reuse is accepted for R compatibility; this methodology recomputes components.
    """
    required = ["PERIODO", "TRIMESTRE", "VIVIENDA", "HOGAR"]
    require_columns(tbl, required)
    if methodology == "2012":
        require_columns(tbl, ["ZONA", "CANTIDAD_MIEMBROS_HOGAR"])
    if tbl[required].isna().any().any():
        raise ValueError("Period and household identifiers cannot be missing.")
    if not all(isinstance(col, str) for col in tbl.columns) or len({col.lower() for col in tbl}) != len(tbl.columns):
        raise ValueError("Column names must be unambiguous strings after case normalization.")
    if ".encftr_rowid" in tbl:
        raise ValueError(".encftr_rowid is reserved.")
    if not isinstance(keep, (bool, list, tuple)):
        raise ValueError("keep must be bool or a list of component names.")
    df = pd.DataFrame(select_variables_pobreza(tbl)).copy().reset_index(drop=True)
    df.columns = df.columns.str.lower()
    original = set(df.columns)
    year, quarter = quarter_parts(tbl)
    df["trimestre"] = (year * 10 + quarter).to_numpy()
    for target, source in PM22["alias_map"].items():
        if target not in df and source in df:
            df[target] = df[source]
    for name in PM22["numeric_zero"]:
        if name not in df:
            df[name] = 0.0
    for name in PM22["numeric_na"]:
        if name not in df:
            df[name] = np.nan
    for column in df:
        if column == "grupo_region" or column.endswith("_moneda"):
            continue
        if pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_string_dtype(df[column]):
            strings = df[column].astype("string").str.strip().replace("", pd.NA)
            if (strings.isna() | strings.str.fullmatch(r"[-+]?[0-9]*\.?[0-9]+")).all():
                df[column] = pd.to_numeric(strings, errors="coerce")
    df["personas"] = 1
    group = ["trimestre", "vivienda", "hogar"]
    df["miembros"] = df.groupby(group, sort=False)["personas"].transform("sum")
    currency_prefixes = ["sueldo_bruto_ap", "ingreso_actividad_in", "ingreso_actividad_is",
        "regalos_ext", "otros_ingresos_ext", "alquiler_ext", "interes_ext", "pension_ext"]
    rates = _table("tipo_cambio_pm22")
    for prefix in currency_prefixes + [f"mes{i}_{j}_ext" for j in range(1, 4) for i in range(1, 7)]:
        column = prefix + "_moneda"
        if column not in df:
            continue
        df[column] = normalize_currency(df[column])
        offset = int(prefix[3]) if prefix.startswith("mes") else 6
        lookup = rates[["periodo", "moneda", f"tasa_a_pesos_mes{offset}"]].rename(
            columns={"moneda": column, f"tasa_a_pesos_mes{offset}": prefix + "_tasa"})
        df = join_table(df, lookup, ["periodo", column])
    df = _assignments(df, PM22["base"])
    remittances = {}
    for j in range(1, 4):
        for i in range(1, 7):
            amount = _column(df, f"mes{i}_{j}_ext_monto")
            rate = _column(df, f"mes{i}_{j}_ext_tasa")
            remittances[f"remp{i}_{j}"] = (amount * rate).where(amount.notna() & amount.ne(0))
    df = pd.concat([df, pd.DataFrame(remittances, index=df.index)], axis=1)
    df = _assignments(df, PM22["totals"])
    df = join_table(df, _table("ipc_pobreza_monetaria_2022"), ["periodo"])
    if methodology == "2012":
        df = join_table(df, _table("ipc_official_2012")[["periodo", "deflactor", "deflactor_movil"]], ["periodo"])
        for region in ("ozama", "norte", "este", "sur"):
            df["deflactor_region" + region] = df["deflactor"]
            df["deflactor_movil_region" + region] = df["deflactor_movil"]
    df["macro_region"] = _macro_region(df)
    derived = {}
    for category, rate_prefix in (("region_vars", "deflactor_region"), ("moving_vars", "deflactor_movil_region")):
        for column in expression(PM22[category], df):
            if column not in df:
                continue
            value = _column(df, column)
            pairs = [(df["macro_region"].eq(region), value * df[rate_prefix + region.lower()])
                     for region in ("Ozama", "Este", "Norte", "Sur")]
            derived["d_" + column] = value * df[rate_prefix + "ozama"] if methodology == "2012" else case_when(df, pairs, value)
    for column in expression(PM22["no_deflate_vars"], df):
        if column in df:
            derived["d_" + column] = df[column]
    df = pd.concat([df, pd.DataFrame(derived, index=df.index)], axis=1)
    df = _assignments(df, PM22["deflated"])
    if methodology == "2012":
        df["IDnlab_nac_TrN_mon"] = df[["d_p_s4d11_1", "d_p_s4d11_2", "d_p_s4d11_3", "d_p_s4d11_4", "d_p_s4d11_7", "d_p_s4d12_1", "d_p_s4d12_2", "d_p_s4d12_3", "d_p_s4d12_6"]].sum(axis=1, skipna=True)
        df["IDnla_trE"] = df[["d_p_s4d21_1", "d_p_s4d21_2", "d_p_s4d21_3", "d_p_s4d21_4", "d_p_s4d22"]].sum(axis=1, skipna=True)
    df["miembros"] = df.groupby(group + ["periodo"], sort=False)["personas"].transform("sum")
    df["d_p_s2_6h"] = df.groupby(group, sort=False)["d_p_s2_6"].transform("sum")
    df["d_p_s2_6m"] = df["d_p_s2_6h"] / df["miembros"]
    total_columns = ["IDlab_tot", "IDnlab_nac_esp", "IDnlab_nac_TrN_mon", "IDnla_trE"]
    df["ID_total"] = df[total_columns].sum(axis=1, skipna=True)
    df["ID_total_a"] = df[total_columns + ["d_p_s2_6m"]].sum(axis=1, skipna=True)
    df["Ihog_ENCFT"] = df.groupby(group, sort=False)["ID_total"].transform("sum")
    df["Ihog_ENCFT_a"] = df[["Ihog_ENCFT", "d_p_s2_6"]].sum(axis=1, skipna=True)
    df["IPCm_ENCFT"] = df["Ihog_ENCFT_a"] / df["miembros"]
    df = join_table(df, _table("lineas_pobreza_monetaria_2022"), ["periodo"])
    for output, prefix in (("linea_pob", "linea_general_region"), ("linea_ind", "linea_extrema_region")):
        df[output] = case_when(df, [(df["macro_region"].eq(region), df[prefix + region.lower()])
                                    for region in ("Ozama", "Este", "Sur", "Norte")])
    if methodology == "2012":
        df = join_table(df, _table("lines_official_2012"), ["periodo"])
        df["IPCm_ENCFT"] = (df["Ihog_ENCFT_a"] / df["cantidad_miembros_hogar"]).where(df["cantidad_miembros_hogar"].gt(0))
        df["linea_pob"] = case_when(df, [(df["zona"].eq(1), df["linea_urbanogeneral"]), (df["zona"].eq(2), df["linea_ruralgeneral"])])
        df["linea_ind"] = case_when(df, [(df["zona"].eq(1), df["linea_urbanoextrema"]), (df["zona"].eq(2), df["linea_ruralextrema"])])
    output = pd.DataFrame({"macro_region_pobreza": df["macro_region"],
        "ing_total_pobreza_def": df["Ihog_ENCFT_a"], "ing_pc_pobreza_def": df["IPCm_ENCFT"],
        "linea_pobreza": df["linea_pob"], "linea_pobreza_extrema": df["linea_ind"]})
    missing = ~np.isfinite(df["IPCm_ENCFT"]) | ~np.isfinite(df["linea_pob"]) | ~np.isfinite(df["linea_ind"])
    output["pobreza_monetaria"] = case_when(df, [(missing, np.nan),
        (df["IPCm_ENCFT"] < df["linea_ind"], 1), (df["IPCm_ENCFT"] < df["linea_pob"], 2)], 3).astype("Int64")
    output["pobre"] = output["pobreza_monetaria"] < 3
    output["indigente"] = output["pobreza_monetaria"] == 1
    nominal = df.copy()
    if methodology == "2012":
        nominal["Inlab_nac_TrN_mon"] = nominal[["p_s4d11_1", "p_s4d11_2", "p_s4d11_3", "p_s4d11_4", "p_s4d11_7", "p_s4d12_1", "p_s4d12_2", "p_s4d12_3", "p_s4d12_6"]].sum(axis=1, skipna=True)
    raw = nominal[["Ilab_tot", "Inlab_nac_esp", "Inlab_nac_TrN_mon", "Inla_trE"]].sum(axis=1, skipna=True)
    output["ing_total_pobreza"] = raw.groupby([nominal[c] for c in group], sort=False).transform("sum") + nominal["p_s2_6"]
    extras = [col for col in df if col not in original and col not in output]
    if keep is True:
        output = pd.concat([output, df[extras]], axis=1)
    elif isinstance(keep, (list, tuple)):
        output = pd.concat([output, df[[col for col in keep if col in extras]]], axis=1)
    result = tbl.copy(deep=True)
    output.index = result.index
    for column in output:
        result[column] = output[column]
    return result


def prepare_poverty(tbl):
    """Resolve documented questionnaire aliases and optional methodology fields.

    This does not impute other required responses. Existing columns retain their
    names; added compatibility columns use uppercase names, as in the questionnaire.
    """
    require_columns(tbl, [])
    if len({c.lower() for c in tbl}) != len(tbl.columns):
        raise ValueError("Ambiguous column names after case normalization.")
    result = tbl.copy()
    lookup = {c.lower(): c for c in result}
    for target, source in PM22["alias_map"].items():
        if target not in lookup and source in lookup:
            result[target.upper()] = result[lookup[source]]
            lookup[target] = target.upper()
    for names, value in ((PM22["numeric_zero"], 0.0), (PM22["numeric_na"], np.nan)):
        for name in names:
            if name not in lookup:
                result[name.upper()] = value
    return result


def select_variables_pobreza(tbl):
    """Keep recognized questionnaire inputs and compatibility aliases in input order."""
    from .dictionaries import get_dict
    require_columns(tbl, [])
    names = {name.lower() for name in get_dict()} | set(PM22["numeric_zero"]) | set(PM22["numeric_na"]) | set(PM22["alias_map"])
    names.update(["periodo", "trimestre", "ano", "mes", "vivienda", "hogar", "miembro"])
    names.update(PM22["alias_map"].values())
    return tbl.loc[:, [name for name in tbl if name.lower() in names]].copy()


def pobreza_monetaria_2022(tbl, keep=False, reuse=False):
    """2022 poverty, regional deflators and lines, including school food income.

    Returns household/per-capita monthly DOP income, poverty lines, category
    (1 extreme, 2 general, 3 nonpoor), pobre and indigente. Missing inputs remain
    unclassified. keep retains intermediate components; reuse is compatibility-only.
    """
    return _pobreza_monetaria(tbl, keep, reuse, methodology="2022")


def pobreza_monetaria_2012(tbl, keep=False, reuse=False):
    """2012 poverty, national deflation and urban/rural lines from official code.

    Requires CANTIDAD_MIEMBROS_HOGAR as the per-capita denominator, matching the
    official reference. School food is excluded. Missing lines remain unclassified.
    keep retains intermediate components; reuse is accepted but recomputes results.
    """
    return _pobreza_monetaria(tbl, keep, reuse, methodology="2012")


def ing_total_pobreza(tbl, keep=False, reuse=False):
    """Compose the legacy income helpers into nominal and deflated household totals.

    This compatibility composition follows ftc_ing_total_pobreza in R. Use
    pobreza_monetaria_2012/2022 for the independently verified official workflows.
    keep/reuse accept booleans or lists of intermediate component names.
    """
    from .rules import run_rule
    names = ["ing_alquiler_imputado", "ing_laboral_monetario", "ing_no_monetario_laboral",
        "ing_monetario_no_laboral", "ing_no_monetario_no_laboral", "ing_transferencias_sociales", "ing_monetario_ext"]
    grouped = set(names) - {"ing_alquiler_imputado", "ing_transferencias_sociales"}
    if not isinstance(keep, (bool, list, tuple)) or not isinstance(reuse, (bool, list, tuple)):
        raise ValueError("keep/reuse must be bool or lists of component names.")
    df = tbl.copy()
    computed = []
    for name in names:
        retained = name in df if reuse is True else name in reuse if reuse is not False else False
        if not retained:
            df = run_rule(df, name, **({"keep": keep, "reuse": reuse} if name in grouped else {}))
            computed.append(name)
    require_columns(df, names + [name + "_def" for name in names] + ["TRIMESTRE", "VIVIENDA", "HOGAR"])
    income_names = names[1:]
    raw = df[income_names].sum(axis=1, skipna=False)
    adjusted = df[[name + "_def" for name in income_names]].sum(axis=1, skipna=False)
    keys = [df[name] for name in ("TRIMESTRE", "VIVIENDA", "HOGAR")]
    df["ing_total_pobreza"] = raw.groupby(keys, sort=False).transform(lambda x: x.sum(skipna=False)) + df["ing_alquiler_imputado"]
    df["ing_total_pobreza_def"] = adjusted.groupby(keys, sort=False).transform(lambda x: x.sum(skipna=False)) + df["ing_alquiler_imputado_def"]
    drop = [] if keep is True else [name for name in computed if keep is False or name not in keep]
    drop += [name + "_def" for name in computed if keep is False or isinstance(keep, (list, tuple)) and name + "_def" not in keep]
    return df.drop(columns=drop, errors="ignore")


def ing_pc_pobreza_def(tbl, keep=False, reuse=False):
    """Per-capita result of the legacy component composition; see ing_total_pobreza."""
    df = ing_total_pobreza(tbl, keep=keep, reuse=reuse)
    count = df.groupby(["TRIMESTRE", "VIVIENDA", "HOGAR"], sort=False)["HOGAR"].transform("size")
    df["ing_pc_pobreza_def"] = df["ing_total_pobreza_def"] / count
    return df
