# Integración y equivalencias con R

El nuevo módulo es aditivo en endompy 0.8.0; conserva las interfaces previas de ENCFT, ENFT y ENHOGAR. Los catorce nombres públicos de funciones de `engihr 0.3.0`, incluidos los dos alias antiguos, tienen equivalente Python. El operador `%>%` se expresa con llamadas, métodos o `DataFrame.pipe`; no se crea un operador R en Python.

`egi_dict` corresponde a `get_dict`, `egi_example` a `example` y los demás nombres pierden el prefijo `egi_`. El prefijo también se conserva como alias. `egi_setLabels`/`egi_useLabels` avisan de su deprecación. El argumento `dict` de R se llama `dictionary` en Python; el orden posicional se conserva. Los diccionarios antiguos `lab/labs` se aceptan con los mismos controles de módulo/edición cuando su metadata los declara.

`EngihDataFrame.set_labels()` y `.use_labels()` conservan el tipo de tabla; `.validate()` devuelve una tabla diagnóstica ordinaria. Se preservan índices duplicados. La equivalencia compara contenido y categorías, no clases internas de R con tipos de pandas. R no es una dependencia de ejecución.

```python
from endompy import EngihDataFrame, engihr as e
x = EngihDataFrame(e.example())
result = x.pipe(e.egi_set_labels).use_labels(vars=["A201"])
assert isinstance(result, EngihDataFrame)
assert e.egi_dict is e.get_dict
assert result["A101"].equals(x["A101"])
```
