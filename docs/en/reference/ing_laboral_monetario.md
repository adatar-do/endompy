# Monetary labour income

```python
encftr.ing_laboral_monetario(tbl, deflactar=True, keep=False, reuse=False)
```

Calculates monetary labour income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| deflactar | `True` | Applies the component deflator when true; preserves its nominal output. |
| keep | `False` | True retains components; a list retains selected names; false removes calculated helper columns. |
| reuse | `False` | In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute. |

Columns referenced by calculation rules: `ALIMENTACION_ESPECIE_AP`, `ALIMENTACION_ESPECIE_AP_MONTO`, `BENEFICIOS_MARGINALES_AP_MONTO`, `BONIFICACION_AP_MONTO`, `CELULAR_ESPECIE_AP`, `CELULAR_ESPECIE_AP_MONTO`, `COMISIONES_AP_MONTO`, `DIVIDENDOS_AP_MONTO`, `GANANCIA_IN_PRODUCTOR`, `GANANCIA_IN_PRODUCTOR_MONEDA`, `GANANCIA_IN_PRODUCTOR_MONTO`, `GANANCIA_IS_PRODUCTOR`, `GANANCIA_IS_PRODUCTOR_MONEDA`, `GANANCIA_IS_PRODUCTOR_MONTO`, `GANANCIA_PRINC_IMP_MONTO`, `GANANCIA_SECUN_IMP_MONTO`, `GASOLINA_ESPECIE_AP`, `GASOLINA_ESPECIE_AP_MONTO`, `HORAS_EXTRA_AP_MONTO`, `HORAS_TRABAJO_EFECT_TOTAL`, `INGRESO_ACTIVIDAD_IN`, `INGRESO_ACTIVIDAD_IN_DIAS`, `INGRESO_ACTIVIDAD_IN_MONEDA`, `INGRESO_ACTIVIDAD_IN_MONTO`, `INGRESO_ACTIVIDAD_IN_PERIODO`, `INGRESO_ACTIVIDAD_IS`, `INGRESO_ACTIVIDAD_IS_DIAS`, `INGRESO_ACTIVIDAD_IS_MONEDA`, `INGRESO_ACTIVIDAD_IS_MONTO`, `INGRESO_ACTIVIDAD_IS_PERIODO`, `OTROS_BENEFICIOS_AS_MONTO`, `OTROS_PAGO_AS_MONTO`, `PROPINAS_AP_MONTO`, `REGALIA_AP`, `REGALIA_AP_MONTO`, `REGALIA_PASCUAL`, `REGALIA_PENSION_NAC_ANO`, `REGALIA_PENSION_NAC_ANO_MONTO`, `SALARIO_PRINC_IMP_MONTO`, `SALARIO_SECUN_IMP_MONTO`, `SUELDO_BRUTO_AP`, `SUELDO_BRUTO_AP_MONEDA`, `SUELDO_BRUTO_AP_MONTO`, `SUELDO_BRUTO_AS`, `SUELDO_BRUTO_AS_MONEDA`, `SUELDO_BRUTO_AS_MONTO`, `TIEMPO_RECIBE_PAGO_AP`, `TIEMPO_RECIBE_PAGO_DIAS_AP`, `TRANSPORTE_ESPECIE_AP`, `TRANSPORTE_ESPECIE_AP_MONTO`, `UTILIDAD_EMPRESARIAL_AP_MONTO`, `VACACIONES_AP_MONTO`, `VIVIENDA_ESPECIE_AP`, `VIVIENDA_ESPECIE_AP_MONTO`.

Components: ing_mensual_ocup_prin_asalariado, ing_mensual_ocup_prin_cuenta_propia, ing_comisiones, ing_propinas, ing_horas_extra, ing_especie_alimentos, ing_especie_viviendas, ing_especie_transporte, ing_especie_combustible, ing_especie_celular, ing_mensual_ocup_sec_asalariado, ing_mensual_ocup_sec_cuenta_propia, ing_otros_ocup_sec_asalariado, ing_beneficios_marginales_anual, ing_vacaciones, ing_dividendos, ing_bonificaciones, ing_regalia_pascual, ing_utilidades_empresariales, ing_beneficios_marginales, ing_pension_jubilacion_anual, ing_mensual_ocup_prin_independiente, ing_mensual_ocup_sec_independiente.

Calculation rules from the equivalent R implementation:

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

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
