# ing_propinas

```python
encftr.ing_propinas(tbl)
```

Calcula el indicador ing_propinas. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `PROPINAS_AP_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
PROPINAS_AP_MONTO = as.double(PROPINAS_AP_MONTO)
ing_propinas = case_when((is.na(PROPINAS_AP_MONTO) ~ 0), ((PROPINAS_AP_MONTO >= 0) ~ PROPINAS_AP_MONTO), (TRUE ~ 0))
ing_propinas = as.double(ing_propinas)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
