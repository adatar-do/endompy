# In-kind housing income

```python
encftr.ing_especie_viviendas(tbl)
```

Calculates in-kind housing income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `VIVIENDA_ESPECIE_AP`, `VIVIENDA_ESPECIE_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_especie_viviendas = case_when((is.na(VIVIENDA_ESPECIE_AP_MONTO) ~ 0), ((VIVIENDA_ESPECIE_AP == 1) ~ as.numeric(VIVIENDA_ESPECIE_AP_MONTO)), (TRUE ~ 0))
ing_especie_viviendas = as.double(ing_especie_viviendas)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
