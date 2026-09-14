# Annual domestic remittances, monthly equivalent

```python
encftr.ing_remesas_nacionales_anual(tbl)
```

Calculates annual domestic remittances, monthly equivalent. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `REMESAS_NAC_ANO`, `REMESAS_NAC_ANO_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_remesas_nacionales_anual = case_when((is.na(REMESAS_NAC_ANO) ~ 0), ((REMESAS_NAC_ANO == 1) ~ (REMESAS_NAC_ANO_MONTO / 12)), (TRUE ~ 0))
ing_remesas_nacionales_anual = as.double(ing_remesas_nacionales_anual)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
