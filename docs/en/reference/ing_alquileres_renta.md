# Domestic rental income

```python
encftr.ing_alquileres_renta(tbl)
```

Calculates domestic rental income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `ALQUILER_NAC`, `ALQUILER_NAC_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ALQUILER_NAC_MONTO = as.double(ALQUILER_NAC_MONTO)
ing_alquileres_renta = case_when((is.na(ALQUILER_NAC_MONTO) ~ 0), ((ALQUILER_NAC == 1) ~ ALQUILER_NAC_MONTO), (TRUE ~ 0))
ing_alquileres_renta = as.double(ing_alquileres_renta)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
