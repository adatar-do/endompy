# Christmas bonus, monthly equivalent

```python
encftr.ing_regalia_pascual(tbl)
```

Calculates christmas bonus, monthly equivalent. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `REGALIA_AP`, `REGALIA_AP_MONTO`, `REGALIA_PASCUAL`.

Calculation rules from the equivalent R implementation:

```r
ing_regalia_pascual = case_when(((REGALIA_AP_MONTO >= 0) ~ (REGALIA_AP_MONTO / 12)), ((REGALIA_AP == 2) ~ REGALIA_PASCUAL), (TRUE ~ 0))
ing_regalia_pascual = as.double(ing_regalia_pascual)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
