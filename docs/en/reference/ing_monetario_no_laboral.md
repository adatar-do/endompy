# Domestic non-labour monetary income

```python
encftr.ing_monetario_no_laboral(tbl, deflactar=True, keep=False, reuse=False)
```

Calculates domestic non-labour monetary income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| deflactar | `True` | Applies the component deflator when true; preserves its nominal output. |
| keep | `False` | True retains components; a list retains selected names; false removes calculated helper columns. |
| reuse | `False` | In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute. |

Columns referenced by calculation rules: `ALQUILER_NAC`, `ALQUILER_NAC_ANO`, `ALQUILER_NAC_ANO_MONTO`, `ALQUILER_NAC_MONTO`, `AYUDA_ESPECIE_NAC_ANO_MONTO`, `INTERESES_NAC`, `INTERESES_NAC_ANO`, `INTERESES_NAC_ANO_MONTO`, `INTERESES_NAC_MONTO`, `PENSION_IMP_MONTO`, `PENSION_NAC`, `PENSION_NAC_MONTO`, `REMESAS_NAC`, `REMESAS_NAC_ANO`, `REMESAS_NAC_ANO_MONTO`, `REMESAS_NAC_MONTO`.

Components: ing_remesas_nacionales, ing_alquileres_renta, ing_intereses_dividendos, ing_pension_jubilacion, ing_especie_ayuda_ong_anual, ing_remesas_nacionales_anual, ing_alquileres_renta_anual, ing_intereses_dividendos_anual.

Calculation rules from the equivalent R implementation:

```r
mnl_1 = (((ing_intereses_dividendos_anual + ing_alquileres_renta_anual) + ing_remesas_nacionales_anual) + ing_especie_ayuda_ong_anual)
mnl_2 = (((ing_pension_jubilacion + ing_intereses_dividendos) + ing_alquileres_renta) + ing_remesas_nacionales)
ing_monetario_no_laboral = (mnl_1 + mnl_2)
ing_monetario_no_laboral = as.double(ing_monetario_no_laboral)
mnl_1 = as.double(mnl_1)
mnl_2 = as.double(mnl_2)
# deflactar = TRUE
# join ipc_2020 by PERIODO
mnl_2_def = ((IPCcentral / IPCanterior) * mnl_2)
mnl_2_def = as.double(mnl_2_def)
ing_monetario_no_laboral_def = (mnl_1 + mnl_2_def)
ing_monetario_no_laboral_def = as.double(ing_monetario_no_laboral_def)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
