"""Copy verified engihr 0.3.0 metadata unchanged; --check only compares bytes."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("source", nargs="?", default=str(root.parent / "engihr"))
parser.add_argument("--check", action="store_true")
args = parser.parse_args()
source = Path(args.source).resolve()
assert "Version: 0.3.0" in (source / "DESCRIPTION").read_text(encoding="utf-8")
destination = root / "endompy/engihr/resources"
files = [p for folder in ("dictionaries", "reference") for p in (source / "inst" / folder).rglob("*") if p.is_file()]
assert len(files) == 58 and len(list((source / "inst/dictionaries").glob("*.json"))) == 50
report = {}
for file in files:
    rel = file.relative_to(source / "inst")
    target = destination / rel
    if not args.check:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(file, target)
    assert file.read_bytes() == target.read_bytes(), rel
    report[rel.as_posix()] = hashlib.sha256(file.read_bytes()).hexdigest()
print(json.dumps({"r_package": "engihr 0.3.0", "files_verified": len(report), "sha256": report}, indent=2))
