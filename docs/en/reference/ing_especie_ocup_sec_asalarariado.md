# In-kind secondary salaried income

```python
encftr.ing_especie_ocup_sec_asalarariado(tbl)
```

Calculates in-kind secondary salaried income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `PAGO_EN_ESPECIE_AS_MONTO`.

Calculation rules from the equivalent R implementation:

```r
PAGO_EN_ESPECIE_AS_MONTO = as.double(PAGO_EN_ESPECIE_AS_MONTO)
ing_especie_ocup_sec_asalarariado = case_when((is.na(PAGO_EN_ESPECIE_AS_MONTO) ~ 0), ((PAGO_EN_ESPECIE_AS_MONTO > 0) ~ PAGO_EN_ESPECIE_AS_MONTO), (TRUE ~ 0))
ing_especie_ocup_sec_asalarariado = as.double(ing_especie_ocup_sec_asalarariado)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
