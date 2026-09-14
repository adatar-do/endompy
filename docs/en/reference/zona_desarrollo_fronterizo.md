# Border development zone

```python
encftr.zona_desarrollo_fronterizo(tbl)
```

Calculates border development zone. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `ID_PROVINCIA`.

Calculation rules from the equivalent R implementation:

```r
zona_desarrollo_fronterizo = case_when(((ID_PROVINCIA %in% c(16, 10, 7, 5, 15, 26, 3)) ~ 1), (TRUE ~ 0))
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
