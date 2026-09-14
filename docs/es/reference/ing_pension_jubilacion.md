# ing_pension_jubilacion

```python
encftr.ing_pension_jubilacion(tbl)
```

Calcula el indicador ing_pension_jubilacion. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `PENSION_IMP_MONTO`, `PENSION_NAC`, `PENSION_NAC_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
PENSION_NAC_MONTO = as.double(PENSION_NAC_MONTO)
ing_pension_jubilacion = case_when((is.na(PENSION_NAC_MONTO) ~ 0), ((PENSION_NAC == 1) ~ as.numeric(PENSION_NAC_MONTO)), ((PENSION_NAC == 3) ~ as.numeric(PENSION_IMP_MONTO)), (TRUE ~ 0))
ing_pension_jubilacion = as.double(ing_pension_jubilacion)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
