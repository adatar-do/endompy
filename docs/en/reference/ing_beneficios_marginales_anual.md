# Annual fringe benefits, monthly equivalent

```python
encftr.ing_beneficios_marginales_anual(tbl)
```

Calculates annual fringe benefits, monthly equivalent. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `OTROS_BENEFICIOS_AS_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_beneficios_marginales_anual = case_when((is.na(OTROS_BENEFICIOS_AS_MONTO) ~ 0), ((OTROS_BENEFICIOS_AS_MONTO >= 0) ~ (OTROS_BENEFICIOS_AS_MONTO / 12)), (TRUE ~ 0))
ing_beneficios_marginales_anual = as.double(ing_beneficios_marginales_anual)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
