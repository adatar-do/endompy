# get_dict

```python
encftr.get_dict(version=None, at=None, con=None)
```

Carga una edición completa e íntegra; baseline-1 no declara vigencia histórica.

[Contrato y ejemplo completo](../diccionario.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| version | `None` | Identificador exacto de edición, sin sustitución silenciosa. baseline-1 es la única incluida. |
| at | `None` | Fecha ISO de aplicabilidad. Requiere intervalos documentados; falla si no hay coincidencia única. |
| con | `None` | Conexión al registro SQLite de revisiones. El llamador administra su ciclo de vida. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
