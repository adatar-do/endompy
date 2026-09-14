# ing_mensual_ocup_prin

```python
encftr.ing_mensual_ocup_prin(tbl)
```

Calcula el indicador ing_mensual_ocup_prin. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Reglas de cálculo de la implementación R equivalente:

```r
ing_mensual_ocup_prin = ((ing_mensual_ocup_prin_asalariado + ing_mensual_ocup_prin_cuenta_propia) + ing_mensual_ocup_prin_independiente)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
