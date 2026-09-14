# tiempo_total_empleo_dias

```python
encftr.tiempo_total_empleo_dias(tbl)
```

Calcula el indicador tiempo_total_empleo_dias. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `TIEMPO_EMPLEO_ANOS`, `TIEMPO_EMPLEO_DIAS`, `TIEMPO_EMPLEO_MESES`.

Reglas de cálculo de la implementación R equivalente:

```r
tiempo_total_empleo_dias = (((TIEMPO_EMPLEO_ANOS * 365.25) + ((TIEMPO_EMPLEO_MESES * 365.25) / 12)) + TIEMPO_EMPLEO_DIAS)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
