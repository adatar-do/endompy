# ing_especie_ocup_sec_cuenta_propia

```python
encftr.ing_especie_ocup_sec_cuenta_propia(tbl)
```

Calcula el indicador ing_especie_ocup_sec_cuenta_propia. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `PAGO_ESPECIES_IS_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
ing_especie_ocup_sec_cuenta_propia = case_when(((PAGO_ESPECIES_IS_MONTO > 0) ~ as.numeric(PAGO_ESPECIES_IS_MONTO)), (TRUE ~ 0))
ing_especie_ocup_sec_cuenta_propia = as.double(ing_especie_ocup_sec_cuenta_propia)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
