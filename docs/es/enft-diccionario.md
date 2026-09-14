# Diccionarios y revisiones

La revisión incluida `baseline-1` registra las 120 definiciones disponibles. No afirma cobertura de todas las variables ni vigencia histórica. La selección por fecha requiere revisiones con intervalos documentados; una fecha desconocida o ambigua produce un error.

## Cambios parciales entre ediciones

Cada edición resuelve un diccionario completo. El registro reutiliza las definiciones que no cambian y añade únicamente las nuevas definiciones, conservando identificadores y hashes. Cambiar una etiqueta no obliga a duplicar las otras 119. Las revisiones publicadas son inmutables: para editar, cree un borrador y registre una nueva versión.

Las fechas del ejemplo siguiente son inventadas para mostrar la API. No representan cambios documentados de la ENFT. El registro SQLite pertenece al usuario.

## Pendiente identificado en el diccionario de origen

`S3B_P10` enlazaba con `EFT_SE_MATRICULO`, una definición inexistente. Se conserva la pregunta escrita por el autor y no se asignan códigos de categoría inventados. El detalle aparece en `metadata.unresolved_legacy_links`. También se normalizaron las tildes y los escapes Unicode heredados. Las advertencias de compatibilidad temporal siguen disponibles al etiquetar.

## Ejemplo ejecutable
```python
import json
from importlib.resources import files
import pandas as pd
from endompy import enftr as ft
x = pd.DataFrame(json.loads(files("endompy.enftr").joinpath("resources/synthetic-members.json").read_text()))
import sqlite3
base = ft.get_dict()
with sqlite3.connect(":memory:") as con:
    first = ft.register_dict(con, base.draft(), "example-1", valid_from="2005-01-01", valid_to="2005-12-31")
    draft = first.draft()
    draft["EFT_ZONA"].label = "Zona de residencia"
    second = ft.register_dict(con, draft, "example-2", parent_version="example-1", valid_from="2006-01-01", valid_to="2006-12-31")
    selected = ft.get_dict(con=con, at="2006-06-01")
    print(selected.revision()["version"])
    a, b = first.revision()["variable_refs"], second.revision()["variable_refs"]
    print(sum(a[k]["definition_hash"] == b[k]["definition_hash"] for k in a))
```
