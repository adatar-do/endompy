# ingreso_laboral_total

```python
encftr.ingreso_laboral_total(tbl)
```

Calcula el indicador ingreso_laboral_total. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `BONO_VACACIONES`, `HORAS_EXTRA`, `INCENTIVO_ANTIGUEDAD`, `INGRESO_ASALARIADO`, `INGRESO_INDEPENDIENTES`, `OTROS_BENEFICIOS`, `OTROS_PAGOS`, `REGALIA_PASCUAL`.

Reglas de cálculo de la implementación R equivalente:

```r
ingreso_laboral_total = ((((((((((INGRESO_ASALARIADO + COMISIONES) + PROPINAS) + HORAS_EXTRA) + OTROS_PAGOS) + BONO_VACACIONES) + BONIFICACIONES) + REGALIA_PASCUAL) + INCENTIVO_ANTIGUEDAD) + OTROS_BENEFICIOS) + INGRESO_INDEPENDIENTES)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
