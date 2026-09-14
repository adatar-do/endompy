# Semester expansion weights

```python
encftr.factor_expansion_semestre(tbl, periods=None)
```

Semester expansion weights. See the guide's calculation contract and parameters.

[Contract and complete example](../encftr.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| periods | `None` | Declared divisor: 1–4 annual, 1–2 semester. Omitted uses observed coverage within year. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
