# Foreign pension income

```python
encftr.ing_pension_ext(tbl)
```

Calculates foreign pension income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `PENSION_EXT_MONEDA`, `PENSION_EXT_MONTO`.

Calculation rules from the equivalent R implementation:

```r
# exchange rates for the preceding calendar month
PENSION_EXT_MONTO = ifelse(is.na(PENSION_EXT_MONTO), 0, PENSION_EXT_MONTO)
PENSION_EXT_MONEDA = ifelse(is.na(PENSION_EXT_MONEDA), 0, PENSION_EXT_MONEDA)
PENSION_EXT_MONTO = as.double(PENSION_EXT_MONTO)
ing_pension_ext = case_when(((PENSION_EXT_MONEDA == "DOP") ~ PENSION_EXT_MONTO), ((PENSION_EXT_MONEDA == "BRL") ~ (PENSION_EXT_MONTO * BRL)), ((PENSION_EXT_MONEDA == "CAD") ~ (PENSION_EXT_MONTO * CAD)), ((PENSION_EXT_MONEDA == "CHF") ~ (PENSION_EXT_MONTO * CHF)), ((PENSION_EXT_MONEDA == "CNY") ~ (PENSION_EXT_MONTO * CNY)), ((PENSION_EXT_MONEDA == "DEG") ~ (PENSION_EXT_MONTO * DEG)), ((PENSION_EXT_MONEDA == "DKK") ~ (PENSION_EXT_MONTO * DKK)), ((PENSION_EXT_MONEDA == "EUR") ~ (PENSION_EXT_MONTO * EUR)), ((PENSION_EXT_MONEDA == "GBP") ~ (PENSION_EXT_MONTO * GBP)), ((PENSION_EXT_MONEDA == "JPY") ~ (PENSION_EXT_MONTO * JPY)), ((PENSION_EXT_MONEDA == "NOK") ~ (PENSION_EXT_MONTO * NOK)), ((PENSION_EXT_MONEDA == "LESC") ~ (PENSION_EXT_MONTO * LESC)), ((PENSION_EXT_MONEDA == "SEK") ~ (PENSION_EXT_MONTO * SEK)), ((PENSION_EXT_MONEDA == "USD") ~ (PENSION_EXT_MONTO * USD)), ((PENSION_EXT_MONEDA == "VEF") ~ (PENSION_EXT_MONTO * VEF)), ((PENSION_EXT_MONEDA == "ARS") ~ (PENSION_EXT_MONTO * ARS)), (TRUE ~ 0))
ing_pension_ext = as.double(ing_pension_ext)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
