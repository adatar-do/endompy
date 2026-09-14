# Build and deploy endompy

Builds and checks are local. Uploading distributions or enabling Pages is a
separate publication action.

1. Use Python >= 3.9. Install the supplied labelerpy >= 0.2.2 wheel before endompy
   if that version is not available in a package index. Install `.[dev,docs]`
   and build tooling (`build`, `twine`).
2. Run `python -m pytest tests` and `python -m build`. Run
   `python -m twine check dist/*`. Inspect both the wheel and sdist for all bundled
   JSON resources, license and absence of microdata.
3. Install the wheel in a fresh environment using
   `python -m pip install labelerpy-0.2.2-py3-none-any.whl endompy-0.8.0-py3-none-any.whl`.
   Run the synthetic examples and parity tests against that installed package.
4. From ENDOM, regenerate rules with `Rscript encftr/scripts/export-rules.R`,
   `python endompy/scripts/compile-survey-rules.py` and
   `python endompy/scripts/compile-iih.py`. These are development steps; users do
   not need R. Regenerate documentation with `python encftr/scripts/author-docs.py`
   and `python endompy/scripts/build-reference.py` after reviewing API changes.
5. Run `python scripts/build-docs.py` and
   `python scripts/check-sites.py ../artifacts/endompy-engih-release/sites/python --kind python`.
   Spanish is at the root, English at `en/`; each edition has independent search
   and links to its counterpart. The configured canonical URL is
   https://adatar-do.github.io/endompy/.

Archive only the static site directory for Pages. Preserve build-info.json,
site-check.json and artifact SHA256 hashes. Keep raw surveys, intermediate
person/household comparison files, virtual environments and credentials out of
the public delivery. Aggregate validation summaries and synthetic examples may
be included. Dictionary versions, economic tables and model versions are
independent reproducibility inputs.

The parity manifest covers all exported R API entries. Native R database
configuration and the pipe operator use caller-owned Python DB-API connections
and DataFrame.pipe. Advanced Dmisc-specific cut functions require explicit
pandas boundaries; there is no general automatic translation of arbitrary R
functions. Use explicit labels when comparing categorical results.

## ICV SIUBEN / encftr0

Run `Rscript encftr/scripts/export-icv-rules.R` before building the Python wheel. This exports the closed historical ICV pipelines and shared synthetic example. Install encftr 0.10.0 before the optional encftr0 0.1.0 compatibility package. See the ICV migration guide. Set `ENCFT_RELEASE_DIR` to a separate artifact directory to preserve an earlier release.


## ENGIH 2018

See [ENGIH installation and verification](engih-deployment.md) and [sources and coverage](engih-fuentes.md).
