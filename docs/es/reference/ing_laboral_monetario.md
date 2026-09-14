# ing_laboral_monetario

```python
encftr.ing_laboral_monetario(tbl, deflactar=True, keep=False, reuse=False)
```

Calcula el indicador ing_laboral_monetario. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| deflactar | `True` | Aplica el deflactor del componente cuando es verdadero; conserva su salida nominal. |
| keep | `False` | Verdadero conserva componentes; una lista conserva los nombres indicados; falso retira los auxiliares calculados. |
| reuse | `False` | En auxiliares: reutiliza componentes disponibles o nombrados. En pobreza 2012/2022 se acepta y siempre recalcula. |

Columnas referidas por las reglas: `ALIMENTACION_ESPECIE_AP`, `ALIMENTACION_ESPECIE_AP_MONTO`, `BENEFICIOS_MARGINALES_AP_MONTO`, `BONIFICACION_AP_MONTO`, `CELULAR_ESPECIE_AP`, `CELULAR_ESPECIE_AP_MONTO`, `COMISIONES_AP_MONTO`, `DIVIDENDOS_AP_MONTO`, `GANANCIA_IN_PRODUCTOR`, `GANANCIA_IN_PRODUCTOR_MONEDA`, `GANANCIA_IN_PRODUCTOR_MONTO`, `GANANCIA_IS_PRODUCTOR`, `GANANCIA_IS_PRODUCTOR_MONEDA`, `GANANCIA_IS_PRODUCTOR_MONTO`, `GANANCIA_PRINC_IMP_MONTO`, `GANANCIA_SECUN_IMP_MONTO`, `GASOLINA_ESPECIE_AP`, `GASOLINA_ESPECIE_AP_MONTO`, `HORAS_EXTRA_AP_MONTO`, `HORAS_TRABAJO_EFECT_TOTAL`, `INGRESO_ACTIVIDAD_IN`, `INGRESO_ACTIVIDAD_IN_DIAS`, `INGRESO_ACTIVIDAD_IN_MONEDA`, `INGRESO_ACTIVIDAD_IN_MONTO`, `INGRESO_ACTIVIDAD_IN_PERIODO`, `INGRESO_ACTIVIDAD_IS`, `INGRESO_ACTIVIDAD_IS_DIAS`, `INGRESO_ACTIVIDAD_IS_MONEDA`, `INGRESO_ACTIVIDAD_IS_MONTO`, `INGRESO_ACTIVIDAD_IS_PERIODO`, `OTROS_BENEFICIOS_AS_MONTO`, `OTROS_PAGO_AS_MONTO`, `PROPINAS_AP_MONTO`, `REGALIA_AP`, `REGALIA_AP_MONTO`, `REGALIA_PASCUAL`, `REGALIA_PENSION_NAC_ANO`, `REGALIA_PENSION_NAC_ANO_MONTO`, `SALARIO_PRINC_IMP_MONTO`, `SALARIO_SECUN_IMP_MONTO`, `SUELDO_BRUTO_AP`, `SUELDO_BRUTO_AP_MONEDA`, `SUELDO_BRUTO_AP_MONTO`, `SUELDO_BRUTO_AS`, `SUELDO_BRUTO_AS_MONEDA`, `SUELDO_BRUTO_AS_MONTO`, `TIEMPO_RECIBE_PAGO_AP`, `TIEMPO_RECIBE_PAGO_DIAS_AP`, `TRANSPORTE_ESPECIE_AP`, `TRANSPORTE_ESPECIE_AP_MONTO`, `UTILIDAD_EMPRESARIAL_AP_MONTO`, `VACACIONES_AP_MONTO`, `VIVIENDA_ESPECIE_AP`, `VIVIENDA_ESPECIE_AP_MONTO`.

Componentes: ing_mensual_ocup_prin_asalariado, ing_mensual_ocup_prin_cuenta_propia, ing_comisiones, ing_propinas, ing_horas_extra, ing_especie_alimentos, ing_especie_viviendas, ing_especie_transporte, ing_especie_combustible, ing_especie_celular, ing_mensual_ocup_sec_asalariado, ing_mensual_ocup_sec_cuenta_propia, ing_otros_ocup_sec_asalariado, ing_beneficios_marginales_anual, ing_vacaciones, ing_dividendos, ing_bonificaciones, ing_regalia_pascual, ing_utilidades_empresariales, ing_beneficios_marginales, ing_pension_jubilacion_anual, ing_mensual_ocup_prin_independiente, ing_mensual_ocup_sec_independiente.

Reglas de cálculo de la implementación R equivalente:

```r
ml_1 = (((((((((((((ing_mensual_ocup_prin_asalariado + ing_mensual_ocup_prin_cuenta_propia) + ing_comisiones) + ing_propinas) + ing_horas_extra) + ing_especie_alimentos) + ing_especie_viviendas) + ing_especie_transporte) + ing_especie_combustible) + ing_especie_celular) + ing_mensual_ocup_sec_asalariado) + ing_mensual_ocup_sec_cuenta_propia) + ing_otros_ocup_sec_asalariado) + ing_beneficios_marginales_anual)
ml_2 = ((((((ing_vacaciones + ing_dividendos) + ing_bonificaciones) + ing_regalia_pascual) + ing_utilidades_empresariales) + ing_beneficios_marginales) + ing_pension_jubilacion_anual)
ml_3 = (ing_mensual_ocup_prin_independiente + ing_mensual_ocup_sec_independiente)
ing_laboral_monetario = ((ml_1 + ml_2) + ml_3)
ing_laboral_monetario = as.double(ing_laboral_monetario)
ml_1 = as.double(ml_1)
ml_2 = as.double(ml_2)
ml_3 = as.double(ml_3)
# deflactar = TRUE
# join ipc_2020 by PERIODO
ml_1_def = ((IPCcentral / IPCanterior) * ml_1)
ml_1_def = as.double(ml_1_def)
ml_3_def = ((IPCcentral / IPCprom) * ml_3)
ml_3_def = as.double(ml_3_def)
ing_laboral_monetario_def = ((ml_1_def + ml_2) + ml_3_def)
ing_laboral_monetario_def = as.double(ing_laboral_monetario_def)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
