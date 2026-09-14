# ing_especie_combustible

```python
encftr.ing_especie_combustible(tbl)
```

Calcula el indicador ing_especie_combustible. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `GASOLINA_ESPECIE_AP`, `GASOLINA_ESPECIE_AP_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
GASOLINA_ESPECIE_AP_MONTO = as.double(GASOLINA_ESPECIE_AP_MONTO)
ing_especie_combustible = case_when((is.na(GASOLINA_ESPECIE_AP_MONTO) ~ 0), ((GASOLINA_ESPECIE_AP == 1) ~ GASOLINA_ESPECIE_AP_MONTO), (TRUE ~ 0))
ing_especie_combustible = as.double(ing_especie_combustible)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
