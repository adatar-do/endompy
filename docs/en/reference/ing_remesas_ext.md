# Monthly foreign remittances

```python
encftr.ing_remesas_ext(tbl)
```

Sums three remittance streams over six months using their respective monthly rates, then divides by six. Missing components contribute zero.

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
