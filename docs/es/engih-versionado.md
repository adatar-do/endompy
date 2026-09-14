# Revisiones cuando cambian pocas variables

Cada módulo conserva exactamente la revisión `baseline-1` distribuida por R: misma identidad, huella de contenido y referencias de definición. La edición de encuesta 2018 y la revisión de metadatos son identificadores distintos.

Para modificar una definición use `dictionary.draft()`, edite la variable y registre una nueva revisión con `register_dict()`. Las variables sin cambios reutilizan sus definiciones; la variable modificada conserva su identidad. `parent_version` permite elegir un padre explícito y `renames` declarar cambios de nombre.

La conexión `sqlite3` pertenece al usuario: las operaciones no la cierran y respetan sus transacciones. Un registro requiere `version` explícita o una fecha `at` con vigencia documentada. No se infiere la revisión más reciente ni se inventa vigencia a partir de 2018. Las revisiones incluidas carecen de intervalos y rechazan selección por fecha.

El JSON intercambiable y `RevisionRegistry.import_revision()` permiten trasladar diccionarios de R. Las huellas detectan alteraciones del contenido; no son firmas de autor. El ejemplo usa una base SQLite en memoria.

Cada módulo incluye `baseline-1` y su hija `coverage-2`. Sin registro externo, se selecciona `coverage-2` por defecto; indique `version="baseline-1"` para reproducir la revisión inicial. Las 530 referencias anteriores no cambian.

```python
import sqlite3
from labelerpy import RevisionRegistry
from endompy import engihr as e
con = sqlite3.connect(":memory:")
original = e.get_dict("b1", version="baseline-1")
RevisionRegistry(con).import_revision(original)
draft = original.draft()
field = "FREC_COMPRA_ALIMENTOS"
draft[field].label = "Reviewed purchase frequency"
revised = e.register_dict(con, draft, "review-2", module="b1")
before = original.revision()["variable_refs"]
after = revised.revision()["variable_refs"]
assert all(before[k] == after[k] for k in before if k != field)
assert before[field]["variable_id"] == after[field]["variable_id"]
assert len(e.dict_versions("b1", con=con)) == 2
assert e.get_dict("b1", con=con, version="baseline-1").revision() == original.revision()
con.close()
```
