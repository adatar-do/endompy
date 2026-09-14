# Economic activity groups

```python
encftr.grupo_rama_pib(tbl)
```

Calculates economic activity groups. Returns a copy with calculated columns and preserves input rows. 

[Contract and complete example](../indicadores.md).

| Parameter | Default | Contract |
|---|---|---|
| tbl | — | Local table of person responses with original ENCFT names and codes. |

Columns referenced by calculation rules: `CATEGORIA_PRINCIPAL`, `GRUPO_RAMA`, `RAMA_PRINCIPAL_COD`.

Calculation rules from the equivalent R implementation:

```r
grupo_rama_pib = case_when(((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "sin rama de actividad")) ~ NA), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Agr.c")) ~ 1), (((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Industr")) & (CATEGORIA_PRINCIPAL == 4)) ~ 3), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Industr")) ~ 4), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Electric")) ~ 6), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Constr")) ~ 5), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Comerc")) ~ 7), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Transp")) ~ 9), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Hoteles")) ~ 8), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "financ")) ~ 11), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "p.blica y def")) ~ 16), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Ense.anza")) ~ 13), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Salud")) ~ 14), ((is.na(RAMA_PRINCIPAL_COD) & str_detect(GRUPO_RAMA, "Otros")) ~ 17), (between(RAMA_PRINCIPAL_COD, 111, 322) ~ 1), (between(RAMA_PRINCIPAL_COD, 510, 990) ~ 2), ((between(RAMA_PRINCIPAL_COD, 1010, 3320) & (CATEGORIA_PRINCIPAL == 4)) ~ 3), ((between(RAMA_PRINCIPAL_COD, 1010, 3320) & (CATEGORIA_PRINCIPAL != 4)) ~ 4), (between(RAMA_PRINCIPAL_COD, 3510, 3900) ~ 6), (between(RAMA_PRINCIPAL_COD, 4100, 4390) ~ 5), (between(RAMA_PRINCIPAL_COD, 4510, 4799) ~ 7), (between(RAMA_PRINCIPAL_COD, 4911, 5320) ~ 9), (between(RAMA_PRINCIPAL_COD, 5510, 5630) ~ 8), (between(RAMA_PRINCIPAL_COD, 5811, 6399) ~ 10), (between(RAMA_PRINCIPAL_COD, 6411, 6630) ~ 11), (between(RAMA_PRINCIPAL_COD, 6810, 6820) ~ 12), (between(RAMA_PRINCIPAL_COD, 6910, 8299) ~ 15), (between(RAMA_PRINCIPAL_COD, 8411, 8430) ~ 16), (between(RAMA_PRINCIPAL_COD, 8510, 8550) ~ 13), (between(RAMA_PRINCIPAL_COD, 8610, 8890) ~ 14), (between(RAMA_PRINCIPAL_COD, 9000, 9900) ~ 17))
```

Equivalent ftc_* names are listed in api-parity.json. Functions accepting tbl are also EncftDataFrame methods.
