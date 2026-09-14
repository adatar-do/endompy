# ing_monetario_no_laboral

```python
encftr.ing_monetario_no_laboral(tbl, deflactar=True, keep=False, reuse=False)
```

Calcula el indicador ing_monetario_no_laboral. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| deflactar | `True` | Aplica el deflactor del componente cuando es verdadero; conserva su salida nominal. |
| keep | `False` | Verdadero conserva componentes; una lista conserva los nombres indicados; falso retira los auxiliares calculados. |
| reuse | `False` | En auxiliares: reutiliza componentes disponibles o nombrados. En pobreza 2012/2022 se acepta y siempre recalcula. |

Columnas referidas por las reglas: `ALQUILER_NAC`, `ALQUILER_NAC_ANO`, `ALQUILER_NAC_ANO_MONTO`, `ALQUILER_NAC_MONTO`, `AYUDA_ESPECIE_NAC_ANO_MONTO`, `INTERESES_NAC`, `INTERESES_NAC_ANO`, `INTERESES_NAC_ANO_MONTO`, `INTERESES_NAC_MONTO`, `PENSION_IMP_MONTO`, `PENSION_NAC`, `PENSION_NAC_MONTO`, `REMESAS_NAC`, `REMESAS_NAC_ANO`, `REMESAS_NAC_ANO_MONTO`, `REMESAS_NAC_MONTO`.

Componentes: ing_remesas_nacionales, ing_alquileres_renta, ing_intereses_dividendos, ing_pension_jubilacion, ing_especie_ayuda_ong_anual, ing_remesas_nacionales_anual, ing_alquileres_renta_anual, ing_intereses_dividendos_anual.

Reglas de cálculo de la implementación R equivalente:

```r
mnl_1 = (((ing_intereses_dividendos_anual + ing_alquileres_renta_anual) + ing_remesas_nacionales_anual) + ing_especie_ayuda_ong_anual)
mnl_2 = (((ing_pension_jubilacion + ing_intereses_dividendos) + ing_alquileres_renta) + ing_remesas_nacionales)
ing_monetario_no_laboral = (mnl_1 + mnl_2)
ing_monetario_no_laboral = as.double(ing_monetario_no_laboral)
mnl_1 = as.double(mnl_1)
mnl_2 = as.double(mnl_2)
# deflactar = TRUE
# join ipc_2020 by PERIODO
mnl_2_def = ((IPCcentral / IPCanterior) * mnl_2)
mnl_2_def = as.double(mnl_2_def)
ing_monetario_no_laboral_def = (mnl_1 + mnl_2_def)
ing_monetario_no_laboral_def = as.double(ing_monetario_no_laboral_def)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
