# Other in-kind income

```python
encftr.ing_especie_otros(tbl)
```

Calculates other in-kind income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `OTROS_ESPECIE_AP`, `OTROS_ESPECIE_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_especie_otros = case_when((is.na(OTROS_ESPECIE_AP_MONTO) ~ 0), ((OTROS_ESPECIE_AP == 1) ~ as.numeric(OTROS_ESPECIE_AP_MONTO)), (TRUE ~ 0))
ing_especie_otros = as.double(ing_especie_otros)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
