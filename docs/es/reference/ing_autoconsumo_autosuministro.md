# ing_autoconsumo_autosuministro

```python
encftr.ing_autoconsumo_autosuministro(tbl)
```

Calcula el indicador ing_autoconsumo_autosuministro. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `CONSUMIO_BIENES_IN`, `CONSUMIO_BIENES_IN_MONTO`, `CONSUMIO_BIENES_IS_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
autoconsumoprin = case_when(((is.na(CONSUMIO_BIENES_IN) | is.na(CONSUMIO_BIENES_IN_MONTO)) ~ 0), ((CONSUMIO_BIENES_IN_MONTO > 0) ~ CONSUMIO_BIENES_IN_MONTO), (TRUE ~ 0))
ing_autoconsumo_autosuministro = case_when(((CONSUMIO_BIENES_IS_MONTO > 0) ~ CONSUMIO_BIENES_IS_MONTO), (TRUE ~ 0))
ing_autoconsumo_autosuministro = as.double((ing_autoconsumo_autosuministro + autoconsumoprin))
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
