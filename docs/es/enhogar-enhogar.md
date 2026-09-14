# Primeros pasos con ENHOGAR

`enhogar 0.5.0` y `endompy.enhogar` en `endompy 0.8.0` admiten **2018 y 2022**. Las 20 funciones tienen equivalentes en ambos lenguajes. Trabajan con tablas locales de códigos numéricos: materialice las consultas a bases de datos antes del cálculo.

## Selección de edición

Use `edition=2022` para declarar el cuestionario. También se reconoce por las columnas: H203/H501:H507 identifican 2018 y P203/P501:P508 identifican 2022. Mezclar ambos grupos o indicar una edición incompatible produce error. Una tabla vacía con esas columnas conserva su edición.

`HANO` es el año de entrevista. En el cuestionario 2022 admite 2021 y 2022; no exige un solo año. Sin columnas específicas, un HANO compuesto solo por 2021 es ambiguo y necesita edición explícita. Los años ausentes o incompatibles se rechazan cuando la columna existe y hay filas.

La selección explícita tiene prioridad sobre la opción configurada; ambas se contrastan con los datos. Sin configuración ni evidencia se conserva 2018 por compatibilidad. Para etiquetar una tabla que solo contiene identificadores comunes, declare la edición. `guess_enhogar_edition()` exige evidencia suficiente y no modifica opciones. `get_enhogar_edition()` consulta la selección sin modificarla. Restablezca con `enhogar_edition(NULL)` en R o `enhogar_edition(None)` en Python, cuya opción es local al contexto.

## Datos y resultados

Se conservan datos originales, filas y orden; Python conserva también índices duplicados. Los resultados se recalculan. Columnas ausentes, textos, factores y códigos no admitidos producen errores. Los valores desconocidos necesarios siguen siendo desconocidos.

`enhogar_example()` conserva los doce casos inventados de 2018. `enhogar_example(2022)` ofrece otros doce casos adaptados al cuestionario 2022. No son personas encuestadas ni permiten estimar cifras nacionales.

[Guía de la edición 2022](enhogar-edicion-2022.md).

```python
from endompy import enhogar as e
x = e.enhogar_example()
print(e.ocupado(x)[["case_id", "pet", "ocupado"]])
```
