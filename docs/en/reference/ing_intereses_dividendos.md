# Domestic interest and dividends

```python
encftr.ing_intereses_dividendos(tbl)
```

Calculates domestic interest and dividends. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `INTERESES_NAC`, `INTERESES_NAC_MONTO`.

Calculation rules from the equivalent R implementation:

```r
INTERESES_NAC_MONTO = as.double(INTERESES_NAC_MONTO)
ing_intereses_dividendos = case_when((is.na(INTERESES_NAC_MONTO) ~ 0), ((INTERESES_NAC == 1) ~ INTERESES_NAC_MONTO), (TRUE ~ 0))
ing_intereses_dividendos = as.double(ing_intereses_dividendos)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
