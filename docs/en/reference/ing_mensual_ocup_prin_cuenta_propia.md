# Monthly main own-account occupation income

```python
encftr.ing_mensual_ocup_prin_cuenta_propia(tbl)
```

Calculates monthly main own-account occupation income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `GANANCIA_PRINC_IMP_MONTO`, `INGRESO_ACTIVIDAD_IN`, `INGRESO_ACTIVIDAD_IN_DIAS`, `INGRESO_ACTIVIDAD_IN_MONEDA`, `INGRESO_ACTIVIDAD_IN_MONTO`, `INGRESO_ACTIVIDAD_IN_PERIODO`.

Calculation rules from the equivalent R implementation:

```r
# exchange rates for the preceding calendar month
INGRESO_ACTIVIDAD_IN_MONTO = as.double(INGRESO_ACTIVIDAD_IN_MONTO)
ingprinctaprop = case_when(((INGRESO_ACTIVIDAD_IN_MONEDA == "DOP") ~ INGRESO_ACTIVIDAD_IN_MONTO), ((INGRESO_ACTIVIDAD_IN_MONEDA == "BRL") ~ (INGRESO_ACTIVIDAD_IN_MONTO * BRL)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "CAD") ~ (INGRESO_ACTIVIDAD_IN_MONTO * CAD)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "CHF") ~ (INGRESO_ACTIVIDAD_IN_MONTO * CHF)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "CNY") ~ (INGRESO_ACTIVIDAD_IN_MONTO * CNY)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "DEG") ~ (INGRESO_ACTIVIDAD_IN_MONTO * DEG)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "DKK") ~ (INGRESO_ACTIVIDAD_IN_MONTO * DKK)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "EUR") ~ (INGRESO_ACTIVIDAD_IN_MONTO * EUR)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "GBP") ~ (INGRESO_ACTIVIDAD_IN_MONTO * GBP)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "JPY") ~ (INGRESO_ACTIVIDAD_IN_MONTO * JPY)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "NOK") ~ (INGRESO_ACTIVIDAD_IN_MONTO * NOK)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "LESC") ~ (INGRESO_ACTIVIDAD_IN_MONTO * LESC)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "SEK") ~ (INGRESO_ACTIVIDAD_IN_MONTO * SEK)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "USD") ~ (INGRESO_ACTIVIDAD_IN_MONTO * USD)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "VEF") ~ (INGRESO_ACTIVIDAD_IN_MONTO * VEF)), ((INGRESO_ACTIVIDAD_IN_MONEDA == "ARS") ~ (INGRESO_ACTIVIDAD_IN_MONTO * ARS)), (TRUE ~ 0))
ingprinctaprop = as.double(ingprinctaprop)
periprinctaprop = ifelse(is.na(INGRESO_ACTIVIDAD_IN_PERIODO), 0, INGRESO_ACTIVIDAD_IN_PERIODO)
diasprinctaprop = ifelse(is.na(INGRESO_ACTIVIDAD_IN_DIAS), 0, INGRESO_ACTIVIDAD_IN_DIAS)
ing_mensual_ocup_prin_cuenta_propia = case_when(((periprinctaprop == 1) ~ ((diasprinctaprop * ingprinctaprop) * 4.3)), ((periprinctaprop == 2) ~ (ingprinctaprop * 4.3)), ((periprinctaprop == 3) ~ (ingprinctaprop * 2)), ((periprinctaprop == 4) ~ ingprinctaprop), ((INGRESO_ACTIVIDAD_IN == 2) ~ if_else(is.na(GANANCIA_PRINC_IMP_MONTO), 0, as.numeric(GANANCIA_PRINC_IMP_MONTO))), (TRUE ~ 0))
ing_mensual_ocup_prin_cuenta_propia = as.double(ing_mensual_ocup_prin_cuenta_propia)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
