# Monthly main occupation income

```python
encftr.ing_mensual_ocup_prin(tbl)
```

Calculates monthly main occupation income. Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../pobreza-monetaria.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Calculation rules from the equivalent R implementation:

```r
ing_mensual_ocup_prin = ((ing_mensual_ocup_prin_asalariado + ing_mensual_ocup_prin_cuenta_propia) + ing_mensual_ocup_prin_independiente)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
