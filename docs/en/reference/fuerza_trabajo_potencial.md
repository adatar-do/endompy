# Potential labour force

```python
encftr.fuerza_trabajo_potencial(tbl)
```

Calculates potential labour force. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `DISP_SEMANA_PASADA`, `TIEMPO_GESTION_TRABAJO`.

Calculation rules from the equivalent R implementation:

```r
fuerza_trabajo_potencial = case_when((((TIEMPO_GESTION_TRABAJO == 1) & (DISP_SEMANA_PASADA == 2)) ~ 1), (((AMPLIADO == 1) & (INACTIVO == 1)) ~ 1), ((INACTIVO == 1) ~ 0))
fuerza_trabajo_potencial = case_when(((EDAD >= 15) ~ fuerza_trabajo_potencial))
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
