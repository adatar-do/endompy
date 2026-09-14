# ing_especie_ocup_sec_asalarariado

```python
encftr.ing_especie_ocup_sec_asalarariado(tbl)
```

Calcula el indicador ing_especie_ocup_sec_asalarariado. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `PAGO_EN_ESPECIE_AS_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
PAGO_EN_ESPECIE_AS_MONTO = as.double(PAGO_EN_ESPECIE_AS_MONTO)
ing_especie_ocup_sec_asalarariado = case_when((is.na(PAGO_EN_ESPECIE_AS_MONTO) ~ 0), ((PAGO_EN_ESPECIE_AS_MONTO > 0) ~ PAGO_EN_ESPECIE_AS_MONTO), (TRUE ~ 0))
ing_especie_ocup_sec_asalarariado = as.double(ing_especie_ocup_sec_asalarariado)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
