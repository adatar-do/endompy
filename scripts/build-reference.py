"""Build paired API references and the English pkgdown Rd edition.

The API manifest checks every R export against a callable Python entry point or
an explicit native-environment adapter. Signatures and examples are preserved.
"""
import hashlib
import inspect
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "endompy"), str(ROOT / "labelerpy")]
import endompy.encftr as api
from endompy.encftr.rules import RULES, RESOURCES

R = ROOT / "encftr"
P = ROOT / "endompy"
EN = R / "pkgdown/i18n/en/man"
EN.mkdir(parents=True, exist_ok=True)

PARAMS = {
"tbl": ("Tabla local de respuestas de personas, con nombres y códigos originales de ENCFT.", "Local table of person responses with original ENCFT names and codes."),
"vivienda_tbl": ("Tabla opcional de vivienda; completa texto de paredes por PERIODO y VIVIENDA.", "Optional dwelling table; fills wall text by PERIODO and VIVIENDA."),
"dict": ("Diccionario explícito; NULL usa la edición indicada o los metadatos guardados según la función.", "Explicit dictionary; NULL uses the selected edition or stored metadata, depending on the function."),
"dictionary": ("Diccionario explícito; None usa la edición indicada o los metadatos guardados según la función.", "Explicit dictionary; None uses the selected edition or stored metadata, depending on the function."),
"con": ("Conexión al registro SQLite de revisiones. El llamador administra su ciclo de vida.", "Connection to the SQLite revision registry. The caller owns its lifecycle."),
"version": ("Identificador exacto de edición, sin sustitución silenciosa. baseline-1 es la única incluida.", "Exact edition identifier with no silent fallback. baseline-1 is the only bundled edition."),
"at": ("Fecha ISO de aplicabilidad. Requiere intervalos documentados; falla si no hay coincidencia única.", "ISO applicability date. Requires documented intervals and a unique match."),
"valid_from": ("Primera fecha ISO de vigencia inclusiva; omitida si no se conoce.", "Inclusive first ISO applicability date; omitted if unknown."),
"valid_to": ("Última fecha ISO de vigencia inclusiva; omitida si no se conoce.", "Inclusive last ISO applicability date; omitted if unknown."),
"subset": ("Nombres de columnas a etiquetar; omitido aplica a las coincidencias disponibles.", "Column names to label; omitted applies to available matches."),
"vars": ("Nombres de columnas seleccionadas; en los auxiliares anteriores equivale a subset.", "Selected column names; equivalent to subset in legacy labeling helpers."),
"min_edad": ("Límite inferior inclusivo de edad en años.", "Inclusive lower age bound in years."),
"max_edad": ("Límite superior inclusivo de edad en años.", "Inclusive upper age bound in years."),
"periods": ("Divisor declarado: 1–4 anual, 1–2 semestral. Omitido usa cobertura observada por año.", "Declared divisor: 1–4 annual, 1–2 semester. Omitted uses observed coverage within year."),
"secundaria_base": ("armonizada_6_6, legacy_8_4 o historica_por_ano. Define la base antes del grado secundario.", "armonizada_6_6, legacy_8_4 or historica_por_ano. Sets the offset before secondary grade."),
"anio_corte": ("Primer año con base secundaria de seis años para historica_por_ano.", "First year with a six-year secondary offset for historica_por_ano."),
"summer_fix": ("Incluye la espera de inicio de clases codificada en junio–agosto.", "Includes coded waiting for classes in June–August."),
"nrezagos": ("Años de rezago sobre la edad esperada según escolaridad completada más seis.", "Years of delay beyond expected age based on completed schooling plus six."),
"limit": ("both, above o below: dependientes totales, mayores o menores.", "both, above or below: all, older or younger dependents."),
"breaks": ("Límites numéricos de intervalos o número de grupos. Use límites explícitos para comparar lenguajes.", "Numeric interval boundaries or number of groups. Use explicit boundaries for cross-language comparisons."),
"labels": ("Etiquetas para los intervalos. Use etiquetas explícitas para comparar lenguajes.", "Interval labels. Use explicit labels for cross-language comparisons."),
"deflactar": ("Aplica el deflactor del componente cuando es verdadero; conserva su salida nominal.", "Applies the component deflator when true; preserves its nominal output."),
"keep": ("Verdadero conserva componentes; una lista conserva los nombres indicados; falso retira los auxiliares calculados.", "True retains components; a list retains selected names; false removes calculated helper columns."),
"reuse": ("En auxiliares: reutiliza componentes disponibles o nombrados. En pobreza 2012/2022 se acepta y siempre recalcula.", "In helpers: reuses available or named components. Poverty 2012/2022 accept this option and always recompute."),
"return_households": ("Verdadero devuelve una fila por hogar; falso adjunta resultados a cada persona.", "True returns one row per household; false attaches results to each person."),
"include_details": ("Incluye componentes y diagnósticos del modelo. En ICV actualiza componentes existentes aun siendo falso.", "Includes model components and diagnostics. ICV refreshes existing components even when false."),
"method": ("Identificador histórico exacto: encftr0-0.0.2.9002.", "Exact historical identifier: encftr0-0.0.2.9002."),
"filter_valid_households": ("Conserva hogares con hconmissing igual a cero; en salida por persona mantiene filas y deja puntuaciones ausentes.", "Retains households with hconmissing zero; person output preserves rows and leaves filtered scores missing."),
"...": ("Opciones adicionales de labeler: metadatos de revisión o política de etiquetas según la función.", "Additional labeler options: revision metadata or labeling policy, depending on the function."),
"kwargs": ("Opciones adicionales de labelerpy: metadatos de revisión o política de etiquetas según la función.", "Additional labelerpy options: revision metadata or labeling policy, depending on the function.")
}

