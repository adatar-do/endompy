# fuerza_trabajo_potencial

```python
encftr.fuerza_trabajo_potencial(tbl)
```

Calcula el indicador fuerza_trabajo_potencial. Devuelve una copia con columnas calculadas y conserva las filas de entrada. 

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Columnas referidas por las reglas: `DISP_SEMANA_PASADA`, `TIEMPO_GESTION_TRABAJO`.

Reglas de cálculo de la implementación R equivalente:

```r
fuerza_trabajo_potencial = case_when((((TIEMPO_GESTION_TRABAJO == 1) & (DISP_SEMANA_PASADA == 2)) ~ 1), (((AMPLIADO == 1) & (INACTIVO == 1)) ~ 1), ((INACTIVO == 1) ~ 0))
fuerza_trabajo_potencial = case_when(((EDAD >= 15) ~ fuerza_trabajo_potencial))
```

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
