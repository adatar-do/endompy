# Diccionario ENCFT

El diccionario de la ENCFT contiene **636 variables** con sus etiquetas y valores codificados.

## Cargar el Diccionario

```python
from endompy.encftr import get_dict

dict = get_dict()
print(f"Nombre: {dict.metadata.name}")
print(f"Variables: {len(dict)}")
```

## Explorar Variables

```python
# Ver una variable específica
var = dict["SEXO"]
print(f"Etiqueta: {var.label}")
print(f"Valores: {var.labels}")

# Listar todas las variables
for nombre in dict:
    print(nombre)
```

## Variables Principales

| Variable | Etiqueta | Valores |
|----------|----------|---------|
| SEXO | Sexo del miembro del hogar | 1=Hombre, 2=Mujer |
| EDAD | Edad en años cumplidos | Numérico |
| FACTOR_EXPANSION | Factor de expansión | Numérico |
| ESTADO_CIVIL | Estado civil | 1-6 |
| CATEGORIA_PRINCIPAL | Categoría ocupacional | 1-8 |

## Archivo JSON

El diccionario se almacena en formato JSON compatible con R:

**Ubicación**: `endompy/encftr/encft_dict.json`

Puede ser usado directamente con el paquete R `labeler`:

```r
library(labeler)
dict <- from_json("encft_dict.json")
```
