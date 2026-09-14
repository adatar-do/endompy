# ing_no_monetario_no_laboral

```python
encftr.ing_no_monetario_no_laboral(tbl, deflactar=True, keep=False, reuse=False)
```

Calcula el indicador ing_no_monetario_no_laboral. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| deflactar | `True` | Aplica el deflactor del componente cuando es verdadero; conserva su salida nominal. |
| keep | `False` | Verdadero conserva componentes; una lista conserva los nombres indicados; falso retira los auxiliares calculados. |
| reuse | `False` | En auxiliares: reutiliza componentes disponibles o nombrados. En pobreza 2012/2022 se acepta y siempre recalcula. |

Columnas referidas por las reglas: `AYUDA_ESPECIE_NAC_MONTO`, `CONSUMIO_BIENES_IN`, `CONSUMIO_BIENES_IN_MONTO`, `CONSUMIO_BIENES_IS_MONTO`.

Componentes: ing_autoconsumo_autosuministro, ing_especie_ayuda_ong.

Reglas de cálculo de la implementación R equivalente:

```r
ing_no_monetario_no_laboral = (ing_especie_ayuda_ong + ing_autoconsumo_autosuministro)
ing_no_monetario_no_laboral = as.double(ing_no_monetario_no_laboral)
# deflactar = TRUE
# join ipc_2020 by PERIODO
ing_no_monetario_no_laboral_def = ((IPCcentral / IPCanterior) * ing_no_monetario_no_laboral)
ing_no_monetario_no_laboral_def = as.double(ing_no_monetario_no_laboral_def)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
