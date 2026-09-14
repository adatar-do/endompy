# ing_remesas_nacionales

```python
encftr.ing_remesas_nacionales(tbl)
```

Calcula el indicador ing_remesas_nacionales. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `REMESAS_NAC`, `REMESAS_NAC_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
REMESAS_NAC_MONTO = as.double(REMESAS_NAC_MONTO)
ing_remesas_nacionales = case_when((is.na(REMESAS_NAC_MONTO) ~ 0), ((REMESAS_NAC == 1) ~ REMESAS_NAC_MONTO), (TRUE ~ 0))
ing_remesas_nacionales = as.double(ing_remesas_nacionales)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
