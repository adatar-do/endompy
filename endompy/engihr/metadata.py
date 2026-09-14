"""Official ENGIH metadata copied without changing the R package's resources."""
import gzip
import json
import numbers
from pathlib import Path
import pandas as pd

RESOURCE = Path(__file__).parent / "resources"


def _edition(edition):
    if isinstance(edition, bool) or not isinstance(edition, numbers.Real) or edition != 2018:
        raise ValueError("Only ENGIH 2018 is bundled")


def _text(value, name):
    if not isinstance(value, str) or not value:
        raise ValueError(name + " must be one nonempty string")


def _json(name):
    opener = gzip.open if name.endswith(".gz") else open
    with opener(RESOURCE / "reference" / name, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def _metadata_version(version=None):
    version = "coverage-2" if version is None else version
    _text(version, "version")
    if version not in ("baseline-1", "coverage-2"):
        raise ValueError("Revision not bundled")
    return version


def _schemas(version=None):
    return _json("schemas.json" if _metadata_version(version) == "baseline-1" else "schemas-coverage-2.json")


def _module(module, edition=2018, version=None):
    _edition(edition)
    _text(module, "module")
    schemas = _schemas(version)
    if module not in schemas:
        raise ValueError("Unknown module; see modules()")
    return schemas[module]


def modules(edition=2018, version=None):
    """Return the 25 worksheet inventories and documented/undocumented counts."""
    _edition(edition)
    return pd.DataFrame([{
        "module": s["module"], "edition": edition, "workbook": s["workbook"],
        "sheet": s["sheet"], "source_rows": s["source_rows"], "fields": len(s["fields"]),
        "documented": len(s["documented_fields"]), "undocumented": len(s["fields_without_definition"]),
    } for s in _schemas(version).values()])


def schema(module="personas", edition=2018, version=None):
    """Return every field in worksheet order and whether a definition is bundled."""
    source = _module(module, edition, version)
    return pd.DataFrame({"position": range(1, len(source["fields"]) + 1),
        "field": source["fields"],
        "documented": [name in source["documented_fields"] for name in source["fields"]]})


def catalog(catalog="variedades", edition=2018):
    """Return original reference records: variedades, unidades, establecimientos, paises or monedas."""
    _edition(edition)
    _text(catalog, "catalog")
    catalogs = _json("catalogs.json.gz")
    if catalog not in catalogs:
        raise ValueError("Unknown catalog")
    return pd.DataFrame(catalogs[catalog])


def source_issues(edition=2018):
    """Return the three documented source inconsistencies and their resolutions."""
    _edition(edition)
    return pd.DataFrame(_json("source-issues.json"))


def example():
    """Return five invented rows, matching egi_example() in R; no respondent records."""
    return pd.DataFrame({"A101": [1, 2, 3, None, 1], "A102": [1, 1, 2, 1, None],
        "A201": [1, 4, 5, 99, None], "ALUMBRADO_PUBLICO": [1, 2, 1, 2, None],
        "example_id": ["synthetic-" + str(i) for i in range(1, 6)]})


def dictionary_coverage(provenance=False, edition=2018, version=None):
    """Return totals/limits or field provenance; historical baseline remains selectable."""
    _edition(edition)
    version = _metadata_version(version)
    if not isinstance(provenance, bool):
        raise ValueError("provenance must be True or False")
    if not provenance:
        return _json("coverage.json" if version == "baseline-1" else "coverage-2.json")
    entries = _json("provenance-coverage-2.json")
    if version == "baseline-1":
        entries = {key: value for key, value in entries.items() if value["definition_status"] == "official_dictionary"}
    return entries
