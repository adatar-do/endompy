# Household dependency ratio

```python
encftr.tasa_dependencia(tbl, min_edad=15, max_edad=64, limit='both', breaks=None, labels=None)
```

Household dependency ratio. See the guide's calculation contract and parameters.

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| min_edad | `15` | Inclusive lower age bound in years. |
| max_edad | `64` | Inclusive upper age bound in years. |
| limit | `'both'` | both, above or below: all, older or younger dependents. |
| breaks | `None` | Numeric interval boundaries or number of groups. Use explicit boundaries for cross-language comparisons. |
| labels | `None` | Interval labels. Use explicit labels for cross-language comparisons. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
