# Instalación, migración y despliegue

## Instalar artefactos locales

Instale primero `labeler >= 0.11.0` y las dependencias declaradas. Después instale `enhogar_0.5.0.tar.gz` como fuente o `enhogar_0.5.0.zip` como binario Windows compatible con su versión de R. Python requiere `labelerpy >= 0.2.2`, pandas >= 1.5, NumPy y Python >= 3.9; instale `endompy-0.8.0-py3-none-any.whl`.

## Cambios desde enhogar 0.2.0

- set_labels conserva códigos y adjunta metadatos; use_labels convierte para presentación.
- inactivo usa PEA y ya no falla por pea_abierta inexistente.
- En 2018, edad 99 y respuestas 9 no se convierten en población activa o inactiva conocida.
- Se aceptan 2018 y 2022; se rechazan datos mixtos, códigos desconocidos y esquemas inválidos.
- El diccionario tiene nombres únicos, revisión verificable y cambios parciales compartidos.
- Se elimina la advertencia repetida de búsqueda de empleo: el alcance aproximado queda documentado en la API y esta guía.

## Construir y publicar

Desde la raíz ENDOM, ejecute `Rscript enhogar/scripts/check-release.R`, `Rscript enhogar/scripts/build-docs.R` y `python enhogar/scripts/check-sites.py artifacts/enhogar-2022-release/sites/r --kind r`. El constructor genera español en la raíz e inglés en `en/`. La auditoría comprueba pares de idioma, enlaces, recursos, anclas e índices de búsqueda. Para Python ejecute `python endompy/scripts/build-docs.py artifacts/enhogar-2022-release/sites/python` y la misma auditoría con `--kind python`.

Los scripts construyen localmente. El workflow pkgdown permite compilar manualmente; solo publica al activar su entrada publish. Publique antes las versiones mínimas de las dependencias. Los sitios estáticos y artefactos incluidos son desplegables, pero esta entrega no ejecuta publicación ni CI remoto. El binario Windows se verifica en R 4.5.1; otras plataformas requieren su propio check.

No ejecute data-raw para preparar una instalación: conserva rutas de desarrollo históricas. La entrega se construye desde recursos versionados y ejemplos inventados.
