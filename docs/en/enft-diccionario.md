# Dictionaries and revisions

Bundled revision `baseline-1` registers the 120 available definitions. It does not claim full variable coverage or historical applicability. Date selection requires documented intervals; an unknown or ambiguous date raises an error.

## Partial changes between editions

Each edition resolves a complete dictionary. The registry reuses unchanged definitions and adds only changed definitions, retaining stable identifiers and hashes. Changing one label does not duplicate the other 119 definitions. Registered revisions are immutable: create a draft and register a new version to edit them.

Dates in this example are invented API demonstrations, not documented ENFT questionnaire changes. The caller owns the SQLite registry.

## Identified gap in the source dictionary

`S3B_P10` linked to the nonexistent `EFT_SE_MATRICULO` definition. The author's question wording is preserved; no category codes are invented. Details are stored in `metadata.unresolved_legacy_links`. Legacy accents and Unicode escapes have also been normalized. Historical compatibility warnings remain available when labeling.

Survey labels are retained in their original Spanish in both documentation editions.

## Runnable example
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
