# Household income index (IIH)

```python
encftr.iih(tbl, vivienda_tbl=None, return_households=False, include_details=False, filter_valid_households=False)
```

Estimates income and IIH category using fixed household models; this is distinct from observed monetary poverty.

[Contract and complete example](../iih.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| vivienda_tbl | `None` | Optional dwelling table; fills wall text by PERIODO and VIVIENDA. |
| return_households | `False` | True returns one row per household; false attaches results to each person. |
| include_details | `False` | Includes model components and diagnostics. ICV refreshes existing components even when false. |
| filter_valid_households | `False` | Retains households with hconmissing zero; person output preserves rows and leaves filtered scores missing. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
