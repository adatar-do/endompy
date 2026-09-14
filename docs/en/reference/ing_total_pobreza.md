# Legacy household income composition

```python
encftr.ing_total_pobreza(tbl, keep=False, reuse=False)
```

Composes legacy helpers into nominal and deflated household income. Use the explicit 2012 or 2022 function for an official methodology workflow.

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| keep | `False` | True retains components; a list retains selected names; false removes calculated helper columns. |
| reuse | `False` | In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
