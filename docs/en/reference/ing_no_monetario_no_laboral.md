# Domestic non-labour in-kind income

```python
encftr.ing_no_monetario_no_laboral(tbl, deflactar=True, keep=False, reuse=False)
```

Calculates domestic non-labour in-kind income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| deflactar | `True` | Applies the component deflator when true; preserves its nominal output. |
| keep | `False` | True retains components; a list retains selected names; false removes calculated helper columns. |
| reuse | `False` | In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute. |

Columns referenced by calculation rules: `AYUDA_ESPECIE_NAC_MONTO`, `CONSUMIO_BIENES_IN`, `CONSUMIO_BIENES_IN_MONTO`, `CONSUMIO_BIENES_IS_MONTO`.

Components: ing_autoconsumo_autosuministro, ing_especie_ayuda_ong.

Calculation rules from the equivalent R implementation:

```r
ing_no_monetario_no_laboral = (ing_especie_ayuda_ong + ing_autoconsumo_autosuministro)
ing_no_monetario_no_laboral = as.double(ing_no_monetario_no_laboral)
# deflactar = TRUE
# join ipc_2020 by PERIODO
ing_no_monetario_no_laboral_def = ((IPCcentral / IPCanterior) * ing_no_monetario_no_laboral)
ing_no_monetario_no_laboral_def = as.double(ing_no_monetario_no_laboral_def)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
