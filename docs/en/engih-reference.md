# ENGIH reference

Functions available in `endompy.engihr`. Prefixed `egi_` aliases are retained.

## modules

```text
modules(edition=2018, version=None)
```

Return the 25 worksheet inventories and documented/undocumented counts.

| Argument | Contract |
|---|---|
| `edition` | Numeric survey edition 2018. |
| `version` | Exact revision; baseline-1 without a registry when None. |

## schema

```text
schema(module='personas', edition=2018, version=None)
```

Return every field in worksheet order and whether a definition is bundled.

| Argument | Contract |
|---|---|
| `module` | Exact modules() identifier; personas by default. |
| `edition` | Numeric survey edition 2018. |
| `version` | Exact revision; baseline-1 without a registry when None. |

## catalog

```text
catalog(catalog='variedades', edition=2018)
```

Return original reference records: variedades, unidades, establecimientos, paises or monedas.

| Argument | Contract |
|---|---|
| `catalog` | variedades, unidades, establecimientos, paises or monedas. |
| `edition` | Numeric survey edition 2018. |

## source_issues

```text
source_issues(edition=2018)
```

Return the three documented source inconsistencies and their resolutions.

| Argument | Contract |
|---|---|
| `edition` | Numeric survey edition 2018. |

## example

```text
example()
```

Return five invented rows, matching egi_example() in R; no respondent records.

| Argument | Contract |
|---|---|
| — | No arguments. |

## get_dict

```text
get_dict(module='personas', edition=2018, version=None, at=None, con=None)
```

Select coverage-2, an explicit baseline-1, or an exact registry revision/applicability date.

| Argument | Contract |
|---|---|
| `module` | Exact modules() identifier; personas by default. |
| `edition` | Numeric survey edition 2018. |
| `version` | Exact revision; baseline-1 without a registry when None. |
| `at` | ISO date requiring documented applicability. |
| `con` | Caller-owned sqlite3 connection. |

## dict_versions

```text
dict_versions(module='personas', edition=2018, con=None)
```

List revision identity, parent, dates, author, message and content fingerprint.

| Argument | Contract |
|---|---|
| `module` | Exact modules() identifier; personas by default. |
| `edition` | Numeric survey edition 2018. |
| `con` | Caller-owned sqlite3 connection. |

## register_dict

```text
register_dict(con, dictionary, version, module='personas', edition=2018, valid_from=None, valid_to=None, **kwargs)
```

Register a Dict draft, reusing unchanged definitions and caller-owned transactions.

| Argument | Contract |
|---|---|
| `con` | Caller-owned sqlite3 connection. |
| `dictionary` | Dict or legacy lab/labs mapping; None selects a revision. |
| `version` | Exact revision; baseline-1 without a registry when None. |
| `module` | Exact modules() identifier; personas by default. |
| `edition` | Numeric survey edition 2018. |
| `valid_from` | Inclusive applicability start or None. |
| `valid_to` | Inclusive applicability end or None. |
| `kwargs` | Registration metadata: parent_version, author, message and renames. |

## set_labels

```text
set_labels(tbl, dictionary=None, vars=None, module='personas', edition=2018, version=None, at=None, con=None, strict=False)
```

Attach labels/provenance while preserving values, dtypes, columns and index.

Type mismatches always fail. strict=True also rejects unknown codes; the
default preserves them. Only selected documented fields receive labels.

| Argument | Contract |
|---|---|
| `tbl` | Local DataFrame with original codes. |
| `dictionary` | Dict or legacy lab/labs mapping; None selects a revision. |
| `vars` | Unique existing column names; None uses the default selection. |
| `module` | Exact modules() identifier; personas by default. |
| `edition` | Numeric survey edition 2018. |
| `version` | Exact revision; baseline-1 without a registry when None. |
| `at` | ISO date requiring documented applicability. |
| `con` | Caller-owned sqlite3 connection. |
| `strict` | True rejects unknown codes; incompatible types always fail. |

## use_labels

```text
use_labels(tbl, dictionary=None, vars=None, module='personas', edition=2018, version=None, at=None, con=None, strict=False)
```

Return categorical presentation columns, retaining missing and unknown values.

Label-only fields remain numeric. Unknown codes that equal a known display
label receive [unlabelled code: ...]. Input and duplicate row indices survive.

| Argument | Contract |
|---|---|
| `tbl` | Local DataFrame with original codes. |
| `dictionary` | Dict or legacy lab/labs mapping; None selects a revision. |
| `vars` | Unique existing column names; None uses the default selection. |
| `module` | Exact modules() identifier; personas by default. |
| `edition` | Numeric survey edition 2018. |
| `version` | Exact revision; baseline-1 without a registry when None. |
| `at` | ISO date requiring documented applicability. |
| `con` | Caller-owned sqlite3 connection. |
| `strict` | True rejects unknown codes; incompatible types always fail. |

## validate

```text
validate(tbl, dictionary=None, vars=None, module='personas', edition=2018, version=None, at=None, con=None)
```

Report field, status, n, missing and unknown without changing the table.

Status: unmapped, label_only, ok, unknown_codes or type_mismatch. This checks
metadata/code coverage; it does not certify survey consistency or estimates.

| Argument | Contract |
|---|---|
| `tbl` | Local DataFrame with original codes. |
| `dictionary` | Dict or legacy lab/labs mapping; None selects a revision. |
| `vars` | Unique existing column names; None uses the default selection. |
| `module` | Exact modules() identifier; personas by default. |
| `edition` | Numeric survey edition 2018. |
| `version` | Exact revision; baseline-1 without a registry when None. |
| `at` | ISO date requiring documented applicability. |
| `con` | Caller-owned sqlite3 connection. |

## dictionary_coverage

```text
dictionary_coverage(provenance=False, edition=2018, version=None)
```

Return totals/limits or field provenance; historical baseline remains selectable.

| Argument | Contract |
|---|---|
| `provenance` | True returns field provenance; False totals and limits. |
| `edition` | Numeric survey edition 2018. |
| `version` | Exact revision; baseline-1 without a registry when None. |

## Aliases and integration

`egi_dict = get_dict`; `egi_example = example`; `egi_modules = modules`, `egi_schema = schema`, `egi_catalog = catalog`, `egi_source_issues = source_issues`, `egi_dict_versions = dict_versions`, `egi_register_dict = register_dict`, `egi_set_labels = set_labels`, `egi_use_labels = use_labels`, `egi_validate = validate`, `egi_dictionary_coverage = dictionary_coverage`.

`egi_setLabels` and `egi_useLabels` emit DeprecationWarning; use set_labels/use_labels. EngihDataFrame exposes both methods and validate(). Executable examples are in the six guides.
