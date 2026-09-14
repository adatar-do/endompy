# Time in employment in years

```python
encftr.tiempo_total_empleo_anos(tbl)
```

Calculates time in employment in years. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Calculation rules from the equivalent R implementation:

```r
tiempo_total_empleo_anos = (tiempo_total_empleo_meses / 12)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
