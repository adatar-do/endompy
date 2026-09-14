# Primeros pasos con la ENFT

`enftr 0.9.0` y `endompy.enftr 0.4.0` procesan la encuesta tradicional semestral. La ENCFT continua utiliza otro módulo y otros contratos.

El ejemplo contiene 72 personas completamente inventadas, agrupadas en 24 hogares-período de 2000 a 2016. No permite estimar cifras nacionales. La generación usa constantes y nombres de variables, sin valores de personas encuestadas.

## Estructura y períodos

`EFT_PERIODO` acepta `1/2005`, `2005/1` y `20051`, incluso mezclados por fila. `PERIALFA` identifica la estructura antigua. Solo la separación de período y la zona admiten ambas estructuras; los demás cálculos requieren las columnas `EFT_` que aparecen en la referencia. El paquete no infiere equivalencias entre cuestionarios.

La versión de estructura, la revisión del diccionario y el identificador metodológico de pobreza son conceptos independientes. La función de versión reconoce columnas; no fecha el cuestionario.

Trabaje con tablas locales y conserve las columnas requeridas. Materialice las consultas antes de calcular. Las funciones conservan filas y orden; Python también conserva el índice, incluso cuando se repite.

## Ejemplo ejecutable
```python
import json
from importlib.resources import files
import pandas as pd
from endompy import enftr as ft
x = pd.DataFrame(json.loads(files("endompy.enftr").joinpath("resources/synthetic-members.json").read_text()))
result = ft.peri_vars(x)
result = ft.ocupado(result)
print(result[["EFT_PERIODO", "ano", "semestre", "ocupado"]].head())
```
