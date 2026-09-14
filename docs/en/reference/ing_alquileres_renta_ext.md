# Foreign rental income

```python
encftr.ing_alquileres_renta_ext(tbl)
```

Calculates foreign rental income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `ALQUILER_EXT_MONEDA`, `ALQUILER_EXT_MONTO`.

Calculation rules from the equivalent R implementation:

```r
# exchange rates for the preceding calendar month
ing_alquileres_renta_ext = case_when(((ALQUILER_EXT_MONEDA == "DOP") ~ as.numeric(ALQUILER_EXT_MONTO)), ((ALQUILER_EXT_MONEDA == "BRL") ~ (as.numeric(ALQUILER_EXT_MONTO) * BRL)), ((ALQUILER_EXT_MONEDA == "CAD") ~ (as.numeric(ALQUILER_EXT_MONTO) * CAD)), ((ALQUILER_EXT_MONEDA == "CHF") ~ (as.numeric(ALQUILER_EXT_MONTO) * CHF)), ((ALQUILER_EXT_MONEDA == "CNY") ~ (as.numeric(ALQUILER_EXT_MONTO) * CNY)), ((ALQUILER_EXT_MONEDA == "DEG") ~ (as.numeric(ALQUILER_EXT_MONTO) * DEG)), ((ALQUILER_EXT_MONEDA == "DKK") ~ (as.numeric(ALQUILER_EXT_MONTO) * DKK)), ((ALQUILER_EXT_MONEDA == "EUR") ~ (as.numeric(ALQUILER_EXT_MONTO) * EUR)), ((ALQUILER_EXT_MONEDA == "GBP") ~ (as.numeric(ALQUILER_EXT_MONTO) * GBP)), ((ALQUILER_EXT_MONEDA == "JPY") ~ (as.numeric(ALQUILER_EXT_MONTO) * JPY)), ((ALQUILER_EXT_MONEDA == "NOK") ~ (as.numeric(ALQUILER_EXT_MONTO) * NOK)), ((ALQUILER_EXT_MONEDA == "LESC") ~ (as.numeric(ALQUILER_EXT_MONTO) * LESC)), ((ALQUILER_EXT_MONEDA == "SEK") ~ (as.numeric(ALQUILER_EXT_MONTO) * SEK)), ((ALQUILER_EXT_MONEDA == "USD") ~ (as.numeric(ALQUILER_EXT_MONTO) * USD)), ((ALQUILER_EXT_MONEDA == "VEF") ~ (as.numeric(ALQUILER_EXT_MONTO) * VEF)), ((ALQUILER_EXT_MONEDA == "ARS") ~ (as.numeric(ALQUILER_EXT_MONTO) * ARS)), (TRUE ~ 0))
ing_alquileres_renta_ext = as.double(ing_alquileres_renta_ext)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
