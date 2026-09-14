# Diccionarios y ediciones

La edición incluida se llama `baseline-1` y contiene 636 definiciones. Conserva la versión disponible en el proyecto, con integridad verificable, pero no declara fechas históricas de vigencia. Por eso una selección por fecha falla hasta que se registre una edición fechada con respaldo documental. No se interpreta la fecha de creación como fecha de vigencia.

Cada edición es una instantánea completa y se registra con un identificador inmutable. Internamente se guardan definiciones por contenido: si cambia una sola variable entre dos ediciones de 636 variables, las otras 635 reutilizan sus definiciones. La aplicación recibe un diccionario completo, sin tener que resolver parches manualmente. Los nombres y etiquetas de las variables pueden cambiar sin alterar las ediciones ya registradas.

La selección admite una versión exacta o una fecha ISO de aplicabilidad. Los intervalos son inclusivos. Fechas sin cobertura o ambiguas producen error. Los renombramientos deben declararse explícitamente al registrar la revisión; no se infieren por coincidencia de etiquetas. Use `labeler::dict_diff()` en R o el método `diff()` en Python para inspeccionar las diferencias entre ediciones.

El siguiente registro usa fechas ficticias únicamente para explicar el mecanismo. No representa una serie histórica oficial de ENCFT. La conexión pertenece al llamador. Use archivos SQLite separados para sus registros de trabajo y siga la política de transacciones de labeler/labelerpy.

La versión del diccionario describe el cuestionario; `pobreza_monetaria_2012` y `pobreza_monetaria_2022` eligen la metodología del cálculo. Son decisiones independientes. Al guardar un análisis conserve versión del paquete, versión y hash del diccionario, metodología, período de las respuestas y cobertura de las tablas económicas.

```python
import sqlite3
from endompy import encftr as encft
con = sqlite3.connect(":memory:")
v1 = encft.register_dict(con, encft.get_dict().draft(), "example-1", valid_from="2020-01-01", valid_to="2020-12-31")
draft = v1.draft()
draft["SEXO"].label = "Sexo de la persona"
v2 = encft.register_dict(con, draft, "example-2", valid_from="2021-01-01", valid_to="2021-12-31")
selected = encft.get_dict(at="2021-04-01", con=con)
assert selected.revision()["version"] == "example-2"
print(encft.dict_versions(con))
con.close()
```
