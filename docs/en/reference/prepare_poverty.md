# Prepare poverty questionnaire compatibility fields

```python
encftr.prepare_poverty(tbl)
```

Prepare poverty questionnaire compatibility fields. See the guide's calculation contract and parameters.

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
