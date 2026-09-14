# ing_mensual_ocup_prin_cuenta_propia

```python
encftr.ing_mensual_ocup_prin_cuenta_propia(tbl)
```

Calcula el indicador ing_mensual_ocup_prin_cuenta_propia. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `GANANCIA_PRINC_IMP_MONTO`, `INGRESO_ACTIVIDAD_IN`, `INGRESO_ACTIVIDAD_IN_DIAS`, `INGRESO_ACTIVIDAD_IN_MONEDA`, `INGRESO_ACTIVIDAD_IN_MONTO`, `INGRESO_ACTIVIDAD_IN_PERIODO`.

Reglas de cálculo de la implementación R equivalente:

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

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
