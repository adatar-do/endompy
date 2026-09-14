# matriculacion_escolar

```python
encftr.matriculacion_escolar(tbl, min_edad=6, max_edad=17, summer_fix=False)
```

Calcula o consulta matriculacion_escolar. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../indicadores.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| min_edad | `6` | Límite inferior inclusivo de edad en años. |
| max_edad | `17` | Límite superior inclusivo de edad en años. |
| summer_fix | `False` | Incluye la espera de inicio de clases codificada en junio–agosto. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
