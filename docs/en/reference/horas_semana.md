# Weekly working hours

```python
encftr.horas_semana(tbl)
```

Calculates weekly working hours. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `HORAS_TRABAJA_SEMANA_PRINCIPAL`, `HORAS_TRABAJO_EFECT_TOTAL`.

Calculation rules from the equivalent R implementation:

```r
horas_semana = case_when(((HORAS_TRABAJO_EFECT_TOTAL == 0) ~ HORAS_TRABAJA_SEMANA_PRINCIPAL), (TRUE ~ HORAS_TRABAJO_EFECT_TOTAL))
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
