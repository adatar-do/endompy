# Non-monetary labour income

```python
encftr.ing_no_monetario_laboral(tbl, deflactar=True, keep=False, reuse=False)
```

Calculates non-monetary labour income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| deflactar | `True` | Applies the component deflator when true; preserves its nominal output. |
| keep | `False` | True retains components; a list retains selected names; false removes calculated helper columns. |
| reuse | `False` | In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute. |

Columns referenced by calculation rules: `OTROS_ESPECIE_AP`, `OTROS_ESPECIE_AP_MONTO`, `PAGO_EN_ESPECIE_AS_MONTO`, `PAGO_ESPECIES_IN_MONTO`, `PAGO_ESPECIES_IS_MONTO`.

Components: ing_especie_ocup_sec_cuenta_propia, ing_especie_ocup_sec_asalarariado, ing_especie_cuenta_propia, ing_especie_otros.

Calculation rules from the equivalent R implementation:

```r
ing_no_monetario_laboral = (((ing_especie_otros + ing_especie_cuenta_propia) + ing_especie_ocup_sec_asalarariado) + ing_especie_ocup_sec_cuenta_propia)
ing_no_monetario_laboral = as.double(ing_no_monetario_laboral)
# deflactar = TRUE
# join ipc_2020 by PERIODO
ing_no_monetario_laboral_def = ((IPCcentral / IPCanterior) * ing_no_monetario_laboral)
ing_no_monetario_laboral_def = as.double(ing_no_monetario_laboral_def)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
