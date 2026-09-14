# ENFT API reference

All public R functions are mapped below. Database configuration and the pipe operator are native R interfaces. Python calculations require no R runtime.

## ft_alfabeta

Literacy status

```python
ft.ft_alfabeta(tbl, min_edad=15)
```

Literacy status. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_ALFABETISMO`, `EFT_EDAD`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    ft_check_age(min_edad)
    EFT_ALFABETISMO <- NULL
    tbl %>% dplyr::mutate(alfabeta = dplyr::case_when(EFT_EDAD >= min_edad & EFT_ALFABETISMO %in% 1:2 ~ 
        EFT_ALFABETISMO))
}
```

</details>

## ft_ano

Validate and extract the semiannual period

```python
ft.ft_ano(tbl)
```

Validate and extract the semiannual period. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO or PERIALFA`.

## ft_anos_educacion

Years of education

```python
ft.ft_anos_educacion(tbl)
```

Years of education. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_EDAD`, `EFT_ULT_ANO_APROBADO`, `EFT_ULT_NIVEL_ALCANZADO`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    EFT_EDAD <- NULL
    EFT_ULT_NIVEL_ALCANZADO <- NULL
    EFT_ULT_ANO_APROBADO <- NULL
    tbl %>% dplyr::mutate(anos_educacion = dplyr::case_when(EFT_EDAD <= 3 ~ NA_integer_, EFT_ULT_NIVEL_ALCANZADO %in% 
        c(1, 7) ~ 0, EFT_ULT_NIVEL_ALCANZADO == 2 ~ EFT_ULT_ANO_APROBADO, EFT_ULT_NIVEL_ALCANZADO %in% 
        c(3, 4) ~ 8 + EFT_ULT_ANO_APROBADO, EFT_ULT_NIVEL_ALCANZADO == 5 ~ 12 + EFT_ULT_ANO_APROBADO, 
        EFT_ULT_NIVEL_ALCANZADO == 6 ~ 16 + EFT_ULT_ANO_APROBADO))
}
```

</details>

## ft_browse_dict

Browse a dictionary as a table or widget

```python
ft.ft_browse_dict(version=None, at=None, con=None)
```

Browse a dictionary as a table or widget. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_cantidad_personas_trabajan

Harmonized workplace size

```python
ft.ft_cantidad_personas_trabajan(tbl)
```

Harmonized workplace size. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_CANT_PERS_TRAB`, `EFT_PERIODO or PERIALFA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_peri_vars() %>% dplyr::mutate(cantidad_personas_trabajan = dplyr::case_when(ano >= 2004 & 
        EFT_CANT_PERS_TRAB %in% 1:2 ~ 1, ano >= 2004 & EFT_CANT_PERS_TRAB %in% 3:4 ~ EFT_CANT_PERS_TRAB - 
        1, ano >= 2004 & EFT_CANT_PERS_TRAB >= 5 ~ 4, EFT_CANT_PERS_TRAB != 0 ~ EFT_CANT_PERS_TRAB))
}
```

</details>

## ft_categoria_ocupacion_principal

Harmonized main-job occupational category

```python
ft.ft_categoria_ocupacion_principal(tbl)
```

Harmonized main-job occupational category. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_CATEGORIA_OCUP_PRINC`, `EFT_PERIODO or PERIALFA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_peri_vars() %>% dplyr::mutate(categoria_ocupacion_principal = dplyr::case_when(dplyr::between(ano, 
        2000, 2004) & EFT_CATEGORIA_OCUP_PRINC %in% 7:8 ~ 7, dplyr::between(ano, 2000, 2004) & EFT_CATEGORIA_OCUP_PRINC %in% 
        9:10 ~ 8, TRUE ~ EFT_CATEGORIA_OCUP_PRINC))
}
```

</details>

## ft_compute_ano

Validate and extract the semiannual period

```python
ft.ft_compute_ano(tbl)
```

Validate and extract the semiannual period. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO or PERIALFA`.

## ft_compute_peri_vars

Validate and extract the semiannual period

```python
ft.ft_compute_peri_vars(tbl, rm=False, ano=True, semestre=True, periodo=True)
```

Validate and extract the semiannual period. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO or PERIALFA`.

## ft_compute_zona

Residence zone

```python
ft.ft_compute_zona(tbl)
```

Residence zone. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO + EFT_ZONA or PERIALFA + S1_P4`.

## ft_dbConnect

Connect using the requested Dmisc database name

Use user-owned Python database tooling and provide a pandas DataFrame. No automatic Dmisc profile translation is performed.

Connect using the requested Dmisc database name. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_db_connect

Connect using the requested Dmisc database name

Use user-owned Python database tooling and provide a pandas DataFrame. No automatic Dmisc profile translation is performed.

Connect using the requested Dmisc database name. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_desempleo_abierto

Open unemployment

```python
ft.ft_desempleo_abierto(tbl, min_edad=15)
```

Open unemployment. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% dplyr::mutate(desempleo_abierto = dplyr::case_when(ocupado == 1 ~ 
        0, pet == 1 & EFT_BUSCO_TRAB_SEM_ANT == 1 ~ 1, pet == 1 & EFT_BUSCO_TRAB_MES_ANT == 1 ~ 1, ocupado == 
        1 ~ 0))
}
```

</details>

## ft_desempleo_ampliado

Expanded unemployment

```python
ft.ft_desempleo_ampliado(tbl, min_edad=15)
```

Expanded unemployment. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_desempleo_abierto(min_edad) %>% dplyr::mutate(desempleo_ampliado = dplyr::case_when(ocupado == 
        1 ~ 0, desempleo_abierto == 1 ~ 1, EFT_TIENE_COND_JORNADA == 1 ~ 1, ocupado == 1 ~ 0), desempleo_ampliado = dplyr::case_when(pet == 
        1 ~ desempleo_ampliado))
}
```

</details>

## ft_desempleo_cesante_abierto

Open unemployment among previous workers

```python
ft.ft_desempleo_cesante_abierto(tbl, min_edad=15)
```

Open unemployment among previous workers. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_ANTES`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_desempleo_abierto(min_edad) %>% dplyr::mutate(desempleo_cesante_abierto = dplyr::case_when(desempleo_abierto == 
        1 & EFT_TRABAJO_ANTES == 1 ~ 1, desempleo_abierto == 1 ~ 0))
}
```

</details>

## ft_desempleo_cesante_ampliado

Expanded unemployment among previous workers

```python
ft.ft_desempleo_cesante_ampliado(tbl, min_edad=15)
```

Expanded unemployment among previous workers. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_ANTES`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_desempleo_ampliado(min_edad) %>% dplyr::mutate(desempleo_cesante_ampliado = dplyr::case_when(desempleo_ampliado == 
        1 & EFT_TRABAJO_ANTES != 1 ~ 0, desempleo_ampliado == 1 ~ 1))
}
```

</details>

## ft_desempleo_nuevo_abierto

Open unemployment among new entrants

```python
ft.ft_desempleo_nuevo_abierto(tbl, min_edad=15)
```

Open unemployment among new entrants. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_ANTES`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_desempleo_abierto(min_edad) %>% dplyr::mutate(desempleo_nuevo_abierto = dplyr::case_when(desempleo_abierto == 
        1 & EFT_TRABAJO_ANTES != 1 ~ 1, desempleo_abierto == 1 ~ 0))
}
```

</details>

## ft_desempleo_nuevo_ampliado

Expanded unemployment among new entrants

```python
ft.ft_desempleo_nuevo_ampliado(tbl, min_edad=15)
```

Expanded unemployment among new entrants. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_ANTES`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_desempleo_ampliado(min_edad) %>% dplyr::mutate(desempleo_nuevo_ampliado = dplyr::case_when(desempleo_ampliado == 
        1 & EFT_TRABAJO_ANTES == 1 ~ 0, desempleo_ampliado == 1 ~ 1))
}
```

