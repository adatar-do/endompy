# pobreza_monetaria_2012

```python
encftr.pobreza_monetaria_2012(tbl, keep=False, reuse=False)
```

Calcula ingresos nominales y deflactados, líneas urbanas/rurales y clasificación 2012 con denominador reportado del hogar.

[Contrato y ejemplo completo](../pobreza-monetaria.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| keep | `False` | Verdadero conserva componentes; una lista conserva los nombres indicados; falso retira los auxiliares calculados. |
| reuse | `False` | En auxiliares: reutiliza componentes disponibles o nombrados. En pobreza 2012/2022 se acepta y siempre recalcula. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
