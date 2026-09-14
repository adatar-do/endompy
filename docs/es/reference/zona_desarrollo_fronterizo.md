# zona_desarrollo_fronterizo

```python
encftr.zona_desarrollo_fronterizo(tbl)
```

Calcula el indicador zona_desarrollo_fronterizo. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `ID_PROVINCIA`.

Reglas de cálculo de la implementación R equivalente:

```r
zona_desarrollo_fronterizo = case_when(((ID_PROVINCIA %in% c(16, 10, 7, 5, 15, 26, 3)) ~ 1), (TRUE ~ 0))
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
