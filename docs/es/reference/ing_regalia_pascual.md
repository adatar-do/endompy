# ing_regalia_pascual

```python
encftr.ing_regalia_pascual(tbl)
```

Calcula el indicador ing_regalia_pascual. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `REGALIA_AP`, `REGALIA_AP_MONTO`, `REGALIA_PASCUAL`.

Reglas de cálculo de la implementación R equivalente:

```r
ing_regalia_pascual = case_when(((REGALIA_AP_MONTO >= 0) ~ (REGALIA_AP_MONTO / 12)), ((REGALIA_AP == 2) ~ REGALIA_PASCUAL), (TRUE ~ 0))
ing_regalia_pascual = as.double(ing_regalia_pascual)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
