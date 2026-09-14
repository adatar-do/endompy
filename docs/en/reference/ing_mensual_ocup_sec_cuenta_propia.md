# Monthly secondary own-account occupation income

```python
encftr.ing_mensual_ocup_sec_cuenta_propia(tbl)
```

Calculates monthly secondary own-account occupation income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `GANANCIA_SECUN_IMP_MONTO`, `INGRESO_ACTIVIDAD_IS`, `INGRESO_ACTIVIDAD_IS_DIAS`, `INGRESO_ACTIVIDAD_IS_MONEDA`, `INGRESO_ACTIVIDAD_IS_MONTO`, `INGRESO_ACTIVIDAD_IS_PERIODO`.

Calculation rules from the equivalent R implementation:

```r
# exchange rates for the preceding calendar month
ingsecctaprop = case_when(((INGRESO_ACTIVIDAD_IS_MONEDA == "DOP") ~ INGRESO_ACTIVIDAD_IS_MONTO), ((INGRESO_ACTIVIDAD_IS_MONEDA == "BRL") ~ (INGRESO_ACTIVIDAD_IS_MONTO * BRL)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "CAD") ~ (INGRESO_ACTIVIDAD_IS_MONTO * CAD)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "CHF") ~ (INGRESO_ACTIVIDAD_IS_MONTO * CHF)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "CNY") ~ (INGRESO_ACTIVIDAD_IS_MONTO * CNY)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "DEG") ~ (INGRESO_ACTIVIDAD_IS_MONTO * DEG)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "DKK") ~ (INGRESO_ACTIVIDAD_IS_MONTO * DKK)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "EUR") ~ (INGRESO_ACTIVIDAD_IS_MONTO * EUR)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "GBP") ~ (INGRESO_ACTIVIDAD_IS_MONTO * GBP)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "JPY") ~ (INGRESO_ACTIVIDAD_IS_MONTO * JPY)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "NOK") ~ (INGRESO_ACTIVIDAD_IS_MONTO * NOK)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "LESC") ~ (INGRESO_ACTIVIDAD_IS_MONTO * LESC)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "SEK") ~ (INGRESO_ACTIVIDAD_IS_MONTO * SEK)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "USD") ~ (INGRESO_ACTIVIDAD_IS_MONTO * USD)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "VEF") ~ (INGRESO_ACTIVIDAD_IS_MONTO * VEF)), ((INGRESO_ACTIVIDAD_IS_MONEDA == "ARS") ~ (INGRESO_ACTIVIDAD_IS_MONTO * ARS)), (TRUE ~ 0))
ingsecctaprop = as.double(ingsecctaprop)
perisecctaprop = ifelse(is.na(INGRESO_ACTIVIDAD_IS_PERIODO), 0, as.numeric(INGRESO_ACTIVIDAD_IS_PERIODO))
diassecctaprop = ifelse(is.na(INGRESO_ACTIVIDAD_IS_DIAS), 0, as.numeric(INGRESO_ACTIVIDAD_IS_DIAS))
ing_mensual_ocup_sec_cuenta_propia = case_when(((perisecctaprop == 1) ~ ((4.3 * diassecctaprop) * ingsecctaprop)), ((perisecctaprop == 2) ~ (4.3 * ingsecctaprop)), ((perisecctaprop == 3) ~ (2 * ingsecctaprop)), ((perisecctaprop == 4) ~ ingsecctaprop), ((INGRESO_ACTIVIDAD_IS == 2) ~ ifelse(is.na(GANANCIA_SECUN_IMP_MONTO), 0, as.numeric(GANANCIA_SECUN_IMP_MONTO))), (TRUE ~ 0))
ing_mensual_ocup_sec_cuenta_propia = as.double(ing_mensual_ocup_sec_cuenta_propia)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
