# Own consumption and self-supply income

```python
encftr.ing_autoconsumo_autosuministro(tbl)
```

Calculates own consumption and self-supply income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `CONSUMIO_BIENES_IN`, `CONSUMIO_BIENES_IN_MONTO`, `CONSUMIO_BIENES_IS_MONTO`.

Calculation rules from the equivalent R implementation:

```r
autoconsumoprin = case_when(((is.na(CONSUMIO_BIENES_IN) | is.na(CONSUMIO_BIENES_IN_MONTO)) ~ 0), ((CONSUMIO_BIENES_IN_MONTO > 0) ~ CONSUMIO_BIENES_IN_MONTO), (TRUE ~ 0))
ing_autoconsumo_autosuministro = case_when(((CONSUMIO_BIENES_IS_MONTO > 0) ~ CONSUMIO_BIENES_IS_MONTO), (TRUE ~ 0))
ing_autoconsumo_autosuministro = as.double((ing_autoconsumo_autosuministro + autoconsumoprin))
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
