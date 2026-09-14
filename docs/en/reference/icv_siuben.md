# Historical ICV SIUBEN

```python
encftr.icv_siuben(tbl, include_details=True, method='encftr0-0.0.2.9002')
```

Reproduces ICV from encftr0 0.0.2.9002 for complete households with one head. Preserves rows and adds category, score and method. Does not certify current SIUBEN methodology. See the guide for missing-value rules, keys, components and migration.

[Contract and complete example](../icv-siuben.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| include_details | `True` | Includes model components and diagnostics. ICV refreshes existing components even when false. |
| method | `'encftr0-0.0.2.9002'` | Exact historical identifier: encftr0-0.0.2.9002. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
