# Time in employment in months

```python
encftr.tiempo_total_empleo_meses(tbl)
```

Calculates time in employment in months. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Calculation rules from the equivalent R implementation:

```r
tiempo_total_empleo_meses = (tiempo_total_empleo_dias / (((365.25 / 12)))
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
