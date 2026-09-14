# Diccionarios, etiquetas y revisiones

La guía siguiente detalla el contrato heredado de **2018**. Para los campos y códigos de 2022 consulte la guía de la edición 2022. Ambos cuestionarios tienen reglas explícitas y diccionarios separados.

## Revisión incluida

`baseline-1`, identificador `enhogar-2018`, contiene **447 definiciones** del diccionario existente. Las 456 entradas originales tenían nueve nombres repetidos: Region, HPROVI, UPM, HVIVIEN, HHOGAR, HLINEA, HESTRAT, HZONA y grupsec. Se conserva la primera definición, igual que el acceso nominal del código original; no se mezclan dos definiciones incompatibles. En AD105, dos códigos llamados Sark se distinguen como `Sark [728]` y `Sark [729]` conservando sus valores. Los metadatos registran estos ajustes. Se normalizan los escapes Unicode.

Esta revisión no afirma cobertura exhaustiva ni vigencia por fechas. La selección por fecha exige intervalos documentados en un registro; fechas desconocidas o ambiguas producen error. 2018 conserva baseline-1; 2022 añade coverage-2 y cinco módulos redatam-1 con procedencia documentada.

## Cuando solo cambian unas variables

Cada revisión resuelve un diccionario completo, pero el registro almacena definiciones compartidas. El siguiente ejemplo modifica una etiqueta y reutiliza **446 de 447 definiciones**. Las revisiones registradas son inmutables; se editan borradores. Los intervalos del ejemplo son ficticios para enseñar la API, no una cronología de ENHOGAR. La conexión SQLite pertenece al usuario.

## Etiquetar y calcular

`ehg_set_labels()` en R y `set_labels()` en Python adjuntan etiquetas y procedencia sin cambiar códigos. `ehg_use_labels()` / `use_labels()` sustituyen códigos por etiquetas para presentación y conservan nombres de columnas. `vars` limita las columnas; un nombre ausente se omite. Conserve los datos numéricos para calcular. Los alias antiguos setLabels/useLabels siguen disponibles con advertencia de deprecación.

[Guía de la edición 2022](enhogar-edicion-2022.md).

```python
from endompy import enhogar as e
import sqlite3
with sqlite3.connect(":memory:") as con:
    first = e.register_dict(con, e.get_dict().draft(), "example-1", valid_from="2018-01-01", valid_to="2018-06-30")
    draft = first.draft()
    draft["HZONA"].label = "Zona de residencia revisada"
    second = e.register_dict(con, draft, "example-2", parent_version="example-1", valid_from="2018-07-01", valid_to="2018-12-31")
    a, b = first.revision()["variable_refs"], second.revision()["variable_refs"]
    print(sum(a[k]["definition_hash"] == b[k]["definition_hash"] for k in a))
    print(e.get_dict(con=con, at="2018-07-01").revision()["version"])
```
