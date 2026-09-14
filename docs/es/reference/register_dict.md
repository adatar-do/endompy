# register_dict

```python
encftr.register_dict(con, dictionary, version, valid_from=None, valid_to=None, **kwargs)
```

Registra una edición inmutable y reutiliza las definiciones sin cambios.

[Contrato y ejemplo completo](../diccionario.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| con | — | Conexión al registro SQLite de revisiones. El llamador administra su ciclo de vida. |
| dictionary | — | Diccionario explícito; None usa la edición indicada o los metadatos guardados según la función. |
| version | — | Identificador exacto de edición, sin sustitución silenciosa. baseline-1 es la única incluida. |
| valid_from | `None` | Primera fecha ISO de vigencia inclusiva; omitida si no se conoce. |
| valid_to | `None` | Última fecha ISO de vigencia inclusiva; omitida si no se conoce. |
| kwargs | — | Opciones adicionales de labelerpy: metadatos de revisión o política de etiquetas según la función. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
