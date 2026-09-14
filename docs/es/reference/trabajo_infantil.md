# trabajo_infantil

```python
encftr.trabajo_infantil(tbl, summer_fix=False)
```

Calcula o consulta trabajo_infantil. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| summer_fix | `False` | Incluye la espera de inicio de clases codificada en junio–agosto. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
