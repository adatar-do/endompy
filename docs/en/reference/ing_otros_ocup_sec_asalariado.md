# Other secondary salaried occupation income

```python
encftr.ing_otros_ocup_sec_asalariado(tbl)
```

Calculates other secondary salaried occupation income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `OTROS_PAGO_AS_MONTO`.

Calculation rules from the equivalent R implementation:

```r
OTROS_PAGO_AS_MONTO = as.double(OTROS_PAGO_AS_MONTO)
ing_otros_ocup_sec_asalariado = case_when((is.na(OTROS_PAGO_AS_MONTO) ~ 0), ((OTROS_PAGO_AS_MONTO >= 0) ~ OTROS_PAGO_AS_MONTO), (TRUE ~ 0))
ing_otros_ocup_sec_asalariado = as.double(ing_otros_ocup_sec_asalariado)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
