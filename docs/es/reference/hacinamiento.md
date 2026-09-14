# hacinamiento

```python
encftr.hacinamiento(tbl, breaks=None, labels=None)
```

Calcula o consulta hacinamiento. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| breaks | `None` | Límites numéricos de intervalos o número de grupos. Use límites explícitos para comparar lenguajes. |
| labels | `None` | Etiquetas para los intervalos. Use etiquetas explícitas para comparar lenguajes. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