</details>

## ft_dias_semana_ocupacion_principal

Main-job working days per week

```python
ft.ft_dias_semana_ocupacion_principal(tbl)
```

Main-job working days per week. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_DIAS_SEM_OCUP_PRINC`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(dias_semana_ocupacion_principal = dplyr::case_when(EFT_DIAS_SEM_OCUP_PRINC > 
        0 ~ EFT_DIAS_SEM_OCUP_PRINC))
}
```

</details>

## ft_dict

Select an immutable dictionary revision

```python
ft.ft_dict(version=None, at=None, con=None)
```

Select an immutable dictionary revision. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_dict_versions

List dictionary revisions

```python
ft.ft_dict_versions(con=None)
```

List dictionary revisions. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_dominios_inferencia

Period-specific inference domains

```python
ft.ft_dominios_inferencia(tbl)
```

Period-specific inference domains. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO + EFT_ZONA or PERIALFA + S1_P4`, `EFT_PERIODO or PERIALFA`, `EFT_PROVINCIA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    dominios_inferencia1 <- NULL
    dominios_inferencia2 <- NULL
    dominios_inferencia3 <- NULL
    tbl %>% ft_peri_vars() %>% ft_dominios_inferencia1() %>% ft_dominios_inferencia2() %>% ft_dominios_inferencia3() %>% 
        dplyr::mutate(dominios_inferencia = dplyr::case_when(dplyr::between(periodo, 20001, 20031) ~ 
            dominios_inferencia1, dplyr::between(periodo, 20032, 20072) & dominios_inferencia2 == 1 ~ 
            1, dplyr::between(periodo, 20032, 20072) ~ dominios_inferencia2 + 2, dplyr::between(periodo, 
            20081, 20162) ~ dominios_inferencia3 + 11))
}
```

</details>

## ft_dominios_inferencia1

Inference domains for 2000/1 to 2003/1

```python
ft.ft_dominios_inferencia1(tbl)
```

Inference domains for 2000/1 to 2003/1. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO + EFT_ZONA or PERIALFA + S1_P4`, `EFT_PROVINCIA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_zona() %>% dplyr::mutate(dominios_inferencia1 = dplyr::case_when(EFT_PROVINCIA %in% c(1, 
        32) ~ 1, zona == 1 ~ 2, zona == 2 ~ 3))
}
```

</details>

## ft_dominios_inferencia2

Inference domains for 2003/2 to 2007/2

```python
ft.ft_dominios_inferencia2(tbl)
```

Inference domains for 2003/2 to 2007/2. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PROVINCIA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    regiones_desarrollo_685_00 <- NULL
    tbl %>% ft_regiones_desarrollo_685_00() %>% dplyr::mutate(dominios_inferencia2 = regiones_desarrollo_685_00)
}
```

</details>

## ft_dominios_inferencia3

Inference domains from 2008/1

```python
ft.ft_dominios_inferencia3(tbl)
```

Inference domains from 2008/1. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PROVINCIA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(dominios_inferencia3 = dplyr::case_when(EFT_PROVINCIA == 1 ~ 1, EFT_PROVINCIA == 
        32 ~ 2, EFT_PROVINCIA == 25 ~ 3, EFT_PROVINCIA == 9 ~ 4, EFT_PROVINCIA == 18 ~ 5, EFT_PROVINCIA == 
        13 ~ 6, EFT_PROVINCIA == 24 ~ 7, EFT_PROVINCIA == 28 ~ 7, EFT_PROVINCIA == 6 ~ 8, EFT_PROVINCIA == 
        14 ~ 9, EFT_PROVINCIA == 20 ~ 10, EFT_PROVINCIA == 19 ~ 11, EFT_PROVINCIA == 27 ~ 12, EFT_PROVINCIA == 
        5 ~ 13, EFT_PROVINCIA == 15 ~ 13, EFT_PROVINCIA == 26 ~ 13, EFT_PROVINCIA == 21 ~ 14, EFT_PROVINCIA == 
        2 ~ 15, EFT_PROVINCIA == 17 ~ 15, EFT_PROVINCIA == 31 ~ 15, EFT_PROVINCIA == 22 ~ 16, EFT_PROVINCIA == 
        7 ~ 17, EFT_PROVINCIA == 4 ~ 18, EFT_PROVINCIA == 3 ~ 19, EFT_PROVINCIA == 10 ~ 19, EFT_PROVINCIA == 
        16 ~ 19, EFT_PROVINCIA == 23 ~ 20, EFT_PROVINCIA == 29 ~ 21, EFT_PROVINCIA == 30 ~ 21, EFT_PROVINCIA == 
        12 ~ 22, EFT_PROVINCIA == 11 ~ 23, EFT_PROVINCIA == 8 ~ 24))
}
```

</details>

## ft_grupo_ocupacion

Occupational group

```python
ft.ft_grupo_ocupacion(tbl, min_edad=15)
```

Occupational group. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_OCUPACION_PRINC`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_pea_ampliada(min_edad) %>% dplyr::mutate(grupo_ocupacion = dplyr::case_when(EFT_OCUPACION_PRINC < 
        12 ~ 5, dplyr::between(EFT_OCUPACION_PRINC, 12, 199) ~ 1, EFT_OCUPACION_PRINC < 300 ~ 2, EFT_OCUPACION_PRINC < 
        400 ~ 3, EFT_OCUPACION_PRINC < 500 ~ 4, EFT_OCUPACION_PRINC < 600 ~ 5, EFT_OCUPACION_PRINC < 
        700 ~ 6, EFT_OCUPACION_PRINC < 800 ~ 7, EFT_OCUPACION_PRINC < 900 ~ 8, EFT_OCUPACION_PRINC > 
        900 ~ 9, pea_ampliada == 1 ~ 10))
}
```

</details>

## ft_grupo_rama

Economic activity group

```python
ft.ft_grupo_rama(tbl)
```

Economic activity group. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_RAMA_PRINC`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(grupo_rama = dplyr::case_when(EFT_RAMA_PRINC < 100 ~ 1, EFT_RAMA_PRINC < 150 ~ 
        2, EFT_RAMA_PRINC < 400 ~ 3, EFT_RAMA_PRINC < 450 ~ 4, EFT_RAMA_PRINC < 500 ~ 5, EFT_RAMA_PRINC < 
        550 ~ 6, EFT_RAMA_PRINC < 600 ~ 7, EFT_RAMA_PRINC < 650 ~ 8, EFT_RAMA_PRINC < 700 ~ 9, EFT_RAMA_PRINC < 
        750 ~ 11, EFT_RAMA_PRINC < 800 ~ 10, EFT_RAMA_PRINC >= 800 ~ 11))
}
```

</details>

## ft_horas_semanal

Weekly hours worked

```python
ft.ft_horas_semanal(tbl, min_edad=15)
```

Weekly hours worked. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_CATEGORIA_OCUP_PRINC`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_perceptores_ingresos(min_edad) %>% dplyr::mutate(horas_semanal = dplyr::case_when(EFT_HORAS_SEM_OCUP_PRINC > 
        0 & perceptores_ingresos == 1 ~ EFT_HORAS_SEM_OCUP_PRINC))
}
```

</details>

## ft_ing_alqui_renta_propiedades

Income: domestic property rent

```python
ft.ft_ing_alqui_renta_propiedades(tbl)
```

Compute domestic property rent using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_MONTO_ALQUILER_ING_NAC`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    EFT_MONTO_ALQUILER_ING_NAC <- NULL
    tbl %>% dplyr::mutate(ing_alqui_renta_propiedades = dplyr::if_else(is.na(EFT_MONTO_ALQUILER_ING_NAC), 
        0, EFT_MONTO_ALQUILER_ING_NAC))
}
```

</details>

## ft_ing_alquiler_anual

Income: annual rent converted to monthly

```python
ft.ft_ing_alquiler_anual(tbl)
```

