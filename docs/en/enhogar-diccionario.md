# Dictionaries, labels and revisions

The following guide details the **2018** contract. See the 2022 edition guide for its fields and codes. Both questionnaires have explicit rules and separate dictionaries.

## Bundled revision

`baseline-1`, dictionary identifier `enhogar-2018`, contains **447 definitions** from the existing dictionary. The original 456 entries contained nine repeated names: Region, HPROVI, UPM, HVIVIEN, HHOGAR, HLINEA, HESTRAT, HZONA and grupsec. The first definition is retained, matching original named lookup; incompatible definitions are not merged. AD105 contains two codes called Sark, distinguished as `Sark [728]` and `Sark [729]` without changing values. Metadata records these adjustments. Unicode escapes are normalized.

This revision claims neither exhaustive coverage nor date applicability. Date selection requires documented intervals in a registry; unknown or ambiguous dates raise errors. One revision per edition is bundled; no historical changes are invented.

## When only a few variables change

Every revision resolves a complete dictionary, while the registry stores shared definitions. The example changes one label and reuses **446 of 447 definitions**. Registered revisions are immutable; edit a draft. The example's date intervals are invented to demonstrate the API, not an ENHOGAR chronology. The caller owns the SQLite connection.

## Labeling and calculation

`ehg_set_labels()` in R and `set_labels()` in Python attach labels and provenance without changing codes. `ehg_use_labels()` / `use_labels()` replace codes for presentation while retaining column names. `vars` limits selection; absent names are skipped. Keep numeric inputs for calculation. Old setLabels/useLabels aliases remain available with deprecation warnings.

[2022 edition guide](enhogar-edicion-2022.md).

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
