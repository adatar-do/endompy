# ing_alquiler_imputado

```python
encftr.ing_alquiler_imputado(tbl, deflactar=True)
```

Calcula el indicador ing_alquiler_imputado. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| deflactar | `True` | Aplica el deflactor del componente cuando es verdadero; conserva su salida nominal. |

Columnas referidas por las reglas: `MONTO_ALQUILARIA_VIVIENDA_MES`.

Reglas de cálculo de la implementación R equivalente:

```r
ing_alquiler_imputado = case_when((is.na(MONTO_ALQUILARIA_VIVIENDA_MES) ~ 0), ((MONTO_ALQUILARIA_VIVIENDA_MES >= 0) ~ MONTO_ALQUILARIA_VIVIENDA_MES), (TRUE ~ 0))
ing_alquiler_imputado = as.double(ing_alquiler_imputado)
# deflactar = TRUE
# join ipc_2020 by PERIODO
ing_alquiler_imputado_def = ((IPCcentral / IPCanterior) * ing_alquiler_imputado)
ing_alquiler_imputado_def = as.double(ing_alquiler_imputado_def)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