Compute annual rent converted to monthly using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ANIO_PASADO_MONTO_ALQUILER`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_alquiler_anual = dplyr::case_when(is.na(EFT_ANIO_PASADO_MONTO_ALQUILER) ~ 
        0, TRUE ~ EFT_ANIO_PASADO_MONTO_ALQUILER/12))
}
```

</details>

## ft_ing_ayuda_gobierno

Income: government assistance

```python
ft.ft_ing_ayuda_gobierno(tbl)
```

Compute government assistance using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_MONTO_GOBIERNO_ING_NAC`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    EFT_MONTO_GOBIERNO_ING_NAC <- NULL
    tbl %>% dplyr::mutate(ing_ayuda_gobierno = dplyr::if_else(is.na(EFT_MONTO_GOBIERNO_ING_NAC), 0, EFT_MONTO_GOBIERNO_ING_NAC))
}
```

</details>

## ft_ing_beneficios_marginales

Income: fringe benefits

```python
ft.ft_ing_beneficios_marginales(tbl)
```

Compute fringe benefits using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ULT_DOCE_BENEFICIOS_MARG`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_beneficios_marginales = dplyr::case_when(is.na(EFT_ULT_DOCE_BENEFICIOS_MARG) ~ 
        0, TRUE ~ EFT_ULT_DOCE_BENEFICIOS_MARG/12))
}
```

</details>

## ft_ing_bonificaciones

Income: bonuses

```python
ft.ft_ing_bonificaciones(tbl)
```

Compute bonuses using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ULT_DOCE_BONIFICACION`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_bonificaciones = dplyr::case_when(is.na(EFT_ULT_DOCE_BONIFICACION) ~ 0, 
        TRUE ~ EFT_ULT_DOCE_BONIFICACION/12))
}
```

</details>

## ft_ing_comisiones

Income: commissions

```python
ft.ft_ing_comisiones(tbl)
```

Compute commissions using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_MES_PASADO_COMISIONES`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_comisiones = dplyr::case_when(is.na(EFT_MES_PASADO_COMISIONES) ~ 0, TRUE ~ 
        EFT_MES_PASADO_COMISIONES))
}
```

</details>

## ft_ing_dividendos

Income: dividends

```python
ft.ft_ing_dividendos(tbl)
```

Compute dividends using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ULT_DOCE_DIVIDENDOS`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_dividendos = dplyr::case_when(is.na(EFT_ULT_DOCE_DIVIDENDOS) ~ 0, TRUE ~ 
        EFT_ULT_DOCE_DIVIDENDOS/12))
}
```

</details>

## ft_ing_especie_alimentos

Income: in-kind food

```python
ft.ft_ing_especie_alimentos(tbl)
```

Compute in-kind food using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PAGO_ALIMENTOS_MONTO`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_alimentos = dplyr::case_when(is.na(EFT_PAGO_ALIMENTOS_MONTO) ~ 
        0, !is.na(EFT_PAGO_ALIMENTOS_MONTO) ~ EFT_PAGO_ALIMENTOS_MONTO))
}
```

</details>

## ft_ing_especie_auto

Income: self-produced consumption

```python
ft.ft_ing_especie_auto(tbl)
```

Compute self-produced consumption using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_BIENES_CONSUMO_ANUAL`, `EFT_BIENES_CONSUMO_MENSUAL`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    EFT_BIENES_CONSUMO_MENSUAL <- NULL
    EFT_BIENES_CONSUMO_ANUAL <- NULL
    tbl %>% dplyr::mutate(ing_especie_auto = dplyr::if_else(is.na(EFT_BIENES_CONSUMO_MENSUAL), 0, EFT_BIENES_CONSUMO_MENSUAL) + 
        dplyr::if_else(is.na(EFT_BIENES_CONSUMO_ANUAL), 0, EFT_BIENES_CONSUMO_ANUAL)/12)
}
```

</details>

## ft_ing_especie_ayuda_ong

Income: family, employer, government and NGO assistance

```python
ft.ft_ing_especie_ayuda_ong(tbl)
```

Compute family, employer, government and NGO assistance using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_AYUDA_FAMILIARES_ANUAL`, `EFT_AYUDA_FAMILIARES_MENSUAL`, `EFT_ESPECIE_EMPRESAS_ANO_VAL`, `EFT_ESPECIE_EMPRESAS_MES_VAL`, `EFT_ESPECIE_FAMILIARES_ANO_VAL`, `EFT_ESPECIE_FAMILIARES_MES_VAL`, `EFT_ESPECIE_GOBIERNO_ANO_VAL`, `EFT_ESPECIE_GOBIERNO_MES_VAL`, `EFT_ESPECIE_OTROS_VAL`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    EFT_AYUDA_FAMILIARES_ANUAL <- NULL
    EFT_AYUDA_FAMILIARES_MENSUAL <- NULL
    EFT_ESPECIE_FAMILIARES_ANO_VAL <- NULL
    EFT_ESPECIE_FAMILIARES_MES_VAL <- NULL
    EFT_ESPECIE_EMPRESAS_ANO_VAL <- NULL
    EFT_ESPECIE_EMPRESAS_MES_VAL <- NULL
    EFT_ESPECIE_GOBIERNO_ANO_VAL <- NULL
    EFT_ESPECIE_GOBIERNO_MES_VAL <- NULL
    EFT_ESPECIE_OTROS_VAL <- NULL
    ing_ayuda_familiares <- NULL
    ing_ayuda_especie_familiares <- NULL
    ing_ayuda_especie_empresas <- NULL
    ing_ayuda_especie_gob <- NULL
    ing_ayuda_especie_otros <- NULL
    tbl %>% dplyr::mutate(ing_ayuda_familiares = dplyr::if_else(dplyr::if_else(is.na(EFT_AYUDA_FAMILIARES_ANUAL), 
        0, EFT_AYUDA_FAMILIARES_ANUAL) == (dplyr::if_else(is.na(EFT_AYUDA_FAMILIARES_MENSUAL), 0, EFT_AYUDA_FAMILIARES_MENSUAL) * 
        12), dplyr::if_else(is.na(EFT_AYUDA_FAMILIARES_MENSUAL), 0, EFT_AYUDA_FAMILIARES_MENSUAL), dplyr::if_else(is.na(EFT_AYUDA_FAMILIARES_MENSUAL), 
        0, EFT_AYUDA_FAMILIARES_MENSUAL) + dplyr::if_else(is.na(EFT_AYUDA_FAMILIARES_ANUAL), 0, EFT_AYUDA_FAMILIARES_ANUAL)/12), 
        ing_ayuda_especie_familiares = dplyr::if_else(dplyr::if_else(is.na(EFT_ESPECIE_FAMILIARES_ANO_VAL), 
            0, EFT_ESPECIE_FAMILIARES_ANO_VAL) == (dplyr::if_else(is.na(EFT_ESPECIE_FAMILIARES_MES_VAL), 
            0, EFT_ESPECIE_FAMILIARES_MES_VAL) * 12), dplyr::if_else(is.na(EFT_ESPECIE_FAMILIARES_MES_VAL), 
            0, EFT_ESPECIE_FAMILIARES_MES_VAL), dplyr::if_else(is.na(EFT_ESPECIE_FAMILIARES_MES_VAL), 
            0, EFT_ESPECIE_FAMILIARES_MES_VAL) + dplyr::if_else(is.na(EFT_ESPECIE_FAMILIARES_ANO_VAL), 
            0, EFT_ESPECIE_FAMILIARES_ANO_VAL)/12), ing_ayuda_especie_empresas = dplyr::if_else(dplyr::if_else(is.na(EFT_ESPECIE_EMPRESAS_ANO_VAL), 
            0, EFT_ESPECIE_EMPRESAS_ANO_VAL) == (dplyr::if_else(is.na(EFT_ESPECIE_EMPRESAS_MES_VAL), 
            0, EFT_ESPECIE_EMPRESAS_MES_VAL) * 12), dplyr::if_else(is.na(EFT_ESPECIE_EMPRESAS_MES_VAL), 
            0, EFT_ESPECIE_EMPRESAS_MES_VAL), dplyr::if_else(is.na(EFT_ESPECIE_EMPRESAS_MES_VAL), 0, 
            EFT_ESPECIE_EMPRESAS_MES_VAL) + dplyr::if_else(is.na(EFT_ESPECIE_EMPRESAS_ANO_VAL), 0, EFT_ESPECIE_EMPRESAS_ANO_VAL)/12), 
        ing_ayuda_especie_gob = dplyr::if_else(dplyr::if_else(is.na(EFT_ESPECIE_GOBIERNO_ANO_VAL), 0, 
            EFT_ESPECIE_GOBIERNO_ANO_VAL) == (dplyr::if_else(is.na(EFT_ESPECIE_GOBIERNO_MES_VAL), 0, 
            EFT_ESPECIE_GOBIERNO_MES_VAL) * 12), dplyr::if_else(is.na(EFT_ESPECIE_GOBIERNO_MES_VAL), 
            0, EFT_ESPECIE_GOBIERNO_MES_VAL), dplyr::if_else(is.na(EFT_ESPECIE_GOBIERNO_MES_VAL), 0, 
            EFT_ESPECIE_GOBIERNO_MES_VAL) + dplyr::if_else(is.na(EFT_ESPECIE_GOBIERNO_ANO_VAL), 0, EFT_ESPECIE_GOBIERNO_ANO_VAL)/12), 
        ing_ayuda_especie_otros = dplyr::if_else(is.na(EFT_ESPECIE_OTROS_VAL), 0, EFT_ESPECIE_OTROS_VAL), 
        ing_especie_ayuda_ong = dplyr::if_else(is.na(ing_ayuda_familiares), 0, ing_ayuda_familiares) + 
            dplyr::if_else(is.na(ing_ayuda_especie_familiares), 0, ing_ayuda_especie_familiares) + dplyr::if_else(is.na(ing_ayuda_especie_empresas), 
            0, ing_ayuda_especie_empresas) + dplyr::if_else(is.na(ing_ayuda_especie_gob), 0, ing_ayuda_especie_gob) + 
            dplyr::if_else(is.na(ing_ayuda_especie_otros), 0, ing_ayuda_especie_otros))
}
```

