# Domestic pension income

```python
encftr.ing_pension_jubilacion(tbl)
```

Calculates domestic pension income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `PENSION_IMP_MONTO`, `PENSION_NAC`, `PENSION_NAC_MONTO`.

Calculation rules from the equivalent R implementation:

```r
PENSION_NAC_MONTO = as.double(PENSION_NAC_MONTO)
ing_pension_jubilacion = case_when((is.na(PENSION_NAC_MONTO) ~ 0), ((PENSION_NAC == 1) ~ as.numeric(PENSION_NAC_MONTO)), ((PENSION_NAC == 3) ~ as.numeric(PENSION_IMP_MONTO)), (TRUE ~ 0))
ing_pension_jubilacion = as.double(ing_pension_jubilacion)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
