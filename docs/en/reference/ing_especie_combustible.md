# In-kind fuel income

```python
encftr.ing_especie_combustible(tbl)
```

Calculates in-kind fuel income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `GASOLINA_ESPECIE_AP`, `GASOLINA_ESPECIE_AP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
GASOLINA_ESPECIE_AP_MONTO = as.double(GASOLINA_ESPECIE_AP_MONTO)
ing_especie_combustible = case_when((is.na(GASOLINA_ESPECIE_AP_MONTO) ~ 0), ((GASOLINA_ESPECIE_AP == 1) ~ GASOLINA_ESPECIE_AP_MONTO), (TRUE ~ 0))
ing_especie_combustible = as.double(ing_especie_combustible)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
