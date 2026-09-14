# alfabetizacion

```python
encftr.alfabetizacion(tbl, min_edad=0, max_edad=inf)
```

Calcula o consulta alfabetizacion. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| min_edad | `0` | Límite inferior inclusivo de edad en años. |
| max_edad | `inf` | Límite superior inclusivo de edad en años. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
