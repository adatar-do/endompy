# ing_total_pobreza

```python
encftr.ing_total_pobreza(tbl, keep=False, reuse=False)
```

Compone los auxiliares históricos en ingresos nominales y deflactados del hogar. Para la metodología oficial use la función 2012 o 2022 explícita.

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| keep | `False` | Verdadero conserva componentes; una lista conserva los nombres indicados; falso retira los auxiliares calculados. |
| reuse | `False` | En auxiliares: reutiliza componentes disponibles o nombrados. En pobreza 2012/2022 se acepta y siempre recalcula. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
