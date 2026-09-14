# perceptores_ingresos

```python
encftr.perceptores_ingresos(tbl, min_edad=15)
```

Calcula el indicador perceptores_ingresos. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| min_edad | `15` | Límite inferior inclusivo de edad en años. |

Columnas referidas por las reglas: `CATEGORIA_PRINCIPAL`.

Reglas de cálculo de la implementación R equivalente:

```r
perceptores_ingresos = case_when(((((EDAD >= min_edad) & (CATEGORIA_PRINCIPAL %in% (1 : 7))) & (OCUPADO == 1)) ~ 1), ((OCUPADO == 0) ~ 0))
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
