# Foreign interest and dividends

```python
encftr.ing_intereses_dividendos_ext(tbl)
```

Calculates foreign interest and dividends. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `INTERES_EXT_MONEDA`, `INTERES_EXT_MONTO`.

Calculation rules from the equivalent R implementation:

```r
# exchange rates for the preceding calendar month
ing_intereses_dividendos_ext = case_when(((INTERES_EXT_MONEDA == "DOP") ~ as.numeric(INTERES_EXT_MONTO)), ((INTERES_EXT_MONEDA == "BRL") ~ (as.numeric(INTERES_EXT_MONTO) * BRL)), ((INTERES_EXT_MONEDA == "CAD") ~ (as.numeric(INTERES_EXT_MONTO) * CAD)), ((INTERES_EXT_MONEDA == "CHF") ~ (as.numeric(INTERES_EXT_MONTO) * CHF)), ((INTERES_EXT_MONEDA == "CNY") ~ (as.numeric(INTERES_EXT_MONTO) * CNY)), ((INTERES_EXT_MONEDA == "DEG") ~ (as.numeric(INTERES_EXT_MONTO) * DEG)), ((INTERES_EXT_MONEDA == "DKK") ~ (as.numeric(INTERES_EXT_MONTO) * DKK)), ((INTERES_EXT_MONEDA == "EUR") ~ (as.numeric(INTERES_EXT_MONTO) * EUR)), ((INTERES_EXT_MONEDA == "GBP") ~ (as.numeric(INTERES_EXT_MONTO) * GBP)), ((INTERES_EXT_MONEDA == "JPY") ~ (as.numeric(INTERES_EXT_MONTO) * JPY)), ((INTERES_EXT_MONEDA == "NOK") ~ (as.numeric(INTERES_EXT_MONTO) * NOK)), ((INTERES_EXT_MONEDA == "LESC") ~ (as.numeric(INTERES_EXT_MONTO) * LESC)), ((INTERES_EXT_MONEDA == "SEK") ~ (as.numeric(INTERES_EXT_MONTO) * SEK)), ((INTERES_EXT_MONEDA == "USD") ~ (as.numeric(INTERES_EXT_MONTO) * USD)), ((INTERES_EXT_MONEDA == "VEF") ~ (as.numeric(INTERES_EXT_MONTO) * VEF)), ((INTERES_EXT_MONEDA == "ARS") ~ (as.numeric(INTERES_EXT_MONTO) * ARS)), (TRUE ~ 0))
ing_intereses_dividendos_ext = as.double(ing_intereses_dividendos_ext)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
