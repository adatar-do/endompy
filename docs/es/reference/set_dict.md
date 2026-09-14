# set_dict

```python
encftr.set_dict(tbl, dictionary=None, subset=None, *, version=None, at=None, con=None, **kwargs)
```

Calcula o consulta set_dict. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../diccionario.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| dictionary | `None` | Diccionario explícito; None usa la edición indicada o los metadatos guardados según la función. |
| subset | `None` | Nombres de columnas a etiquetar; omitido aplica a las coincidencias disponibles. |
| version | `None` | Identificador exacto de edición, sin sustitución silenciosa. baseline-1 es la única incluida. |
| at | `None` | Fecha ISO de aplicabilidad. Requiere intervalos documentados; falla si no hay coincidencia única. |
| con | `None` | Conexión al registro SQLite de revisiones. El llamador administra su ciclo de vida. |
| kwargs | — | Opciones adicionales de labelerpy: metadatos de revisión o política de etiquetas según la función. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
