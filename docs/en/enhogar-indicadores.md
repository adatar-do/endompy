# Labour indicators and missing values

The following guide details the **2018** contract. See the 2022 edition guide for its fields and codes. Both questionnaires have explicit rules and separate dictionaries.

## Methodological scope

The implementation retains the package's historical approximation. **It is not a certified reproduction of official open unemployment or the ILO potential labour force.** Questionnaire editions and dictionary revisions are independent from calculation rules.

The official and legacy dictionaries describe H507 as work or establishing a business. The historical code used it as a job-search proxy. This discrepancy is explicit: original wording is retained, and H507 is not claimed to measure exactly four-week job search. H509 asks about accepting an offer and H510 about time and conditions to work; neither is interpreted as desire to work.

## Implemented rules

| Output | Rule within working-age population |
|---|---|
| `pet` | Age within inclusive thresholds; zero outside them |
| `ocupado` | Any yes in H501:H506; zero only when all six are no |
| `desocupado` | Known nonworker and H507=1; employed always gives zero |
| `pea` | Union of employed and proxy unemployed |
| `inactivo` | Complement of PEA when known |
| `fuerza_trabajo_potencial` | Outside PEA with an affirmative H509 or H510 |

The default age threshold of 15 is configurable for analysis, not a legal claim. The integer minimum may be as low as 10, the economic module's starting age. H203 accepts 0–120, with **99 reserved for unknown age**, following the bundled dictionary. H501:H507, H509 and H510 accept 1, 2, 9 and NA; 9 means missing information.

## Unknown values

Indicators other than PET return NA outside PET or when age is unknown. Missing necessary evidence remains unknown. Conclusive evidence can settle an outcome: one employment yes suffices despite other missing responses; an employed person is not unemployed despite missing H507. Unknown employment with H507=2 yields desocupado=0, but unknown PEA and inactivity.

The package does not estimate weighted rates, sampling errors or official totals. Survey weights and design require a separate analysis.

Sources: [ONE, 2018 codebook](https://www.one.gob.do/catalogo-datos/ENHOGAR/ENHOGAR-2018-Base-SPSS-PUB/Libro%20de%20c%C3%B3digos_Personas_ENH2018.htm) · [ENHOGAR 2018 report](https://www.one.gob.do/publicaciones/2019/encuesta-nacional-de-hogares-de-propositos-multiples-enhogar-2018-informe-general/).

[2022 edition guide](enhogar-edicion-2022.md).

```python
from endompy import enhogar as e
x = e.enhogar_example()
result = e.fuerza_trabajo_potencial(e.inactivo(x))
print(result[["pea", "inactivo", "fuerza_trabajo_potencial"]])
```
