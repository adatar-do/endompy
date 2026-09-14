# Overtime income

```python
encftr.ing_horas_extra(tbl)
```

Calculates overtime income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `HORAS_EXTRA_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
HORAS_EXTRA_AP_MONTO = as.double(HORAS_EXTRA_AP_MONTO)
ing_horas_extra = case_when((is.na(HORAS_EXTRA_AP_MONTO) ~ 0), ((HORAS_EXTRA_AP_MONTO >= 0) ~ HORAS_EXTRA_AP_MONTO), (TRUE ~ 0))
ing_horas_extra = as.double(ing_horas_extra)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
