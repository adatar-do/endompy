# ing_no_monetario_laboral

```python
encftr.ing_no_monetario_laboral(tbl, deflactar=True, keep=False, reuse=False)
```

Calcula el indicador ing_no_monetario_laboral. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| deflactar | `True` | Aplica el deflactor del componente cuando es verdadero; conserva su salida nominal. |
| keep | `False` | Verdadero conserva componentes; una lista conserva los nombres indicados; falso retira los auxiliares calculados. |
| reuse | `False` | En auxiliares: reutiliza componentes disponibles o nombrados. En pobreza 2012/2022 se acepta y siempre recalcula. |

Columnas referidas por las reglas: `OTROS_ESPECIE_AP`, `OTROS_ESPECIE_AP_MONTO`, `PAGO_EN_ESPECIE_AS_MONTO`, `PAGO_ESPECIES_IN_MONTO`, `PAGO_ESPECIES_IS_MONTO`.

Componentes: ing_especie_ocup_sec_cuenta_propia, ing_especie_ocup_sec_asalarariado, ing_especie_cuenta_propia, ing_especie_otros.

Reglas de cálculo de la implementación R equivalente:

```r
ing_no_monetario_laboral = (((ing_especie_otros + ing_especie_cuenta_propia) + ing_especie_ocup_sec_asalarariado) + ing_especie_ocup_sec_cuenta_propia)
ing_no_monetario_laboral = as.double(ing_no_monetario_laboral)
# deflactar = TRUE
# join ipc_2020 by PERIODO
ing_no_monetario_laboral_def = ((IPCcentral / IPCanterior) * ing_no_monetario_laboral)
ing_no_monetario_laboral_def = as.double(ing_no_monetario_laboral_def)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
