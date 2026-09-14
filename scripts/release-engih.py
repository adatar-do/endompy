"""Build and verify locally in an explicit output directory.

Needs build, twine and docs dependencies in the tooling environment. Optional
--wheelhouse supplies offline dependencies; --labeler-wheel supplies a compatible
unpublished wheel. The test environment stays inside the output directory.
"""
import argparse
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("output")
parser.add_argument("--wheelhouse")
parser.add_argument("--labeler-wheel")
args = parser.parse_args()
output = Path(args.output).resolve()
if output == root or output in root.parents or (output.exists() and any(output.iterdir())):
    raise SystemExit("Choose a new output directory outside the source root")
output.mkdir(parents=True)


def run(arguments, cwd=root):
    subprocess.run([str(a) for a in arguments], cwd=cwd, check=True)


run([sys.executable, "-m", "build", "--outdir", output / "dist"])
run([sys.executable, "-m", "twine", "check", *sorted((output / "dist").iterdir())])
environment = output / "environment"
run([sys.executable, "-m", "venv", environment])
python = environment / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
options = ["--no-index", "--find-links", Path(args.wheelhouse).resolve()] if args.wheelhouse else []
packages = [Path(args.labeler_wheel).resolve()] if args.labeler_wheel else []
run([python, "-m", "pip", "install", *options, *packages, *sorted((output / "dist").glob("*.whl")), "pytest"])
run([python, "-m", "pip", "check"])
run([python, "-I", "-m", "pytest", root / "tests", "--import-mode=importlib", "--junitxml=" + str(output / "tests.xml")], cwd=output)
run([python, "-I", root / "scripts/check-examples.py"], cwd=output)
run([sys.executable, root / "scripts/build-docs.py", output / "site"])
run([sys.executable, root / "scripts/check-sites.py", output / "site", "--kind", "python"])
print("Built source/wheel, checked installed tests/examples and bilingual site:", output)
