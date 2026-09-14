# endompy 0.8.0

Python tools for Dominican surveys, with reproducible calculations, code labels and immutable dictionary revisions. ENCFT follows encftr 0.10.0; ENFT follows enftr 0.9.0; ENHOGAR follows enhogar 0.4.0. The new ENGIH module follows engihr 0.3.0. R is not needed at runtime.

Requires Python >= 3.9, pandas >= 1.5, numpy >= 1.21 and labelerpy >= 0.2.2.
R is not required at runtime. Install the supplied labelerpy wheel before the
endompy wheel when these versions are not yet available in a package index.

```python
from endompy import EngihDataFrame, engihr as e
x = EngihDataFrame(e.example())  # Invented rows
labelled = x.set_labels()       # Original codes and dtypes
display = x.use_labels()        # Categorical labels for presentation
assert labelled["A201"].equals(x["A201"])
assert display.loc[1, "A201"] == "Apartamento en edificio con ascensor"
```

Read the paired [Spanish](docs/es/encftr.md) and [English](docs/en/encftr.md)
guides, [dictionary editions](docs/en/diccionario.md),
[methodology contracts](docs/en/pobreza-monetaria.md) and
[deployment guide](DEPLOYMENT.md).

The traditional ENFT module matches enftr 0.9.0. See [Spanish](docs/es/enft-enftr.md) and [English](docs/en/enft-enftr.md) guides for semester contracts, historical income/poverty and dictionary revisions.


ENHOGAR 2018 and 2022 are available through `EnhogarDataFrame` and `endompy.enhogar`, matching enhogar 0.4.0. Six labour indicators use questionnaire-specific fields and missing-value rules. Immutable baseline dictionaries contain 447 definitions for 2018 and 30 scoped definitions for 2022 (24 source variables plus 6 indicators, not the complete questionnaire). See the [Spanish](docs/es/enhogar-edicion-2022.md) and [English](docs/en/enhogar-edicion-2022.md) 2022 guides.

ENGIH 2018 is available through `EngihDataFrame` and `endompy.engihr`: 25 modules, five catalogs, labels, validation and partial dictionary revisions. It inventories 1702 field occurrences; 530 have verified definitions, including 386 of 1132 Persons fields. Undocumented columns remain intact. All 30 metadata files retain the exact bytes and revision fingerprints of engihr 0.3.0.

Read the [Spanish ENGIH guide](docs/es/engih-engihr.md), [English ENGIH guide](docs/en/engih-engihr.md), [dictionary versioning](docs/en/engih-versionado.md) and [coverage and source decisions](docs/en/engih-fuentes.md). The delivery contains synthetic examples and official metadata with provenance, not original household records. Prepared workflows and local validation do not constitute remote publication or certification of survey estimates.
