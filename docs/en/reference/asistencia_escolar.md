# School attendance

```python
encftr.asistencia_escolar(tbl, min_edad=6, max_edad=17, summer_fix=False)
```

School attendance. See the guide's calculation contract and parameters.

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| min_edad | `6` | Inclusive lower age bound in years. |
| max_edad | `17` | Inclusive upper age bound in years. |
| summer_fix | `False` | Includes coded waiting for classes in June–August. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
