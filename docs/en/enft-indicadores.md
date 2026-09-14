# Indicators and compatibility

Indicators retain the traditional questionnaire codes. `min_edad` defaults to 15 and must be a nonnegative integer; change it only when the analytical definition requires it. Employed status takes precedence over questions about searching for another job when classifying unemployment.

Years of education retain the historical structure: level 2 uses approved grade; levels 3 and 4 add 8; level 5 adds 12; level 6 adds 16. Children younger than four and unrecognized levels produce missing values. The ENCFT structure is not substituted.

Occupational categories change in 2005. Combined inference domains use 2000/1–2003/1, 2003/2–2007/2 and 2008/1–2016/2. The combined function derives the period before selecting a segment. Decree-specific regional functions transform historical geographic codes.

## R and Python

Python provides unprefixed functions, R-style `ft_` aliases and `EnftDataFrame`. Older period, zone and labeling aliases remain available. `ft_db_connect` and `ft_dbConnect` belong to R's Dmisc configuration; Python receives user-loaded pandas tables. `%>%` is an R operator. Private algorithms are not promoted to public API.

Parity uses 144 invented branch cases and 72 grouped synthetic people for income and poverty. This establishes software consistency, not validation of national estimates.

## Runnable example
```python
import json
from importlib.resources import files
import pandas as pd
from endompy import enftr as ft
x = pd.DataFrame(json.loads(files("endompy.enftr").joinpath("resources/synthetic-members.json").read_text()))
result = ft.anos_educacion(x)
result = ft.alfabeta(result, min_edad=15)
result = ft.pea_ampliada(result, min_edad=15)
result = ft.dominios_inferencia(result)
print(result[["anos_educacion", "alfabeta", "pea_ampliada", "dominios_inferencia"]].head())
```
