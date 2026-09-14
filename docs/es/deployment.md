# Construcción y despliegue de endompy

Las verificaciones y la construcción son locales. Publicar archivos en un
registro de paquetes o activar GitHub Pages es una acción separada.

1. Use Python >= 3.9. Instale primero el wheel de labelerpy >= 0.2.2 incluido en
   la entrega si todavía no está publicado. Instale las dependencias `.[dev,docs]`
   y las herramientas `build` y `twine`.
2. Ejecute `python -m pytest tests`, `python -m build` y
   `python -m twine check dist/*`. Compruebe que wheel y paquete fuente incluyen
   todos los JSON, licencia y ejemplos sintéticos, y que excluyen los microdatos.
3. Instale ambos wheels en un entorno nuevo con `python -m pip install`.
   Ejecute `python -I -m pytest tests --import-mode=importlib` y
   `python -I scripts/check-examples.py` contra el paquete instalado.
4. Desde ENDOM, regenere reglas con `Rscript encftr/scripts/export-rules.R`,
   `python endompy/scripts/compile-survey-rules.py` y
   `python endompy/scripts/compile-iih.py`. Son pasos de desarrollo: quien usa
   endompy no necesita R. Regenere la documentación con
   `python encftr/scripts/author-docs.py` y `python endompy/scripts/build-reference.py`.
5. Desde endompy, ejecute `python scripts/build-docs.py` y
   `python scripts/check-sites.py ../artifacts/endompy-engih-release/sites/python --kind python`.
   El sitio tiene español en la raíz, inglés en `en/`, búsqueda independiente y
   vínculos entre páginas equivalentes. El destino canónico configurado es
   https://adatar-do.github.io/endompy/.

Archive únicamente el directorio del sitio para Pages. Conserve build-info.json,
site-check.json y los hashes SHA256 de los archivos. Excluya encuestas originales,
comparaciones con datos de personas/hogares, entornos virtuales y credenciales.
Sí se incluyen ejemplos sintéticos y resúmenes agregados de validación.

El manifiesto de paridad cubre todos los elementos exportados de R. Para la
conexión configurada de R y el operador pipe, Python usa conexiones DB-API propias
y `DataFrame.pipe`. Los cortes avanzados de Dmisc requieren límites explícitos
en pandas; no existe una conversión general de funciones arbitrarias de R.
Use etiquetas explícitas al comparar resultados categóricos.

Los flujos de GitHub generan artefactos de prueba. El flujo de Pages publica
solo cuando se activa expresamente su opción `publish`. La CI remota requiere
que labelerpy >= 0.2.2 esté disponible; las pruebas locales usan el wheel incluido.

## ICV SIUBEN / encftr0

Ejecute `Rscript encftr/scripts/export-icv-rules.R` antes de construir el wheel de Python. Exporta las reglas cerradas del ICV histórico y el ejemplo sintético compartido. Instale encftr 0.10.0 antes del paquete opcional de compatibilidad encftr0 0.1.0. Consulte la guía de migración del ICV. Defina `ENCFT_RELEASE_DIR` con otra carpeta de artefactos para conservar una entrega anterior.


## ENGIH 2018

Consulte [instalación y validación de ENGIH](engih-deployment.md) y [fuentes y cobertura](engih-fuentes.md).
