# ENHOGAR API reference

20 public R functions have Python equivalents. [Labour contracts](enhogar-indicadores.md) · [Dictionary revisions](enhogar-diccionario.md).

## ehg_browse_dict

Return the selected revision as an interactive R widget or a local data.frame. Python returns a pandas table for notebooks.

```python
endompy.enhogar.browse_dict(edition=2018, version=None, at=None, con=None, module='all')
```

R implementation:

```r
{
    dict <- ehg_dict(edition, version, at, con, module)
    if (!is.logical(interactive) || length(interactive) != 1L || is.na(interactive)) 
        stop("interactive must be TRUE or FALSE", call. = FALSE)
    if (interactive) 
        labeler::browse_dict(dict)
    else as.data.frame(dict)
}
```

## ehg_desocupado

Among known nonworkers, use H507=1 for the historical 2018 proxy or P508=1 for four-week search in 2022. P507 is a reason, not search. Employed people receive zero despite missing search. P508=yes skips availability, which is not required for unemployment. Official aggregates are not certified.

```python
endompy.enhogar.desocupado(tbl, min_edad=15, max_edad=inf, edition=None)
```

R implementation:

```r
{
    edition <- .ehg_edition(tbl, edition)
    tbl <- ehg_ocupado(tbl, min_edad, max_edad, edition)
    search <- .ehg_response(tbl, .ehg_schema(edition)$search, edition)
    tbl$desocupado <- .ehg_mask(tbl$ocupado == 0 & search, tbl$pet)
    tbl
}
```

## ehg_dict

Load a verified immutable revision: 2018 retains 447 definitions; 2022 all defaults to coverage-2 with 603 definitions, preserving baseline-1 and its 30 references. Five complete REDATAM module dictionaries use redatam-1. No applicability dates are inferred.

```python
endompy.enhogar.get_dict(edition=2018, version=None, at=None, con=None, module='all')
```

R implementation:

```r
{
    spec <- .ehg_dict_spec(edition, module)
    if (!is.null(con)) 
        result <- labeler::db_load_dict_version(con, spec$dictionary_id, version = version, at = at)
    else {
        if (is.null(version)) 
            version <- spec$default_version
        if (!is.character(version) || length(version) != 1L || is.na(version) || !version %in% spec$versions) 
            stop("Revision not bundled", call. = FALSE)
        result <- labeler::from_json(system.file("dictionaries", spec$files[[version]], package = "enhogar"))
    }
    revision <- labeler::dict_revision(result, at = at)
    if (revision$dictionary_id != spec$dictionary_id) 
        stop("Dictionary identity does not match edition/module", call. = FALSE)
    result
}
```

## ehg_dict_modules

List all and the five complete ONE REDATAM module inventories, with exact revision identifiers.

```python
endompy.enhogar.dict_modules(edition=2018)
```

R implementation:

```r
{
    .ehg_year(edition)
    names <- if (edition == 2018) 
        "all"
    else c("all", "viviendas", "hogares", "personas", "elegidos", "geografia")
    do.call(rbind, lapply(names, function(module) {
        spec <- .ehg_dict_spec(edition, module)
        data.frame(module = module, dictionary_id = spec$dictionary_id, default_version = spec$default_version, 
            definitions = as.integer(spec$definitions))
    }))
}
```

## ehg_dict_versions

List revision identifiers, parent revisions, date intervals and content hashes. 2018 retains baseline-1; 2022 all bundles baseline-1 and coverage-2, with redatam-1 for module dictionaries.

```python
endompy.enhogar.dict_versions(edition=2018, con=None, module='all')
```

R implementation:

```r
{
    spec <- .ehg_dict_spec(edition, module)
    if (!is.null(con)) 
        return(labeler::db_list_dict_versions(con, spec$dictionary_id))
    fields <- c("dictionary_id", "version", "parent_version", "created_at", "author", "message", "valid_from", 
        "valid_to", "content_hash")
    do.call(rbind, lapply(spec$versions, function(version) {
        revision <- labeler::dict_revision(ehg_dict(edition, version, module = module))
        as.data.frame(stats::setNames(lapply(fields, function(n) if (is.null(revision[[n]])) 
            NA_character_
        else revision[[n]]), fields))
    }))
}
```

## ehg_dictionary_coverage

Audit the 592 source field occurrences, categories, conflicting names and per-field source provenance.

```python
endompy.enhogar.dictionary_coverage(provenance=False)
```

R implementation:

```r
{
    if (!is.logical(provenance) || length(provenance) != 1L || is.na(provenance)) 
        stop("provenance must be TRUE or FALSE", call. = FALSE)
    file <- if (provenance) 
        "2022-full-provenance.json"
    else "2022-full-coverage.json"
    jsonlite::fromJSON(system.file("reference", file, package = "enhogar"), simplifyVector = FALSE)
}
```