</details>

## ft_ing_especie_celulares

Income: in-kind mobile phones

```python
ft.ft_ing_especie_celulares(tbl)
```

Compute in-kind mobile phones using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PAGO_COMUNICACION_MONTO`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_celulares = dplyr::case_when(is.na(EFT_PAGO_COMUNICACION_MONTO) ~ 
        0, TRUE ~ EFT_PAGO_COMUNICACION_MONTO))
}
```

</details>

## ft_ing_especie_otros

Income: other in-kind earnings

```python
ft.ft_ing_especie_otros(tbl)
```

Compute other in-kind earnings using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PAGO_OTROS_MONTO`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_otros = dplyr::case_when(is.na(EFT_PAGO_OTROS_MONTO) ~ 0, TRUE ~ 
        EFT_PAGO_OTROS_MONTO))
}
```

</details>

## ft_ing_especie_transporte

Income: in-kind transport

```python
ft.ft_ing_especie_transporte(tbl)
```

Compute in-kind transport using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PAGO_TRANSPORTE_MONTO`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_transporte = dplyr::case_when(is.na(EFT_PAGO_TRANSPORTE_MONTO) ~ 
        0, TRUE ~ EFT_PAGO_TRANSPORTE_MONTO))
}
```

</details>

## ft_ing_especie_vestido

Income: in-kind clothing

```python
ft.ft_ing_especie_vestido(tbl)
```

Compute in-kind clothing using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PAGO_VESTIDO_MONTO`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_vestido = dplyr::case_when(is.na(EFT_PAGO_VESTIDO_MONTO) ~ 0, TRUE ~ 
        EFT_PAGO_VESTIDO_MONTO/12))
}
```

</details>

## ft_ing_especie_viviendas

Income: in-kind housing

```python
ft.ft_ing_especie_viviendas(tbl)
```

Compute in-kind housing using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PAGO_VIVIENDAS_MONTO`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_viviendas = dplyr::case_when(is.na(EFT_PAGO_VIVIENDAS_MONTO) ~ 
        0, TRUE ~ EFT_PAGO_VIVIENDAS_MONTO))
}
```

</details>

## ft_ing_ext_intereses_alquiler

Income: external interest and rent

```python
ft.ft_ing_ext_intereses_alquiler(tbl, ing_ext=None)
```

Compute external interest and rent using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_MONTO_ING_INTERES_MES`, `EFT_MONEDA_ING_INTERES_MES`.

## ft_ing_ext_pension

Income: external pension

```python
ft.ft_ing_ext_pension(tbl, ing_ext=None)
```

Compute external pension using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_MONTO_ING_PENSION_MES`, `EFT_MONEDA_ING_PENSION_MES`.

## ft_ing_gobierno_anual

Income: annual government assistance converted to monthly

```python
ft.ft_ing_gobierno_anual(tbl)
```

Compute annual government assistance converted to monthly using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ANIO_PASADO_MONTO_GOBIERNO`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    EFT_ANIO_PASADO_MONTO_GOBIERNO <- NULL
    tbl %>% dplyr::mutate(ing_gobierno_anual = dplyr::if_else(is.na(EFT_ANIO_PASADO_MONTO_GOBIERNO), 
        0, EFT_ANIO_PASADO_MONTO_GOBIERNO/12))
}
```

</details>

## ft_ing_horas_extras

Income: overtime

```python
ft.ft_ing_horas_extras(tbl)
```

Compute overtime using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_MES_PASADO_HORAS_EXTRAS`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_horas_extras = dplyr::case_when(is.na(EFT_MES_PASADO_HORAS_EXTRAS) ~ 0, 
        TRUE ~ EFT_MES_PASADO_HORAS_EXTRAS))
}
```

</details>

## ft_ing_imputado_vivienda_propia

Income: owner-occupied imputed rent

```python
ft.ft_ing_imputado_vivienda_propia(tbl)
```

