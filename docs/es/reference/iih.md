# iih

```python
encftr.iih(tbl, vivienda_tbl=None, return_households=False, include_details=False, filter_valid_households=False)
```

Estima ingresos y categoría IIH con coeficientes fijos, a nivel de hogar; no es pobreza monetaria observada.

[Contrato y ejemplo completo](../iih.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| vivienda_tbl | `None` | Tabla opcional de vivienda; completa texto de paredes por PERIODO y VIVIENDA. |
| return_households | `False` | Verdadero devuelve una fila por hogar; falso adjunta resultados a cada persona. |
| include_details | `False` | Incluye componentes y diagnósticos del modelo. En ICV actualiza componentes existentes aun siendo falso. |
| filter_valid_households | `False` | Conserva hogares con hconmissing igual a cero; en salida por persona mantiene filas y deja puntuaciones ausentes. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
