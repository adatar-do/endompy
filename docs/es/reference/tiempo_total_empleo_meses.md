# tiempo_total_empleo_meses

```python
encftr.tiempo_total_empleo_meses(tbl)
```

Calcula el indicador tiempo_total_empleo_meses. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Reglas de cálculo de la implementación R equivalente:

```r
tiempo_total_empleo_meses = (tiempo_total_empleo_dias / (((365.25 / 12)))
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
