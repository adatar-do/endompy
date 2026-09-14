# factor_expansion_anual

```python
encftr.factor_expansion_anual(tbl, periods=None)
```

Calcula o consulta factor_expansion_anual. Consulte el contrato de la guía y los parámetros.

[Contrato y ejemplo completo](../encftr.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| periods | `None` | Divisor declarado: 1–4 anual, 1–2 semestral. Omitido usa cobertura observada por año. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
