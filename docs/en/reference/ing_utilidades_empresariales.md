# Business profit sharing, monthly equivalent

```python
encftr.ing_utilidades_empresariales(tbl)
```

Calculates business profit sharing, monthly equivalent. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `UTILIDAD_EMPRESARIAL_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_utilidades_empresariales = case_when((is.na(UTILIDAD_EMPRESARIAL_AP_MONTO) ~ 0), ((UTILIDAD_EMPRESARIAL_AP_MONTO >= 0) ~ (as.numeric(UTILIDAD_EMPRESARIAL_AP_MONTO) / 12)), (TRUE ~ 0))
ing_utilidades_empresariales = as.double(ing_utilidades_empresariales)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
