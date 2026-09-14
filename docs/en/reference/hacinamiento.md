# People per dwelling bedroom

```python
encftr.hacinamiento(tbl, breaks=None, labels=None)
```

People per dwelling bedroom. See the guide's calculation contract and parameters.

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| breaks | `None` | Numeric interval boundaries or number of groups. Use explicit boundaries for cross-language comparisons. |
| labels | `None` | Interval labels. Use explicit labels for cross-language comparisons. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
