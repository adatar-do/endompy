# Legacy deflated per-capita household income

```python
encftr.ing_pc_pobreza_def(tbl, keep=False, reuse=False)
```

Legacy deflated per-capita household income. See the guide's calculation contract and parameters.

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| keep | `False` | True retains components; a list retains selected names; false removes calculated helper columns. |
| reuse | `False` | In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
