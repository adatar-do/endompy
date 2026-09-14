# regiones_desarrollo

```python
encftr.regiones_desarrollo(tbl)
```

Calcula el indicador regiones_desarrollo. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `ID_PROVINCIA`.

Reglas de cálculo de la implementación R equivalente:

```r
regiones_desarrollo = case_when(((ID_PROVINCIA %in% c(25, 18, 9)) ~ 1), ((ID_PROVINCIA %in% c(13, 24, 28)) ~ 2), ((ID_PROVINCIA %in% c(6, 19, 14, 20)) ~ 3), ((ID_PROVINCIA %in% c(27, 15, 5, 26)) ~ 4), ((ID_PROVINCIA %in% c(21, 2, 17, 31)) ~ 5), ((ID_PROVINCIA %in% c(4, 3, 16, 10)) ~ 6), ((ID_PROVINCIA %in% c(22, 7)) ~ 7), ((ID_PROVINCIA %in% c(12, 11, 8)) ~ 8), ((ID_PROVINCIA %in% c(23, 30, 29)) ~ 9), ((ID_PROVINCIA %in% c(1, 32)) ~ 10))
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
