"""Build two strict MkDocs editions locally. No publication or network writes."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import yaml

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("output", nargs="?", default=str(ROOT.parent / "artifacts/endompy-engih-release/sites/python"))
args = parser.parse_args()
output = Path(args.output).resolve()
if output == ROOT or output in ROOT.parents: raise SystemExit("Unsafe output directory")
marker = output / ".endompy-docs-output"
if output.exists() and any(output.iterdir()) and not marker.exists(): raise SystemExit("Choose an empty output directory")
output.mkdir(parents=True, exist_ok=True); marker.write_text("endompy docs output")
for lang in ("es", "en"):
    config = {"site_name": "endompy 0.8.0", "site_url": "https://adatar-do.github.io/endompy/" + ("en/" if lang == "en" else ""),
        "docs_dir": str(ROOT / "docs" / lang), "site_dir": str(output / "en" if lang == "en" else output),
        "theme": {"name": "material", "language": lang, "palette": {"primary": "teal", "accent": "teal"},
                  "features": ["navigation.top", "content.code.copy"]},
        "plugins": [{"search": {"lang": lang}}],
        "use_directory_urls": False,
        "markdown_extensions": ["tables", "fenced_code", "admonition", "pymdownx.superfences", {"toc": {"permalink": True}}],
        "nav": [{"Inicio" if lang == "es" else "Home": "index.md"}, {"ENCFT": "encftr.md"},
                {"ENFT": [{"Inicio" if lang == "es" else "Start": "enft-enftr.md"},
                          {"Diccionario" if lang == "es" else "Dictionary": "enft-diccionario.md"},
                          {"Pobreza" if lang == "es" else "Poverty": "enft-pobreza-monetaria.md"},
                          {"Indicadores" if lang == "es" else "Indicators": "enft-indicadores.md"},
                          {"API ENFT": "enft-reference.md"}]},
                {"ENHOGAR": [{"Inicio" if lang == "es" else "Start": "enhogar-enhogar.md"},
                             {"Edición 2022" if lang == "es" else "2022 edition": "enhogar-edicion-2022.md"},
                             {"Indicadores" if lang == "es" else "Indicators": "enhogar-indicadores.md"},
                             {"Diccionario" if lang == "es" else "Dictionary": "enhogar-diccionario.md"},
                             {"Despliegue" if lang == "es" else "Deployment": "enhogar-deployment.md"},
                             {"API ENHOGAR": "enhogar-reference.md"}]},
                {"ENGIH": [{"Inicio" if lang == "es" else "Start": "engih-engihr.md"},
                           {"Etiquetas" if lang == "es" else "Labels": "engih-etiquetas.md"},
                           {"Versionado" if lang == "es" else "Versioning": "engih-versionado.md"},
                           {"Fuentes" if lang == "es" else "Sources": "engih-fuentes.md"},
                           {"Integración" if lang == "es" else "Integration": "engih-integracion.md"},
                           {"Despliegue" if lang == "es" else "Deployment": "engih-deployment.md"},
                           {"API ENGIH": "engih-reference.md"}]},
                {"Diccionarios" if lang == "es" else "Dictionaries": "diccionario.md"},
                {"Pobreza" if lang == "es" else "Poverty": "pobreza-monetaria.md"},
                {"Indicadores" if lang == "es" else "Indicators": "indicadores.md"}, {"IIH": "iih.md"},
                {"ICV SIUBEN": "icv-siuben.md"}, {"API": "reference/index.md"}, {"Despliegue" if lang == "es" else "Deployment": "deployment.md"}]}
    with tempfile.TemporaryDirectory(prefix="endompy-docs-") as temporary:
        path = Path(temporary) / "mkdocs.yml"
        path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False), encoding="utf-8")
        subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", str(path)], check=True)
marker.write_text("endompy docs output")
(output / "build-info.json").write_text(json.dumps({"package": "endompy", "version": "0.8.0", "languages": ["es", "en"]}, indent=2))
print("Built bilingual MkDocs:", output)