Compute owner-occupied imputed rent using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_PARENTESCO_CON_JEFE`, `EFT_MONTO_PROBABLE_ALQ`.

## ft_ing_interes_anual

Income: annual interest converted to monthly

```python
ft.ft_ing_interes_anual(tbl)
```

Compute annual interest converted to monthly using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ANIO_PASADO_MONTO_INTERES`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_interes_anual = dplyr::case_when(is.na(EFT_ANIO_PASADO_MONTO_INTERES) ~ 
        0, TRUE ~ EFT_ANIO_PASADO_MONTO_INTERES/12))
}
```

</details>

## ft_ing_intereses_dividendo

Income: domestic interest and dividends

```python
ft.ft_ing_intereses_dividendo(tbl)
```

Compute domestic interest and dividends using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_MONTO_INTERES_ING_NAC`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_intereses_dividendo = dplyr::case_when(is.na(EFT_MONTO_INTERES_ING_NAC) ~ 
        0, TRUE ~ EFT_MONTO_INTERES_ING_NAC))
}
```

</details>

## ft_ing_ocup_prin

Income: main-job earnings

```python
ft.ft_ing_ocup_prin(tbl)
```

Compute main-job earnings using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_PRINC`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_ocup_prin = dplyr::case_when(EFT_PERIODO_ING_OCUP_PRINC == 1 ~ EFT_ING_OCUP_PRINC * 
        4.3 * EFT_HORAS_SEM_OCUP_PRINC, EFT_PERIODO_ING_OCUP_PRINC == 2 ~ EFT_ING_OCUP_PRINC * 4.3 * 
        EFT_DIAS_SEM_OCUP_PRINC, EFT_PERIODO_ING_OCUP_PRINC == 3 ~ EFT_ING_OCUP_PRINC * 4.3, EFT_PERIODO_ING_OCUP_PRINC == 
        4 ~ EFT_ING_OCUP_PRINC * 2, EFT_PERIODO_ING_OCUP_PRINC == 5 ~ EFT_ING_OCUP_PRINC, TRUE ~ 0))
}
```

</details>

## ft_ing_ocup_secun

Income: secondary-job earnings

```python
ft.ft_ing_ocup_secun(tbl)
```

Compute secondary-job earnings using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_DIAS_SEM_OCUP_SECUN`, `EFT_HORAS_SEM_OCUP_SECUN`, `EFT_ING_OCUP_SECUN`, `EFT_PERIODO or PERIALFA`, `EFT_PERIODO_ING_OCUP_SECUN`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_peri_vars() %>% dplyr::mutate(ing_ocup_secun = dplyr::case_when(ano >= 2005 ~ EFT_ING_OCUP_SECUN, 
        EFT_PERIODO_ING_OCUP_SECUN == 1 ~ EFT_ING_OCUP_SECUN * 4.3 * EFT_HORAS_SEM_OCUP_SECUN, EFT_PERIODO_ING_OCUP_SECUN == 
            2 ~ EFT_ING_OCUP_SECUN * 4.3 * EFT_DIAS_SEM_OCUP_SECUN, EFT_PERIODO_ING_OCUP_SECUN == 3 ~ 
            EFT_ING_OCUP_SECUN * 4.3, EFT_PERIODO_ING_OCUP_SECUN == 4 ~ EFT_ING_OCUP_SECUN * 2, EFT_PERIODO_ING_OCUP_SECUN == 
            5 ~ EFT_ING_OCUP_SECUN), ing_ocup_secun = dplyr::case_when(is.na(ing_ocup_secun) ~ 0, TRUE ~ 
        ing_ocup_secun))
}
```

</details>

## ft_ing_pc_pobreza_monetaria

Monthly household income per capita

```python
ft.ft_ing_pc_pobreza_monetaria(tbl, ing_ext=None, remesas=None, keep=False, reuse=False)
```

Use the historical 34-component monthly income model for 2005/1 to 2016/2. Unknown individual income leaves the household unclassified. Values outside coverage remain missing. This is not a certified reproduction of official ENFT production.

**Required columns:** `EFT_ANIO_PASADO_MONTO_ALQUILER`, `EFT_ANIO_PASADO_MONTO_GOBIERNO`, `EFT_ANIO_PASADO_MONTO_INTERES`, `EFT_ANIO_PASADO_MONTO_PENSION`, `EFT_ANIO_PASADO_MONTO_REMESAS`, `EFT_AYUDA_FAMILIARES_ANUAL`, `EFT_AYUDA_FAMILIARES_MENSUAL`, `EFT_BIENES_CONSUMO_ANUAL`, `EFT_BIENES_CONSUMO_MENSUAL`, `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_DIAS_SEM_OCUP_SECUN`, `EFT_ESPECIE_EMPRESAS_ANO_VAL`, `EFT_ESPECIE_EMPRESAS_MES_VAL`, `EFT_ESPECIE_FAMILIARES_ANO_VAL`, `EFT_ESPECIE_FAMILIARES_MES_VAL`, `EFT_ESPECIE_GOBIERNO_ANO_VAL`, `EFT_ESPECIE_GOBIERNO_MES_VAL`, `EFT_ESPECIE_OTROS_VAL`, `EFT_FRECUENCIA_AGO`, `EFT_FRECUENCIA_JUL`, `EFT_FRECUENCIA_PER4`, `EFT_FRECUENCIA_PER5`, `EFT_FRECUENCIA_PER6`, `EFT_FRECUENCIA_SEP`, `EFT_HOGAR`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_HORAS_SEM_OCUP_SECUN`, `EFT_ING_OCUP_PRINC`, `EFT_ING_OCUP_SECUN`, `EFT_MES_PASADO_COMISIONES`, `EFT_MES_PASADO_HORAS_EXTRAS`, `EFT_MES_PASADO_PROPINAS`, `EFT_MIEMBRO`, `EFT_MONEDA_AGO`, `EFT_MONEDA_ING_INTERES_MES`, `EFT_MONEDA_ING_PENSION_MES`, `EFT_MONEDA_ING_REMESA_SEM`, `EFT_MONEDA_JUL`, `EFT_MONEDA_PER4`, `EFT_MONEDA_PER5`, `EFT_MONEDA_PER6`, `EFT_MONEDA_SEP`, `EFT_MONTO_AGO`, `EFT_MONTO_ALQUILER_ING_NAC`, `EFT_MONTO_EQUIV_REGALO`, `EFT_MONTO_GOBIERNO_ING_NAC`, `EFT_MONTO_ING_INTERES_MES`, `EFT_MONTO_ING_PENSION_MES`, `EFT_MONTO_ING_REMESA_SEM`, `EFT_MONTO_INTERES_ING_NAC`, `EFT_MONTO_JUL`, `EFT_MONTO_PENSION_ING_NAC`, `EFT_MONTO_PER4`, `EFT_MONTO_PER5`, `EFT_MONTO_PER6`, `EFT_MONTO_PROBABLE_ALQ`, `EFT_MONTO_REMESAS_ING_NAC`, `EFT_MONTO_SEP`, `EFT_PAGO_ALIMENTOS_MONTO`, `EFT_PAGO_COMUNICACION_MONTO`, `EFT_PAGO_OTROS_MONTO`, `EFT_PAGO_TRANSPORTE_MONTO`, `EFT_PAGO_VESTIDO_MONTO`, `EFT_PAGO_VIVIENDAS_MONTO`, `EFT_PARENTESCO_CON_JEFE`, `EFT_PERIODO`, `EFT_PERIODO or PERIALFA`, `EFT_PERIODO_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_SECUN`, `EFT_RECIBIO_ING_REMESA_SEM`, `EFT_RECIBIO_REMESA`, `EFT_ULT_DOCE_BENEFICIOS_MARG`, `EFT_ULT_DOCE_BONIFICACION`, `EFT_ULT_DOCE_DIVIDENDOS`, `EFT_ULT_DOCE_REGALIA_PASCUAL`, `EFT_ULT_DOCE_UTILIDADES_EMP`, `EFT_ULT_DOCE_VACACIONES_PAGAS`, `EFT_VIVIENDA`, `EFT_ZONA`.

## ft_ing_pension_anual

Income: annual pension converted to monthly

```python
ft.ft_ing_pension_anual(tbl)
```

Compute annual pension converted to monthly using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ANIO_PASADO_MONTO_PENSION`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_pension_anual = dplyr::case_when(is.na(EFT_ANIO_PASADO_MONTO_PENSION) ~ 
        0, TRUE ~ EFT_ANIO_PASADO_MONTO_PENSION/12))
}
```

</details>

## ft_ing_pension_jubilacion

Income: domestic pension

```python
ft.ft_ing_pension_jubilacion(tbl)
```

Compute domestic pension using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_MONTO_PENSION_ING_NAC`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_pension_jubilacion = dplyr::case_when(is.na(EFT_MONTO_PENSION_ING_NAC) ~ 
        0, TRUE ~ EFT_MONTO_PENSION_ING_NAC))
}
```

</details>

## ft_ing_propinas

Income: tips

```python
ft.ft_ing_propinas(tbl)
```

Compute tips using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_MES_PASADO_PROPINAS`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_propinas = dplyr::case_when(is.na(EFT_MES_PASADO_PROPINAS) ~ 0, TRUE ~ 
        EFT_MES_PASADO_PROPINAS))
}
```

</details>

## ft_ing_regalia_pascual

Income: Christmas bonus

```python
ft.ft_ing_regalia_pascual(tbl)
```

