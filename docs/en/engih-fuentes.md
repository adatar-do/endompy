# Sources, coverage and corrections

Metadata come from the [Central Bank ENGIH 2018 workbooks and questionnaires](https://www.bancentral.gov.do/a/d/4796-engih-2018). All 58 metadata/dictionary files from `engihr 0.3.0` are copied unchanged, retaining source URLs, SHA256 and row provenance. Original household records are not bundled.

Catalogs contain 8090 varieties, 120 units, 202 establishments, 249 countries and 72 currencies. Unit and establishment labels append bracketed codes to distinguish repeated descriptions; `catalog()` retains original text.

Three documented decisions are retained: A101 is a count according to questionnaire A, PDF page 5, so incorrect Yes/No codes are omitted; C2/C3 are matched by explicit periodicity where section numbers conflict; an unnamed C6C dictionary row is not assigned to an invented field. A102, street lighting, paved streets and ZONA where present are backed by the questionnaire.

The module does not calculate expenditure, income, poverty, weights or official aggregates. Worksheets have different observation units: check cardinality and design before joining.

The default `coverage-2` revision documents 1,700 of 1,702 field occurrences across 25 modules: 530 original official dictionary definitions, 647 verified questionnaire cells and 523 descriptions of published headers. Header descriptions do not specify undocumented formulas, imputations, code universes or uniqueness rules. Persons covers 1,130 of 1,132 fields; the other 24 modules cover their entire inventories.

`HOLGURA` and `PERDIDA_TURISMO` remain without verifiable definitions and outside the dictionary. Original columns survive and are listed as unresolved. `dictionary_coverage()` exposes totals and limits; `dictionary_coverage(provenance=True)` returns field provenance. Historical `baseline-1` retains all 530 original references unchanged. `modules(version="baseline-1")` and `schema(version="baseline-1")` expose historical coverage.

D802 monthly fields are matrix positions whose calendar period depends on `REPLICA`: M1 is not universally January. Countries and currencies retain official text codes. A201_APTOS counts apartments per floor; A401A is total household membership. Missing-value codes are not invented for amounts or counts.

```python
from endompy import engihr as e
assert e.modules()["documented"].sum() == 1700
assert len(e.schema()) == 1132
assert e.schema()["documented"].sum() == 1130
assert len(e.catalog("variedades")) == 8090
assert len(e.source_issues()) == 3
assert e.get_dict()["A101"].labels is None
```
