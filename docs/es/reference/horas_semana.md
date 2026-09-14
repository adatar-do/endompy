# horas_semana

```python
encftr.horas_semana(tbl)
```

Calcula el indicador horas_semana. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `HORAS_TRABAJA_SEMANA_PRINCIPAL`, `HORAS_TRABAJO_EFECT_TOTAL`.

Reglas de cálculo de la implementación R equivalente:

```r
horas_semana = case_when(((HORAS_TRABAJO_EFECT_TOTAL == 0) ~ HORAS_TRABAJA_SEMANA_PRINCIPAL), (TRUE ~ HORAS_TRABAJO_EFECT_TOTAL))
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
