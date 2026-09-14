# Indicadores y compatibilidad

Los indicadores conservan las codificaciones del cuestionario tradicional. `min_edad` vale 15 por defecto y debe ser un entero no negativo; ajústelo solo si la definición analítica lo requiere. La población ocupada tiene prioridad sobre las preguntas de búsqueda de otro trabajo al clasificar desempleo.

Los años de educación conservan la estructura histórica: nivel 2 usa el grado aprobado; niveles 3 y 4 añaden 8; nivel 5 añade 12; nivel 6 añade 16. Menores de cuatro años y códigos no reconocidos producen `NA`. No se sustituye esta estructura por la de la ENCFT.

Las categorías ocupacionales cambian en 2005; los dominios de inferencia combinan los tramos 2000/1–2003/1, 2003/2–2007/2 y 2008/1–2016/2. La función compuesta calcula el período antes de elegir el tramo. Las funciones de mapeo regional por decreto son transformaciones de códigos históricos.

## R y Python

Python ofrece las funciones sin prefijo y los alias `ft_` de R, además de `EnftDataFrame`. Los alias antiguos de período, zona y etiquetado siguen disponibles. Los conectores `ft_db_connect` y `ft_dbConnect` son específicos de R y su configuración Dmisc; Python recibe tablas pandas cargadas por el usuario. El operador `%>%` pertenece a R. Los algoritmos privados no se convierten en API pública.

La paridad se verifica con 144 filas sintéticas que recorren ramas y 72 personas agrupadas para ingresos y pobreza. Es evidencia de consistencia del software, no validación de estimaciones nacionales.

## Ejemplo ejecutable
```python
import json
from importlib.resources import files
import pandas as pd
from endompy import enftr as ft
x = pd.DataFrame(json.loads(files("endompy.enftr").joinpath("resources/synthetic-members.json").read_text()))
result = ft.anos_educacion(x)
result = ft.alfabeta(result, min_edad=15)
result = ft.pea_ampliada(result, min_edad=15)
result = ft.dominios_inferencia(result)
print(result[["anos_educacion", "alfabeta", "pea_ampliada", "dominios_inferencia"]].head())
```
