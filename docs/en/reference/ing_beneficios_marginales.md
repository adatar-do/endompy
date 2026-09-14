# Fringe benefits

```python
encftr.ing_beneficios_marginales(tbl)
```

Calculates fringe benefits. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `BENEFICIOS_MARGINALES_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_beneficios_marginales = case_when((is.na(BENEFICIOS_MARGINALES_AP_MONTO) ~ 0), ((BENEFICIOS_MARGINALES_AP_MONTO >= 0) ~ (as.numeric(BENEFICIOS_MARGINALES_AP_MONTO) / 12)), (TRUE ~ 0))
ing_beneficios_marginales = as.double(ing_beneficios_marginales)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
