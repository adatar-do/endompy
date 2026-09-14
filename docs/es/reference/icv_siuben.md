# icv_siuben

```python
encftr.icv_siuben(tbl, include_details=True, method='encftr0-0.0.2.9002')
```

Reproduce el ICV de encftr0 0.0.2.9002 para hogares completos con una jefatura. Conserva filas y agrega clase, puntaje y método. No certifica una metodología vigente de SIUBEN. Consulte la guía para reglas de ausentes, claves, componentes y migración.

[Contrato y ejemplo completo](../icv-siuben.md).

| Parámetro | Predeterminado | Contrato |
|---|---|---|
| tbl | — | Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT. |
| include_details | `True` | Incluye componentes y diagnósticos del modelo. En ICV actualiza componentes existentes aun siendo falso. |
| method | `'encftr0-0.0.2.9002'` | Identificador histórico exacto: encftr0-0.0.2.9002. |

Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame.
