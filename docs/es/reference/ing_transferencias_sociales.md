# ing_transferencias_sociales

```python
encftr.ing_transferencias_sociales(tbl, deflactar=True)
```

Calcula el indicador ing_transferencias_sociales. Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| deflactar | `True` | Aplica el deflactor del componente cuando es verdadero; conserva su salida nominal. |

Columnas referidas por las reglas: `GOBIERNO_NAC`, `GOB_BONOGAS_CHOFERES_MONTO`, `GOB_BONOGAS_HOGARES_MONTO`, `GOB_BONO_ESTUDIANTE_PROG_MONTO`, `GOB_BONO_LUZ_MONTO`, `GOB_COMER_PRIMERO_MONTO`, `GOB_FONDO_ASISTENCIA_FASE`, `GOB_INC_ASIS_ESCOLAR_MONTO`, `GOB_INC_EDUCACION_SUP_MONTO`, `GOB_INC_MARINA_GUERRA_MONTO`, `GOB_INC_POLICIA_PREV_MONTO`, `GOB_PROGRAMA_PATI`, `GOB_PROTECCION_VEJEZ_MONTO`, `GOB_QUEDATE_EN_CASA`.

Reglas de cálculo de la implementación R equivalente:

```r
comeresprimero = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_COMER_PRIMERO_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ as.numeric(GOB_COMER_PRIMERO_MONTO)), (TRUE ~ 0))
comeresprimero = as.double(comeresprimero)
asistescolar = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_INC_ASIS_ESCOLAR_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_INC_ASIS_ESCOLAR_MONTO), (TRUE ~ 0))
asistescolar = as.double(asistescolar)
bonoluzhog = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_BONO_LUZ_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_BONO_LUZ_MONTO), (TRUE ~ 0))
bonoluzhog = as.double(bonoluzhog)
bonogaschof = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_BONOGAS_CHOFERES_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_BONOGAS_CHOFERES_MONTO), (TRUE ~ 0))
bonogaschof = as.double(bonogaschof)
bonogashog = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_BONOGAS_HOGARES_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_BONOGAS_HOGARES_MONTO), (TRUE ~ 0))
bonogashog = as.double(bonogashog)
protvejez = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_PROTECCION_VEJEZ_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_PROTECCION_VEJEZ_MONTO), (TRUE ~ 0))
protvejez = as.double(protvejez)
bonoest = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_BONO_ESTUDIANTE_PROG_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_BONO_ESTUDIANTE_PROG_MONTO), (TRUE ~ 0))
bonoest = as.double(bonoest)
incedusup = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_INC_EDUCACION_SUP_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_INC_EDUCACION_SUP_MONTO), (TRUE ~ 0))
incedusup = as.double(incedusup)
incpolpre = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_INC_POLICIA_PREV_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_INC_POLICIA_PREV_MONTO), (TRUE ~ 0))
incpolpre = as.double(incpolpre)
incmarina = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_INC_MARINA_GUERRA_MONTO) ~ 0), ((GOBIERNO_NAC == 1) ~ GOB_INC_MARINA_GUERRA_MONTO), (TRUE ~ 0))
incmarina = as.double(incmarina)
ingquedate = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_QUEDATE_EN_CASA) ~ 0), ((GOBIERNO_NAC == 1) ~ as.numeric(GOB_QUEDATE_EN_CASA)), (TRUE ~ 0))
ingquedate = as.double(ingquedate)
ingfase = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_FONDO_ASISTENCIA_FASE) ~ 0), ((GOBIERNO_NAC == 1) ~ as.numeric(GOB_FONDO_ASISTENCIA_FASE)), (TRUE ~ 0))
ingfase = as.double(ingfase)
ingpati = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(GOB_PROGRAMA_PATI) ~ 0), ((GOBIERNO_NAC == 1) ~ as.numeric(GOB_PROGRAMA_PATI)), (TRUE ~ 0))
ingpati = as.double(ingpati)
superate = case_when((is.na(GOBIERNO_NAC) ~ 0), (is.na(SUPERATE) ~ 0), ((GOBIERNO_NAC == 1) ~ as.numeric(SUPERATE)), (TRUE ~ 0))
superate = as.double(superate)
ing_transferencias_sociales = (((((((((((((comeresprimero + asistescolar) + bonoluzhog) + bonogaschof) + bonogashog) + protvejez) + bonoest) + incedusup) + incpolpre) + incmarina) + ingquedate) + ingfase) + ingpati) + superate)
# deflactar = TRUE
# join ipc_2020 by PERIODO
ing_transferencias_sociales_def = ((IPCcentral / IPCanterior) * ing_transferencias_sociales)
ing_transferencias_sociales_def = as.double(ing_transferencias_sociales_def)
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
