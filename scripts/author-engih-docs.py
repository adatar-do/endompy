"""Author paired ENGIH guides and API documentation without changing other modules."""
from pathlib import Path
import inspect
import json
import sys

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from endompy import engihr as e

guides = {'engih-engihr': ('ENGIH 2018 en Python',
                  'ENGIH 2018 in Python',
                  '`endompy.engihr` reproduce los contratos de `engihr 0.3.0` para los metadatos de ENGIH 2018. '
                  'Incluye 25 módulos, diccionarios inmutables y catálogos oficiales. No necesita R durante su '
                  'uso.\n'
                  '\n'
                  'Seleccione `module` para hojas de gasto: el valor predeterminado es `personas`. `get_dict()` '
                  'identifica una revisión; `modules()` y `schema()` muestran qué datos están documentados. El '
                  'inventario suma 1702 apariciones de campos; 1700 tienen definición verificada, incluyendo 1130 '
                  'de 1132 campos de Personas.\n'
                  '\n'
                  'Use `set_labels()` para conservar códigos y `use_labels()` para presentación. El ejemplo '
                  'siguiente es inventado. [Etiquetas y validación](engih-etiquetas.md) explica tipos y '
                  'faltantes; [fuentes](engih-fuentes.md) detalla cobertura y correcciones. Consulte también '
                  '[versionado](engih-versionado.md), [integración](engih-integracion.md), '
                  '[instalación](engih-deployment.md) y [referencia](engih-reference.md).\n'
                  '\n'
                  'Consulte la guía de fuentes: distingue las definiciones originales, las celdas de cuestionario '
                  'y las descripciones de encabezados. Los dos campos técnicos sin definición se mantienen '
                  'explícitos.',
                  '`endompy.engihr` follows `engihr 0.3.0` contracts for ENGIH 2018 metadata. It bundles 25 '
                  'modules, immutable dictionaries and official catalogs. R is not needed at runtime.\n'
                  '\n'
                  'Choose `module` for expenditure worksheets; the default is `personas`. `get_dict()` selects a '
                  'revision, while `modules()` and `schema()` expose documented coverage. The inventory contains '
                  '1702 field occurrences; 1700 have verified definitions, including 1130 of 1132 Persons '
                  'fields.\n'
                  '\n'
                  'Use `set_labels()` to retain codes and `use_labels()` for presentation. The following example '
                  'is invented. [Labels and validation](engih-etiquetas.md) explains types and missingness; '
                  '[sources](engih-fuentes.md) details coverage and corrections. See '
                  '[versioning](engih-versionado.md), [integration](engih-integracion.md), '
                  '[installation](engih-deployment.md) and [reference](engih-reference.md).\n'
                  '\n'
                  'Consult the sources guide for the distinction between original definitions, questionnaire '
                  'cells and header descriptions. Two undefined technical fields remain explicit.',
                  'from endompy import EngihDataFrame, engihr as e\n'
                  'x = EngihDataFrame(e.example())\n'
                  'y = x.set_labels()\n'
                  'assert y["A201"].equals(x["A201"])\n'
                  'assert x.use_labels().loc[1, "A201"] == "Apartamento en edificio con ascensor"\n'
                  'assert len(e.modules()) == 25\n'),
 'engih-etiquetas': ('Etiquetas, códigos y validación',
                     'Labels, codes and validation',
                     '`set_labels(tbl, dictionary=None, vars=None, module="personas", edition=2018, version=None, '
                     'at=None, con=None, strict=False)` conserva valores, tipos de pandas, nombres e índice. Solo '
                     'etiqueta los campos seleccionados presentes en el diccionario. El módulo admite tablas '
                     'locales y nombres de columnas únicos y no vacíos; `vars` es una lista de nombres existentes '
                     'sin repetición.\n'
                     '\n'
                     '`use_labels()` devuelve categorías de pandas para las columnas con catálogo. Conserva NA y '
                     'códigos desconocidos; cuando un desconocido coincide con una etiqueta, se distingue '
                     'mediante `[unlabelled code: ...]`. Los conteos A101 y A102 permanecen numéricos. '
                     '`strict=True` rechaza códigos fuera del catálogo.\n'
                     '\n'
                     'Los códigos numéricos requieren una columna numérica; no se interpretan cadenas como '
                     'números, categorías existentes ni booleanos como 1/0. Se admiten columnas completamente '
                     'ausentes y tipos anulables de pandas. `validate()` informa `unmapped`, `label_only`, `ok`, '
                     '`unknown_codes` o `type_mismatch`. No evalúa saltos, imputaciones, ponderaciones ni '
                     'estimaciones de encuesta.\n'
                     '\n'
                     'Los metadatos de tabla se conservan en `DataFrame.attrs`; consulte etiquetas mediante '
                     '`df.labeler.get_label()` y `df.labeler.get_labels()`. `labeler_provenance` identifica '
                     'revisión y definición por variable. Las categorías y los atributos de R/pandas son '
                     'representaciones propias de cada lenguaje; las comprobaciones comparan valores, etiquetas, '
                     'orden, faltantes y procedencia.',
                     '`set_labels(tbl, dictionary=None, vars=None, module="personas", edition=2018, version=None, '
                     'at=None, con=None, strict=False)` preserves values, pandas dtypes, column names and index. '
                     'It labels only selected fields found in the dictionary. Tables must be local and column '
                     'names unique and nonempty; `vars` is a list of unique existing names.\n'
                     '\n'
                     '`use_labels()` returns pandas categorical columns for mapped value codes. Missing and '
                     'unknown values survive; an unknown code equal to a known label receives `[unlabelled code: '
                     '...]`. Counts A101 and A102 remain numeric. `strict=True` rejects codes outside the '
                     'catalog.\n'
                     '\n'
                     'Numeric codes require numeric columns. Strings are not parsed as numbers, existing '
                     'categories are rejected, and booleans are not treated as 1/0. All-missing columns and '
                     'nullable pandas dtypes are supported. `validate()` reports `unmapped`, `label_only`, `ok`, '
                     '`unknown_codes` or `type_mismatch`. It does not evaluate skip patterns, imputations, '
                     'weights or survey estimates.\n'
                     '\n'
                     'Table metadata live in `DataFrame.attrs`; inspect labels through `df.labeler.get_label()` '
                     'and `df.labeler.get_labels()`. `labeler_provenance` identifies each variable revision and '
                     'definition. R and pandas use their own categorical/attribute representations; checks '
                     'compare values, labels, order, missingness and provenance.',
                     'import pandas as pd\n'
                     'from endompy import engihr as e\n'
                     'x = pd.DataFrame({"A201": [1, 1234, None], "A101": [1, 3, None]})\n'
                     'x.index = [7, 7, 2]\n'
                     'y = e.set_labels(x)\n'
                     'z = e.use_labels(x)\n'
                     'assert y["A201"].equals(x["A201"])\n'
                     'assert z.loc[2, "A101"] != z.loc[2, "A101"]\n'
                     'assert z["A201"].iloc[1] == "1234"\n'
                     'assert e.validate(x).loc[0, "status"] == "unknown_codes"\n'
                     'assert y.labeler.get_label("A101")\n'),
 'engih-versionado': ('Revisiones cuando cambian pocas variables',
                      'Revisions when few variables change',
                      'Cada módulo conserva exactamente la revisión `baseline-1` distribuida por R: misma '
                      'identidad, huella de contenido y referencias de definición. La edición de encuesta 2018 y '
                      'la revisión de metadatos son identificadores distintos.\n'
                      '\n'
                      'Para modificar una definición use `dictionary.draft()`, edite la variable y registre una '
                      'nueva revisión con `register_dict()`. Las variables sin cambios reutilizan sus '
                      'definiciones; la variable modificada conserva su identidad. `parent_version` permite '
                      'elegir un padre explícito y `renames` declarar cambios de nombre.\n'
                      '\n'
                      'La conexión `sqlite3` pertenece al usuario: las operaciones no la cierran y respetan sus '
                      'transacciones. Un registro requiere `version` explícita o una fecha `at` con vigencia '
                      'documentada. No se infiere la revisión más reciente ni se inventa vigencia a partir de '
                      '2018. Las revisiones incluidas carecen de intervalos y rechazan selección por fecha.\n'
                      '\n'
                      'El JSON intercambiable y `RevisionRegistry.import_revision()` permiten trasladar '
                      'diccionarios de R. Las huellas detectan alteraciones del contenido; no son firmas de '
                      'autor. El ejemplo usa una base SQLite en memoria.\n'
                      '\n'
                      'Cada módulo incluye `baseline-1` y su hija `coverage-2`. Sin registro externo, se '
                      'selecciona `coverage-2` por defecto; indique `version="baseline-1"` para reproducir la '
                      'revisión inicial. Las 530 referencias anteriores no cambian.',
                      'Each module retains the exact `baseline-1` revision distributed by R: identical dictionary '
                      'identity, content fingerprint and definition references. Survey edition 2018 and metadata '
                      'revision are separate identifiers.\n'
                      '\n'
                      'Use `dictionary.draft()`, edit a definition and call `register_dict()` to create a new '
                      'revision. Unchanged variables reuse their definitions; the modified variable retains its '
                      'identity. `parent_version` chooses an explicit parent and `renames` declares variable '
                      'renames.\n'
                      '\n'
                      'The caller owns the `sqlite3` connection: operations do not close it and preserve caller '
                      'transactions. Registry selection requires an explicit `version` or an `at` date with '
                      'documented applicability. The latest revision is not inferred, and 2018 does not invent '
                      'validity dates. Bundled revisions have no intervals and reject date selection.\n'
                      '\n'
                      'Interchange JSON and `RevisionRegistry.import_revision()` import dictionaries from R. '
                      'Fingerprints detect content modifications; they are not author signatures. This example '
                      'uses an in-memory SQLite database.\n'
                      '\n'
                      'Each module includes `baseline-1` and its child `coverage-2`. Without an external '
                      'registry, `coverage-2` is the default; pass `version="baseline-1"` to reproduce the '
                      'original revision. All 530 earlier references are unchanged.',
                      'import sqlite3\n'
                      'from labelerpy import RevisionRegistry\n'
                      'from endompy import engihr as e\n'
                      'con = sqlite3.connect(":memory:")\n'
                      'original = e.get_dict("b1", version="baseline-1")\n'
                      'RevisionRegistry(con).import_revision(original)\n'
                      'draft = original.draft()\n'
                      'field = "FREC_COMPRA_ALIMENTOS"\n'
                      'draft[field].label = "Reviewed purchase frequency"\n'
                      'revised = e.register_dict(con, draft, "review-2", module="b1")\n'
                      'before = original.revision()["variable_refs"]\n'
                      'after = revised.revision()["variable_refs"]\n'
                      'assert all(before[k] == after[k] for k in before if k != field)\n'
                      'assert before[field]["variable_id"] == after[field]["variable_id"]\n'
                      'assert len(e.dict_versions("b1", con=con)) == 2\n'
                      'assert e.get_dict("b1", con=con, version="baseline-1").revision() == original.revision()\n'
                      'con.close()\n'),
 'engih-fuentes': ('Fuentes, cobertura y correcciones',
                   'Sources, coverage and corrections',
                   'Los metadatos proceden de los [Excel y cuestionarios de ENGIH 2018 del Banco '
                   'Central](https://www.bancentral.gov.do/a/d/4796-engih-2018). Se copian sin cambios los 58 '
                   'archivos de metadatos/diccionarios de `engihr 0.3.0`, con URL, SHA256 y filas de procedencia. '
                   'No se incluyen registros originales de hogares.\n'
                   '\n'
                   'Los catálogos contienen 8090 variedades, 120 unidades, 202 establecimientos, 249 países y 72 '
                   'monedas. Las etiquetas de unidades y establecimientos añaden códigos entre corchetes para '
                   'distinguir textos repetidos; `catalog()` conserva los textos originales.\n'
                   '\n'
                   'Se conservan tres decisiones documentadas: A101 es un conteo según el cuestionario A, página '
                   'PDF 5, y se omite su codificación Sí/No errónea; C2/C3 se vinculan por periodicidad explícita '
                   'ante numeración inconsistente; una fila de C6C sin identificador no se asigna a un campo '
                   'inventado. A102, alumbrado, calles asfaltadas y ZONA donde existe se respaldan con el '
                   'cuestionario.\n'
                   '\n'
                   'El módulo no calcula gastos, ingresos, pobreza, ponderaciones ni agregados oficiales. Las '
                   'hojas tienen distintas unidades de observación: compruebe cardinalidad y diseño antes de '
                   'unirlas.\n'
                   '\n'
                   'La revisión predeterminada `coverage-2` documenta 1,700 de 1,702 apariciones de campos en 25 '
                   'módulos: 530 definiciones originales del diccionario oficial, 647 celdas verificadas de '
                   'cuestionarios y 523 descripciones de encabezados publicados. Estas últimas no especifican '
                   'fórmulas, imputaciones, universos de códigos ni reglas de unicidad que la fuente no '
                   'documenta. Personas cubre 1,130 de 1,132 campos; los otros 24 módulos cubren su inventario '
                   'completo.\n'
                   '\n'
                   '`HOLGURA` y `PERDIDA_TURISMO` permanecen sin definición verificable y fuera del diccionario. '
                   'Se conservan sus columnas originales y se muestran como pendientes. `dictionary_coverage()` '
                   'expone los totales y límites; `dictionary_coverage(provenance=True)` devuelve la procedencia '
                   'por campo. La revisión histórica `baseline-1` conserva exactamente sus 530 referencias '
                   'originales. `modules(version="baseline-1")` y `schema(version="baseline-1")` permiten '
                   'consultar su cobertura histórica.\n'
                   '\n'
                   'Los campos mensuales D802 son posiciones de una matriz cuyo período depende de `REPLICA`: no '
                   'se asigna enero a M1 de forma general. Los países y monedas mantienen los códigos de texto de '
                   'sus catálogos oficiales. A201_APTOS cuenta apartamentos por piso; A401A es el total de '
                   'miembros del hogar. No se inventan códigos de valores perdidos para montos o conteos.',
                   'Metadata come from the [Central Bank ENGIH 2018 workbooks and '
                   'questionnaires](https://www.bancentral.gov.do/a/d/4796-engih-2018). All 58 '
                   'metadata/dictionary files from `engihr 0.3.0` are copied unchanged, retaining source URLs, '
                   'SHA256 and row provenance. Original household records are not bundled.\n'
                   '\n'
                   'Catalogs contain 8090 varieties, 120 units, 202 establishments, 249 countries and 72 '
                   'currencies. Unit and establishment labels append bracketed codes to distinguish repeated '
                   'descriptions; `catalog()` retains original text.\n'
                   '\n'
                   'Three documented decisions are retained: A101 is a count according to questionnaire A, PDF '
                   'page 5, so incorrect Yes/No codes are omitted; C2/C3 are matched by explicit periodicity '
                   'where section numbers conflict; an unnamed C6C dictionary row is not assigned to an invented '
                   'field. A102, street lighting, paved streets and ZONA where present are backed by the '
                   'questionnaire.\n'
                   '\n'
                   'The module does not calculate expenditure, income, poverty, weights or official aggregates. '
                   'Worksheets have different observation units: check cardinality and design before joining.\n'
                   '\n'
                   'The default `coverage-2` revision documents 1,700 of 1,702 field occurrences across 25 '
                   'modules: 530 original official dictionary definitions, 647 verified questionnaire cells and '
                   '523 descriptions of published headers. Header descriptions do not specify undocumented '
                   'formulas, imputations, code universes or uniqueness rules. Persons covers 1,130 of 1,132 '
                   'fields; the other 24 modules cover their entire inventories.\n'
                   '\n'
                   '`HOLGURA` and `PERDIDA_TURISMO` remain without verifiable definitions and outside the '
                   'dictionary. Original columns survive and are listed as unresolved. `dictionary_coverage()` '
                   'exposes totals and limits; `dictionary_coverage(provenance=True)` returns field provenance. '
                   'Historical `baseline-1` retains all 530 original references unchanged. '
                   '`modules(version="baseline-1")` and `schema(version="baseline-1")` expose historical '
                   'coverage.\n'
                   '\n'
                   'D802 monthly fields are matrix positions whose calendar period depends on `REPLICA`: M1 is '
                   'not universally January. Countries and currencies retain official text codes. A201_APTOS '
                   'counts apartments per floor; A401A is total household membership. Missing-value codes are not '
                   'invented for amounts or counts.',
                   'from endompy import engihr as e\n'
                   'assert e.modules()["documented"].sum() == 1700\n'
                   'assert len(e.schema()) == 1132\n'
                   'assert e.schema()["documented"].sum() == 1130\n'
                   'assert len(e.catalog("variedades")) == 8090\n'
                   'assert len(e.source_issues()) == 3\n'
                   'assert e.get_dict()["A101"].labels is None\n'),
 'engih-integracion': ('Integración y equivalencias con R',
                       'Integration and R equivalents',
                       'El nuevo módulo es aditivo en endompy 0.8.0; conserva las interfaces previas de ENCFT, '
                       'ENFT y ENHOGAR. Los catorce nombres públicos de funciones de `engihr 0.3.0`, incluidos '
                       'los dos alias antiguos, tienen equivalente Python. El operador `%>%` se expresa con '
                       'llamadas, métodos o `DataFrame.pipe`; no se crea un operador R en Python.\n'
                       '\n'
                       '`egi_dict` corresponde a `get_dict`, `egi_example` a `example` y los demás nombres '
                       'pierden el prefijo `egi_`. El prefijo también se conserva como alias. '
                       '`egi_setLabels`/`egi_useLabels` avisan de su deprecación. El argumento `dict` de R se '
                       'llama `dictionary` en Python; el orden posicional se conserva. Los diccionarios antiguos '
                       '`lab/labs` se aceptan con los mismos controles de módulo/edición cuando su metadata los '
                       'declara.\n'
                       '\n'
                       '`EngihDataFrame.set_labels()` y `.use_labels()` conservan el tipo de tabla; `.validate()` '
                       'devuelve una tabla diagnóstica ordinaria. Se preservan índices duplicados. La '
                       'equivalencia compara contenido y categorías, no clases internas de R con tipos de pandas. '
                       'R no es una dependencia de ejecución.',
                       'The new module is additive in endompy 0.8.0; existing ENCFT, ENFT and ENHOGAR interfaces '
                       'remain available. All fourteen public function names in `engihr 0.3.0`, including two '
                       'legacy aliases, have Python equivalents. Express `%>%` using calls, methods or '
                       '`DataFrame.pipe`; Python does not acquire an R operator.\n'
                       '\n'
                       '`egi_dict` maps to `get_dict`, `egi_example` to `example`, and other names drop `egi_`. '
                       'Prefixed aliases are also available. `egi_setLabels`/`egi_useLabels` emit deprecation '
                       "warnings. R's `dict` argument is named `dictionary` in Python; positional order is "
                       'preserved. Legacy `lab/labs` dictionaries are accepted with module/edition checks when '
                       'metadata declares them.\n'
                       '\n'
                       '`EngihDataFrame.set_labels()` and `.use_labels()` preserve the table subclass; '
                       '`.validate()` returns an ordinary diagnostic table. Duplicate row indices survive. '
                       'Equivalence compares content and category definitions, not R internals with pandas '
                       'dtypes. R is not a runtime dependency.',
                       'from endompy import EngihDataFrame, engihr as e\n'
                       'x = EngihDataFrame(e.example())\n'
                       'result = x.pipe(e.egi_set_labels).use_labels(vars=["A201"])\n'
                       'assert isinstance(result, EngihDataFrame)\n'
                       'assert e.egi_dict is e.get_dict\n'
                       'assert result["A101"].equals(x["A101"])\n'),
 'engih-deployment': ('Instalación, validación y despliegue',
                      'Installation, verification and deployment',
                      'Instale Python >= 3.9, pandas >= 1.5 y numpy >= 1.21. La entrega incluye `labelerpy 0.2.1` '
                      'y el wheel/sdist de `endompy 0.8.0`. Use `python -m pip install '
                      'labelerpy-0.2.1-py3-none-any.whl endompy-0.8.0-py3-none-any.whl` dentro de un entorno '
                      'virtual; las dependencias deben estar disponibles o ser accesibles en el índice '
                      'configurado.\n'
                      '\n'
                      'Para reconstruir: `python -m build`; `python -m twine check dist/*`; instale el wheel y '
                      'ejecute `python -I -m pytest tests --import-mode=importlib` y `python -I '
                      'scripts/check-examples.py`. `scripts/release-engih.py` reúne construcción, pruebas y sitio '
                      'en una salida explícita. La entrega local verifica instalaciones nuevas en Python '
                      '3.9/pandas 1.5 y Python 3.13/pandas 3, con regresiones de los módulos previos.\n'
                      '\n'
                      '`scripts/build-docs.py SALIDA` construye español e inglés; `scripts/check-sites.py SALIDA '
                      '--kind python` verifica enlaces, recursos, buscadores y páginas equivalentes. Sirva la '
                      'carpeta estática por HTTP conservando `en/`. Los workflows están preparados; publicación y '
                      'CI remoto requieren sus propias ejecuciones y la disponibilidad de labelerpy en el '
                      'índice.\n'
                      '\n'
                      'Para actualizar la referencia de ENGIH, desde ENDOM ejecute `Rscript '
                      'endompy/scripts/export-engih-reference.R` con `engihr 0.3.0` instalado y `python '
                      'endompy/scripts/sync-engih-resources.py engihr --check`. La referencia es sintética e '
                      'incluye todos los códigos categóricos, un desconocido y NA. Los recursos registrados no se '
                      'modifican al instalar el paquete. Los originales Excel y cuestionarios no forman parte de '
                      'la entrega.',
                      'Install Python >= 3.9, pandas >= 1.5 and numpy >= 1.21. The delivery includes `labelerpy '
                      '0.2.1` and the `endompy 0.8.0` wheel/sdist. Run `python -m pip install '
                      'labelerpy-0.2.1-py3-none-any.whl endompy-0.8.0-py3-none-any.whl` inside a virtual '
                      'environment; dependencies must be available or reachable through the configured index.\n'
                      '\n'
                      'To rebuild: `python -m build`; `python -m twine check dist/*`; install the wheel and run '
                      '`python -I -m pytest tests --import-mode=importlib` and `python -I '
                      'scripts/check-examples.py`. `scripts/release-engih.py` combines building, tests and site '
                      'generation in an explicit output. The local delivery verifies fresh Python 3.9/pandas 1.5 '
                      'and Python 3.13/pandas 3 environments, including existing-module regressions.\n'
                      '\n'
                      '`scripts/build-docs.py OUTPUT` builds both editions; `scripts/check-sites.py OUTPUT --kind '
                      'python` checks links, resources, search and equivalent pages. Serve the static folder over '
                      'HTTP and retain `en/`. Workflows are prepared; publishing and remote CI need separate runs '
                      'and labelerpy availability in the index.\n'
                      '\n'
                      'To refresh ENGIH references, run `Rscript endompy/scripts/export-engih-reference.R` from '
                      'ENDOM with `engihr 0.3.0` installed, then `python endompy/scripts/sync-engih-resources.py '
                      'engihr --check`. Synthetic references include every categorical code, an unknown value and '
                      'NA. Installing the package does not change registered revisions. Original Excel files and '
                      'questionnaires are not bundled.',
                      'from endompy import __version__, engihr as e\n'
                      'assert __version__ == "0.8.0"\n'
                      'assert e.get_dict("b1").revision()["dictionary_id"] == "engih-2018-b1"\n'
                      'assert e.get_dict("b1").revision()["version"] == "coverage-2"\n')}

