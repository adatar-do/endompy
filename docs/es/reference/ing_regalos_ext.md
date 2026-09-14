# ing_regalos_ext

```python
encftr.ing_regalos_ext(tbl)
```

Calcula el indicador ing_regalos_ext. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `REGALOS_EXT`, `REGALOS_EXT_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
REGALOS_EXT_MONTO = as.double(REGALOS_EXT_MONTO)
ing_regalos_ext = case_when((is.na(REGALOS_EXT_MONTO) ~ 0), ((REGALOS_EXT == 1) ~ REGALOS_EXT_MONTO), (TRUE ~ 0))
ing_regalos_ext = as.double(ing_regalos_ext)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
