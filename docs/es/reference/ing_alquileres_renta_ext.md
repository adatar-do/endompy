# ing_alquileres_renta_ext

```python
encftr.ing_alquileres_renta_ext(tbl)
```

Calcula el indicador ing_alquileres_renta_ext. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `ALQUILER_EXT_MONEDA`, `ALQUILER_EXT_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
# exchange rates for the preceding calendar month
ing_alquileres_renta_ext = case_when(((ALQUILER_EXT_MONEDA == "DOP") ~ as.numeric(ALQUILER_EXT_MONTO)), ((ALQUILER_EXT_MONEDA == "BRL") ~ (as.numeric(ALQUILER_EXT_MONTO) * BRL)), ((ALQUILER_EXT_MONEDA == "CAD") ~ (as.numeric(ALQUILER_EXT_MONTO) * CAD)), ((ALQUILER_EXT_MONEDA == "CHF") ~ (as.numeric(ALQUILER_EXT_MONTO) * CHF)), ((ALQUILER_EXT_MONEDA == "CNY") ~ (as.numeric(ALQUILER_EXT_MONTO) * CNY)), ((ALQUILER_EXT_MONEDA == "DEG") ~ (as.numeric(ALQUILER_EXT_MONTO) * DEG)), ((ALQUILER_EXT_MONEDA == "DKK") ~ (as.numeric(ALQUILER_EXT_MONTO) * DKK)), ((ALQUILER_EXT_MONEDA == "EUR") ~ (as.numeric(ALQUILER_EXT_MONTO) * EUR)), ((ALQUILER_EXT_MONEDA == "GBP") ~ (as.numeric(ALQUILER_EXT_MONTO) * GBP)), ((ALQUILER_EXT_MONEDA == "JPY") ~ (as.numeric(ALQUILER_EXT_MONTO) * JPY)), ((ALQUILER_EXT_MONEDA == "NOK") ~ (as.numeric(ALQUILER_EXT_MONTO) * NOK)), ((ALQUILER_EXT_MONEDA == "LESC") ~ (as.numeric(ALQUILER_EXT_MONTO) * LESC)), ((ALQUILER_EXT_MONEDA == "SEK") ~ (as.numeric(ALQUILER_EXT_MONTO) * SEK)), ((ALQUILER_EXT_MONEDA == "USD") ~ (as.numeric(ALQUILER_EXT_MONTO) * USD)), ((ALQUILER_EXT_MONEDA == "VEF") ~ (as.numeric(ALQUILER_EXT_MONTO) * VEF)), ((ALQUILER_EXT_MONEDA == "ARS") ~ (as.numeric(ALQUILER_EXT_MONTO) * ARS)), (TRUE ~ 0))
ing_alquileres_renta_ext = as.double(ing_alquileres_renta_ext)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
