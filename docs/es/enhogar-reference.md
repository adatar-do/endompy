# Referencia API ENHOGAR

Las 20 funciones públicas de R tienen equivalentes Python. [Contratos laborales](enhogar-indicadores.md) · [Revisiones](enhogar-diccionario.md).

## ehg_browse_dict

Devuelve un widget o tabla en R; en Python devuelve una tabla pandas.

```python
endompy.enhogar.browse_dict(edition=2018, version=None, at=None, con=None, module='all')
```

Implementación R:

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

Entre no ocupados conocidos, H507=1 es la aproximación de 2018 y P508=1 es búsqueda de cuatro semanas en 2022. P507 no mide búsqueda. Los saltos de P508 no exigen disponibilidad. No certifica agregados oficiales.

```python
endompy.enhogar.desocupado(tbl, min_edad=15, max_edad=inf, edition=None)
```

Implementación R:

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

2018 conserva baseline-1 (447 definiciones); 2022 all selecciona coverage-2 (603 definiciones) y conserva baseline-1. Los cinco módulos completos usan redatam-1. No se inventan vigencias.

```python
endompy.enhogar.get_dict(edition=2018, version=None, at=None, con=None, module='all')
```

Implementación R:

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

Implementación R:

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

Lista identificadores, padres, intervalos y hashes de las revisiones.

```python
endompy.enhogar.dict_versions(edition=2018, con=None, module='all')
```

Implementación R:

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

Implementación R:

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

Aproximación de disponibilidad fuera de PEA con H509/H510 (2018) o P510/P511 (2022). No interpreta estas preguntas como deseo de trabajar.

```python
endompy.enhogar.fuerza_trabajo_potencial(tbl, min_edad=15, max_edad=inf, edition=None)
```

Implementación R:

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

Complemento de PEA conocida dentro de PET. Corrige la referencia inexistente pea_abierta.

```python
endompy.enhogar.inactivo(tbl, min_edad=15, max_edad=inf, edition=None)
```

Implementación R:

```r
{
    edition <- .ehg_edition(tbl, edition)
    tbl <- ehg_pea(tbl, min_edad, max_edad, edition)
    tbl$inactivo <- .ehg_mask(tbl$pea == 0, tbl$pet)
    tbl
}
```

## ehg_ocupado

Algún sí en H501:H506 (2018) o P501:P506 (2022) establece ocupación; seis no establecen cero. Los demás casos permanecen desconocidos.

```python
endompy.enhogar.ocupado(tbl, min_edad=15, max_edad=inf, edition=None)
```

Implementación R:

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

Unión de ocupado y desocupado según edición; conserva los faltantes necesarios.

```python
endompy.enhogar.pea(tbl, min_edad=15, max_edad=inf, edition=None)
```

Implementación R:

```r
{
    edition <- .ehg_edition(tbl, edition)
    tbl <- ehg_desocupado(tbl, min_edad, max_edad, edition)
    tbl$pea <- .ehg_mask(tbl$ocupado == 1 | tbl$desocupado == 1, tbl$pet)
    tbl
}
```

## ehg_pet

Calcula PET con H203 en 2018 o P203 en 2022. Edad 99 es desconocida solo en 2018; válida en 2022. Umbrales inclusivos y analíticos.

```python
endompy.enhogar.pet(tbl, min_edad=15, max_edad=inf, edition=None)
```

Implementación R:

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

Registra una revisión completa compartiendo definiciones sin cambios; una modificación reutiliza 446 definiciones en 2018 o 29 en la revisión inicial 2022; las revisiones ampliadas también reutilizan definiciones.

```python
endompy.enhogar.register_dict(con, dictionary, version, edition=2018, valid_from=None, valid_to=None, module='all', **kwargs)
```

Implementación R:

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

Alias obsoleto. Adjunta etiquetas y procedencia sin cambiar los códigos numéricos.

```python
endompy.enhogar.setLabels(tbl, vars=None, edition=None, version=None, at=None, con=None, module='all')
```

Implementación R:

```r
{
    lifecycle::deprecate_warn("0.1.0", "ehg_setLabels()", "ehg_set_labels()")
    ehg_set_labels(tbl, vars, edition, version, at, con, module)
}
```

## ehg_set_labels

Adjunta etiquetas y procedencia sin cambiar los códigos numéricos.

```python
endompy.enhogar.set_labels(tbl, vars=None, edition=None, version=None, at=None, con=None, module='all')
```

Implementación R:

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

Alias obsoleto. Sustituye códigos por etiquetas para presentación conservando los nombres de columnas.

```python
endompy.enhogar.useLabels(tbl, vars=None, edition=None, version=None, at=None, con=None, module='all')
```

Implementación R:

```r
{
    lifecycle::deprecate_warn("0.1.0", "ehg_useLabels()", "ehg_use_labels()")
    ehg_use_labels(tbl, vars, edition, version, at, con, module)
}
```

## ehg_use_labels

Sustituye códigos por etiquetas para presentación conservando los nombres de columnas.

```python
endompy.enhogar.use_labels(tbl, vars=None, edition=None, version=None, at=None, con=None, module='all')
```

Implementación R:

```r
{
    x <- ehg_set_labels(tbl, vars, edition, version, at, con, module)
    if (!is.null(vars)) 
        vars <- intersect(vars, names(x))
    labeler::with_Dict(x, subset = vars, use_label = FALSE, use_labels = TRUE)
}
```

## enhogar_edition

Configura 2018/2022 o restablece con None; Python usa configuración local al contexto.

```python
endompy.enhogar.enhogar_edition(year)
```

Implementación R:

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

Devuelve doce casos inventados para 2018 (predeterminado) o 2022; no sirven para estimaciones nacionales.

```python
endompy.enhogar.enhogar_example(edition=2018)
```

Implementación R:

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

Resuelve 2018/2022 por estructura, años de entrevista y opción sin modificarla. 2018 sigue como valor de compatibilidad sin evidencia.

```python
endompy.enhogar.get_enhogar_edition(tbl=None)
```

Implementación R:

```r
.ehg_edition(tbl)
```

## guess_enhogar_edition

Infiere por columnas de cuestionario, incluso tablas vacías, o años de entrevista inequívocos. Rechaza mezclas, conflictos y faltantes; HANO=2021 solo requiere edición explícita.

```python
endompy.enhogar.guess_enhogar_edition(tbl)
```

Implementación R:

```r
{
    observed <- .ehg_evidence(tbl)
    if (is.null(observed)) 
        stop("Cannot infer edition; supply questionnaire columns or specify edition", call. = FALSE)
    .ehg_edition(tbl, observed)
}
```

