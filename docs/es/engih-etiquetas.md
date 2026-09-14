# Etiquetas, códigos y validación

`set_labels(tbl, dictionary=None, vars=None, module="personas", edition=2018, version=None, at=None, con=None, strict=False)` conserva valores, tipos de pandas, nombres e índice. Solo etiqueta los campos seleccionados presentes en el diccionario. El módulo admite tablas locales y nombres de columnas únicos y no vacíos; `vars` es una lista de nombres existentes sin repetición.

`use_labels()` devuelve categorías de pandas para las columnas con catálogo. Conserva NA y códigos desconocidos; cuando un desconocido coincide con una etiqueta, se distingue mediante `[unlabelled code: ...]`. Los conteos A101 y A102 permanecen numéricos. `strict=True` rechaza códigos fuera del catálogo.

Los códigos numéricos requieren una columna numérica; no se interpretan cadenas como números, categorías existentes ni booleanos como 1/0. Se admiten columnas completamente ausentes y tipos anulables de pandas. `validate()` informa `unmapped`, `label_only`, `ok`, `unknown_codes` o `type_mismatch`. No evalúa saltos, imputaciones, ponderaciones ni estimaciones de encuesta.

Los metadatos de tabla se conservan en `DataFrame.attrs`; consulte etiquetas mediante `df.labeler.get_label()` y `df.labeler.get_labels()`. `labeler_provenance` identifica revisión y definición por variable. Las categorías y los atributos de R/pandas son representaciones propias de cada lenguaje; las comprobaciones comparan valores, etiquetas, orden, faltantes y procedencia.

```python
import pandas as pd
from endompy import engihr as e
x = pd.DataFrame({"A201": [1, 1234, None], "A101": [1, 3, None]})
x.index = [7, 7, 2]
y = e.set_labels(x)
z = e.use_labels(x)
assert y["A201"].equals(x["A201"])
assert z.loc[2, "A101"] != z.loc[2, "A101"]
assert z["A201"].iloc[1] == "1234"
assert e.validate(x).loc[0, "status"] == "unknown_codes"
assert y.labeler.get_label("A101")
```
