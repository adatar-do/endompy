# Monthly main salaried occupation income

```python
encftr.ing_mensual_ocup_prin_asalariado(tbl)
```

Calculates monthly main salaried occupation income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `HORAS_TRABAJO_EFECT_TOTAL`, `SALARIO_PRINC_IMP_MONTO`, `SUELDO_BRUTO_AP`, `SUELDO_BRUTO_AP_MONEDA`, `SUELDO_BRUTO_AP_MONTO`, `TIEMPO_RECIBE_PAGO_AP`, `TIEMPO_RECIBE_PAGO_DIAS_AP`.

Calculation rules from the equivalent R implementation:

```r
# exchange rates for the preceding calendar month
ingasal = case_when((is.na(SUELDO_BRUTO_AP_MONEDA) ~ 0), (is.na(SUELDO_BRUTO_AP_MONTO) ~ 0), ((SUELDO_BRUTO_AP_MONEDA == "DOP") ~ SUELDO_BRUTO_AP_MONTO), ((SUELDO_BRUTO_AP_MONEDA == "BRL") ~ (SUELDO_BRUTO_AP_MONTO * BRL)), ((SUELDO_BRUTO_AP_MONEDA == "CAD") ~ (SUELDO_BRUTO_AP_MONTO * CAD)), ((SUELDO_BRUTO_AP_MONEDA == "CHF") ~ (SUELDO_BRUTO_AP_MONTO * CHF)), ((SUELDO_BRUTO_AP_MONEDA == "CNY") ~ (SUELDO_BRUTO_AP_MONTO * CNY)), ((SUELDO_BRUTO_AP_MONEDA == "DEG") ~ (SUELDO_BRUTO_AP_MONTO * DEG)), ((SUELDO_BRUTO_AP_MONEDA == "DKK") ~ (SUELDO_BRUTO_AP_MONTO * DKK)), ((SUELDO_BRUTO_AP_MONEDA == "EUR") ~ (SUELDO_BRUTO_AP_MONTO * EUR)), ((SUELDO_BRUTO_AP_MONEDA == "GBP") ~ (SUELDO_BRUTO_AP_MONTO * GBP)), ((SUELDO_BRUTO_AP_MONEDA == "JPY") ~ (SUELDO_BRUTO_AP_MONTO * JPY)), ((SUELDO_BRUTO_AP_MONEDA == "NOK") ~ (SUELDO_BRUTO_AP_MONTO * NOK)), ((SUELDO_BRUTO_AP_MONEDA == "LESC") ~ (SUELDO_BRUTO_AP_MONTO * LESC)), ((SUELDO_BRUTO_AP_MONEDA == "SEK") ~ (SUELDO_BRUTO_AP_MONTO * SEK)), ((SUELDO_BRUTO_AP_MONEDA == "USD") ~ (SUELDO_BRUTO_AP_MONTO * USD)), ((SUELDO_BRUTO_AP_MONEDA == "VEF") ~ (SUELDO_BRUTO_AP_MONTO * VEF)), ((SUELDO_BRUTO_AP_MONEDA == "ARS") ~ (SUELDO_BRUTO_AP_MONTO * ARS)), (TRUE ~ 0))
ingasal = as.double(ingasal)
horasocupprin = if_else(is.na(HORAS_TRABAJO_EFECT_TOTAL), 0, HORAS_TRABAJO_EFECT_TOTAL)
periocupprin = if_else(is.na(TIEMPO_RECIBE_PAGO_AP), 0, TIEMPO_RECIBE_PAGO_AP)
diasocupprin = if_else(is.na(TIEMPO_RECIBE_PAGO_DIAS_AP), 0, TIEMPO_RECIBE_PAGO_DIAS_AP)
ing_mensual_ocup_prin_asalariado = case_when((is.na(periocupprin) ~ 0), ((periocupprin == 1) ~ ((as.numeric(diasocupprin) * ingasal) * 4.3)), ((periocupprin == 2) ~ (ingasal * 4.3)), ((periocupprin == 3) ~ (ingasal * 2)), ((periocupprin == 4) ~ ingasal), ((SUELDO_BRUTO_AP == 2) ~ if_else(is.na(SALARIO_PRINC_IMP_MONTO), 0, as.numeric(SALARIO_PRINC_IMP_MONTO))), (TRUE ~ 0))
ing_mensual_ocup_prin_asalariado = as.double(ing_mensual_ocup_prin_asalariado)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
