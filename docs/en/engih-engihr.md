# ENGIH 2018 in Python

`endompy.engihr` follows `engihr 0.3.0` contracts for ENGIH 2018 metadata. It bundles 25 modules, immutable dictionaries and official catalogs. R is not needed at runtime.

Choose `module` for expenditure worksheets; the default is `personas`. `get_dict()` selects a revision, while `modules()` and `schema()` expose documented coverage. The inventory contains 1702 field occurrences; 1700 have verified definitions, including 1130 of 1132 Persons fields.

Use `set_labels()` to retain codes and `use_labels()` for presentation. The following example is invented. [Labels and validation](engih-etiquetas.md) explains types and missingness; [sources](engih-fuentes.md) details coverage and corrections. See [versioning](engih-versionado.md), [integration](engih-integracion.md), [installation](engih-deployment.md) and [reference](engih-reference.md).

Consult the sources guide for the distinction between original definitions, questionnaire cells and header descriptions. Two undefined technical fields remain explicit.

```python
from endompy import EngihDataFrame, engihr as e
x = EngihDataFrame(e.example())
y = x.set_labels()
assert y["A201"].equals(x["A201"])
assert x.use_labels().loc[1, "A201"] == "Apartamento en edificio con ascensor"
assert len(e.modules()) == 25
```
