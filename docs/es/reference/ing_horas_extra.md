# ing_horas_extra

```python
encftr.ing_horas_extra(tbl)
```

Calcula el indicador ing_horas_extra. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `HORAS_EXTRA_AP_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
HORAS_EXTRA_AP_MONTO = as.double(HORAS_EXTRA_AP_MONTO)
ing_horas_extra = case_when((is.na(HORAS_EXTRA_AP_MONTO) ~ 0), ((HORAS_EXTRA_AP_MONTO >= 0) ~ HORAS_EXTRA_AP_MONTO), (TRUE ~ 0))
ing_horas_extra = as.double(ing_horas_extra)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
