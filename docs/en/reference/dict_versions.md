# Available dictionary editions

```python
encftr.dict_versions(con=None)
```

Returns a table of available edition metadata, intervals and hashes.

[Contract and complete example](../diccionario.md).

| Parameter | Default | Contract |
|---|---|---|
| con | `None` | Connection to the SQLite revision registry. The caller owns its lifecycle. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
