# ing_especie_alimentos

```python
encftr.ing_especie_alimentos(tbl)
```

Calcula el indicador ing_especie_alimentos. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `ALIMENTACION_ESPECIE_AP`, `ALIMENTACION_ESPECIE_AP_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
ing_especie_alimentos = case_when((is.na(ALIMENTACION_ESPECIE_AP_MONTO) ~ 0), ((ALIMENTACION_ESPECIE_AP == 1) ~ ALIMENTACION_ESPECIE_AP_MONTO), (TRUE ~ 0))
ing_especie_alimentos = as.double(ing_especie_alimentos)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