functions = ["modules", "schema", "catalog", "source_issues", "example", "get_dict", "dict_versions", "register_dict", "set_labels", "use_labels", "validate", "dictionary_coverage"]
for name, (es_title, en_title, es, en, code) in guides.items():
    for lang, title, body in (("es", es_title, es), ("en", en_title, en)):
        (root / "docs" / lang / (name + ".md")).write_text("# " + title + "\n\n" + body + "\n\n```python\n" + code.rstrip() + "\n```\n", encoding="utf-8")
for lang in ("es", "en"):
    lines = ["# " + ("Referencia ENGIH" if lang == "es" else "ENGIH reference"), "",
        ("Funciones disponibles en `endompy.engihr`. Se conservan alias con prefijo `egi_`." if lang == "es" else "Functions available in `endompy.engihr`. Prefixed `egi_` aliases are retained."), ""]
    parameters = {
        "tbl": ("DataFrame local con códigos originales.", "Local DataFrame with original codes."),
        "dictionary": ("Dict o diccionario antiguo lab/labs; None selecciona una revisión.", "Dict or legacy lab/labs mapping; None selects a revision."),
        "vars": ("Lista de columnas existentes sin repetición; None usa la selección predeterminada.", "Unique existing column names; None uses the default selection."),
        "module": ("Módulo exacto de modules(); personas por defecto.", "Exact modules() identifier; personas by default."),
        "edition": ("Edición numérica 2018.", "Numeric survey edition 2018."),
        "version": ("Revisión exacta; baseline-1 sin registro cuando es None.", "Exact revision; baseline-1 without a registry when None."),
        "at": ("Fecha ISO de vigencia documentada; no inferida.", "ISO date requiring documented applicability."),
        "con": ("Conexión sqlite3 propiedad del usuario.", "Caller-owned sqlite3 connection."),
        "strict": ("True rechaza códigos desconocidos; tipos incompatibles siempre fallan.", "True rejects unknown codes; incompatible types always fail."),
        "catalog": ("variedades, unidades, establecimientos, paises o monedas.", "variedades, unidades, establecimientos, paises or monedas."),
        "valid_from": ("Inicio inclusivo de vigencia o None.", "Inclusive applicability start or None."),
        "valid_to": ("Final inclusivo de vigencia o None.", "Inclusive applicability end or None."),
        "provenance": ("True devuelve procedencia por campo; False totales y límites.", "True returns field provenance; False totals and limits."),
        "kwargs": ("Metadatos de registro: parent_version, author, message y renames.", "Registration metadata: parent_version, author, message and renames.")}
    descriptions_es = dict(zip(functions, ["Inventario de módulos y cobertura.", "Inventario completo de campos de una hoja.", "Catálogo oficial de códigos y textos.", "Incidencias y resoluciones de las fuentes.", "Cinco filas inventadas para ejemplos.", "Diccionario completo con integridad y ámbito verificados.", "Tabla de revisiones, fechas y huellas.", "Nueva revisión Dict con definiciones reutilizadas.", "Tabla etiquetada que conserva códigos, tipos e índice.", "Tabla de presentación con categorías y faltantes preservados.", "Tabla por campo con estado, n, missing y unknown.", "Cobertura, fuerza de la fuente y campos sin definición."]))
    for name in functions:
        function = getattr(e, name)
        lines += ["## " + name, "", "```text", name + str(inspect.signature(function)), "```", "",
            descriptions_es[name] if lang == "es" else inspect.getdoc(function), "",
            "| " + ("Argumento | Contrato" if lang == "es" else "Argument | Contract") + " |", "|---|---|"]
        for parameter in inspect.signature(function).parameters:
            lines.append("| `" + parameter + "` | " + parameters[parameter][0 if lang == "es" else 1] + " |")
        if not inspect.signature(function).parameters:
            lines.append("| — | " + ("Sin argumentos." if lang == "es" else "No arguments.") + " |")
        lines.append("")
    lines += ["## " + ("Alias e integración" if lang == "es" else "Aliases and integration"), "",
        "`egi_dict = get_dict`; `egi_example = example`; " + ", ".join("`egi_" + n + " = " + n + "`" for n in functions if n not in ("get_dict", "example")) + ".", "",
        ("`egi_setLabels` y `egi_useLabels` emiten DeprecationWarning; use set_labels/use_labels. EngihDataFrame incorpora ambos métodos y validate(). Los ejemplos ejecutables están en las seis guías." if lang == "es" else "`egi_setLabels` and `egi_useLabels` emit DeprecationWarning; use set_labels/use_labels. EngihDataFrame exposes both methods and validate(). Executable examples are in the six guides."), ""]
    (root / "docs" / lang / "engih-reference.md").write_text("\n".join(lines), encoding="utf-8")
mapping = {"egi_" + ("dict" if n == "get_dict" else n): "endompy.engihr." + n for n in functions}
mapping.update({"egi_setLabels": "endompy.engihr.egi_setLabels", "egi_useLabels": "endompy.engihr.egi_useLabels"})
(root / "engih-api-parity.json").write_text(json.dumps({"r_package": "engihr", "r_version": "0.3.0", "python_package": "endompy", "python_version": "0.8.0", "functions": mapping,
    "representations": {"factor": "pandas.Categorical", "dict_argument": "dictionary", "pipe": "DataFrame.pipe", "dataset_dict": "get_dict()"},
    "coverage": {"modules": 25, "field_occurrences": 1702, "documented_descriptions": 1700, "original_definitions": 530, "questionnaire_definitions": 647, "published_headers": 523, "unresolved_fields": 2, "personas_fields": 1132, "personas_definitions": 1130}}, indent=2), encoding="utf-8")
print("Authored six paired ENGIH guides, complete API reference and 14-function parity map")
