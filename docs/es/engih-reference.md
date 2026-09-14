# Referencia ENGIH

Funciones disponibles en `endompy.engihr`. Se conservan alias con prefijo `egi_`.

## modules

```text
modules(edition=2018, version=None)
```

Inventario de módulos y cobertura.

| Argumento | Contrato |
|---|---|
| `edition` | Edición numérica 2018. |
| `version` | Revisión exacta; baseline-1 sin registro cuando es None. |

## schema

```text
schema(module='personas', edition=2018, version=None)
```

Inventario completo de campos de una hoja.

| Argumento | Contrato |
|---|---|
| `module` | Módulo exacto de modules(); personas por defecto. |
| `edition` | Edición numérica 2018. |
| `version` | Revisión exacta; baseline-1 sin registro cuando es None. |

## catalog

```text
catalog(catalog='variedades', edition=2018)
```

Catálogo oficial de códigos y textos.

| Argumento | Contrato |
|---|---|
| `catalog` | variedades, unidades, establecimientos, paises o monedas. |
| `edition` | Edición numérica 2018. |

## source_issues

```text
source_issues(edition=2018)
```

Incidencias y resoluciones de las fuentes.

| Argumento | Contrato |
|---|---|
| `edition` | Edición numérica 2018. |

## example

```text
example()
```

Cinco filas inventadas para ejemplos.

| Argumento | Contrato |
|---|---|
| — | Sin argumentos. |

## get_dict

```text
get_dict(module='personas', edition=2018, version=None, at=None, con=None)
```

Diccionario completo con integridad y ámbito verificados.

| Argumento | Contrato |
|---|---|
| `module` | Módulo exacto de modules(); personas por defecto. |
| `edition` | Edición numérica 2018. |
| `version` | Revisión exacta; baseline-1 sin registro cuando es None. |
| `at` | Fecha ISO de vigencia documentada; no inferida. |
| `con` | Conexión sqlite3 propiedad del usuario. |

## dict_versions

```text
dict_versions(module='personas', edition=2018, con=None)
```

Tabla de revisiones, fechas y huellas.

| Argumento | Contrato |
|---|---|
| `module` | Módulo exacto de modules(); personas por defecto. |
| `edition` | Edición numérica 2018. |
| `con` | Conexión sqlite3 propiedad del usuario. |

## register_dict

```text
register_dict(con, dictionary, version, module='personas', edition=2018, valid_from=None, valid_to=None, **kwargs)
```

Nueva revisión Dict con definiciones reutilizadas.

| Argumento | Contrato |
|---|---|
| `con` | Conexión sqlite3 propiedad del usuario. |
| `dictionary` | Dict o diccionario antiguo lab/labs; None selecciona una revisión. |
| `version` | Revisión exacta; baseline-1 sin registro cuando es None. |
| `module` | Módulo exacto de modules(); personas por defecto. |
| `edition` | Edición numérica 2018. |
| `valid_from` | Inicio inclusivo de vigencia o None. |
| `valid_to` | Final inclusivo de vigencia o None. |
| `kwargs` | Metadatos de registro: parent_version, author, message y renames. |

## set_labels

```text
set_labels(tbl, dictionary=None, vars=None, module='personas', edition=2018, version=None, at=None, con=None, strict=False)
```

Tabla etiquetada que conserva códigos, tipos e índice.

| Argumento | Contrato |
|---|---|
| `tbl` | DataFrame local con códigos originales. |
| `dictionary` | Dict o diccionario antiguo lab/labs; None selecciona una revisión. |
| `vars` | Lista de columnas existentes sin repetición; None usa la selección predeterminada. |
| `module` | Módulo exacto de modules(); personas por defecto. |
| `edition` | Edición numérica 2018. |
| `version` | Revisión exacta; baseline-1 sin registro cuando es None. |
| `at` | Fecha ISO de vigencia documentada; no inferida. |
| `con` | Conexión sqlite3 propiedad del usuario. |
| `strict` | True rechaza códigos desconocidos; tipos incompatibles siempre fallan. |

## use_labels

```text
use_labels(tbl, dictionary=None, vars=None, module='personas', edition=2018, version=None, at=None, con=None, strict=False)
```

Tabla de presentación con categorías y faltantes preservados.

| Argumento | Contrato |
|---|---|
| `tbl` | DataFrame local con códigos originales. |
| `dictionary` | Dict o diccionario antiguo lab/labs; None selecciona una revisión. |
| `vars` | Lista de columnas existentes sin repetición; None usa la selección predeterminada. |
| `module` | Módulo exacto de modules(); personas por defecto. |
| `edition` | Edición numérica 2018. |
| `version` | Revisión exacta; baseline-1 sin registro cuando es None. |
| `at` | Fecha ISO de vigencia documentada; no inferida. |
| `con` | Conexión sqlite3 propiedad del usuario. |
| `strict` | True rechaza códigos desconocidos; tipos incompatibles siempre fallan. |

## validate

```text
validate(tbl, dictionary=None, vars=None, module='personas', edition=2018, version=None, at=None, con=None)
```

Tabla por campo con estado, n, missing y unknown.

| Argumento | Contrato |
|---|---|
| `tbl` | DataFrame local con códigos originales. |
| `dictionary` | Dict o diccionario antiguo lab/labs; None selecciona una revisión. |
| `vars` | Lista de columnas existentes sin repetición; None usa la selección predeterminada. |
| `module` | Módulo exacto de modules(); personas por defecto. |
| `edition` | Edición numérica 2018. |
| `version` | Revisión exacta; baseline-1 sin registro cuando es None. |
| `at` | Fecha ISO de vigencia documentada; no inferida. |
| `con` | Conexión sqlite3 propiedad del usuario. |

## dictionary_coverage

```text
dictionary_coverage(provenance=False, edition=2018, version=None)
```

Cobertura, fuerza de la fuente y campos sin definición.

| Argumento | Contrato |
|---|---|
| `provenance` | True devuelve procedencia por campo; False totales y límites. |
| `edition` | Edición numérica 2018. |
| `version` | Revisión exacta; baseline-1 sin registro cuando es None. |

## Alias e integración

`egi_dict = get_dict`; `egi_example = example`; `egi_modules = modules`, `egi_schema = schema`, `egi_catalog = catalog`, `egi_source_issues = source_issues`, `egi_dict_versions = dict_versions`, `egi_register_dict = register_dict`, `egi_set_labels = set_labels`, `egi_use_labels = use_labels`, `egi_validate = validate`, `egi_dictionary_coverage = dictionary_coverage`.

`egi_setLabels` y `egi_useLabels` emiten DeprecationWarning; use set_labels/use_labels. EngihDataFrame incorpora ambos métodos y validate(). Los ejemplos ejecutables están en las seis guías.
