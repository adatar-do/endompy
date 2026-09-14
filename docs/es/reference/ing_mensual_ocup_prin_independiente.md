# ing_mensual_ocup_prin_independiente

```python
encftr.ing_mensual_ocup_prin_independiente(tbl)
```

Calcula el indicador ing_mensual_ocup_prin_independiente. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `GANANCIA_IN_PRODUCTOR`, `GANANCIA_IN_PRODUCTOR_MONEDA`, `GANANCIA_IN_PRODUCTOR_MONTO`, `GANANCIA_PRINC_IMP_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
ing_mensual_ocup_prin_independiente = case_when((is.na(GANANCIA_IN_PRODUCTOR) ~ 0), ((is.na(GANANCIA_IN_PRODUCTOR_MONTO) & is.na(GANANCIA_PRINC_IMP_MONTO)) ~ 0), ((GANANCIA_IN_PRODUCTOR_MONEDA == "DOP") ~ (as.numeric(GANANCIA_IN_PRODUCTOR_MONTO) / 6)), ((GANANCIA_IN_PRODUCTOR == 2) ~ as.numeric(GANANCIA_PRINC_IMP_MONTO)), (TRUE ~ 0))
ing_mensual_ocup_prin_independiente = as.double(ing_mensual_ocup_prin_independiente)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
