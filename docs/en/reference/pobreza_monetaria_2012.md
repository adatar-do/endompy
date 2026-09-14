# Monetary poverty: 2012 methodology

```python
encftr.pobreza_monetaria_2012(tbl, keep=False, reuse=False)
```

Calculates nominal and deflated income, urban/rural lines and 2012 classification using reported household size.

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| keep | `False` | True retains components; a list retains selected names; false removes calculated helper columns. |
| reuse | `False` | In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
