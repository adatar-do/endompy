# In-kind transport income

```python
encftr.ing_especie_transporte(tbl)
```

Calculates in-kind transport income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `TRANSPORTE_ESPECIE_AP`, `TRANSPORTE_ESPECIE_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
TRANSPORTE_ESPECIE_AP_MONTO = as.double(TRANSPORTE_ESPECIE_AP_MONTO)
ing_especie_transporte = case_when((is.na(TRANSPORTE_ESPECIE_AP_MONTO) ~ 0), ((TRANSPORTE_ESPECIE_AP == 1) ~ TRANSPORTE_ESPECIE_AP_MONTO), (TRUE ~ 0))
ing_especie_transporte = as.double(ing_especie_transporte)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
