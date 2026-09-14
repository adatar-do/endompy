# Getting started with ENCFT

encftr 0.10.0 and endompy 0.3.0 prepare and analyze person responses from the Dominican Republic Continuous National Labour Force Survey. They include labeling, education, labour, income, household indicators, monetary poverty 2012/2022 and the household income index (IIH).

Install labeler >= 0.11.0 for R or labelerpy >= 0.2.2 for Python first. The delivery includes local packages so installation does not depend on these versions being published. R requires R >= 4.1; Python supports Python >= 3.9 with pandas >= 1.5. See the deployment guide for building and installing delivery files.

The bundled example is entirely synthetic: 12 people, four households across periods and fictitious identifiers. It contains no survey microdata. Functions return a table with results and preserve original rows, except when household output is explicitly requested for IIH.

Calculate weights before filtering people. The annual divisor is the number of distinct observed quarters within each year; the semester divisor is calculated within each year and semester. A two-quarter extract does not provide full-year coverage. If an extract has no period fields and its coverage is known, declare `periods = 4` for annual weights or `periods = 2` for semester weights. Otherwise the calculation fails.

`TRIMESTRE` accepts YYYYQ (for example 20191), or 1–4 with `ANO`. Identifiers and periods cannot be missing. Missing weights are preserved; negative, infinite or boolean weights are rejected.

R uses `ftc_*` names; Python provides the same names without the prefix and `ftc_*` aliases for script migration. Calculations are also chainable methods of `EncftDataFrame`. Types follow each language: R factors and NA values, and pandas categories and nullable dtypes.

```python
import json
from importlib.resources import files
from endompy import EncftDataFrame
from endompy import encftr as encft
x = EncftDataFrame(json.loads(files("endompy.encftr").joinpath("resources/synthetic-members.json").read_text()))
y = x.factor_expansion_anual().anos_educacion()
assert len(y) == 12 and (y["factor_expansion_anual"] == 60).all()
print(y[["PERIODO", "EDAD", "anos_educacion", "factor_expansion_anual"]].head())
```
