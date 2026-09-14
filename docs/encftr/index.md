# ENCFT

La **Encuesta Nacional Continua de Fuerza de Trabajo (ENCFT)** es una encuesta trimestral realizada por el Banco Central de la República Dominicana.

## Módulo encftr

Este módulo proporciona:

- **EncftDataFrame**: DataFrame con métodos específicos para la ENCFT
- **get_dict()**: Función para obtener el diccionario de la encuesta
- **Diccionario**: 636 variables con etiquetas y metadatos

## Uso Básico

```python
from endompy.encftr import EncftDataFrame, get_dict

# Cargar datos
df = EncftDataFrame(data)

# Aplicar diccionario automáticamente
df = df.set_dict()

# O cargar el diccionario manualmente
dict = get_dict()
print(f"Variables: {len(dict)}")  # 636
```

## Métodos Disponibles

| Método | Descripción |
|--------|-------------|
| `factor_expansion_anual()` | Calcula FACTOR_EXPANSION / 4 |
| `factor_expansion_semestre()` | Calcula FACTOR_EXPANSION / 2 |
| `set_dict(dict=None)` | Aplica diccionario (auto-carga si None) |

## Diccionario de Variables

El diccionario incluye variables como:

- **SEXO**: Sexo del miembro del hogar
- **EDAD**: Edad en años cumplidos
- **FACTOR_EXPANSION**: Factor de expansión trimestral
- **CATEGORIA_PRINCIPAL**: Categoría ocupacional
- Y 632 variables más...

Ver: [Diccionario completo](dict.md)
