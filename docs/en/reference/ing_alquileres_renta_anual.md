# Annual domestic rental income, monthly equivalent

```python
encftr.ing_alquileres_renta_anual(tbl)
```

Calculates annual domestic rental income, monthly equivalent. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `ALQUILER_NAC_ANO`, `ALQUILER_NAC_ANO_MONTO`.

Calculation rules from the equivalent R implementation:

```r
ing_alquileres_renta_anual = case_when((is.na(ALQUILER_NAC_ANO) ~ 0), ((ALQUILER_NAC_ANO == 1) ~ (as.numeric(ALQUILER_NAC_ANO_MONTO) / 12)), (TRUE ~ 0))
ing_alquileres_renta_anual = as.double(ing_alquileres_renta_anual)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
