# ing_otros_ocup_sec_asalariado

```python
encftr.ing_otros_ocup_sec_asalariado(tbl)
```

Calcula el indicador ing_otros_ocup_sec_asalariado. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `OTROS_PAGO_AS_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
OTROS_PAGO_AS_MONTO = as.double(OTROS_PAGO_AS_MONTO)
ing_otros_ocup_sec_asalariado = case_when((is.na(OTROS_PAGO_AS_MONTO) ~ 0), ((OTROS_PAGO_AS_MONTO >= 0) ~ OTROS_PAGO_AS_MONTO), (TRUE ~ 0))
ing_otros_ocup_sec_asalariado = as.double(ing_otros_ocup_sec_asalariado)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
