# Labels, codes and validation

`set_labels(tbl, dictionary=None, vars=None, module="personas", edition=2018, version=None, at=None, con=None, strict=False)` preserves values, pandas dtypes, column names and index. It labels only selected fields found in the dictionary. Tables must be local and column names unique and nonempty; `vars` is a list of unique existing names.

`use_labels()` returns pandas categorical columns for mapped value codes. Missing and unknown values survive; an unknown code equal to a known label receives `[unlabelled code: ...]`. Counts A101 and A102 remain numeric. `strict=True` rejects codes outside the catalog.

Numeric codes require numeric columns. Strings are not parsed as numbers, existing categories are rejected, and booleans are not treated as 1/0. All-missing columns and nullable pandas dtypes are supported. `validate()` reports `unmapped`, `label_only`, `ok`, `unknown_codes` or `type_mismatch`. It does not evaluate skip patterns, imputations, weights or survey estimates.

Table metadata live in `DataFrame.attrs`; inspect labels through `df.labeler.get_label()` and `df.labeler.get_labels()`. `labeler_provenance` identifies each variable revision and definition. R and pandas use their own categorical/attribute representations; checks compare values, labels, order, missingness and provenance.

```python
import pandas as pd
from endompy import engihr as e
x = pd.DataFrame({"A201": [1, 1234, None], "A101": [1, 3, None]})
x.index = [7, 7, 2]
y = e.set_labels(x)
z = e.use_labels(x)
assert y["A201"].equals(x["A201"])
assert z.loc[2, "A101"] != z.loc[2, "A101"]
assert z["A201"].iloc[1] == "1234"
assert e.validate(x).loc[0, "status"] == "unknown_codes"
assert y.labeler.get_label("A101")
```
