# Domestic remittances

```python
encftr.ing_remesas_nacionales(tbl)
```

Calculates domestic remittances. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `REMESAS_NAC`, `REMESAS_NAC_MONTO`.

Calculation rules from the equivalent R implementation:

```r
REMESAS_NAC_MONTO = as.double(REMESAS_NAC_MONTO)
ing_remesas_nacionales = case_when((is.na(REMESAS_NAC_MONTO) ~ 0), ((REMESAS_NAC == 1) ~ REMESAS_NAC_MONTO), (TRUE ~ 0))
ing_remesas_nacionales = as.double(ing_remesas_nacionales)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
