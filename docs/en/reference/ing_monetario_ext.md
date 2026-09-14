# Foreign monetary income

```python
encftr.ing_monetario_ext(tbl, deflactar=True, keep=False, reuse=False)
```

Calculates foreign monetary income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| deflactar | `True` | Applies the component deflator when true; preserves its nominal output. |
| keep | `False` | True retains components; a list retains selected names; false removes calculated helper columns. |
| reuse | `False` | In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute. |

Columns referenced by calculation rules: `ALQUILER_EXT_MONEDA`, `ALQUILER_EXT_MONTO`, `INTERES_EXT_MONEDA`, `INTERES_EXT_MONTO`, `PENSION_EXT_MONEDA`, `PENSION_EXT_MONTO`, `REGALOS_EXT`, `REGALOS_EXT_MONTO`.

Components: ing_pension_ext, ing_intereses_dividendos_ext, ing_alquileres_renta_ext, ing_regalos_ext, ing_remesas_ext.

Calculation rules from the equivalent R implementation:

```r
mext_1 = (((ing_pension_ext + ing_intereses_dividendos_ext) + ing_alquileres_renta_ext) + ing_regalos_ext)
mext_2 = ing_remesas_ext
ing_monetario_ext = (mext_1 + mext_2)
mext_1 = as.double(mext_1)
mext_2 = as.double(mext_2)
ing_monetario_ext = as.double(ing_monetario_ext)
# deflactar = TRUE
# join ipc_2020 by PERIODO
mext_1_def = ((IPCcentral / IPCanterior) * mext_1)
mext_1_def = as.double(mext_1_def)
mext_2_def = ((IPCcentral / IPCprom) * mext_2)
mext_2_def = as.double(mext_2_def)
ing_monetario_ext_def = (mext_1_def + mext_2_def)
ing_monetario_ext_def = as.double(ing_monetario_ext_def)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
