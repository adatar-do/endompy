# endompy 0.8.0

- ENHOGAR 2022 adds five complete ONE REDATAM module dictionaries and combined coverage-2 (603 definitions), preserving all original revision references.
- ENGIH 2018 adds coverage-2 for 25 modules, explicit historical metadata selection, and field provenance: 1700 of 1702 fields described; HOLGURA and PERDIDA_TURISMO remain unresolved.
- Original baseline-1 revisions and R/Python resource identity remain intact.

# endompy 0.7.0

- Add ENGIH 2018 metadata matching engihr 0.2.0: 25 modules, 530 verified definitions and explicit 1702-field-occurrence coverage.
- Preserve exact R dictionary revisions, source decisions and catalogs; add partial revision registration, validation, labels and EngihDataFrame.
- Add a fresh R oracle covering every categorical code, unknown codes and missingness, six paired guides and complete ENGIH API reference.
- Preserve existing ENCFT, ENFT and ENHOGAR interfaces and resource files.

# endompy 0.6.0

- Add ENHOGAR 2022 parity with enhogar 0.4.0 while retaining 2018 results and dictionary hash.
- Use P203, P501:P506, P508 and P510/P511; do not mistake P507 for job search.
- Preserve valid age 99, reject unsupported response 9, and accept interview years 2021/2022 in the 2022 questionnaire.
- Add an edition-isolated baseline with 24 source fields and six indicators; declare its limited coverage.
- Test immutable partial revisions, unknown responses, questionnaire skips, edition conflicts and 729 employment combinations.
- Add a paired 2022 guide and update bilingual API/deployment documentation.

# endompy 0.5.0

- Add ENHOGAR 2018 parity with enhogar 0.3.0: six labour proxies, edition validation, labeling and immutable dictionary revisions.
- Preserve unknown responses, reserved unknown age 99, input rows and duplicate indexes.
- Add EnhogarDataFrame, 18 R/Python API pairs and four paired guides.
- Preserve existing ENCFT and ENFT APIs.

# endompy 0.4.0

- Add the traditional ENFT module and EnftDataFrame with 84 R-compatible entry points.
- Validate semiannual periods, household/member keys and dictionary revisions.
- Preserve unknown household income and explicit 2005–2016 poverty coverage.
- Correct prior-year remittance slots and occupied/unemployed precedence.
- Add synthetic R/Python parity fixtures and Spanish/English ENFT documentation.
- Verify installation with pandas 1.5 and 3 while preserving ENCFT functionality.

# endompy 0.3.0

- Integrates historical ICV SIUBEN from encftr0 0.0.2.9002, preserving coefficients
  and reference outputs. Adds score, method identifier, explicit inputs,
  grouping by year and household-head validation.
- Retains four deprecated ftc0_* names. encftr0 0.1.0 delegates here; labeling
  now respects selected variables.
- Separate ICV labels preserve the immutable baseline-1 questionnaire.
- Bilingual calculation and migration guide with 108 synthetic person records.
- Parity with encftr 0.10.0. Does not update or certify current SIUBEN methodology.

# endompy 0.2.0

- ENCFT functional parity with encftr 0.9.0: education, labour, income components,
  household indicators, poverty 2012/2022 and the household income index (IIH).
- Pure pandas functions and chainable EncftDataFrame methods, with R-name aliases.
- Verified dictionary revisions through labelerpy >= 0.2.1; unchanged definitions
  are reused across editions. The bundled baseline has no asserted historic dates.
- Annual and semester weights use observed coverage. Calls without quarter fields
  must now declare periods=4 or periods=2 explicitly.
- Bundled rules, reference tables and synthetic examples; no R runtime required.
- Bilingual documentation and reproducible package/site validation scripts.

This release changes some calculations to correct defects in legacy helpers.
Persist package version, dictionary revision, poverty methodology and input coverage
with results. Model-based IIH and observed monetary poverty are separate measures.