TITLES = {
"icv_siuben": "Historical ICV SIUBEN", "variables_icv_siuben": "ICV input and output columns",
"dict_icv_siuben": "ICV result dictionary", "set_labels_icv_siuben": "Label historical ICV results",
"use_labels_icv_siuben": "Convert ICV codes to labeled categories",
"ftc0_compute_icv_siuben": "Compatibility with encftr0",
"alfabetizacion": "Literacy", "anos_educacion": "Years of schooling", "asistencia_escolar": "School attendance",
"matriculacion_escolar": "School enrollment", "sobreedad_escolar": "School overage", "trabajo_infantil": "Child labour",
"tasa_alfabetizacion_hogar": "Household literacy rate", "tasa_dependencia": "Household dependency ratio",
"hacinamiento": "People per dwelling bedroom", "sexo_jefe": "Sex of the household head", "grupos_edad": "Age groups",
"iih": "Household income index (IIH)", "variables_iih": "IIH input and output columns",
"dict": "Select an ENCFT dictionary edition", "get_dict": "Select an ENCFT dictionary edition",
"dict_versions": "Available dictionary editions", "register_dict": "Register a dictionary edition",
"set_Dict": "Apply ENCFT dictionary metadata", "set_dict": "Apply ENCFT dictionary metadata",
"with_Dict": "Use ENCFT dictionary labels", "with_dict": "Use ENCFT dictionary labels",
"browse_dict": "Browse dictionary definitions", "db_connect": "Configured R database connection",
"factor_expansion_anual": "Annual expansion weights", "factor_expansion_semestre": "Semester expansion weights",
"factor_exp_anual": "Deprecated annual expansion weight aliases",
"regiones_desarrollo": "Development regions", "zona_desarrollo_fronterizo": "Border development zone",
"recode_material_pared_exterior": "Recode exterior wall material",
"fuerza_trabajo_potencial": "Potential labour force", "grupo_rama_pib": "Economic activity groups",
"horas_semana": "Weekly working hours", "ingreso_laboral_total": "Total labour income",
"perceptores_ingresos": "Income recipients", "prepare_poverty": "Prepare poverty questionnaire compatibility fields",
"select_variables_pobreza": "Select recognized poverty questionnaire inputs",
"pobreza_monetaria": "Deprecated 2012 monetary poverty entry point", "pobreza_monetaria_2012": "Monetary poverty: 2012 methodology",
"pobreza_monetaria_2022": "Monetary poverty: 2022 methodology", "ing_total_pobreza": "Legacy household income composition",
"ing_pc_pobreza_def": "Legacy deflated per-capita household income", "ing_remesas_ext": "Monthly foreign remittances",
"ing_alquiler_imputado": "Imputed dwelling rent", "ing_alquileres_renta": "Domestic rental income",
"ing_alquileres_renta_anual": "Annual domestic rental income, monthly equivalent", "ing_alquileres_renta_ext": "Foreign rental income",
"ing_autoconsumo_autosuministro": "Own consumption and self-supply income", "ing_beneficios_marginales": "Fringe benefits",
"ing_beneficios_marginales_anual": "Annual fringe benefits, monthly equivalent", "ing_bonificaciones": "Annual bonuses, monthly equivalent",
"ing_comisiones": "Commissions", "ing_dividendos": "Employment dividends", "ing_especie_alimentos": "In-kind food income",
"ing_especie_ayuda_ong": "In-kind domestic organization assistance", "ing_especie_ayuda_ong_anual": "Annual in-kind organization assistance, monthly equivalent",
"ing_especie_celular": "In-kind mobile phone income", "ing_especie_combustible": "In-kind fuel income",
"ing_especie_cuenta_propia": "In-kind self-employment income", "ing_especie_ocup_sec_asalarariado": "In-kind secondary salaried income",
"ing_especie_ocup_sec_cuenta_propia": "In-kind secondary self-employment income", "ing_especie_otros": "Other in-kind income",
"ing_especie_transporte": "In-kind transport income", "ing_especie_viviendas": "In-kind housing income", "ing_horas_extra": "Overtime income",
"ing_intereses_dividendos": "Domestic interest and dividends", "ing_intereses_dividendos_anual": "Annual domestic interest and dividends, monthly equivalent",
"ing_intereses_dividendos_ext": "Foreign interest and dividends", "ing_laboral_monetario": "Monetary labour income",
"ing_mensual_ocup_prin": "Monthly main occupation income", "ing_mensual_ocup_prin_asalariado": "Monthly main salaried occupation income",
"ing_mensual_ocup_prin_cuenta_propia": "Monthly main own-account occupation income", "ing_mensual_ocup_prin_independiente": "Monthly main independent occupation income",
"ing_mensual_ocup_sec_asalariado": "Monthly secondary salaried occupation income", "ing_mensual_ocup_sec_cuenta_propia": "Monthly secondary own-account occupation income",
"ing_mensual_ocup_sec_independiente": "Monthly secondary independent occupation income", "ing_monetario_ext": "Foreign monetary income",
"ing_monetario_no_laboral": "Domestic non-labour monetary income", "ing_no_monetario_laboral": "Non-monetary labour income",
"ing_no_monetario_no_laboral": "Domestic non-labour in-kind income", "ing_otros_ocup_sec_asalariado": "Other secondary salaried occupation income",
"ing_pension_ext": "Foreign pension income", "ing_pension_jubilacion": "Domestic pension income",
"ing_pension_jubilacion_anual": "Annual domestic pension income, monthly equivalent", "ing_propinas": "Tips",
"ing_regalia_pascual": "Christmas bonus, monthly equivalent", "ing_regalos_ext": "Foreign gifts",
"ing_remesas_nacionales": "Domestic remittances", "ing_remesas_nacionales_anual": "Annual domestic remittances, monthly equivalent",
"ing_transferencias_sociales": "Social cash transfers", "ing_utilidades_empresariales": "Business profit sharing, monthly equivalent",
"ing_vacaciones": "Vacation payments, monthly equivalent", "tiempo_total_empleo_anos": "Time in employment in years",
"tiempo_total_empleo_meses": "Time in employment in months", "tiempo_total_empleo_dias": "Time in employment in days",
"encft": "Aggregated 2016 survey example", "ipc_2010": "Consumer price index, 2010 base", "ipc_2020": "Consumer price index, 2020 base",
"lineas_pobreza": "Bundled poverty lines", "salario_minimo": "Minimum wage reference table", "tipo_cambio": "Exchange rate reference table",
"tipo_cambio_monedas": "Foreign currency exchange rates", "pipe": "Pipe operator"
}


