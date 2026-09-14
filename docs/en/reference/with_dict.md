# Use ENCFT dictionary labels

```python
encftr.with_dict(tbl, dictionary=None, subset=None, **kwargs)
```

Use ENCFT dictionary labels. See the guide's calculation contract and parameters.

[Contract and complete example](../diccionario.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| dictionary | `None` | Explicit dictionary; None uses the selected edition or stored metadata, depending on the function. |
| subset | `None` | Column names to label; omitted applies to available matches. |
| kwargs | — | Additional labelerpy options: revision metadata or labeling policy, depending on the function. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
