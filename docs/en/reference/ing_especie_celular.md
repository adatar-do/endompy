# In-kind mobile phone income

```python
encftr.ing_especie_celular(tbl)
```

Calculates in-kind mobile phone income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `CELULAR_ESPECIE_AP`, `CELULAR_ESPECIE_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
CELULAR_ESPECIE_AP_MONTO = as.double(CELULAR_ESPECIE_AP_MONTO)
ing_especie_celular = case_when((is.na(CELULAR_ESPECIE_AP_MONTO) ~ 0), ((CELULAR_ESPECIE_AP == 1) ~ CELULAR_ESPECIE_AP_MONTO), (TRUE ~ 0))
ing_especie_celular = as.double(ing_especie_celular)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
