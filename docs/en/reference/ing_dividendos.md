# Employment dividends

```python
encftr.ing_dividendos(tbl)
```

Calculates employment dividends. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `DIVIDENDOS_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_dividendos = case_when((is.na(DIVIDENDOS_AP_MONTO) ~ 0), ((DIVIDENDOS_AP_MONTO >= 0) ~ (as.numeric(DIVIDENDOS_AP_MONTO) / 12)), (TRUE ~ 0))
ing_dividendos = as.double(ing_dividendos)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
