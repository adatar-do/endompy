# ing_mensual_ocup_sec_asalariado

```python
encftr.ing_mensual_ocup_sec_asalariado(tbl)
```

Calcula el indicador ing_mensual_ocup_sec_asalariado. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `SALARIO_SECUN_IMP_MONTO`, `SUELDO_BRUTO_AS`, `SUELDO_BRUTO_AS_MONEDA`, `SUELDO_BRUTO_AS_MONTO`.

Reglas de cálculo de la implementación R equivalente:

```r
# exchange rates for the preceding calendar month
SALARIO_SECUN_IMP_MONTO = ifelse(is.na(SALARIO_SECUN_IMP_MONTO), 0, SALARIO_SECUN_IMP_MONTO)
SUELDO_BRUTO_AS_MONTO = as.double(SUELDO_BRUTO_AS_MONTO)
ing_mensual_ocup_sec_asalariado = case_when(((SUELDO_BRUTO_AS_MONEDA == "DOP") ~ SUELDO_BRUTO_AS_MONTO), ((SUELDO_BRUTO_AS_MONEDA == "BRL") ~ (SUELDO_BRUTO_AS_MONTO * BRL)), ((SUELDO_BRUTO_AS_MONEDA == "CAD") ~ (SUELDO_BRUTO_AS_MONTO * CAD)), ((SUELDO_BRUTO_AS_MONEDA == "CHF") ~ (SUELDO_BRUTO_AS_MONTO * CHF)), ((SUELDO_BRUTO_AS_MONEDA == "CNY") ~ (SUELDO_BRUTO_AS_MONTO * CNY)), ((SUELDO_BRUTO_AS_MONEDA == "DEG") ~ (SUELDO_BRUTO_AS_MONTO * DEG)), ((SUELDO_BRUTO_AS_MONEDA == "DKK") ~ (SUELDO_BRUTO_AS_MONTO * DKK)), ((SUELDO_BRUTO_AS_MONEDA == "EUR") ~ (SUELDO_BRUTO_AS_MONTO * EUR)), ((SUELDO_BRUTO_AS_MONEDA == "GBP") ~ (SUELDO_BRUTO_AS_MONTO * GBP)), ((SUELDO_BRUTO_AS_MONEDA == "JPY") ~ (SUELDO_BRUTO_AS_MONTO * JPY)), ((SUELDO_BRUTO_AS_MONEDA == "NOK") ~ (SUELDO_BRUTO_AS_MONTO * NOK)), ((SUELDO_BRUTO_AS_MONEDA == "LESC") ~ (SUELDO_BRUTO_AS_MONTO * LESC)), ((SUELDO_BRUTO_AS_MONEDA == "SEK") ~ (SUELDO_BRUTO_AS_MONTO * SEK)), ((SUELDO_BRUTO_AS_MONEDA == "USD") ~ (SUELDO_BRUTO_AS_MONTO * USD)), ((SUELDO_BRUTO_AS_MONEDA == "VEF") ~ (SUELDO_BRUTO_AS_MONTO * VEF)), ((SUELDO_BRUTO_AS_MONEDA == "ARS") ~ (SUELDO_BRUTO_AS_MONTO * ARS)), ((SUELDO_BRUTO_AS == 2) ~ SALARIO_SECUN_IMP_MONTO), (TRUE ~ 0))
ing_mensual_ocup_sec_asalariado = as.double(ing_mensual_ocup_sec_asalariado)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
