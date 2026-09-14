# ing_comisiones

```python
encftr.ing_comisiones(tbl)
```

Calcula el indicador ing_comisiones. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `COMISIONES_AP_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
COMISIONES_AP_MONTO = as.double(COMISIONES_AP_MONTO)
ing_comisiones = case_when((is.na(COMISIONES_AP_MONTO) ~ 0), ((COMISIONES_AP_MONTO >= 0) ~ COMISIONES_AP_MONTO), (TRUE ~ 0))
ing_comisiones = as.double(ing_comisiones)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
