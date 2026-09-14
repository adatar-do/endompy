# Fuentes, cobertura y correcciones

Los metadatos proceden de los [Excel y cuestionarios de ENGIH 2018 del Banco Central](https://www.bancentral.gov.do/a/d/4796-engih-2018). Se copian sin cambios los 58 archivos de metadatos/diccionarios de `engihr 0.3.0`, con URL, SHA256 y filas de procedencia. No se incluyen registros originales de hogares.

Los catálogos contienen 8090 variedades, 120 unidades, 202 establecimientos, 249 países y 72 monedas. Las etiquetas de unidades y establecimientos añaden códigos entre corchetes para distinguir textos repetidos; `catalog()` conserva los textos originales.

Se conservan tres decisiones documentadas: A101 es un conteo según el cuestionario A, página PDF 5, y se omite su codificación Sí/No errónea; C2/C3 se vinculan por periodicidad explícita ante numeración inconsistente; una fila de C6C sin identificador no se asigna a un campo inventado. A102, alumbrado, calles asfaltadas y ZONA donde existe se respaldan con el cuestionario.

El módulo no calcula gastos, ingresos, pobreza, ponderaciones ni agregados oficiales. Las hojas tienen distintas unidades de observación: compruebe cardinalidad y diseño antes de unirlas.

La revisión predeterminada `coverage-2` documenta 1,700 de 1,702 apariciones de campos en 25 módulos: 530 definiciones originales del diccionario oficial, 647 celdas verificadas de cuestionarios y 523 descripciones de encabezados publicados. Estas últimas no especifican fórmulas, imputaciones, universos de códigos ni reglas de unicidad que la fuente no documenta. Personas cubre 1,130 de 1,132 campos; los otros 24 módulos cubren su inventario completo.

`HOLGURA` y `PERDIDA_TURISMO` permanecen sin definición verificable y fuera del diccionario. Se conservan sus columnas originales y se muestran como pendientes. `dictionary_coverage()` expone los totales y límites; `dictionary_coverage(provenance=True)` devuelve la procedencia por campo. La revisión histórica `baseline-1` conserva exactamente sus 530 referencias originales. `modules(version="baseline-1")` y `schema(version="baseline-1")` permiten consultar su cobertura histórica.

Los campos mensuales D802 son posiciones de una matriz cuyo período depende de `REPLICA`: no se asigna enero a M1 de forma general. Los países y monedas mantienen los códigos de texto de sus catálogos oficiales. A201_APTOS cuenta apartamentos por piso; A401A es el total de miembros del hogar. No se inventan códigos de valores perdidos para montos o conteos.

```python
from endompy import engihr as e
assert e.modules()["documented"].sum() == 1700
assert len(e.schema()) == 1132
assert e.schema()["documented"].sum() == 1130
assert len(e.catalog("variedades")) == 8090
assert len(e.source_issues()) == 3
assert e.get_dict()["A101"].labels is None
```
