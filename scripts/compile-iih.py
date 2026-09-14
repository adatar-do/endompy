"""Extract reviewed IIH expressions from the R development export (never at runtime)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = json.loads((ROOT / "scripts/generated/r-functions.json").read_text())


def op(node):
    return node.get("call", "").split("::")[-1] if isinstance(node, dict) else ""


def find(node, name):
    if not isinstance(node, dict):
        return []
    result = [node] if op(node) == name else []
    for arg in node.get("args", []):
        result.extend(find(arg, name))
    return result


result = {}
for stage, fn in [("persons", "prepare_persons"), ("classify", "classify_households"), ("models", "apply_models")]:
    result[stage] = [[name, value] for mutate in find(source["encft_iih_" + fn]["body"], "mutate")
                     for name, value in zip(mutate["names"], mutate["args"])
                     if name and name not in ("calc_id", "anio")]
node = find(source["encft_iih_aggregate_households"]["body"], "summarise")[0]
result["aggregate"] = [[name, value] for name, value in zip(node["names"], node["args"]) if name != ".groups"]
body = source["encft_iih_apply_models"]["body"]
for node in find(body, "<-"):
    if node["args"][0] == {"symbol": "model_columns"}:
        result["model_columns"] = [x["value"] for x in node["args"][1]["args"]]
(ROOT / "endompy/encftr/resources/iih-rules.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
calls = set()
def inventory(node):
    if isinstance(node, dict):
        if op(node): calls.add(op(node))
        for value in node.values(): inventory(value)
    elif isinstance(node, list):
        for value in node: inventory(value)
inventory(result)
print("IIH rules", {key: len(value) for key, value in result.items()}, sorted(calls))
