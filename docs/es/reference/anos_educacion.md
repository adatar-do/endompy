# anos_educacion

```python
encftr.anos_educacion(tbl, breaks=None, labels=None, secundaria_base='armonizada_6_6', anio_corte=2022)
```

Calcula o consulta anos_educacion. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| breaks | `None` | Límites numéricos de intervalos o número de grupos. Use límites explícitos para comparar lenguajes. |
| labels | `None` | Etiquetas para los intervalos. Use etiquetas explícitas para comparar lenguajes. |
| secundaria_base | `'armonizada_6_6'` | armonizada_6_6, legacy_8_4 o historica_por_ano. Define la base antes del grado secundario. |
| anio_corte | `2022` | Primer año con base secundaria de seis años para historica_por_ano. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
