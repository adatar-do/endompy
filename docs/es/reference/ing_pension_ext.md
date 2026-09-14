# ing_pension_ext

```python
encftr.ing_pension_ext(tbl)
```

Calcula el indicador ing_pension_ext. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `PENSION_EXT_MONEDA`, `PENSION_EXT_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
# exchange rates for the preceding calendar month
PENSION_EXT_MONTO = ifelse(is.na(PENSION_EXT_MONTO), 0, PENSION_EXT_MONTO)
PENSION_EXT_MONEDA = ifelse(is.na(PENSION_EXT_MONEDA), 0, PENSION_EXT_MONEDA)
PENSION_EXT_MONTO = as.double(PENSION_EXT_MONTO)
ing_pension_ext = case_when(((PENSION_EXT_MONEDA == "DOP") ~ PENSION_EXT_MONTO), ((PENSION_EXT_MONEDA == "BRL") ~ (PENSION_EXT_MONTO * BRL)), ((PENSION_EXT_MONEDA == "CAD") ~ (PENSION_EXT_MONTO * CAD)), ((PENSION_EXT_MONEDA == "CHF") ~ (PENSION_EXT_MONTO * CHF)), ((PENSION_EXT_MONEDA == "CNY") ~ (PENSION_EXT_MONTO * CNY)), ((PENSION_EXT_MONEDA == "DEG") ~ (PENSION_EXT_MONTO * DEG)), ((PENSION_EXT_MONEDA == "DKK") ~ (PENSION_EXT_MONTO * DKK)), ((PENSION_EXT_MONEDA == "EUR") ~ (PENSION_EXT_MONTO * EUR)), ((PENSION_EXT_MONEDA == "GBP") ~ (PENSION_EXT_MONTO * GBP)), ((PENSION_EXT_MONEDA == "JPY") ~ (PENSION_EXT_MONTO * JPY)), ((PENSION_EXT_MONEDA == "NOK") ~ (PENSION_EXT_MONTO * NOK)), ((PENSION_EXT_MONEDA == "LESC") ~ (PENSION_EXT_MONTO * LESC)), ((PENSION_EXT_MONEDA == "SEK") ~ (PENSION_EXT_MONTO * SEK)), ((PENSION_EXT_MONEDA == "USD") ~ (PENSION_EXT_MONTO * USD)), ((PENSION_EXT_MONEDA == "VEF") ~ (PENSION_EXT_MONTO * VEF)), ((PENSION_EXT_MONEDA == "ARS") ~ (PENSION_EXT_MONTO * ARS)), (TRUE ~ 0))
ing_pension_ext = as.double(ing_pension_ext)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
