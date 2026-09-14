# Development regions

```python
encftr.regiones_desarrollo(tbl)
```

Calculates development regions. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `ID_PROVINCIA`.

Calculation rules from the equivalent R implementation:

```r
regiones_desarrollo = case_when(((ID_PROVINCIA %in% c(25, 18, 9)) ~ 1), ((ID_PROVINCIA %in% c(13, 24, 28)) ~ 2), ((ID_PROVINCIA %in% c(6, 19, 14, 20)) ~ 3), ((ID_PROVINCIA %in% c(27, 15, 5, 26)) ~ 4), ((ID_PROVINCIA %in% c(21, 2, 17, 31)) ~ 5), ((ID_PROVINCIA %in% c(4, 3, 16, 10)) ~ 6), ((ID_PROVINCIA %in% c(22, 7)) ~ 7), ((ID_PROVINCIA %in% c(12, 11, 8)) ~ 8), ((ID_PROVINCIA %in% c(23, 30, 29)) ~ 9), ((ID_PROVINCIA %in% c(1, 32)) ~ 10))
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
