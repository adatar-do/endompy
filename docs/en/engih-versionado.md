# Revisions when few variables change

Each module retains the exact `baseline-1` revision distributed by R: identical dictionary identity, content fingerprint and definition references. Survey edition 2018 and metadata revision are separate identifiers.

Use `dictionary.draft()`, edit a definition and call `register_dict()` to create a new revision. Unchanged variables reuse their definitions; the modified variable retains its identity. `parent_version` chooses an explicit parent and `renames` declares variable renames.

The caller owns the `sqlite3` connection: operations do not close it and preserve caller transactions. Registry selection requires an explicit `version` or an `at` date with documented applicability. The latest revision is not inferred, and 2018 does not invent validity dates. Bundled revisions have no intervals and reject date selection.

Interchange JSON and `RevisionRegistry.import_revision()` import dictionaries from R. Fingerprints detect content modifications; they are not author signatures. This example uses an in-memory SQLite database.

Each module includes `baseline-1` and its child `coverage-2`. Without an external registry, `coverage-2` is the default; pass `version="baseline-1"` to reproduce the original revision. All 530 earlier references are unchanged.

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
