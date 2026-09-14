# Annual domestic pension income, monthly equivalent

```python
encftr.ing_pension_jubilacion_anual(tbl)
```

Calculates annual domestic pension income, monthly equivalent. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `REGALIA_PENSION_NAC_ANO`, `REGALIA_PENSION_NAC_ANO_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_pension_jubilacion_anual = case_when((is.na(REGALIA_PENSION_NAC_ANO) ~ 0), ((REGALIA_PENSION_NAC_ANO == 1) ~ (REGALIA_PENSION_NAC_ANO_MONTO / 12)), (TRUE ~ 0))
ing_pension_jubilacion_anual = as.double(ing_pension_jubilacion_anual)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
