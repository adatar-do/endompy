# Household literacy rate

```python
encftr.tasa_alfabetizacion_hogar(tbl, min_edad=0, max_edad=inf)
```

Household literacy rate. See the guide's calculation contract and parameters.

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| min_edad | `0` | Inclusive lower age bound in years. |
| max_edad | `inf` | Inclusive upper age bound in years. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
