# School overage

```python
encftr.sobreedad_escolar(tbl, nrezagos=2)
```

School overage. See the guide's calculation contract and parameters.

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| nrezagos | `2` | Years of delay beyond expected age based on completed schooling plus six. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