def block(text, tag):
    pattern = re.compile(r"\\" + re.escape(tag) + r"\{")
    result = []
    for match in pattern.finditer(text):
        depth, pos = 1, match.end()
        while depth and pos < len(text):
            if text[pos] in "{}" and text[pos-1] != "\\": depth += 1 if text[pos] == "{" else -1
            pos += 1
        result.append(text[match.start():pos])
    return result


def parameter_description(key, language):
    keys = [name.strip() for name in key.split(",")]
    return " ".join(PARAMS[name if name == "..." else name.lstrip(".")][language] for name in keys)


def render(node):
    if not isinstance(node, dict): return "NULL"
    if "symbol" in node: return node["symbol"]
    if "value" in node:
        v = node["value"]
        return "NA" if v is None else "TRUE" if v is True else "FALSE" if v is False else json.dumps(v, ensure_ascii=False)
    name = node["call"].split("::")[-1]
    args = node.get("args", []); names = node.get("names", [""] * len(args))
    if name in ("+", "-", "*", "/", "^", "==", "!=", "<", "<=", ">", ">=", "&", "|", "%in%", "~", ":"):
        return "(" + (" " + name + " ").join(render(x) for x in args) + ")" if len(args) > 1 else name + render(args[0])
    return name + "(" + ", ".join((key + " = " if key else "") + render(value) for key, value in zip(names, args)) + ")"


