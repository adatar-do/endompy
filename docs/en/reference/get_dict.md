# Select an ENCFT dictionary edition

```python
encftr.get_dict(version=None, at=None, con=None)
```

Loads a complete verified edition; baseline-1 asserts no historical applicability.

[Contract and complete example](../diccionario.md).

| Parameter | Default | Contract |
|---|---|---|
| version | `None` | Exact edition identifier with no silent fallback. baseline-1 is the only bundled edition. |
| at | `None` | ISO applicability date. Requires documented intervals and a unique match. |
| con | `None` | Connection to the SQLite revision registry. The caller owns its lifecycle. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
