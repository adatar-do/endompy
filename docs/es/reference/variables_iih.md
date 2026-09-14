# variables_iih

```python
encftr.variables_iih(include_details=False)
```

Lista columnas obligatorias, opcionales y de salida del IIH.

[Contrato y ejemplo completo](../iih.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| include_details | `False` | Incluye componentes y diagnósticos del modelo. En ICV actualiza componentes existentes aun siendo falso. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
