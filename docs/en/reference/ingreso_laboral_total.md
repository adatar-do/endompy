# Total labour income

```python
encftr.ingreso_laboral_total(tbl)
```

Calculates total labour income. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `BONO_VACACIONES`, `HORAS_EXTRA`, `INCENTIVO_ANTIGUEDAD`, `INGRESO_ASALARIADO`, `INGRESO_INDEPENDIENTES`, `OTROS_BENEFICIOS`, `OTROS_PAGOS`, `REGALIA_PASCUAL`.

Calculation rules from the equivalent R implementation:

```r
ingreso_laboral_total = ((((((((((INGRESO_ASALARIADO + COMISIONES) + PROPINAS) + HORAS_EXTRA) + OTROS_PAGOS) + BONO_VACACIONES) + BONIFICACIONES) + REGALIA_PASCUAL) + INCENTIVO_ANTIGUEDAD) + OTROS_BENEFICIOS) + INGRESO_INDEPENDIENTES)
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
