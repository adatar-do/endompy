# ing_monetario_ext

```python
encftr.ing_monetario_ext(tbl, deflactar=True, keep=False, reuse=False)
```

Calcula el indicador ing_monetario_ext. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| deflactar | `True` | Aplica el deflactor del componente cuando es verdadero; conserva su salida nominal. |
| keep | `False` | Verdadero conserva componentes; una lista conserva los nombres indicados; falso retira los auxiliares calculados. |
| reuse | `False` | En auxiliares: reutiliza componentes disponibles o nombrados. En pobreza 2012/2022 se acepta y siempre recalcula. |

Columnas referidas por las reglas: `ALQUILER_EXT_MONEDA`, `ALQUILER_EXT_MONTO`, `INTERES_EXT_MONEDA`, `INTERES_EXT_MONTO`, `PENSION_EXT_MONEDA`, `PENSION_EXT_MONTO`, `REGALOS_EXT`, `REGALOS_EXT_MONTO`.

Componentes: ing_pension_ext, ing_intereses_dividendos_ext, ing_alquileres_renta_ext, ing_regalos_ext, ing_remesas_ext.

Reglas de cálculo de la implementación R equivalente:

```r
mext_1 = (((ing_pension_ext + ing_intereses_dividendos_ext) + ing_alquileres_renta_ext) + ing_regalos_ext)
mext_2 = ing_remesas_ext
ing_monetario_ext = (mext_1 + mext_2)
mext_1 = as.double(mext_1)
mext_2 = as.double(mext_2)
ing_monetario_ext = as.double(ing_monetario_ext)
# deflactar = TRUE
# join ipc_2020 by PERIODO
mext_1_def = ((IPCcentral / IPCanterior) * mext_1)
mext_1_def = as.double(mext_1_def)
mext_2_def = ((IPCcentral / IPCprom) * mext_2)
mext_2_def = as.double(mext_2_def)
ing_monetario_ext_def = (mext_1_def + mext_2_def)
ing_monetario_ext_def = as.double(ing_monetario_ext_def)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
