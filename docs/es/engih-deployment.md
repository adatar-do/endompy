# Instalación, validación y despliegue

Instale Python >= 3.9, pandas >= 1.5 y numpy >= 1.21. La entrega incluye `labelerpy 0.2.2` y el wheel/sdist de `endompy 0.8.0`. Use `python -m pip install labelerpy-0.2.2-py3-none-any.whl endompy-0.8.0-py3-none-any.whl` dentro de un entorno virtual; las dependencias deben estar disponibles o ser accesibles en el índice configurado.

Para reconstruir: `python -m build`; `python -m twine check dist/*`; instale el wheel y ejecute `python -I -m pytest tests --import-mode=importlib` y `python -I scripts/check-examples.py`. `scripts/release-engih.py` reúne construcción, pruebas y sitio en una salida explícita. La entrega local verifica instalaciones nuevas en Python 3.9/pandas 1.5 y Python 3.13/pandas 3, con regresiones de los módulos previos.

`scripts/build-docs.py SALIDA` construye español e inglés; `scripts/check-sites.py SALIDA --kind python` verifica enlaces, recursos, buscadores y páginas equivalentes. Sirva la carpeta estática por HTTP conservando `en/`. Los workflows están preparados; publicación y CI remoto requieren sus propias ejecuciones y la disponibilidad de labelerpy en el índice.

Para actualizar la referencia de ENGIH, desde ENDOM ejecute `Rscript endompy/scripts/export-engih-reference.R` con `engihr 0.3.0` instalado y `python endompy/scripts/sync-engih-resources.py engihr --check`. La referencia es sintética e incluye todos los códigos categóricos, un desconocido y NA. Los recursos registrados no se modifican al instalar el paquete. Los originales Excel y cuestionarios no forman parte de la entrega.

```python
from endompy import __version__, engihr as e
assert __version__ == "0.8.0"
assert e.get_dict("b1").revision()["dictionary_id"] == "engih-2018-b1"
assert e.get_dict("b1").revision()["version"] == "coverage-2"
```