def inputs(name, seen=None):
    seen = set() if seen is None else seen
    if name not in RULES or name in seen: return set()
    seen.add(name); result = set()
    def walk(node):
        if isinstance(node, dict):
            symbol = node.get("symbol", "")
            if symbol.isupper() and "_" in symbol and not symbol.startswith("NA_"): result.add(symbol)
            for val in node.values(): walk(val)
        elif isinstance(node, list):
            for val in node: walk(val)
    walk(RULES[name]["steps"])
    for dep in RULES[name]["dependencies"]: result.update(inputs(dep, seen))
    return result


def rule_text(name):
    lines = []
    def walk(steps):
        for step in steps:
            if step["op"] == "mutate":
                for key, value in zip(step["names"], step["args"]):
                    if key: lines.append(key + " = " + render(value))
            elif step["op"] == "deflate":
                lines.append("# deflactar = TRUE"); walk(step["steps"])
            elif step["op"] == "left_join_tipo_cambio": lines.append("# exchange rates for the preceding calendar month")
            elif step["op"] == "left_join": lines.append("# join " + render(step["args"][0]) + " by PERIODO")
    if name in RULES: walk(RULES[name]["steps"])
    return "\n".join(lines)


def guide(name):
    if "icv" in name or name.startswith("ftc0_"): return "icv-siuben"
    if "dict" in name.lower() or "labels" in name.lower(): return "diccionario"
    if "iih" in name: return "iih"
    if name.startswith("ing_") or "pobreza" in name or name == "prepare_poverty": return "pobreza-monetaria"
    if "factor_exp" in name: return "encftr"
    return "indicadores"


