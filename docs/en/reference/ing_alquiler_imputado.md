# Imputed dwelling rent

```python
encftr.ing_alquiler_imputado(tbl, deflactar=True)
```

Calculates imputed dwelling rent. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| deflactar | `True` | Applies the component deflator when true; preserves its nominal output. |

Columns referenced by calculation rules: `MONTO_ALQUILARIA_VIVIENDA_MES`.

Calculation rules from the equivalent R implementation:

```r
ing_alquiler_imputado = case_when((is.na(MONTO_ALQUILARIA_VIVIENDA_MES) ~ 0), ((MONTO_ALQUILARIA_VIVIENDA_MES >= 0) ~ MONTO_ALQUILARIA_VIVIENDA_MES), (TRUE ~ 0))
ing_alquiler_imputado = as.double(ing_alquiler_imputado)
# deflactar = TRUE
# join ipc_2020 by PERIODO
ing_alquiler_imputado_def = ((IPCcentral / IPCanterior) * ing_alquiler_imputado)
ing_alquiler_imputado_def = as.double(ing_alquiler_imputado_def)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
