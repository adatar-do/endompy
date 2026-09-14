# Ingresos y pobreza histórica

El identificador `enftr-historical-2005-2016-v2` corresponde a la implementación histórica del paquete, con correcciones de integridad y remesas. No se presenta como reproducción certificada del programa oficial.

## Unidades, claves y cobertura

Los 34 componentes suman ingreso individual mensual en pesos dominicanos. El ingreso per cápita es la suma de los ingresos individuales del hogar dividida entre todos sus miembros presentes. Proporcione hogares completos: la tabla no permite detectar personas omitidas por un filtro previo. Las claves son período, vivienda, hogar y miembro; deben ser únicas y no faltar. Cada hogar requiere exactamente un jefe para asignarle una sola vez la renta imputada. La zona debe ser constante dentro del hogar y usar 0/1.

La clasificación cubre exclusivamente 2005/1–2016/2. Las líneas incluidas abarcan 2000–2016, pero la disponibilidad de una línea no extiende la cobertura del modelo de ingreso. Se conserva el límite inclusivo: ingreso igual a la línea extrema pertenece a categoría 1; igual a la línea general pertenece a categoría 2.

| Salida | Significado |
|---|---|
| `1` | Pobreza extrema |
| `2` | Pobreza moderada |
| `3` | No pobre |
| `NA` + `outside_coverage` | Fuera del intervalo implementado |
| `NA` + `missing_income` | Al menos un miembro tiene ingreso total desconocido |

## Fuentes y faltantes

`ing_ext` admite múltiples transacciones por persona; un registro ausente representa ausencia de transacción, mientras que un importe `NA` conserva el ingreso desconocido. `remesas` requiere una fila por persona con seis casillas. La moneda y el IPC deben estar disponibles para todo importe positivo: una referencia desconocida detiene el cálculo. En otros componentes se mantienen las reglas históricas de recodificación de faltantes, documentadas en la referencia; no todo `NA` del cuestionario indica una respuesta faltante, pues también existen saltos.

En el primer semestre, las casillas PER4/PER5/PER6 corresponden a diciembre, noviembre y octubre del año anterior. Hasta 2007/1 se multiplica por frecuencia y se divide entre 12; desde 2007/2 se divide entre 6. Solo se leen las seis casillas, sin confundir otros campos cuyo nombre comienza por `EFT_MONTO`.

Por defecto se recalculan los componentes. `.reuse` en R y `reuse` en Python permiten reutilización explícita: quien los proporciona responde por sus unidades y vigencia. `.keep`/`keep` conserva componentes para auditoría. Las líneas se unen por período y zona, aunque la entrada ya contenga resultados anteriores.

La cobertura implementada se fija en el código y las tablas incluidas. Como contexto metodológico, consulte los [códigos publicados por el MEPyD](https://mepyd.gob.do/vaes/codigos-de-pobreza/) y la [metodología de pobreza de 2012 de la ONE](https://www.one.gob.do/publicaciones/2013/metodologia-calculo-pobreza-monetaria-diagnostico-y-propuesta-para-la-estimacion-de-la-pobreza-2012/). Estas referencias no certifican la equivalencia numérica de este paquete con la producción oficial de la ENFT.

## Ejemplo ejecutable
```python
import json
from importlib.resources import files
import pandas as pd
from endompy import enftr as ft
x = pd.DataFrame(json.loads(files("endompy.enftr").joinpath("resources/synthetic-members.json").read_text()))
result = ft.pobreza_monetaria(x, keep=True)
print(result["pobreza_estado"].value_counts())
print(result[["ing_total_pobreza_monetaria", "ing_pc_pobreza_monetaria", "pobreza_monetaria"]].tail())
```
