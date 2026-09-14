"""Execute Python fences in paired narrative guides; code must be identical."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
fence = re.compile(r"```python\n(.*?)\n```", re.S)
count = 0
for spanish in sorted((root / "docs/es").glob("*.md")):
    if spanish.name in {"enft-reference.md", "enhogar-reference.md"}: continue  # API signatures, not runnable narrative examples.
    english = root / "docs/en" / spanish.name
    left = fence.findall(spanish.read_text(encoding="utf-8"))
    right = fence.findall(english.read_text(encoding="utf-8"))
    if left != right: raise SystemExit("Examples differ: " + spanish.name)
    for example in left:
        exec(compile(example, str(spanish), "exec"), {"__name__": "__main__"})
        count += 1
print("Executed", count, "paired Python guide examples.")
