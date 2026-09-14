# Installation, verification and deployment

Install Python >= 3.9, pandas >= 1.5 and numpy >= 1.21. The delivery includes `labelerpy 0.2.2` and the `endompy 0.8.0` wheel/sdist. Run `python -m pip install labelerpy-0.2.2-py3-none-any.whl endompy-0.8.0-py3-none-any.whl` inside a virtual environment; dependencies must be available or reachable through the configured index.

To rebuild: `python -m build`; `python -m twine check dist/*`; install the wheel and run `python -I -m pytest tests --import-mode=importlib` and `python -I scripts/check-examples.py`. `scripts/release-engih.py` combines building, tests and site generation in an explicit output. The local delivery verifies fresh Python 3.9/pandas 1.5 and Python 3.13/pandas 3 environments, including existing-module regressions.

`scripts/build-docs.py OUTPUT` builds both editions; `scripts/check-sites.py OUTPUT --kind python` checks links, resources, search and equivalent pages. Serve the static folder over HTTP and retain `en/`. Workflows are prepared; publishing and remote CI need separate runs and labelerpy availability in the index.

To refresh ENGIH references, run `Rscript endompy/scripts/export-engih-reference.R` from ENDOM with `engihr 0.3.0` installed, then `python endompy/scripts/sync-engih-resources.py engihr --check`. Synthetic references include every categorical code, an unknown value and NA. Installing the package does not change registered revisions. Original Excel files and questionnaires are not bundled.

```python
from endompy import __version__, engihr as e
assert __version__ == "0.8.0"
assert e.get_dict("b1").revision()["dictionary_id"] == "engih-2018-b1"
assert e.get_dict("b1").revision()["version"] == "coverage-2"
```
