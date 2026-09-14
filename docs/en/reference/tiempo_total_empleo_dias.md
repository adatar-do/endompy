# Time in employment in days

```python
encftr.tiempo_total_empleo_dias(tbl)
```

Calculates time in employment in days. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `TIEMPO_EMPLEO_ANOS`, `TIEMPO_EMPLEO_DIAS`, `TIEMPO_EMPLEO_MESES`.

Calculation rules from the equivalent R implementation:

```r
tiempo_total_empleo_dias = (((TIEMPO_EMPLEO_ANOS * 365.25) + ((TIEMPO_EMPLEO_MESES * 365.25) / 12)) + TIEMPO_EMPLEO_DIAS)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
