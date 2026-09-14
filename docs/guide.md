# Guía de Uso

## Conceptos Básicos

### EndomDataFrame

`EndomDataFrame` es la clase base para todos los DataFrames de encuestas. Hereda de `pandas.DataFrame` e integra opcionalmente con `labelerpy` para etiquetado.

```python
from endompy import EndomDataFrame

# Crear un DataFrame base
df = EndomDataFrame({"X": [1, 2, 3]})

# Funciona igual que pandas
print(df.describe())
```

### EncftDataFrame

`EncftDataFrame` es una extensión específica para la ENCFT:

```python
from endompy import EncftDataFrame

# Crear desde datos
df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})

# Calcular factor de expansión anual
df = df.factor_expansion_anual()
print(df["factor_expansion_anual"])  # [257.0, 212.0, 100.0]
```

## Trabajar con Etiquetas

### Diccionario Automático

`EncftDataFrame` incluye un diccionario con 636 variables predefinidas:

```python
from endompy import EncftDataFrame

df = EncftDataFrame(data)

# ¡Carga el diccionario automáticamente!
df = df.set_dict()

# Ver etiqueta de una columna
print(df.labeler.get_label("SEXO"))  # "Sexo del miembro del hogar"
```

### Diccionario Personalizado

También puedes usar tu propio diccionario:

```python
from labelerpy import Dict

mi_dict = Dict(
    metadata={"name": "Mi diccionario"},
    variables={"X": {"label": "Mi variable"}}
)

df = df.set_dict(mi_dict)
```

## Métodos Disponibles

### Factor de Expansión

```python
# Anual (÷4 porque es trimestral)
df = df.factor_expansion_anual()

# Semestral (÷2)
df = df.factor_expansion_semestre()
```

## Crear tu Propia Clase

Puedes crear clases personalizadas heredando de `EndomDataFrame`:

```python
from endompy import EndomDataFrame

class MiEncuesta(EndomDataFrame):
    @property
    def _constructor(self):
        return MiEncuesta
    
    def mi_metodo(self):
        return self.copy()
```
