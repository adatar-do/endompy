# IIH input and output columns

```python
encftr.variables_iih(include_details=False)
```

Lists required, optional and output IIH columns.

[Contract and complete example](../iih.md).

| Parameter | Default | Contract |
|---|---|---|
| include_details | `False` | Includes model components and diagnostics. ICV refreshes existing components even when false. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
