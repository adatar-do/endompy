# Installation, migration and deployment

## Install local artifacts

Install `labeler >= 0.11.0` and declared dependencies first. Then install source `enhogar_0.5.0.tar.gz` or Windows binary `enhogar_0.5.0.zip` with a compatible R version. Python requires `labelerpy >= 0.2.2`, pandas >= 1.5, NumPy and Python >= 3.9; install `endompy-0.8.0-py3-none-any.whl`.

## Changes from enhogar 0.2.0

- set_labels retains codes and attaches metadata; use_labels converts for presentation.
- inactivo uses PEA and no longer fails on the nonexistent pea_abierta column.
- In 2018, age 99 and response 9 no longer become known active or inactive population.
- 2018 and 2022 are supported; mixed editions, unsupported codes and invalid schemas are rejected.
- Dictionary names are unique, with verified revisions and shared partial changes.
- The repeated job-search warning is removed: proxy scope is documented in the API and guides.

## Build and publish

From the ENDOM root run `Rscript enhogar/scripts/check-release.R`, `Rscript enhogar/scripts/build-docs.R` and `python enhogar/scripts/check-sites.py artifacts/enhogar-2022-release/sites/r --kind r`. Spanish is built at root and English at `en/`. The audit checks language pairs, links, assets, anchors and search indexes. For Python run `python endompy/scripts/build-docs.py artifacts/enhogar-2022-release/sites/python` and the same audit with `--kind python`.

Scripts build locally. The pkgdown workflow supports manual builds; publishing requires its publish input. Publish minimum dependency versions first. Included static sites and artifacts can be deployed, but this delivery does not publish or run remote CI. The Windows binary is verified on R 4.5.1; other platforms require their own checks.

Do not execute data-raw to prepare an installation: it retains historical development paths. Deliveries are built from versioned resources and invented examples.
