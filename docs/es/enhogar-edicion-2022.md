# ENHOGAR 2022: cuestionario y diccionario

## Cambios del cuestionario

El soporte 2022 cubre los seis indicadores existentes, selección de edición, etiquetas y revisiones del diccionario. El código utiliza campos específicos de cada cuestionario.

| Concepto | 2018 | 2022 |
|---|---|---|
| Edad | H203; 99 desconocida | P203; 99 es una edad válida |
| Ocupación | H501:H506 | P501:P506 |
| Búsqueda | Aproximación histórica con H507 | P508: búsqueda en las últimas cuatro semanas |
| Disponibilidad | H509 o H510 | P510 o P511 |
| Respuestas binarias | 1 sí, 2 no, 9 desconocida | 1 sí, 2 no; 9 se rechaza |
| Año de entrevista HANO | 2018 | 2021 o 2022 |

**P507 no es búsqueda de empleo en 2022**: registra por qué no trabajó. P509 registra por qué no buscó. No se renombran mecánicamente las columnas de 2018.

## Cálculo y saltos

Una afirmación en P501:P506 establece ocupación. Se requieren seis negativas para establecer no ocupación; los demás casos permanecen desconocidos. La desocupación requiere no ocupación conocida y P508=1. Quienes responden sí en P508 saltan a P513 en el cuestionario; el cálculo de desocupación no exige P510/P511.

PEA es la unión de ocupación y desocupación; inactividad es su complemento conocido dentro de PET. La fuerza potencial conserva la aproximación por disponibilidad fuera de PEA mediante P510 o P511. No reproduce íntegramente el concepto OIT ni utiliza todas las preguntas del módulo.

El informe de ONE usa población de **10 años y más** en el módulo económico. El paquete conserva el mínimo analítico predeterminado de 15 por compatibilidad; use `min_edad=10` cuando corresponda al universo de su análisis. No se calculan tasas ponderadas ni errores de muestreo, ni se certifican agregados oficiales.

## Diccionarios completos y versiones

`ehg_dict(2022)` en R y `get_dict(2022)` en Python seleccionan `coverage-2`, un diccionario combinado de **603 definiciones**. Su padre `baseline-1` sigue disponible mediante `version="baseline-1"`, con sus **30 definiciones originales y sus referencias intactas**. La ampliación incorpora el inventario público completo de ONE REDATAM ENH2022 y conserva las variables previas del libro SPSS y los seis indicadores derivados.

| Módulo | Campos del inventario ONE | Revisión |
|---|---:|---|
| viviendas | 10 | redatam-1 |
| hogares | 39 | redatam-1 |
| personas | 43 | redatam-1 |
| elegidos | 491 | redatam-1 |
| geografia | 9 | redatam-1 |

Los cinco módulos suman **592 apariciones de campos** y 2,888 filas de categorías. El total combinado no equivale a sumar las filas: los nombres idénticos con igual definición se comparten; se conservan las variables anteriores que no aparecen en REDATAM.

Consulte `ehg_dict_modules(2022)` / `dict_modules(2022)` para seleccionar un módulo y `ehg_dictionary_coverage()` / `dictionary_coverage()` para cobertura. `provenance=TRUE` en R o `provenance=True` en Python muestra la fuente por campo. El diccionario se elige con `module="personas"`, `module="hogares"`, etc.

`FEXP_VIV`, `FPON_VIV` y `GRUP_SEC` tienen significados distintos en viviendas y hogares. El diccionario `all` califica esos nombres con su entidad; al etiquetar columnas sin calificar exige elegir el módulo correcto. No se mezclan pesos ni se renombran automáticamente los campos SPSS `F_expansión`/`F_ponderación` con los nombres de REDATAM. Tampoco se considera que 99 sea un valor perdido en todas las preguntas.

La revisión 2018 conserva exactamente sus 447 definiciones y su huella. Edición de encuesta, módulo, revisión de diccionario y versión del paquete son selecciones separadas. No se infieren intervalos de vigencia. Un registro SQLite requiere versión exacta o una fecha con vigencia documentada; no elige la última revisión automáticamente.

Fuente de cobertura: [ONE REDATAM ENH2022](https://redatam.one.gob.do/bindom/RpWebEngine.exe/Portal?BASE=ENH2022&lang=ESP). La entrega contiene metadatos y procedencia, sin microdatos de hogares.

Fuentes: [ONE, ENHOGAR 2022 codebook](https://www.one.gob.do/catalogo-datos/ENHOGAR/ENHOGAR_2022_BD_SPSS/Libro%20de%20c%C3%B3digos_ENHOGAR2022_Personas.htm) · [ONE, ENHOGAR 2022 report](https://www.one.gob.do/media/sfahteva/informe-general-enhogar-2022-dic.pdf).

```python
from endompy import enhogar as e
x = e.enhogar_example(2022)
result = e.inactivo(x, min_edad=10, edition=2022)
print(result[['case_id', 'pet', 'ocupado', 'desocupado', 'pea', 'inactivo']])
print(e.get_dict(2022).revision()['dictionary_id'])
```
