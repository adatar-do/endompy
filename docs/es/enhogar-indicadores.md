# Indicadores laborales y faltantes

La guía siguiente detalla el contrato heredado de **2018**. Para los campos y códigos de 2022 consulte la guía de la edición 2022. Ambos cuestionarios tienen reglas explícitas y diccionarios separados.

## Alcance metodológico

La implementación conserva la aproximación histórica del paquete. **No constituye una reproducción certificada de la desocupación abierta oficial ni de la fuerza de trabajo potencial de la OIT.** La edición del cuestionario y la revisión del diccionario son independientes de las reglas de cálculo.

El diccionario oficial y el heredado describen H507 como una pregunta sobre trabajo o establecimiento de un negocio. El código histórico la usaba para aproximar búsqueda de trabajo. Esa discrepancia se hace explícita: se conserva la redacción de origen y no se afirma que H507 mida exactamente búsqueda durante cuatro semanas. H509 pregunta por poder aceptar una oferta y H510 por tiempo y condiciones para trabajar; ninguna se interpreta como deseo de trabajar.

## Reglas implementadas

| Salida | Regla dentro de PET |
|---|---|
| `pet` | Edad entre mínimos y máximos inclusivos; 0 fuera del intervalo |
| `ocupado` | Algún sí en H501:H506; cero solo si las seis son no |
| `desocupado` | No ocupado y H507=1; un ocupado siempre da cero |
| `pea` | Unión de ocupado y desocupado aproximado |
| `inactivo` | Complemento de PEA cuando su valor se conoce |
| `fuerza_trabajo_potencial` | Fuera de PEA y afirmación en H509 o H510 |

El umbral predeterminado de 15 años es una decisión analítica configurable, no una afirmación de edad legal. Se admite un mínimo entero de 10 porque el módulo económico empieza a esa edad. H203 acepta 0–120, con **99 reservado para edad desconocida**, conforme al diccionario incluido. H501:H507, H509 y H510 admiten 1, 2, 9 y NA; 9 representa falta de información.

## Lógica de los desconocidos

Los indicadores distintos de PET devuelven NA fuera de PET o con edad desconocida. Si falta información necesaria, el resultado permanece desconocido. Un hecho concluyente puede resolverlo: un sí de empleo basta aunque otras preguntas falten; un ocupado no es desocupado aunque H507 falte. Una persona con empleo desconocido y H507=2 tiene desocupado=0 pero PEA e inactivo desconocidos.

No se calculan tasas ponderadas, errores de muestreo ni totales oficiales. Los factores y el diseño de encuesta deben tratarse en un análisis separado.

Fuentes: [ONE, 2018 codebook](https://www.one.gob.do/catalogo-datos/ENHOGAR/ENHOGAR-2018-Base-SPSS-PUB/Libro%20de%20c%C3%B3digos_Personas_ENH2018.htm) · [ENHOGAR 2018 report](https://www.one.gob.do/publicaciones/2019/encuesta-nacional-de-hogares-de-propositos-multiples-enhogar-2018-informe-general/).

[Guía de la edición 2022](enhogar-edicion-2022.md).

```python
from endompy import enhogar as e
x = e.enhogar_example()
result = e.fuerza_trabajo_potencial(e.inactivo(x))
print(result[["pea", "inactivo", "fuerza_trabajo_potencial"]])
```
