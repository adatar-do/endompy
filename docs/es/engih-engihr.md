# ENGIH 2018 en Python

`endompy.engihr` reproduce los contratos de `engihr 0.3.0` para los metadatos de ENGIH 2018. Incluye 25 módulos, diccionarios inmutables y catálogos oficiales. No necesita R durante su uso.

Seleccione `module` para hojas de gasto: el valor predeterminado es `personas`. `get_dict()` identifica una revisión; `modules()` y `schema()` muestran qué datos están documentados. El inventario suma 1702 apariciones de campos; 1700 tienen definición verificada, incluyendo 1130 de 1132 campos de Personas.

Use `set_labels()` para conservar códigos y `use_labels()` para presentación. El ejemplo siguiente es inventado. [Etiquetas y validación](engih-etiquetas.md) explica tipos y faltantes; [fuentes](engih-fuentes.md) detalla cobertura y correcciones. Consulte también [versionado](engih-versionado.md), [integración](engih-integracion.md), [instalación](engih-deployment.md) y [referencia](engih-reference.md).

Consulte la guía de fuentes: distingue las definiciones originales, las celdas de cuestionario y las descripciones de encabezados. Los dos campos técnicos sin definición se mantienen explícitos.

```python
from endompy import EngihDataFrame, engihr as e
x = EngihDataFrame(e.example())
y = x.set_labels()
assert y["A201"].equals(x["A201"])
assert x.use_labels().loc[1, "A201"] == "Apartamento en edificio con ascensor"
assert len(e.modules()) == 25
```