def describe(name, lang):
    eng = lang == "en"
    if "icv" in name or name.startswith("ftc0_"):
        descriptions = {
            "variables_icv_siuben": ("Lista las 32 entradas requeridas, opcionales y salidas del ICV histórico.", "Lists the 32 required inputs, optional inputs and historical ICV outputs."),
            "dict_icv_siuben": ("Diccionario de etiquetas del resultado ICV, separado de baseline-1.", "ICV result-label dictionary, separate from baseline-1."),
            "set_labels_icv_siuben": ("Aplica etiquetas a las columnas seleccionadas sin cambiar códigos.", "Applies labels to selected columns while preserving numeric codes."),
            "use_labels_icv_siuben": ("Convierte códigos del ICV a categorías etiquetadas en las columnas seleccionadas.", "Converts selected ICV codes to labeled categories."),
        }
        if name in descriptions: return descriptions[name][eng]
        return ("Reproduce el ICV de encftr0 0.0.2.9002 para hogares completos con una jefatura. Conserva filas y agrega clase, puntaje y método. No certifica una metodología vigente de SIUBEN. Consulte la guía para reglas de ausentes, claves, componentes y migración." if not eng else
            "Reproduces ICV from encftr0 0.0.2.9002 for complete households with one head. Preserves rows and adds category, score and method. Does not certify current SIUBEN methodology. See the guide for missing-value rules, keys, components and migration.")
    if name in RULES:
        result = (("Calculates " + TITLES[name].lower() + ". ") if eng else ("Calcula el indicador " + name + ". "))
        if name.startswith("ing_"):
            result += ("Monetary outputs are monthly Dominican pesos; annual receipts are converted to monthly equivalents by the rules below. Missing-value and eligibility conditions are explicit in each case_when expression. " if eng else "Las salidas monetarias son pesos dominicanos mensuales; las reglas convierten los cobros anuales a equivalentes mensuales. Cada case_when explicita el universo y el tratamiento de ausentes. ")
        result += ("Returns a copy with calculated columns and preserves input rows. " if eng else "Devuelve una copia con columnas calculadas y conserva las filas de entrada. ")
        return result
    descriptions = {
      "encft": ("Agregado de 2016: 256 celdas por trimestre, ano, sexo y provincia con la suma de factores de expansion.", "An existing 2016 aggregate: 256 cells by quarter, year, sex and province, containing summed expansion weights. These are aggregated survey values, not individual records or the new synthetic person example."),
      "iih": ("Estima ingresos y categoría IIH con coeficientes fijos, a nivel de hogar; no es pobreza monetaria observada.", "Estimates income and IIH category using fixed household models; this is distinct from observed monetary poverty."),
      "variables_iih": ("Lista columnas obligatorias, opcionales y de salida del IIH.", "Lists required, optional and output IIH columns."),
      "pobreza_monetaria_2012": ("Calcula ingresos nominales y deflactados, líneas urbanas/rurales y clasificación 2012 con denominador reportado del hogar.", "Calculates nominal and deflated income, urban/rural lines and 2012 classification using reported household size."),
      "pobreza_monetaria_2022": ("Calcula ingresos nominales y deflactados, líneas regionales y clasificación 2022 usando miembros observados.", "Calculates nominal and deflated income, regional lines and 2022 classification using observed household members."),
      "get_dict": ("Carga una edición completa e íntegra; baseline-1 no declara vigencia histórica.", "Loads a complete verified edition; baseline-1 asserts no historical applicability."),
      "dict": ("Carga una edición completa e íntegra; baseline-1 no declara vigencia histórica.", "Loads a complete verified edition; baseline-1 asserts no historical applicability."),
      "register_dict": ("Registra una edición inmutable y reutiliza las definiciones sin cambios.", "Registers an immutable edition and reuses unchanged definitions."),
      "dict_versions": ("Devuelve una tabla con metadatos, intervalos y hash de las ediciones disponibles.", "Returns a table of available edition metadata, intervals and hashes."),
      "ing_remesas_ext": ("Suma tres fuentes de remesas por seis meses, con su tasa mensual correspondiente, y divide entre seis. Componentes ausentes contribuyen cero.", "Sums three remittance streams over six months using their respective monthly rates, then divides by six. Missing components contribute zero."),
      "ing_total_pobreza": ("Compone los auxiliares históricos en ingresos nominales y deflactados del hogar. Para la metodología oficial use la función 2012 o 2022 explícita.", "Composes legacy helpers into nominal and deflated household income. Use the explicit 2012 or 2022 function for an official methodology workflow."),
      "db_connect": ("Abre la conexión encft configurada por Dmisc en el entorno del usuario.", "Opens the encft connection configured by Dmisc in the user's R environment."),
    }
    return descriptions.get(name, ("Calcula o consulta " + name + ". Consulte el contrato de la guía y los parámetros.", TITLES.get(name, name) + ". See the guide's calculation contract and parameters."))[eng]


