# Income recipients

```python
encftr.perceptores_ingresos(tbl, min_edad=15)
```

Calculates income recipients. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |
| min_edad | `15` | Inclusive lower age bound in years. |

Columns referenced by calculation rules: `CATEGORIA_PRINCIPAL`.

Calculation rules from the equivalent R implementation:

```r
perceptores_ingresos = case_when(((((EDAD >= min_edad) & (CATEGORIA_PRINCIPAL %in% (1 : 7))) & (OCUPADO == 1)) ~ 1), ((OCUPADO == 0) ~ 0))
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
