# Apply ENCFT dictionary metadata

```python
encftr.set_dict(tbl, dictionary=None, subset=None, *, version=None, at=None, con=None, **kwargs)
```

Apply ENCFT dictionary metadata. See the guide's calculation contract and parameters.

[Contract and complete example](../diccionario.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| dictionary | `None` | Explicit dictionary; None uses the selected edition or stored metadata, depending on the function. |
| subset | `None` | Column names to label; omitted applies to available matches. |
| version | `None` | Exact edition identifier with no silent fallback. baseline-1 is the only bundled edition. |
| at | `None` | ISO applicability date. Requires documented intervals and a unique match. |
| con | `None` | Connection to the SQLite revision registry. The caller owns its lifecycle. |
| kwargs | — | Additional labelerpy options: revision metadata or labeling policy, depending on the function. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
