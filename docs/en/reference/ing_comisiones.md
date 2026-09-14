# Commissions

```python
encftr.ing_comisiones(tbl)
```

Calculates commissions. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `COMISIONES_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
COMISIONES_AP_MONTO = as.double(COMISIONES_AP_MONTO)
ing_comisiones = case_when((is.na(COMISIONES_AP_MONTO) ~ 0), ((COMISIONES_AP_MONTO >= 0) ~ COMISIONES_AP_MONTO), (TRUE ~ 0))
ing_comisiones = as.double(ing_comisiones)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