manifest = []
exports = re.findall(r'^export\(([^)]+)\)', (R / "NAMESPACE").read_text(), re.M)
for name in exports:
    if name in ('"%>%"', 'ftc_db_connect', 'ftc_dbConnect'):
        target = "DataFrame.pipe" if name == '"%>%"' else "caller-owned DB-API connection"
        manifest.append({"r": name, "python": target, "contract": "native environment adapter"})
    else:
        if not callable(getattr(api, name, None)): raise RuntimeError("Missing Python R API alias: " + name)
        manifest.append({"r": name, "python": "endompy.encftr." + name, "contract": "callable"})
(P / "api-parity.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

public = sorted(name for name in api.__all__ if not name.startswith(("ftc_", "ftc0_", "compute_")) and name not in ("EncftDataFrame", "set_labels", "use_labels", "factor_exp_anual", "pobreza_monetaria"))
for lang in ("es", "en"):
    destination = P / "docs" / lang / "reference"; destination.mkdir(parents=True, exist_ok=True)
    links = []
    for name in public:
        obj = getattr(api, name)
        title = TITLES.get(name, name) if lang == "en" else name
        description = describe(name, lang)
        params = inspect.signature(obj).parameters
        rows = ["| " + key + " | " + ("—" if par.default is inspect.Parameter.empty else "`" + repr(par.default) + "`") + " | " + PARAMS[key.lstrip(".")][lang == "en"] + " |" for key, par in params.items()]
        required = sorted(inputs(name))
        text = f"# {title}\n\n```python\nencftr.{name}{inspect.signature(obj)}\n```\n\n{description}\n\n"
        text += f"[{'Contrato y ejemplo completo' if lang == 'es' else 'Contract and complete example'}](../{guide(name)}.md).\n\n"
        text += ("| Parámetro | Predeterminado | Contrato |\n" if lang == "es" else "| Parameter | Default | Contract |\n") + "|---|---|---|\n" + "\n".join(rows) + "\n"
        if required: text += "\n" + ("Columnas referidas por las reglas" if lang == "es" else "Columns referenced by calculation rules") + ": " + ", ".join("`" + c + "`" for c in required) + ".\n"
        if name in RULES:
            if RULES[name]["dependencies"]: text += "\n" + ("Componentes" if lang == "es" else "Components") + ": " + ", ".join(RULES[name]["dependencies"]) + ".\n"
            text += "\n" + ("Reglas de cálculo de la implementación R equivalente:" if lang == "es" else "Calculation rules from the equivalent R implementation:") + "\n\n```r\n" + rule_text(name) + "\n```\n"
        text += "\n" + ("Los nombres ftc_* equivalentes están incluidos en api-parity.json. Las funciones con entrada tbl también son métodos de EncftDataFrame." if lang == "es" else "Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.") + "\n"
        (destination / (name + ".md")).write_text(text, encoding="utf-8")
        links.append(f"- [{name}]({name}.md)")
    index = "# API\n\n" + "\n".join(links) + "\n\n## R / Python\n\n| R | Python | Contract |\n|---|---|---|\n" + "\n".join(f"| {item['r']} | {item['python']} | {item['contract']} |" for item in manifest)
    index += "\n\n`EncftDataFrame` extends `EndomDataFrame` and `pandas.DataFrame`. Construct it from a mapping or a DataFrame. Slicing, copying and calculations preserve its subclass; labeling uses `df.labeler` metadata. `EndomDataFrame.has_labelerpy()` reports the labeling dependency.\n"
    (destination / "index.md").write_text(index, encoding="utf-8")

for path in R.glob("man/*.Rd"):
    text = path.read_text(encoding="utf-8")
    name = path.stem.removeprefix("ftc_")
    if path.stem == "dict": name = "dict"
    title = TITLES.get(name)
    if title is None: raise RuntimeError("Missing English title: " + name)
    heading = "\n".join(block(text, tag)[0] for tag in ("name",) if block(text, tag))
    heading += "\n" + "\n".join(block(text, "alias"))
    heading += "\n\\title{" + title + "}\n" + "\n".join(block(text, "usage"))
    item_names = [x[len("\\item{"):].split("}")[0] for x in block(text, "item")]
    # Only function argument items are selected; data-format items are described below.
    arguments = block(text, "arguments")
    if arguments:
        item_names = [x[len("\\item{"):].split("}")[0] for x in block(arguments[0], "item")]
        heading += "\n\\arguments{\n" + "\n".join("\\item{" + key + "}{" + parameter_description(key, 1) + "}" for key in item_names) + "\n}"
    heading += "\n\\description{" + describe(name, "en") + "}\n"
    if "\\docType{data}" in text:
        heading += "\\docType{data}\n\\format{A bundled reference object; inspect its columns and period coverage before use.}\n\\keyword{datasets}\n"
    else:
        result = "A table with calculated columns, preserving input rows unless household output is requested."
        if name in ("dict", "register_dict"): result = "A complete Dict with verified revision metadata and content integrity."
        if name == "dict_versions": result = "A data frame of edition identifiers, applicability intervals and content hashes."
        if name == "pipe": result = "The result of evaluating the right-hand expression with the left-hand value."
        if name in ("variables_iih", "variables_icv_siuben"): result = "A list containing required, optional and output column names."
        if name == "dict_icv_siuben": result = "A labeler Dict with ICV result labels and historical method metadata."
        if name == "db_connect": result = "The database connection configured by Dmisc."
        if name == "browse_dict": result = "An interactive HTML dictionary viewer."
        heading += "\\value{" + result + "}\n"
    heading += "\\details{See \\code{vignette(\"" + guide(name) + "\", package = \"encftr\")} for populations, units, missing values and executable workflows. Dictionary edition and poverty methodology are independent choices.}\n"
    heading += "\n".join(block(text, "examples")) + "\n"
    (EN / path.name).write_text(heading, encoding="utf-8")

pairs = {}
for source in sorted(list(R.glob("man/*.Rd")) + list(R.glob("vignettes/*.Rmd")) + [R / name for name in ("README.md", "_pkgdown.yml", "NEWS.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "DEPLOYMENT.md", "LICENSE.md")]):
    if source.name.startswith("_"): continue
    relative = source.relative_to(R)
    translated = R / "pkgdown/i18n/en" / relative
    if not translated.exists(): raise RuntimeError("Missing translation: " + str(relative))
    pairs[str(relative).replace("\\", "/")] = {"source": hashlib.sha256(source.read_bytes()).hexdigest(), "translation": hashlib.sha256(translated.read_bytes()).hexdigest()}
(R / "pkgdown/i18n/manifest.json").write_text(json.dumps(pairs, indent=2), encoding="utf-8")
print(f"Documented {len(public)} Python entry points, {len(manifest)} R exports and {len(pairs)} translated R sources.")
