# Dictionaries and editions

The bundled edition is `baseline-1` and contains 636 definitions. It preserves the dictionary available in the project with verifiable integrity, but asserts no historical applicability dates. Date selection therefore fails until a dated edition supported by documentation is registered. Creation time is not treated as an applicability date.

Each edition is a complete snapshot with an immutable identifier. Definitions are stored by content: if one variable changes between two 636-variable editions, the other 635 reuse their definitions. Applications receive a complete dictionary without manually resolving patches. Names and labels can change without altering previously registered editions.

Selection accepts an exact version or an ISO applicability date. Intervals are inclusive. Uncovered or ambiguous dates raise errors. Renames must be declared explicitly when registering a revision; they are not inferred from matching labels. Use `labeler::dict_diff()` in R or the Python `diff()` method to inspect differences between editions.

The following registry uses fictitious dates only to explain the mechanism. It is not an official historical ENCFT dictionary series. The caller owns the connection. Use separate SQLite files for working registries and follow labeler/labelerpy transaction policy.

Dictionary versions describe questionnaires; `pobreza_monetaria_2012` and `pobreza_monetaria_2022` select calculation methodologies. These are independent choices. Persist package version, dictionary version and hash, methodology, response periods and economic-table coverage with an analysis.

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
