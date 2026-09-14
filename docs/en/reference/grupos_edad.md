# Age groups

```python
encftr.grupos_edad(tbl, breaks=10, labels=None)
```

Age groups. See the guide's calculation contract and parameters.

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| breaks | `10` | Numeric interval boundaries or number of groups. Use explicit boundaries for cross-language comparisons. |
| labels | `None` | Interval labels. Use explicit labels for cross-language comparisons. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
