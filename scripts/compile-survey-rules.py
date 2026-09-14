"""Compile reviewed R income/indicator expressions into a restricted rule file.

Development tool only: no R installation or expression evaluation is needed by users.
Run the sibling encftr AST exporter first. Unsupported statements fail compilation.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = json.loads((ROOT / "endompy/scripts/generated/r-functions.json").read_text())
TARGET = ROOT / "endompy/endompy/encftr/resources"
TARGET.mkdir(parents=True, exist_ok=True)


def call(node):
    return node.get("call", "").split("::")[-1] if isinstance(node, dict) else ""


def sym(node):
    return node.get("symbol") if isinstance(node, dict) else None


def compile_pipe(node):
    op = call(node)
    if sym(node) == "tbl":
        return []
    args = node.get("args", [])
    if op == "%>%":
        return compile_pipe(args[0]) + compile_step(args[1])
    raise ValueError("Unsupported pipeline: " + str(node)[:180])


def compile_step(node):
    op = call(node)
    if op in ("mutate", "select", "left_join", "group_by", "ungroup") or op.startswith("ftc_") or op == "left_join_tipo_cambio":
        return [{"op": op, "args": node.get("args", []), "names": node.get("names", [])}]
    raise ValueError("Unsupported pipeline step: " + op)


def compile_function(name):
    source = SOURCE[name]
    steps = []
    dependencies = []
    for node in source["body"]["args"]:
        op = call(node)
        args = node.get("args", []) if isinstance(node, dict) else []
        if op == "<-":
            target, value = args
            if value == []:
                continue
            if sym(target) == "ingresos":
                dependencies = [x["value"] for x in value["args"]]
            elif sym(target) == "tbl":
                steps.extend(compile_pipe(value))
            else:
                raise ValueError("Unsupported assignment: " + str(target))
        elif op == "%>%":
            steps.extend(compile_pipe(node))
        elif op == "if":
            if sym(args[0]) == "deflactar":
                body = args[1]["args"]
                compiled = []
                for item in body:
                    if call(item) != "<-" or sym(item["args"][0]) != "tbl":
                        raise ValueError("Unsupported conditional")
                    compiled.extend(compile_pipe(item["args"][1]))
                steps.append({"op": "deflate", "steps": compiled})
            elif dependencies:
                # Component reuse and retained columns are handled centrally.
                continue
            else:
                raise ValueError("Unsupported conditional in " + name)
        elif op == "for" and dependencies:
            continue
        elif op.startswith("cli_progress_") or sym(node) == "tbl":
            continue
        else:
            raise ValueError("Unsupported statement " + op)
    return {"source": source["file"], "parameters": source["formals"],
            "dependencies": dependencies, "steps": steps}


names = [name for name, fn in SOURCE.items() if name.startswith("ftc_ing_")
         and name not in ("ftc_ing_remesas_ext", "ftc_ing_total_pobreza", "ftc_ing_pc_pobreza_def")]
names += ["ftc_perceptores_ingresos", "ftc_ingreso_laboral_total", "ftc_horas_semana",
          "ftc_fuerza_trabajo_potencial", "ftc_tiempo_total_empleo_dias",
          "ftc_tiempo_total_empleo_meses", "ftc_tiempo_total_empleo_anos",
          "ftc_grupo_rama_pib", "ftc_regiones_desarrollo", "ftc_zona_desarrollo_fronterizo",
          "ftc_recode_material_pared_exterior"]
rules = {}
for name in names:
    try:
        rules[name.removeprefix("ftc_")] = compile_function(name)
    except ValueError as error:
        raise ValueError(name + ": " + str(error)) from error
(TARGET / "survey-rules.json").write_text(json.dumps(rules, ensure_ascii=False, indent=2), encoding="utf-8")
lines = ['"""ENCFT income and labour indicators. Generated from reviewed survey rules."""',
         'from .rules import run_rule', '']
for name, spec in rules.items():
    params = []
    for parameter, default in spec["parameters"].items():
        parameter = parameter.lstrip(".")
        params.append(parameter if "missing" in default else parameter + "=" + repr(default.get("value")))
    kwargs = ", ".join(f"{p.split('=')[0]}={p.split('=')[0]}" for p in params[1:])
    lines += [f'def {name}({", ".join(params)}):',
              f'    """Compute {name}; see the bilingual reference for inputs, units and missing-value rules.',
              '', '    Returns a copy of tbl with the indicator columns. Input rows are preserved.',
              f'    Corresponding R function: encftr::ftc_{name}.', '    """',
              f'    return run_rule(tbl, "{name}"' + (", " + kwargs if kwargs else "") + ')', '']
(TARGET.parent / "indicators.py").write_text("\n".join(lines), encoding="utf-8")
print(f"Compiled {len(rules)} survey functions.")

# The 2022 methodology keeps its published component expressions and their order.
pm22 = SOURCE["ftc_pobreza_monetaria_2022_impl"]["body"]["args"]
stages = {"base": [], "totals": [], "deflated": []}
stage = None
for node in pm22:
    if call(node) != "<-":
        continue
    target, value = node["args"]
    if call(target) == "$" and sym(target["args"][0]) == "encft":
        name = target["args"][1]["symbol"]
        if name == "p_s4b42": stage = "base"
        if name == "p06_rem1": stage = "totals"
        if name == "macro_region": stage = None
        if name == "ID_lab_mon_op": stage = "deflated"
        if stage is not None:
            stages[stage].append([name, value])
    elif sym(target) in ("region_vars", "moving_vars", "no_deflate_vars"):
        stages[sym(target)] = value
ensure = SOURCE["ftc_pm22_ensure_columns"]["body"]["args"]
for node in ensure:
    if call(node) == "<-" and sym(node["args"][0]) in ("numeric_zero", "numeric_na", "alias_map"):
        name = sym(node["args"][0]); value = node["args"][1]
        stages[name] = dict(zip(value["names"], [x["value"] for x in value["args"]])) if name == "alias_map" else [x["value"] for x in value["args"]]
(TARGET / "poverty-2022-rules.json").write_text(json.dumps(stages, ensure_ascii=False, indent=2), encoding="utf-8")
