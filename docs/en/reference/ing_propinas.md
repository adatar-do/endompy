# Tips

```python
encftr.ing_propinas(tbl)
```

Calculates tips. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `PROPINAS_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
PROPINAS_AP_MONTO = as.double(PROPINAS_AP_MONTO)
ing_propinas = case_when((is.na(PROPINAS_AP_MONTO) ~ 0), ((PROPINAS_AP_MONTO >= 0) ~ PROPINAS_AP_MONTO), (TRUE ~ 0))
ing_propinas = as.double(ing_propinas)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
