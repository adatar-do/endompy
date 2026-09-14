# ing_intereses_dividendos

```python
encftr.ing_intereses_dividendos(tbl)
```

Calcula el indicador ing_intereses_dividendos. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `INTERESES_NAC`, `INTERESES_NAC_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
INTERESES_NAC_MONTO = as.double(INTERESES_NAC_MONTO)
ing_intereses_dividendos = case_when((is.na(INTERESES_NAC_MONTO) ~ 0), ((INTERESES_NAC == 1) ~ INTERESES_NAC_MONTO), (TRUE ~ 0))
ing_intereses_dividendos = as.double(ing_intereses_dividendos)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
