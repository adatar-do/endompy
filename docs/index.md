# endompy

**Librería Python para encuestas dominicanas**

`endompy` proporciona clases DataFrame extendidas para trabajar con datos de encuestas del Banco Central de la República Dominicana.

## Instalación

```bash
pip install endompy
```

Para usar con etiquetado automático:
```bash
pip install endompy labelerpy
```

## Inicio Rápido

```python
from endompy import EncftDataFrame

# Cargar datos de la ENCFT
df = EncftDataFrame(data)

# Aplicar diccionario automáticamente (636 variables)
df = df.set_dict()

# Calcular factor de expansión anual
df = df.factor_expansion_anual()

print(df)
```

## Características

- **EncftDataFrame**: DataFrame para la ENCFT con métodos específicos
- **Diccionario integrado**: 636 variables con etiquetas
- **Integración con labelerpy**: Etiquetado automático de variables
- **Métodos de análisis**: Factor de expansión y más

## Encuestas Soportadas

| Encuesta | Clase | Variables |
|----------|-------|-----------|
| ENCFT (tradicional) | `EncftDataFrame` | 636 |

## Próximos Pasos

- [Guía de Uso](guide.md) - Tutorial completo
- [ENCFT](encftr/index.md) - Documentación de la ENCFT
- [API Reference](api/base.md) - Documentación de la API