## ehg_fuerza_trabajo_potencial

Outside the approximate labour force, an affirmative H509/H510 (2018) or P510/P511 (2022) identifies the availability proxy. These questions are not interpreted as desire to work. This is not a certified ILO potential labour-force indicator.

```python
endompy.enhogar.fuerza_trabajo_potencial(tbl, min_edad=15, max_edad=inf, edition=None)
```

R implementation:

```r
{
    edition <- .ehg_edition(tbl, edition)
    tbl <- ehg_pea(tbl, min_edad, max_edad, edition)
    now <- .ehg_response(tbl, .ehg_schema(edition)$available_now, edition)
    offered <- .ehg_response(tbl, .ehg_schema(edition)$available_offer, edition)
    tbl$fuerza_trabajo_potencial <- .ehg_mask(tbl$pea == 0 & (now | offered), tbl$pet)
    tbl
}
```

## ehg_inactivo

Complement of the approximate labour force when known, within working-age population. Uses pea, fixing the obsolete pea_abierta reference.

```python
endompy.enhogar.inactivo(tbl, min_edad=15, max_edad=inf, edition=None)
```

R implementation:

```r
{
    edition <- .ehg_edition(tbl, edition)
    tbl <- ehg_pea(tbl, min_edad, max_edad, edition)
    tbl$inactivo <- .ehg_mask(tbl$pea == 0, tbl$pet)
    tbl
}
```

## ehg_ocupado

One affirmative answer in H501:H506 (2018) or P501:P506 (2022) establishes employment. Six negative answers establish zero. Otherwise the result remains unknown. Missing skipped questions do not override an affirmative answer.

```python
endompy.enhogar.ocupado(tbl, min_edad=15, max_edad=inf, edition=None)
```

R implementation:

```r
{
    edition <- .ehg_edition(tbl, edition)
    tbl <- ehg_pet(tbl, min_edad, max_edad, edition)
    responses <- lapply(.ehg_schema(edition)$employed, function(n) .ehg_response(tbl, n, edition))
    tbl$ocupado <- .ehg_mask(Reduce(`|`, responses), tbl$pet)
    tbl
}
```

## ehg_pea

Union of employment and edition-specific unemployment. Necessary unknown information remains missing rather than becoming inactivity.

```python
endompy.enhogar.pea(tbl, min_edad=15, max_edad=inf, edition=None)
```

R implementation:

```r
{
    edition <- .ehg_edition(tbl, edition)
    tbl <- ehg_desocupado(tbl, min_edad, max_edad, edition)
    tbl$pea <- .ehg_mask(tbl$ocupado == 1 | tbl$desocupado == 1, tbl$pet)
    tbl
}
```

## ehg_pet

Use H203 (2018) or P203 (2022), ages 0-120. Age 99 is missing only in 2018; it is valid in 2022. PET is zero outside inclusive thresholds and missing when age is unknown. The age threshold is analytical, not a legal claim.

```python
endompy.enhogar.pet(tbl, min_edad=15, max_edad=inf, edition=None)
```

R implementation:

```r
{
    .ehg_table(tbl)
    edition <- .ehg_edition(tbl, edition)
    if (!is.numeric(min_edad) || length(min_edad) != 1L || is.na(min_edad) || !is.finite(min_edad) || 
        min_edad < 10 || min_edad != floor(min_edad)) 
        stop("min_edad must be an integer of at least 10", call. = FALSE)
    if (!is.numeric(max_edad) || length(max_edad) != 1L || is.na(max_edad) || max_edad < min_edad || 
        max_edad != floor(max_edad)) 
        stop("max_edad must be an integer >= min_edad or Inf", call. = FALSE)
    schema <- .ehg_schema(edition)
    age <- .ehg_numeric(tbl, schema$age, 0:120)
    age[age %in% schema$age_missing] <- NA_real_
    tbl$pet <- as.integer(age >= min_edad & age <= max_edad)
    tbl
}
```

## ehg_register_dict

Register an immutable complete revision while sharing unchanged definitions. A one-variable change reuses the other 446 definitions in 2018, or 29 in the original 2022 baseline; unchanged definitions are reused in expanded revisions too. Date intervals must come from documented evidence.

```python
endompy.enhogar.register_dict(con, dictionary, version, edition=2018, valid_from=None, valid_to=None, module='all', **kwargs)
```

R implementation:

```r
{
    spec <- .ehg_dict_spec(edition, module)
    if (!labeler::is.Dict(dict)) 
        stop("dict must be a valid dictionary draft", call. = FALSE)
    if (!is.null(dict$metadata$module) && dict$metadata$module != module) 
        stop("Dictionary module does not match", call. = FALSE)
    if (!is.null(dict$metadata$questionnaire_edition) && dict$metadata$questionnaire_edition != edition) 
        stop("Dictionary edition does not match", call. = FALSE)
    labeler::db_register_dict(con, dict, version, dictionary_id = spec$dictionary_id, valid_from = valid_from, 
        valid_to = valid_to, ...)
}
```

## ehg_setLabels

Deprecated alias. Attach labels and dictionary provenance without changing numeric codes. Select an exact revision or a documented date for reproducibility.

```python
endompy.enhogar.setLabels(tbl, vars=None, edition=None, version=None, at=None, con=None, module='all')
```

R implementation:

```r
{
    lifecycle::deprecate_warn("0.1.0", "ehg_setLabels()", "ehg_set_labels()")
    ehg_set_labels(tbl, vars, edition, version, at, con, module)
}
```

## ehg_set_labels

Attach labels and dictionary provenance without changing numeric codes. Select an exact revision or a documented date for reproducibility.

```python
endompy.enhogar.set_labels(tbl, vars=None, edition=None, version=None, at=None, con=None, module='all')
```

R implementation:

```r
{
    selected <- .ehg_edition(tbl, edition)
    columns <- if (is.null(vars)) 
        names(tbl)
    else vars
    if (selected == 2022 && module == "all" && any(columns %in% c("FEXP_VIV", "FPON_VIV", "GRUP_SEC"))) 
        stop("Ambiguous household/dwelling fields: select module hogares or viviendas", call. = FALSE)
    labeler::set_Dict(tbl, ehg_dict(selected, version, at, con, module), subset = vars, dtypes = FALSE, 
        at = at)
}
```

## ehg_useLabels

Deprecated alias. Replace numeric codes with value labels for presentation, retaining column names. Keep original numeric tables for indicator calculation.

```python
endompy.enhogar.useLabels(tbl, vars=None, edition=None, version=None, at=None, con=None, module='all')
```

R implementation:

```r
{
    lifecycle::deprecate_warn("0.1.0", "ehg_useLabels()", "ehg_use_labels()")
    ehg_use_labels(tbl, vars, edition, version, at, con, module)
}
```

## ehg_use_labels

Replace numeric codes with value labels for presentation, retaining column names. Keep original numeric tables for indicator calculation.

```python
endompy.enhogar.use_labels(tbl, vars=None, edition=None, version=None, at=None, con=None, module='all')
```

R implementation:

```r
{
    x <- ehg_set_labels(tbl, vars, edition, version, at, con, module)
    if (!is.null(vars)) 
        vars <- intersect(vars, names(x))
    labeler::with_Dict(x, subset = vars, use_label = FALSE, use_labels = TRUE)
}
```

## enhogar_edition

Set the ENHOGAR_EDITION option correctly; NULL resets it. Editions 2018 and 2022 are implemented. This is distinct from dictionary revisions.

```python
endompy.enhogar.enhogar_edition(year)
```

R implementation:

```r
{
    old <- getOption("ENHOGAR_EDITION")
    options(ENHOGAR_EDITION = if (is.null(year)) 
        NULL
    else .ehg_year(year))
    invisible(old)
}
```

## enhogar_example

Return twelve entirely invented local cases for edition 2018 (default) or 2022. No respondent records or weights are included; the example cannot estimate national statistics.

```python
endompy.enhogar.enhogar_example(edition=2018)
```

R implementation:

```r
{
    .ehg_year(edition)
    file <- if (edition == 2018) 
        "synthetic.json"
    else "synthetic-2022.json"
    jsonlite::fromJSON(system.file("examples", file, package = "enhogar"))
}
```

## get_enhogar_edition

Resolve 2018 or 2022 from questionnaire columns, compatible interview years and configuration without changing options. HANO allows 2021/2022 for edition 2022; 2018 remains the fallback when no evidence is available.

```python
endompy.enhogar.get_enhogar_edition(tbl=None)
```

R implementation:

```r
.ehg_edition(tbl)
```

## guess_enhogar_edition

Infer 2018/2022 from distinctive questionnaire columns, including empty tables, or unambiguous HANO evidence. Mixed questionnaires and incompatible or missing years raise errors. HANO=2021 alone requires explicit edition selection.

```python
endompy.enhogar.guess_enhogar_edition(tbl)
```

R implementation:

```r
{
    observed <- .ehg_evidence(tbl)
    if (is.null(observed)) 
        stop("Cannot infer edition; supply questionnaire columns or specify edition", call. = FALSE)
    .ehg_edition(tbl, observed)
}
```

