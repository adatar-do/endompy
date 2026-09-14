# Income and historical poverty

Identifier `enftr-historical-2005-2016-v2` denotes the package's historical implementation with integrity and remittance corrections. It is not claimed to reproduce the official program with certified equivalence.

## Units, keys and coverage

The 34 components sum monthly individual income in Dominican pesos. Per capita income is household income divided by all members present. Supply complete households: omitted members cannot be detected from a filtered table. Period, dwelling, household and member form a unique, nonmissing key. Each household needs exactly one head so imputed rent is assigned once. Zone must be constant within a household and coded 0/1.

Classification covers only 2005/1–2016/2. Bundled lines cover 2000–2016, but available lines do not extend the income model. Boundaries are inclusive: income equal to the extreme line is category 1; income equal to the general line is category 2.

| Output | Meaning |
|---|---|
| `1` | Extreme poverty |
| `2` | Moderate poverty |
| `3` | Nonpoor |
| `NA` + `outside_coverage` | Outside the implemented interval |
| `NA` + `missing_income` | At least one member has unknown total income |

## Sources and missing values

`ing_ext` accepts multiple transactions per person. An absent record means no transaction; a missing amount preserves unknown income. `remesas` requires one row per person with six slots. Every positive amount needs valid exchange-rate and CPI references; unknown references stop calculation. Other components retain their historical missing-value recoding rules, documented in the reference. Questionnaire skips and missing responses are not interchangeable.

For semester 1, PER4/PER5/PER6 refer to December, November and October of the prior year. Through 2007/1, multiply by frequency and divide by 12; from 2007/2, divide by 6. Only the six defined slots are used, excluding unrelated `EFT_MONTO` columns.

Components are recalculated by default. R `.reuse` and Python `reuse` explicitly trust supplied components and their units/applicability. `.keep`/`keep` retains components for audit. Lines are matched by period and zone even if previous results are present.

Implemented coverage is defined by the code and bundled tables. For methodological context, see [MEPyD's published programs](https://mepyd.gob.do/vaes/codigos-de-pobreza/) and the [ONE 2012 poverty methodology](https://www.one.gob.do/publicaciones/2013/metodologia-calculo-pobreza-monetaria-diagnostico-y-propuesta-para-la-estimacion-de-la-pobreza-2012/). These references do not certify numerical equivalence with official ENFT production.

## Runnable example
```python
import json
from importlib.resources import files
import pandas as pd
from endompy import enftr as ft
x = pd.DataFrame(json.loads(files("endompy.enftr").joinpath("resources/synthetic-members.json").read_text()))
result = ft.pobreza_monetaria(x, keep=True)
print(result["pobreza_estado"].value_counts())
print(result[["ing_total_pobreza_monetaria", "ing_pc_pobreza_monetaria", "pobreza_monetaria"]].tail())
```
