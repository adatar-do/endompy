# ing_remesas_ext

```python
encftr.ing_remesas_ext(tbl)
```

Suma tres fuentes de remesas por seis meses, con su tasa mensual correspondiente, y divide entre seis. Componentes ausentes contribuyen cero.

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