Compute Christmas bonus using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ULT_DOCE_REGALIA_PASCUAL`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_regalia_pascual = dplyr::case_when(is.na(EFT_ULT_DOCE_REGALIA_PASCUAL) ~ 
        0, TRUE ~ EFT_ULT_DOCE_REGALIA_PASCUAL/12))
}
```

</details>

## ft_ing_regalos_ext

Income: external gifts

```python
ft.ft_ing_regalos_ext(tbl, ing_ext=None)
```

Compute external gifts using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_MONTO_EQUIV_REGALO`.

## ft_ing_remesas_anual

Income: annual remittances converted to monthly

```python
ft.ft_ing_remesas_anual(tbl)
```

Compute annual remittances converted to monthly using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ANIO_PASADO_MONTO_REMESAS`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_remesas_anual = dplyr::case_when(is.na(EFT_ANIO_PASADO_MONTO_REMESAS) ~ 
        0, TRUE ~ EFT_ANIO_PASADO_MONTO_REMESAS/12))
}
```

</details>

## ft_ing_remesas_ext

Income: external remittances

```python
ft.ft_ing_remesas_ext(tbl, remesas=None, ing_ext=None)
```

Compute external remittances using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_RECIBIO_REMESA`, `EFT_MONTO_SEP`, `EFT_MONEDA_SEP`, `EFT_FRECUENCIA_SEP`, `EFT_MONTO_AGO`, `EFT_MONEDA_AGO`, `EFT_FRECUENCIA_AGO`, `EFT_MONTO_JUL`, `EFT_MONEDA_JUL`, `EFT_FRECUENCIA_JUL`, `EFT_MONTO_PER4`, `EFT_MONEDA_PER4`, `EFT_FRECUENCIA_PER4`, `EFT_MONTO_PER5`, `EFT_MONEDA_PER5`, `EFT_FRECUENCIA_PER5`, `EFT_MONTO_PER6`, `EFT_MONEDA_PER6`, `EFT_FRECUENCIA_PER6`, `EFT_RECIBIO_ING_REMESA_SEM`, `EFT_MONTO_ING_REMESA_SEM`, `EFT_MONEDA_ING_REMESA_SEM`.

## ft_ing_remesas_nac

Income: domestic remittances

```python
ft.ft_ing_remesas_nac(tbl)
```

Compute domestic remittances using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_MONTO_REMESAS_ING_NAC`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_remesas_nac = dplyr::case_when(is.na(EFT_MONTO_REMESAS_ING_NAC) ~ 0, TRUE ~ 
        EFT_MONTO_REMESAS_ING_NAC))
}
```

</details>

## ft_ing_total_pobreza_monetaria

Monthly individual income for historical poverty

```python
ft.ft_ing_total_pobreza_monetaria(tbl, ing_ext=None, remesas=None, keep=False, reuse=False)
```

Use the historical 34-component monthly income model for 2005/1 to 2016/2. Unknown individual income leaves the household unclassified. Values outside coverage remain missing. This is not a certified reproduction of official ENFT production.

**Required columns:** `EFT_ANIO_PASADO_MONTO_ALQUILER`, `EFT_ANIO_PASADO_MONTO_GOBIERNO`, `EFT_ANIO_PASADO_MONTO_INTERES`, `EFT_ANIO_PASADO_MONTO_PENSION`, `EFT_ANIO_PASADO_MONTO_REMESAS`, `EFT_AYUDA_FAMILIARES_ANUAL`, `EFT_AYUDA_FAMILIARES_MENSUAL`, `EFT_BIENES_CONSUMO_ANUAL`, `EFT_BIENES_CONSUMO_MENSUAL`, `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_DIAS_SEM_OCUP_SECUN`, `EFT_ESPECIE_EMPRESAS_ANO_VAL`, `EFT_ESPECIE_EMPRESAS_MES_VAL`, `EFT_ESPECIE_FAMILIARES_ANO_VAL`, `EFT_ESPECIE_FAMILIARES_MES_VAL`, `EFT_ESPECIE_GOBIERNO_ANO_VAL`, `EFT_ESPECIE_GOBIERNO_MES_VAL`, `EFT_ESPECIE_OTROS_VAL`, `EFT_FRECUENCIA_AGO`, `EFT_FRECUENCIA_JUL`, `EFT_FRECUENCIA_PER4`, `EFT_FRECUENCIA_PER5`, `EFT_FRECUENCIA_PER6`, `EFT_FRECUENCIA_SEP`, `EFT_HOGAR`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_HORAS_SEM_OCUP_SECUN`, `EFT_ING_OCUP_PRINC`, `EFT_ING_OCUP_SECUN`, `EFT_MES_PASADO_COMISIONES`, `EFT_MES_PASADO_HORAS_EXTRAS`, `EFT_MES_PASADO_PROPINAS`, `EFT_MIEMBRO`, `EFT_MONEDA_AGO`, `EFT_MONEDA_ING_INTERES_MES`, `EFT_MONEDA_ING_PENSION_MES`, `EFT_MONEDA_ING_REMESA_SEM`, `EFT_MONEDA_JUL`, `EFT_MONEDA_PER4`, `EFT_MONEDA_PER5`, `EFT_MONEDA_PER6`, `EFT_MONEDA_SEP`, `EFT_MONTO_AGO`, `EFT_MONTO_ALQUILER_ING_NAC`, `EFT_MONTO_EQUIV_REGALO`, `EFT_MONTO_GOBIERNO_ING_NAC`, `EFT_MONTO_ING_INTERES_MES`, `EFT_MONTO_ING_PENSION_MES`, `EFT_MONTO_ING_REMESA_SEM`, `EFT_MONTO_INTERES_ING_NAC`, `EFT_MONTO_JUL`, `EFT_MONTO_PENSION_ING_NAC`, `EFT_MONTO_PER4`, `EFT_MONTO_PER5`, `EFT_MONTO_PER6`, `EFT_MONTO_PROBABLE_ALQ`, `EFT_MONTO_REMESAS_ING_NAC`, `EFT_MONTO_SEP`, `EFT_PAGO_ALIMENTOS_MONTO`, `EFT_PAGO_COMUNICACION_MONTO`, `EFT_PAGO_OTROS_MONTO`, `EFT_PAGO_TRANSPORTE_MONTO`, `EFT_PAGO_VESTIDO_MONTO`, `EFT_PAGO_VIVIENDAS_MONTO`, `EFT_PARENTESCO_CON_JEFE`, `EFT_PERIODO`, `EFT_PERIODO or PERIALFA`, `EFT_PERIODO_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_SECUN`, `EFT_RECIBIO_ING_REMESA_SEM`, `EFT_RECIBIO_REMESA`, `EFT_ULT_DOCE_BENEFICIOS_MARG`, `EFT_ULT_DOCE_BONIFICACION`, `EFT_ULT_DOCE_DIVIDENDOS`, `EFT_ULT_DOCE_REGALIA_PASCUAL`, `EFT_ULT_DOCE_UTILIDADES_EMP`, `EFT_ULT_DOCE_VACACIONES_PAGAS`, `EFT_VIVIENDA`, `EFT_ZONA`.

## ft_ing_utilidades_empresariales

Income: business profits

```python
ft.ft_ing_utilidades_empresariales(tbl)
```

Compute business profits using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ULT_DOCE_UTILIDADES_EMP`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_utilidades_empresariales = dplyr::case_when(is.na(EFT_ULT_DOCE_UTILIDADES_EMP) ~ 
        0, TRUE ~ EFT_ULT_DOCE_UTILIDADES_EMP/12))
}
```

</details>

## ft_ing_vacaciones

Income: paid leave

```python
ft.ft_ing_vacaciones(tbl)
```

Compute paid leave using the traditional ENFT questionnaire. Amounts contribute to monthly income in Dominican pesos. See the displayed calculation rule for the treatment of questionnaire skips and missing values.

**Required columns:** `EFT_ULT_DOCE_VACACIONES_PAGAS`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(ing_vacaciones = dplyr::case_when(is.na(EFT_ULT_DOCE_VACACIONES_PAGAS) ~ 0, 
        TRUE ~ EFT_ULT_DOCE_VACACIONES_PAGAS/12))
}
```

