# Years of schooling

```python
encftr.anos_educacion(tbl, breaks=None, labels=None, secundaria_base='armonizada_6_6', anio_corte=2022)
```

Years of schooling. See the guide's calculation contract and parameters.

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| breaks | `None` | Numeric interval boundaries or number of groups. Use explicit boundaries for cross-language comparisons. |
| labels | `None` | Interval labels. Use explicit labels for cross-language comparisons. |
| secundaria_base | `'armonizada_6_6'` | armonizada_6_6, legacy_8_4 or historica_por_ano. Sets the offset before secondary grade. |
| anio_corte | `2022` | First year with a six-year secondary offset for historica_por_ano. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
