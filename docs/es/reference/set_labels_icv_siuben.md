# set_labels_icv_siuben

```python
encftr.set_labels_icv_siuben(tbl, vars=None)
```

Aplica etiquetas a las columnas seleccionadas sin cambiar códigos.

[Contrato y ejemplo completo](../icv-siuben.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| vars | `None` | Nombres de columnas seleccionadas; en los auxiliares anteriores equivale a subset. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
