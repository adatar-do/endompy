# ing_intereses_dividendos_ext

```python
encftr.ing_intereses_dividendos_ext(tbl)
```

Calcula el indicador ing_intereses_dividendos_ext. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `INTERES_EXT_MONEDA`, `INTERES_EXT_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
# exchange rates for the preceding calendar month
ing_intereses_dividendos_ext = case_when(((INTERES_EXT_MONEDA == "DOP") ~ as.numeric(INTERES_EXT_MONTO)), ((INTERES_EXT_MONEDA == "BRL") ~ (as.numeric(INTERES_EXT_MONTO) * BRL)), ((INTERES_EXT_MONEDA == "CAD") ~ (as.numeric(INTERES_EXT_MONTO) * CAD)), ((INTERES_EXT_MONEDA == "CHF") ~ (as.numeric(INTERES_EXT_MONTO) * CHF)), ((INTERES_EXT_MONEDA == "CNY") ~ (as.numeric(INTERES_EXT_MONTO) * CNY)), ((INTERES_EXT_MONEDA == "DEG") ~ (as.numeric(INTERES_EXT_MONTO) * DEG)), ((INTERES_EXT_MONEDA == "DKK") ~ (as.numeric(INTERES_EXT_MONTO) * DKK)), ((INTERES_EXT_MONEDA == "EUR") ~ (as.numeric(INTERES_EXT_MONTO) * EUR)), ((INTERES_EXT_MONEDA == "GBP") ~ (as.numeric(INTERES_EXT_MONTO) * GBP)), ((INTERES_EXT_MONEDA == "JPY") ~ (as.numeric(INTERES_EXT_MONTO) * JPY)), ((INTERES_EXT_MONEDA == "NOK") ~ (as.numeric(INTERES_EXT_MONTO) * NOK)), ((INTERES_EXT_MONEDA == "LESC") ~ (as.numeric(INTERES_EXT_MONTO) * LESC)), ((INTERES_EXT_MONEDA == "SEK") ~ (as.numeric(INTERES_EXT_MONTO) * SEK)), ((INTERES_EXT_MONEDA == "USD") ~ (as.numeric(INTERES_EXT_MONTO) * USD)), ((INTERES_EXT_MONEDA == "VEF") ~ (as.numeric(INTERES_EXT_MONTO) * VEF)), ((INTERES_EXT_MONEDA == "ARS") ~ (as.numeric(INTERES_EXT_MONTO) * ARS)), (TRUE ~ 0))
ing_intereses_dividendos_ext = as.double(ing_intereses_dividendos_ext)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
