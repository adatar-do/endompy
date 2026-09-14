# Child labour

```python
encftr.trabajo_infantil(tbl, summer_fix=False)
```

Child labour. See the guide's calculation contract and parameters.

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| summer_fix | `False` | Includes coded waiting for classes in June–August. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
