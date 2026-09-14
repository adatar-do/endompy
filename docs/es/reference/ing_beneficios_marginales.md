# ing_beneficios_marginales

```python
encftr.ing_beneficios_marginales(tbl)
```

Calcula el indicador ing_beneficios_marginales. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `BENEFICIOS_MARGINALES_AP_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
ing_beneficios_marginales = case_when((is.na(BENEFICIOS_MARGINALES_AP_MONTO) ~ 0), ((BENEFICIOS_MARGINALES_AP_MONTO >= 0) ~ (as.numeric(BENEFICIOS_MARGINALES_AP_MONTO) / 12)), (TRUE ~ 0))
ing_beneficios_marginales = as.double(ing_beneficios_marginales)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