</details>

## ft_ingreso_laboral_mensual

Monthly labour income

```python
ft.ft_ingreso_laboral_mensual(tbl, min_edad=15)
```

Monthly labour income. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_CATEGORIA_OCUP_PRINC`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_PRINC`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_perceptores_ingresos(min_edad) %>% dplyr::mutate(ingreso_laboral_mensual = dplyr::case_when(EFT_PERIODO_ING_OCUP_PRINC == 
        1 ~ EFT_ING_OCUP_PRINC * 4.3 * EFT_HORAS_SEM_OCUP_PRINC, EFT_PERIODO_ING_OCUP_PRINC == 2 ~ EFT_ING_OCUP_PRINC * 
        4.3 * EFT_DIAS_SEM_OCUP_PRINC, EFT_PERIODO_ING_OCUP_PRINC == 3 ~ EFT_ING_OCUP_PRINC * 4.3, EFT_PERIODO_ING_OCUP_PRINC == 
        4 ~ EFT_ING_OCUP_PRINC * 2, EFT_PERIODO_ING_OCUP_PRINC == 5 ~ EFT_ING_OCUP_PRINC, TRUE ~ 0), 
        ingreso_laboral_mensual = dplyr::case_when(perceptores_ingresos == 1 ~ ingreso_laboral_mensual))
}
```

</details>

## ft_ocupado

Employed population

```python
ft.ft_ocupado(tbl, min_edad=15)
```

Employed population. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_pet(min_edad) %>% dplyr::mutate(ocupado = dplyr::case_when(EFT_TRABAJO_SEM_ANT == 1 ~ 
        1, EFT_TUVO_ACT_ECON_SEM_ANT == 1 ~ 1, EFT_CULTIVO_SEM_ANT == 1 ~ 1, EFT_ELAB_PROD_SEM_ANT == 
        1 ~ 1, EFT_AYUDO_FAM_SEM_ANT == 1 ~ 1, EFT_COSIO_LAVO_SEM_ANT == 1 ~ 1, pet == 1 ~ 0), ocupado = dplyr::case_when(pet == 
        1 ~ ocupado))
}
```

</details>

## ft_pea_abierta

Open economically active population

```python
ft.ft_pea_abierta(tbl, min_edad=15)
```

Open economically active population. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% ft_desempleo_abierto(min_edad) %>% dplyr::mutate(pea_abierta = dplyr::case_when(ocupado == 
        1 ~ 1, desempleo_abierto == 1 ~ 1, pet == 1 ~ 0))
}
```

</details>

## ft_pea_ampliada

Expanded economically active population

```python
ft.ft_pea_ampliada(tbl, min_edad=15)
```

Expanded economically active population. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% ft_desempleo_ampliado(min_edad) %>% dplyr::mutate(pea_ampliada = dplyr::case_when(ocupado == 
        1 ~ 1, desempleo_ampliado == 1 ~ 1, pet == 1 ~ 0))
}
```

</details>

## ft_perceptores_ingresos

Labour income recipients

```python
ft.ft_perceptores_ingresos(tbl, min_edad=15)
```

Labour income recipients. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_CATEGORIA_OCUP_PRINC`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% dplyr::mutate(perceptores_ingresos = dplyr::case_when(ocupado == 
        1 & EFT_CATEGORIA_OCUP_PRINC != 7 ~ 1, ocupado == 1 ~ 0))
}
```

</details>

## ft_peri_vars

Validate and extract the semiannual period

```python
ft.ft_peri_vars(tbl, rm=False, ano=True, semestre=True, periodo=True)
```

Validate and extract the semiannual period. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO or PERIALFA`.

## ft_pet

Working-age population

```python
ft.ft_pet(tbl, min_edad=15)
```

Working-age population. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_EDAD`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    ft_check_age(min_edad)
    tbl %>% dplyr::mutate(pet = dplyr::case_when(EFT_EDAD >= min_edad ~ 1, EFT_EDAD < min_edad ~ 0))
}
```

</details>

## ft_poblacion_inactiva

Inactive population

```python
ft.ft_poblacion_inactiva(tbl, min_edad=15)
```

Inactive population. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_pea_ampliada(min_edad) %>% dplyr::mutate(poblacion_inactiva = dplyr::case_when(pea_ampliada == 
        1 ~ 0, pet == 1 ~ 1))
}
```

</details>

## ft_pobreza_monetaria

Historical ENFT monetary poverty, 2005-2016

```python
ft.ft_pobreza_monetaria(tbl, ing_ext=None, remesas=None, keep=False, reuse=False)
```

Use the historical 34-component monthly income model for 2005/1 to 2016/2. Unknown individual income leaves the household unclassified. Values outside coverage remain missing. This is not a certified reproduction of official ENFT production.

**Required columns:** `EFT_ANIO_PASADO_MONTO_ALQUILER`, `EFT_ANIO_PASADO_MONTO_GOBIERNO`, `EFT_ANIO_PASADO_MONTO_INTERES`, `EFT_ANIO_PASADO_MONTO_PENSION`, `EFT_ANIO_PASADO_MONTO_REMESAS`, `EFT_AYUDA_FAMILIARES_ANUAL`, `EFT_AYUDA_FAMILIARES_MENSUAL`, `EFT_BIENES_CONSUMO_ANUAL`, `EFT_BIENES_CONSUMO_MENSUAL`, `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_DIAS_SEM_OCUP_SECUN`, `EFT_ESPECIE_EMPRESAS_ANO_VAL`, `EFT_ESPECIE_EMPRESAS_MES_VAL`, `EFT_ESPECIE_FAMILIARES_ANO_VAL`, `EFT_ESPECIE_FAMILIARES_MES_VAL`, `EFT_ESPECIE_GOBIERNO_ANO_VAL`, `EFT_ESPECIE_GOBIERNO_MES_VAL`, `EFT_ESPECIE_OTROS_VAL`, `EFT_FRECUENCIA_AGO`, `EFT_FRECUENCIA_JUL`, `EFT_FRECUENCIA_PER4`, `EFT_FRECUENCIA_PER5`, `EFT_FRECUENCIA_PER6`, `EFT_FRECUENCIA_SEP`, `EFT_HOGAR`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_HORAS_SEM_OCUP_SECUN`, `EFT_ING_OCUP_PRINC`, `EFT_ING_OCUP_SECUN`, `EFT_MES_PASADO_COMISIONES`, `EFT_MES_PASADO_HORAS_EXTRAS`, `EFT_MES_PASADO_PROPINAS`, `EFT_MIEMBRO`, `EFT_MONEDA_AGO`, `EFT_MONEDA_ING_INTERES_MES`, `EFT_MONEDA_ING_PENSION_MES`, `EFT_MONEDA_ING_REMESA_SEM`, `EFT_MONEDA_JUL`, `EFT_MONEDA_PER4`, `EFT_MONEDA_PER5`, `EFT_MONEDA_PER6`, `EFT_MONEDA_SEP`, `EFT_MONTO_AGO`, `EFT_MONTO_ALQUILER_ING_NAC`, `EFT_MONTO_EQUIV_REGALO`, `EFT_MONTO_GOBIERNO_ING_NAC`, `EFT_MONTO_ING_INTERES_MES`, `EFT_MONTO_ING_PENSION_MES`, `EFT_MONTO_ING_REMESA_SEM`, `EFT_MONTO_INTERES_ING_NAC`, `EFT_MONTO_JUL`, `EFT_MONTO_PENSION_ING_NAC`, `EFT_MONTO_PER4`, `EFT_MONTO_PER5`, `EFT_MONTO_PER6`, `EFT_MONTO_PROBABLE_ALQ`, `EFT_MONTO_REMESAS_ING_NAC`, `EFT_MONTO_SEP`, `EFT_PAGO_ALIMENTOS_MONTO`, `EFT_PAGO_COMUNICACION_MONTO`, `EFT_PAGO_OTROS_MONTO`, `EFT_PAGO_TRANSPORTE_MONTO`, `EFT_PAGO_VESTIDO_MONTO`, `EFT_PAGO_VIVIENDAS_MONTO`, `EFT_PARENTESCO_CON_JEFE`, `EFT_PERIODO`, `EFT_PERIODO or PERIALFA`, `EFT_PERIODO_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_SECUN`, `EFT_RECIBIO_ING_REMESA_SEM`, `EFT_RECIBIO_REMESA`, `EFT_ULT_DOCE_BENEFICIOS_MARG`, `EFT_ULT_DOCE_BONIFICACION`, `EFT_ULT_DOCE_DIVIDENDOS`, `EFT_ULT_DOCE_REGALIA_PASCUAL`, `EFT_ULT_DOCE_UTILIDADES_EMP`, `EFT_ULT_DOCE_VACACIONES_PAGAS`, `EFT_VIVIENDA`, `EFT_ZONA`.

## ft_regiones_desarrollo

Historical development regions: decree 710-04

```python
ft.ft_regiones_desarrollo(tbl)
```

Historical development regions: decree 710-04. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PROVINCIA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(regiones_desarrollo_710_04 = dplyr::case_when(EFT_PROVINCIA %in% c(25, 18, 
        9) ~ 1, EFT_PROVINCIA %in% c(13, 24, 28) ~ 2, EFT_PROVINCIA %in% c(6, 19, 14, 20) ~ 3, EFT_PROVINCIA %in% 
        c(27, 15, 5, 26) ~ 4, EFT_PROVINCIA %in% c(21, 2, 17, 31) ~ 5, EFT_PROVINCIA %in% c(4, 3, 16, 
        10) ~ 6, EFT_PROVINCIA %in% c(22, 7) ~ 7, EFT_PROVINCIA %in% c(12, 11, 8) ~ 8, EFT_PROVINCIA %in% 
        c(23, 30, 29) ~ 9, EFT_PROVINCIA %in% c(1, 32) ~ 10))
}
```

