# Select recognized poverty questionnaire inputs

```python
encftr.select_variables_pobreza(tbl)
```

Select recognized poverty questionnaire inputs. See the guide's calculation contract and parameters.

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
