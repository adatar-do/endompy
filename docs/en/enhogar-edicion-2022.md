# ENHOGAR 2022: questionnaire and dictionary

## Questionnaire changes

2022 support covers the six existing indicators, edition selection, labels and dictionary revisions. Each questionnaire has its own field mapping.

| Concept | 2018 | 2022 |
|---|---|---|
| Age | H203; 99 unknown | P203; 99 is a valid age |
| Employment | H501:H506 | P501:P506 |
| Search | Historical H507 proxy | P508: job search in the past four weeks |
| Availability | H509 or H510 | P510 or P511 |
| Binary responses | 1 yes, 2 no, 9 unknown | 1 yes, 2 no; 9 is rejected |
| Interview year HANO | 2018 | 2021 or 2022 |

**P507 is not job search in 2022**: it records the reason for not working. P509 records the reason for not searching. The implementation does not mechanically rename 2018 fields.

## Calculation and skips

Any affirmative P501:P506 establishes employment. Six negative answers are required to establish nonemployment; other cases remain unknown. Unemployment requires known nonemployment and P508=1. A yes in P508 skips to P513 in the questionnaire; unemployment calculation therefore does not require P510/P511.

PEA is the union of employment and unemployment; inactivity is its known complement within working-age population. Potential labour force retains the availability proxy outside PEA using P510 or P511. It does not fully reproduce the ILO concept or use every economic-module question.

The ONE report uses the population **aged 10 and over** for the economic module. The package retains the analytical default of 15 for compatibility; pass `min_edad=10` when appropriate for your analysis population. It does not calculate weighted rates or sampling errors, or certify official aggregates.

## Complete dictionaries and versions

R `ehg_dict(2022)` and Python `get_dict(2022)` select `coverage-2`, a combined dictionary of **603 definitions**. Its parent `baseline-1` remains selectable through `version="baseline-1"`, with **all 30 original definitions and references unchanged**. The extension incorporates the complete ONE REDATAM ENH2022 public inventory and retains prior SPSS codebook variables and the six derived indicators.

| Module | ONE inventory fields | Revision |
|---|---:|---|
| viviendas | 10 | redatam-1 |
| hogares | 39 | redatam-1 |
| personas | 43 | redatam-1 |
| elegidos | 491 | redatam-1 |
| geografia | 9 | redatam-1 |

These modules contain **592 field occurrences** and 2,888 category rows. The combined count is not the sum of rows: identical shared definitions are reused, while prior variables absent from REDATAM are retained.

Use `ehg_dict_modules(2022)` / `dict_modules(2022)` to choose a module and `ehg_dictionary_coverage()` / `dictionary_coverage()` for coverage. R `provenance=TRUE` or Python `provenance=True` exposes each field's source. Select dictionaries using `module="personas"`, `module="hogares"`, and the other exact identifiers.

`FEXP_VIV`, `FPON_VIV` and `GRUP_SEC` have different meanings in dwelling and household modules. The `all` dictionary qualifies them by entity; labeling unqualified columns requires the correct explicit module. Weights are not combined, and SPSS `F_expansión`/`F_ponderación` fields are not automatically renamed to REDATAM names. Code 99 is not assumed to mean missing in every question.

The 2018 revision retains all 447 definitions and its fingerprint. Survey edition, module, dictionary revision and package version are separate selections. No applicability intervals are inferred. A SQLite registry requires an exact revision or a date with documented applicability; it does not automatically select the latest revision.

Coverage source: [ONE REDATAM ENH2022](https://redatam.one.gob.do/bindom/RpWebEngine.exe/Portal?BASE=ENH2022&lang=ESP). The delivery contains metadata and provenance, without household microdata.

Sources: [ONE, ENHOGAR 2022 codebook](https://www.one.gob.do/catalogo-datos/ENHOGAR/ENHOGAR_2022_BD_SPSS/Libro%20de%20c%C3%B3digos_ENHOGAR2022_Personas.htm) · [ONE, ENHOGAR 2022 report](https://www.one.gob.do/media/sfahteva/informe-general-enhogar-2022-dic.pdf).

```python
from endompy import enhogar as e
x = e.enhogar_example(2022)
result = e.inactivo(x, min_edad=10, edition=2022)
print(result[['case_id', 'pet', 'ocupado', 'desocupado', 'pea', 'inactivo']])
print(e.get_dict(2022).revision()['dictionary_id'])
```
