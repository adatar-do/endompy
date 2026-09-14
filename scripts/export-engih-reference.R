# Fresh executable R oracle. Run from the ENDOM workspace.
source("engihr/scripts/bootstrap.R")
.libPaths(c(Sys.getenv("ENGIHR_ORACLE_LIBRARY", "artifacts/endom-closure-release/engihr/package/source-installed"), .libPaths()))
library(engihr)
stopifnot(as.character(packageVersion("engihr")) == "0.3.0")
destination <- Sys.getenv("ENGIHR_ORACLE_OUTPUT", "endompy/tests/fixtures/engih-full")
dir.create(destination, recursive = TRUE, showWarnings = FALSE)
report <- list(r = as.character(getRversion()), package = "engihr", version = "0.3.0", modules = list())
for (module in egi_modules()$module) {
  dict <- egi_dict(module)
  variables <- setdiff(names(dict), "metadata")
  values <- lapply(dict[variables], function(v) {
    if (is.null(v$labels)) return(c(1, 2, 3, NA_real_))
    codes <- unname(unlist(v$labels))
    unknown <- if (is.numeric(codes)) max(codes) + 7777 else "__unknown__"
    c(codes, unknown, NA)
  })
  n <- max(c(4L, lengths(values)))
  x <- as.data.frame(lapply(values, rep_len, length.out = n), check.names = FALSE)
  if (!length(values)) x <- data.frame(row.names = seq_len(n))
  x$synthetic_id <- paste0("invented-", seq_len(n))
  labelled <- egi_set_labels(x, dict, module = module)
  presented <- egi_use_labels(x, dict, module = module)
  for (name in names(x)) stopifnot(identical(as.vector(x[[name]]), as.vector(labelled[[name]])))
  expected <- list(module = module, n = n, input = x,
    display = as.data.frame(lapply(presented, function(v) if (is.factor(v)) as.character(v) else as.vector(v)), check.names = FALSE),
    levels = lapply(presented[vapply(presented, is.factor, logical(1))], levels),
    labels = lapply(dict[variables], function(v) v$label),
    validation = egi_validate(x, dict, module = module), provenance = attr(labelled, "labeler_provenance"),
    revision = labeler::dict_revision(dict), schema = egi_schema(module))
  jsonlite::write_json(expected, file.path(destination, paste0(module, ".json")),
    auto_unbox = TRUE, na = "null", null = "null", dataframe = "columns", digits = NA, pretty = FALSE)
  report$modules[[module]] <- list(rows = n, definitions = length(variables),
    categorical_fields = sum(vapply(presented, is.factor, logical(1))))
}
jsonlite::write_json(list(modules = egi_modules(), issues = egi_source_issues(),
  catalogs = setNames(lapply(c("variedades", "unidades", "establecimientos", "paises", "monedas"), egi_catalog),
    c("variedades", "unidades", "establecimientos", "paises", "monedas"))),
  file.path(destination, "metadata.json"), auto_unbox = TRUE, dataframe = "columns", na = "null", digits = NA)
jsonlite::write_json(report, file.path(destination, "report.json"), auto_unbox = TRUE, pretty = TRUE)
cat("Exported 25 fresh R oracle cases with every available value code, an unknown code and NA\n")
