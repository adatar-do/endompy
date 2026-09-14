# In-kind food income

```python
encftr.ing_especie_alimentos(tbl)
```

Calculates in-kind food income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `ALIMENTACION_ESPECIE_AP`, `ALIMENTACION_ESPECIE_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_especie_alimentos = case_when((is.na(ALIMENTACION_ESPECIE_AP_MONTO) ~ 0), ((ALIMENTACION_ESPECIE_AP == 1) ~ ALIMENTACION_ESPECIE_AP_MONTO), (TRUE ~ 0))
ing_especie_alimentos = as.double(ing_especie_alimentos)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
