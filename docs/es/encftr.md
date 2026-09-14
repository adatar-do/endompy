# Empezar con ENCFT

encftr 0.10.0 y endompy 0.3.0 preparan y analizan respuestas de personas de la Encuesta Nacional Continua de Fuerza de Trabajo. Incluyen etiquetas, educación, trabajo, ingresos, indicadores del hogar, pobreza monetaria 2012/2022 e índice de ingresos del hogar (IIH).

Instale primero labeler >= 0.11.0 en R o labelerpy >= 0.2.2 en Python. La entrega contiene los paquetes locales para instalar sin depender de que esas versiones estén publicadas. Los paquetes de R necesitan R >= 4.1; Python admite Python >= 3.9 con pandas >= 1.5. Consulte la guía de despliegue para construir e instalar desde los archivos de entrega.

El ejemplo incluido es completamente sintético: 12 personas, cuatro hogares a través de los períodos y claves ficticias. No contiene microdatos de la encuesta. Las funciones devuelven una tabla con los resultados y mantienen las filas originales, salvo cuando se solicita explícitamente una salida por hogar del IIH.

Calcule los pesos antes de filtrar personas. El divisor anual es el número de trimestres distintos observados dentro de cada año; el semestral se calcula dentro de cada año y semestre. Una muestra de dos trimestres no equivale a observar un año completo. Si el extracto no contiene períodos y usted conoce su cobertura, declare `periods = 4` para el anual o `periods = 2` para el semestral. Sin esa declaración, el cálculo falla.

`TRIMESTRE` acepta AAAAT (por ejemplo 20191), o 1–4 acompañado de `ANO`. Los identificadores y períodos no pueden estar ausentes. Los pesos ausentes se conservan; pesos negativos, infinitos o de tipo lógico se rechazan.

R usa nombres `ftc_*`; Python ofrece los mismos nombres sin prefijo y alias `ftc_*` para migrar scripts. Las operaciones también están disponibles en `EncftDataFrame` y se pueden encadenar. Las convenciones de tipos son nativas: R usa factores y valores NA; Python usa categorías y tipos anulables de pandas.

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
