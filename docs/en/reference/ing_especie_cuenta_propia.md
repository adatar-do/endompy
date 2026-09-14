# In-kind self-employment income

```python
encftr.ing_especie_cuenta_propia(tbl)
```

Calculates in-kind self-employment income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `PAGO_ESPECIES_IN_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_especie_cuenta_propia = case_when((is.na(PAGO_ESPECIES_IN_MONTO) ~ 0), ((PAGO_ESPECIES_IN_MONTO > 0) ~ as.numeric(PAGO_ESPECIES_IN_MONTO)), (TRUE ~ 0))
ing_especie_cuenta_propia = as.double(ing_especie_cuenta_propia)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
