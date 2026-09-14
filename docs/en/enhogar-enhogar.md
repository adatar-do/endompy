# Getting started with ENHOGAR

`enhogar 0.5.0` and `endompy.enhogar` in `endompy 0.8.0` support **2018 and 2022**. All 20 functions have equivalents in both languages. They process local tables of numeric codes: materialize database queries before calculation.

## Edition selection

Use `edition=2022` to declare the questionnaire. Column evidence also identifies it: H203/H501:H507 indicate 2018, while P203/P501:P508 indicate 2022. Mixed groups and incompatible requested editions raise errors. An empty table with these columns retains its edition.

`HANO` is the interview year. The 2022 questionnaire allows 2021 and 2022, including both together. Without questionnaire columns, HANO containing only 2021 is ambiguous and requires an explicit edition. Missing or incompatible years raise errors when HANO exists and there are rows.

Explicit selection takes precedence over the configured option; both are checked against the data. Without configuration or evidence, 2018 remains the compatibility default. Declare the edition when labeling a table containing only shared identifiers. `guess_enhogar_edition()` requires sufficient evidence and never modifies options. `get_enhogar_edition()` reads selection without modifying it. Reset with `enhogar_edition(NULL)` in R or `enhogar_edition(None)` in Python, whose option is context-local.

## Data and results

Original data, rows and order are retained; Python also preserves duplicate indexes. Results are recomputed. Missing columns, text, factors and unsupported codes raise errors. Necessary unknown values remain unknown.

`enhogar_example()` retains the twelve invented 2018 cases. `enhogar_example(2022)` provides twelve cases adapted to the 2022 questionnaire. They are not respondents and cannot estimate national statistics.

[2022 edition guide](enhogar-edicion-2022.md).

```python
from endompy import enhogar as e
x = e.enhogar_example()
print(e.ocupado(x)[["case_id", "pet", "ocupado"]])
```
