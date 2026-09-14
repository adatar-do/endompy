# Getting started with the ENFT

`enftr 0.9.0` and `endompy.enftr 0.4.0` process the traditional semiannual survey. The continuous ENCFT has its own module and contracts.

The example contains 72 entirely invented people in 24 household-periods from 2000 to 2016. It cannot estimate national statistics. Generation uses constants and variable names, without respondent values.

## Structure and periods

`EFT_PERIODO` accepts `1/2005`, `2005/1` and `20051`, including mixed row formats. `PERIALFA` identifies the older structure. Only period extraction and zone conversion support both structures; other calculations require the `EFT_` columns listed in the reference. No questionnaire crosswalk is inferred.

Column structure version, dictionary revision and poverty method identifier are independent. The version function identifies columns; it does not date the questionnaire.

Use local tables and retain required columns. Materialize database queries before calculating. Functions preserve rows and order; Python also preserves duplicate indexes.

## Runnable example
```python
import json
from importlib.resources import files
import pandas as pd
from endompy import enftr as ft
x = pd.DataFrame(json.loads(files("endompy.enftr").joinpath("resources/synthetic-members.json").read_text()))
result = ft.peri_vars(x)
result = ft.ocupado(result)
print(result[["EFT_PERIODO", "ano", "semestre", "ocupado"]].head())
```
