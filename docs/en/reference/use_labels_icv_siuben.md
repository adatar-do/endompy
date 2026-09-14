# Convert ICV codes to labeled categories

```python
encftr.use_labels_icv_siuben(tbl, vars=None)
```

Converts selected ICV codes to labeled categories.

[Contract and complete example](../icv-siuben.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| vars | `None` | Selected column names; equivalent to subset in legacy labeling helpers. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
