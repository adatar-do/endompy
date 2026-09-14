# browse_dict

```python
encftr.browse_dict(version=None, at=None, con=None)
```

Calcula o consulta browse_dict. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../diccionario.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| version | `None` | Identificador exacto de edición, sin sustitución silenciosa. baseline-1 es la única incluida. |
| at | `None` | Fecha ISO de aplicabilidad. Requiere intervalos documentados; falla si no hay coincidencia única. |
| con | `None` | Conexión al registro SQLite de revisiones. El llamador administra su ciclo de vida. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
