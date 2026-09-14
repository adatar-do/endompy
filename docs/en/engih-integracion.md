# Integration and R equivalents

The new module is additive in endompy 0.8.0; existing ENCFT, ENFT and ENHOGAR interfaces remain available. All fourteen public function names in `engihr 0.3.0`, including two legacy aliases, have Python equivalents. Express `%>%` using calls, methods or `DataFrame.pipe`; Python does not acquire an R operator.

`egi_dict` maps to `get_dict`, `egi_example` to `example`, and other names drop `egi_`. Prefixed aliases are also available. `egi_setLabels`/`egi_useLabels` emit deprecation warnings. R's `dict` argument is named `dictionary` in Python; positional order is preserved. Legacy `lab/labs` dictionaries are accepted with module/edition checks when metadata declares them.

`EngihDataFrame.set_labels()` and `.use_labels()` preserve the table subclass; `.validate()` returns an ordinary diagnostic table. Duplicate row indices survive. Equivalence compares content and category definitions, not R internals with pandas dtypes. R is not a runtime dependency.

```python
from endompy import EngihDataFrame, engihr as e
x = EngihDataFrame(e.example())
result = x.pipe(e.egi_set_labels).use_labels(vars=["A201"])
assert isinstance(result, EngihDataFrame)
assert e.egi_dict is e.get_dict
assert result["A101"].equals(x["A101"])
```
