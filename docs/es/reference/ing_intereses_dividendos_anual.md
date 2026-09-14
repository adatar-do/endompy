# ing_intereses_dividendos_anual

```python
encftr.ing_intereses_dividendos_anual(tbl)
```

Calcula el indicador ing_intereses_dividendos_anual. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `INTERESES_NAC_ANO`, `INTERESES_NAC_ANO_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
ing_intereses_dividendos_anual = case_when((is.na(INTERESES_NAC_ANO) ~ 0), ((INTERESES_NAC_ANO == 1) ~ (as.numeric(INTERESES_NAC_ANO_MONTO) / 12)), (TRUE ~ 0))
ing_intereses_dividendos_anual = as.double(ing_intereses_dividendos_anual)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
