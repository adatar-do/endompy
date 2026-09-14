# Foreign gifts

```python
encftr.ing_regalos_ext(tbl)
```

Calculates foreign gifts. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `REGALOS_EXT`, `REGALOS_EXT_MONTO`.

Calculation rules from the equivalent R implementation:

```r
REGALOS_EXT_MONTO = as.double(REGALOS_EXT_MONTO)
ing_regalos_ext = case_when((is.na(REGALOS_EXT_MONTO) ~ 0), ((REGALOS_EXT == 1) ~ REGALOS_EXT_MONTO), (TRUE ~ 0))
ing_regalos_ext = as.double(ing_regalos_ext)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