</details>

## ft_regiones_desarrollo_685_00

Historical development regions: decree 685-00

```python
ft.ft_regiones_desarrollo_685_00(tbl)
```

Historical development regions: decree 685-00. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PROVINCIA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(regiones_desarrollo_685_00 = dplyr::case_when(EFT_PROVINCIA %in% c(1, 32) ~ 
        1, EFT_PROVINCIA %in% c(17, 21, 29, 31) ~ 2, EFT_PROVINCIA %in% c(23, 12, 11, 30, 8) ~ 3, EFT_PROVINCIA %in% 
        c(19, 6, 14, 20) ~ 4, EFT_PROVINCIA %in% c(28, 13, 24) ~ 5, EFT_PROVINCIA %in% c(25, 18, 9) ~ 
        6, EFT_PROVINCIA %in% c(27, 26, 15, 5) ~ 7, EFT_PROVINCIA %in% c(2, 22, 7) ~ 8, EFT_PROVINCIA %in% 
        c(4, 3, 16, 10) ~ 9))
}
```

</details>

## ft_regiones_desarrollo_710_04

Historical development regions: decree 710-04

```python
ft.ft_regiones_desarrollo_710_04(tbl)
```

Historical development regions: decree 710-04. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PROVINCIA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% dplyr::mutate(regiones_desarrollo_710_04 = dplyr::case_when(EFT_PROVINCIA %in% c(25, 18, 
        9) ~ 1, EFT_PROVINCIA %in% c(13, 24, 28) ~ 2, EFT_PROVINCIA %in% c(6, 19, 14, 20) ~ 3, EFT_PROVINCIA %in% 
        c(27, 15, 5, 26) ~ 4, EFT_PROVINCIA %in% c(21, 2, 17, 31) ~ 5, EFT_PROVINCIA %in% c(4, 3, 16, 
        10) ~ 6, EFT_PROVINCIA %in% c(22, 7) ~ 7, EFT_PROVINCIA %in% c(12, 11, 8) ~ 8, EFT_PROVINCIA %in% 
        c(23, 30, 29) ~ 9, EFT_PROVINCIA %in% c(1, 32) ~ 10))
}
```

</details>

## ft_register_dict

Register a dictionary edition with shared definitions

```python
ft.ft_register_dict(con, dictionary, version, valid_from=None, valid_to=None, **kwargs)
```

Register a dictionary edition with shared definitions. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_sector_ocupacion

Occupational sector

```python
ft.ft_sector_ocupacion(tbl, min_edad=15)
```

Occupational sector. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_CANT_PERS_TRAB`, `EFT_CATEGORIA_OCUP_PRINC`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_OCUPACION_PRINC`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% ft_grupo_ocupacion(min_edad) %>% dplyr::mutate(sector_ocupacion = dplyr::case_when(EFT_CATEGORIA_OCUP_PRINC <= 
        3 & dplyr::between(EFT_CANT_PERS_TRAB, 3, 7) ~ 0, EFT_CATEGORIA_OCUP_PRINC %in% 4:6 & grupo_ocupacion == 
        1 ~ 0, EFT_CATEGORIA_OCUP_PRINC %in% 4:6 & grupo_ocupacion == 2 ~ 0, EFT_CATEGORIA_OCUP_PRINC %in% 
        4:6 & EFT_OCUPACION_PRINC == 341 ~ 0, .default = 1), sector_ocupacion = dplyr::case_when(ocupado == 
        1 ~ sector_ocupacion))
}
```

</details>

## ft_setLabels

Apply dictionary metadata

```python
ft.ft_setLabels(tbl, dict=None, vars=None)
```

Apply dictionary metadata. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_set_Dict

Apply dictionary metadata

```python
ft.ft_set_Dict(tbl, dictionary=None, subset=None, *, version=None, at=None, con=None, **kwargs)
```

Apply dictionary metadata. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_set_labels

Apply dictionary metadata

```python
ft.ft_set_labels(tbl, dict=None, vars=None)
```

Apply dictionary metadata. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_useLabels

Use variable and value labels

```python
ft.ft_useLabels(tbl, dict=None, vars=None, **kwargs)
```

Use variable and value labels. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_use_labels

Use variable and value labels

```python
ft.ft_use_labels(tbl, dict=None, vars=None, **kwargs)
```

Use variable and value labels. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_version

Identify ENFT column structure

```python
ft.ft_version(tbl)
```

Identify ENFT column structure. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO or PERIALFA`.

## ft_with_Dict

Use variable and value labels

```python
ft.ft_with_Dict(tbl, dictionary=None, subset=None, **kwargs)
```

Use variable and value labels. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

## ft_zona

Residence zone

```python
ft.ft_zona(tbl)
```

Residence zone. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PERIODO + EFT_ZONA or PERIALFA + S1_P4`.

## ft_zona_desarrollo_fronterizo

Historical border-development area

```python
ft.ft_zona_desarrollo_fronterizo(tbl)
```

Historical border-development area. Preserve input rows and order. Use the original questionnaire codes; unsupported or out-of-population values follow the displayed rule. Column structure does not imply a dated questionnaire revision.

**Required columns:** `EFT_PROVINCIA`.

<details><summary>Calculation rule in R notation</summary>

```r
{
    tbl %>% ft_regiones_desarrollo_710_04() %>% dplyr::mutate(zona_desarrollo_fronterizo = dplyr::case_when(as.numeric(EFT_PROVINCIA) %in% 
        as.numeric(c("16", "10", "07", "05", "15", "26", "03")) ~ 1, TRUE ~ 0))
}
```

</details>

The `EnftDataFrame` class exposes the same calculations as chainable methods. Use bracket column access when a column has the same name as a method.
