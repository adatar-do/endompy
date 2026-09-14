# Monthly secondary independent occupation income

```python
encftr.ing_mensual_ocup_sec_independiente(tbl)
```

Calculates monthly secondary independent occupation income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `GANANCIA_IS_PRODUCTOR`, `GANANCIA_IS_PRODUCTOR_MONEDA`, `GANANCIA_IS_PRODUCTOR_MONTO`, `GANANCIA_SECUN_IMP_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_mensual_ocup_sec_independiente = case_when(((GANANCIA_IS_PRODUCTOR_MONEDA == "DOP") ~ (as.numeric(GANANCIA_IS_PRODUCTOR_MONTO) / 6)), ((GANANCIA_IS_PRODUCTOR == 2) ~ as.numeric(GANANCIA_SECUN_IMP_MONTO)), (TRUE ~ 0))
ing_mensual_ocup_sec_independiente = as.double(ing_mensual_ocup_sec_independiente)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
