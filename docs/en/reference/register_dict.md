# Register a dictionary edition

```python
encftr.register_dict(con, dictionary, version, valid_from=None, valid_to=None, **kwargs)
```

Registers an immutable edition and reuses unchanged definitions.

[Contract and complete example](../diccionario.md).

| Parameter | Default | Contract |
|---|---|---|
| con | — | Connection to the SQLite revision registry. The caller owns its lifecycle. |
| dictionary | — | Explicit dictionary; None uses the selected edition or stored metadata, depending on the function. |
| version | — | Exact edition identifier with no silent fallback. baseline-1 is the only bundled edition. |
| valid_from | `None` | Inclusive first ISO applicability date; omitted if unknown. |
| valid_to | `None` | Inclusive last ISO applicability date; omitted if unknown. |
| kwargs | — | Additional labelerpy options: revision metadata or labeling policy, depending on the function. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
