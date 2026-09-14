# tasa_dependencia

```python
encftr.tasa_dependencia(tbl, min_edad=15, max_edad=64, limit='both', breaks=None, labels=None)
```

Calcula o consulta tasa_dependencia. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| min_edad | `15` | Límite inferior inclusivo de edad en años. |
| max_edad | `64` | Límite superior inclusivo de edad en años. |
| limit | `'both'` | both, above o below: dependientes totales, mayores o menores. |
| breaks | `None` | Límites numéricos de intervalos o número de grupos. Use límites explícitos para comparar lenguajes. |
| labels | `None` | Etiquetas para los intervalos. Use etiquetas explícitas para comparar lenguajes. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
