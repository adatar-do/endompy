# Referencia de la API ENFT

Aquí se relacionan todas las funciones públicas de R. La configuración de bases de datos y el operador pipe son interfaces propias de R. Los cálculos Python no requieren R en ejecución.

## ft_alfabeta

Alfabetismo de la persona (Sabe leer y escribir)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_alfabeta(tbl, min_edad=15)
```


Entre 2000 y 2005, se incluyó cero (0) en la variable para identificar aquellos
casos en que la pregunta no aplicaba. Esta variable omite esos valores.


**Columnas requeridas:** `EFT_ALFABETISMO`, `EFT_EDAD`.

<details><summary>Regla de cálculo en notación R</summary>

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

Separar y validar el periodo semestral de la ENFT

```python
ft.ft_ano(tbl)
```


Acepta S/AAAA, AAAA/S o AAAAS; reconoce EFT_PERIODO o PERIALFA.
Valida cada fila incluso cuando se combinan formatos. No modifica la columna
original salvo que rm sea TRUE. Solo recalcula las salidas solicitadas.


**Columnas requeridas:** `EFT_PERIODO or PERIALFA`.

## ft_anos_educacion

Años de educación
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_anos_educacion(tbl)
```


Años de educación
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_EDAD`, `EFT_ULT_ANO_APROBADO`, `EFT_ULT_NIVEL_ALCANZADO`.

<details><summary>Regla de cálculo en notación R</summary>

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

Consultar el diccionario ENFT

```python
ft.ft_browse_dict(version=None, at=None, con=None)
```


Consultar el diccionario ENFT


## ft_cantidad_personas_trabajan

Cantidad de personas trabajan en la empresa
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_cantidad_personas_trabajan(tbl)
```


Esta función homologa los rangos de cantidad de personas que laboran en la
empresa. Para el período 2000-2003 se incluían solo 4 categorías, pero de
2004 en adelante se incluyen 7 categorías. Vea los cuestionarios
correspondientes a esos periodos para más información.


**Columnas requeridas:** `EFT_CANT_PERS_TRAB`, `EFT_PERIODO or PERIALFA`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_peri_vars() %>% dplyr::mutate(cantidad_personas_trabajan = dplyr::case_when(ano >= 2004 & 
        EFT_CANT_PERS_TRAB %in% 1:2 ~ 1, ano >= 2004 & EFT_CANT_PERS_TRAB %in% 3:4 ~ EFT_CANT_PERS_TRAB - 
        1, ano >= 2004 & EFT_CANT_PERS_TRAB >= 5 ~ 4, EFT_CANT_PERS_TRAB != 0 ~ EFT_CANT_PERS_TRAB))
}
```

</details>

## ft_categoria_ocupacion_principal

Categoría de la ocupación principal
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_categoria_ocupacion_principal(tbl)
```


Las encuestas levantadas entre 2000 y 2004 contemplaban 10 categorías de
ocupación, pero en 2005 se redujeron a 8. Vea los cuestionarios
correspondientes a esos periodos para más información.


**Columnas requeridas:** `EFT_CATEGORIA_OCUP_PRINC`, `EFT_PERIODO or PERIALFA`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_peri_vars() %>% dplyr::mutate(categoria_ocupacion_principal = dplyr::case_when(dplyr::between(ano, 
        2000, 2004) & EFT_CATEGORIA_OCUP_PRINC %in% 7:8 ~ 7, dplyr::between(ano, 2000, 2004) & EFT_CATEGORIA_OCUP_PRINC %in% 
        9:10 ~ 8, TRUE ~ EFT_CATEGORIA_OCUP_PRINC))
}
```

</details>

## ft_compute_ano

Separar y validar el periodo semestral de la ENFT

```python
ft.ft_compute_ano(tbl)
```


Acepta S/AAAA, AAAA/S o AAAAS; reconoce EFT_PERIODO o PERIALFA.
Valida cada fila incluso cuando se combinan formatos. No modifica la columna
original salvo que rm sea TRUE. Solo recalcula las salidas solicitadas.


**Columnas requeridas:** `EFT_PERIODO or PERIALFA`.

## ft_compute_peri_vars

Separar y validar el periodo semestral de la ENFT

```python
ft.ft_compute_peri_vars(tbl, rm=False, ano=True, semestre=True, periodo=True)
```


Acepta S/AAAA, AAAA/S o AAAAS; reconoce EFT_PERIODO o PERIALFA.
Valida cada fila incluso cuando se combinan formatos. No modifica la columna
original salvo que rm sea TRUE. Solo recalcula las salidas solicitadas.


**Columnas requeridas:** `EFT_PERIODO or PERIALFA`.

## ft_compute_zona

Zona de residencia
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_compute_zona(tbl)
```


La base de datos de ne ENFT en su primera versión imputaba las zonas de
residencia con los valores de 0 y 1, para compatibilidad con la segunda
versión y la encuesta continua (ENCFT) se crea una variable zona que imputa
los valores como 1 y 2.


**Columnas requeridas:** `EFT_PERIODO + EFT_ZONA or PERIALFA + S1_P4`.

## ft_dbConnect

Conexión a base de datos
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]
Vea Dmisc::db_connect

Use sus herramientas de base de datos de Python y proporcione un DataFrame pandas. Los perfiles Dmisc no se traducen automáticamente.


Conexión a base de datos
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]
Vea Dmisc::db_connect


## ft_db_connect

Conexión a base de datos
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]
Vea Dmisc::db_connect

Use sus herramientas de base de datos de Python y proporcione un DataFrame pandas. Los perfiles Dmisc no se traducen automáticamente.


Conexión a base de datos
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]
Vea Dmisc::db_connect


## ft_desempleo_abierto

Población en condición de desempleo abierto
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_desempleo_abierto(tbl, min_edad=15)
```


Población en condición de desempleo abierto
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% dplyr::mutate(desempleo_abierto = dplyr::case_when(ocupado == 1 ~ 
        0, pet == 1 & EFT_BUSCO_TRAB_SEM_ANT == 1 ~ 1, pet == 1 & EFT_BUSCO_TRAB_MES_ANT == 1 ~ 1, ocupado == 
        1 ~ 0))
}
```

</details>

## ft_desempleo_ampliado

Población en condición de desempleo ampliado
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_desempleo_ampliado(tbl, min_edad=15)
```


Población en condición de desempleo ampliado
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_desempleo_abierto(min_edad) %>% dplyr::mutate(desempleo_ampliado = dplyr::case_when(ocupado == 
        1 ~ 0, desempleo_abierto == 1 ~ 1, EFT_TIENE_COND_JORNADA == 1 ~ 1, ocupado == 1 ~ 0), desempleo_ampliado = dplyr::case_when(pet == 
        1 ~ desempleo_ampliado))
}
```

</details>

## ft_desempleo_cesante_abierto

Población censante en condición de desempleo abierto
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_desempleo_cesante_abierto(tbl, min_edad=15)
```


Población censante en condición de desempleo abierto
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_ANTES`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_desempleo_abierto(min_edad) %>% dplyr::mutate(desempleo_cesante_abierto = dplyr::case_when(desempleo_abierto == 
        1 & EFT_TRABAJO_ANTES == 1 ~ 1, desempleo_abierto == 1 ~ 0))
}
```

</details>

## ft_desempleo_cesante_ampliado

Población censante en condición de desempleo ampliado
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_desempleo_cesante_ampliado(tbl, min_edad=15)
```


Población censante en condición de desempleo ampliado
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_ANTES`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_desempleo_ampliado(min_edad) %>% dplyr::mutate(desempleo_cesante_ampliado = dplyr::case_when(desempleo_ampliado == 
        1 & EFT_TRABAJO_ANTES != 1 ~ 0, desempleo_ampliado == 1 ~ 1))
}
```

</details>

## ft_desempleo_nuevo_abierto

Población nueva en condición de desempleo abierto
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_desempleo_nuevo_abierto(tbl, min_edad=15)
```


Población nueva en condición de desempleo abierto
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_ANTES`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_desempleo_abierto(min_edad) %>% dplyr::mutate(desempleo_nuevo_abierto = dplyr::case_when(desempleo_abierto == 
        1 & EFT_TRABAJO_ANTES != 1 ~ 1, desempleo_abierto == 1 ~ 0))
}
```

</details>

## ft_desempleo_nuevo_ampliado

Población nueva en condición de desempleo ampliado
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_desempleo_nuevo_ampliado(tbl, min_edad=15)
```


Población nueva en condición de desempleo ampliado
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_ANTES`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_desempleo_ampliado(min_edad) %>% dplyr::mutate(desempleo_nuevo_ampliado = dplyr::case_when(desempleo_ampliado == 
        1 & EFT_TRABAJO_ANTES == 1 ~ 0, desempleo_ampliado == 1 ~ 1))
}
```

</details>

## ft_dias_semana_ocupacion_principal

Número de días trabajados a la semana por ocupación principal
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_dias_semana_ocupacion_principal(tbl)
```


Número de días trabajados a la semana por ocupación principal
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_DIAS_SEM_OCUP_PRINC`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(dias_semana_ocupacion_principal = dplyr::case_when(EFT_DIAS_SEM_OCUP_PRINC > 
        0 ~ EFT_DIAS_SEM_OCUP_PRINC))
}
```

</details>

## ft_dict

Seleccionar una revision del diccionario ENFT

```python
ft.ft_dict(version=None, at=None, con=None)
```


La revision incluida baseline-1 conserva el diccionario disponible en el
proyecto y no declara vigencia historica. Para seleccionar por fecha se
requiere un registro con intervalos documentados. La version del diccionario
no selecciona la metodologia de pobreza.


## ft_dict_versions

Revisiones disponibles del diccionario ENFT

```python
ft.ft_dict_versions(con=None)
```


Revisiones disponibles del diccionario ENFT


## ft_dominios_inferencia

Dominios de inferencia ENFT
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_dominios_inferencia(tbl)
```


Dominios de inferencia ENFT
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PERIODO + EFT_ZONA or PERIALFA + S1_P4`, `EFT_PERIODO or PERIALFA`, `EFT_PROVINCIA`.

<details><summary>Regla de cálculo en notación R</summary>

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

Dominios de inferencia ENFT (20001 - 20031)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_dominios_inferencia1(tbl)
```


Dominios de inferencia ENFT (20001 - 20031)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PERIODO + EFT_ZONA or PERIALFA + S1_P4`, `EFT_PROVINCIA`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_zona() %>% dplyr::mutate(dominios_inferencia1 = dplyr::case_when(EFT_PROVINCIA %in% c(1, 
        32) ~ 1, zona == 1 ~ 2, zona == 2 ~ 3))
}
```

</details>

## ft_dominios_inferencia2

Dominios de inferencia ENFT (20032 - 20072)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_dominios_inferencia2(tbl)
```


Dominios de inferencia ENFT (20032 - 20072)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PROVINCIA`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    regiones_desarrollo_685_00 <- NULL
    tbl %>% ft_regiones_desarrollo_685_00() %>% dplyr::mutate(dominios_inferencia2 = regiones_desarrollo_685_00)
}
```

</details>

## ft_dominios_inferencia3

Dominios de inferencia ENFT (20081 - )
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_dominios_inferencia3(tbl)
```


Dominios de inferencia ENFT (20081 - )
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PROVINCIA`.

<details><summary>Regla de cálculo en notación R</summary>

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

Grupo de ocupación
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_grupo_ocupacion(tbl, min_edad=15)
```


Grupo de ocupación
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_OCUPACION_PRINC`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

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

Grupos Ramas de actividad económica
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_grupo_rama(tbl)
```


Grupos Ramas de actividad económica
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_RAMA_PRINC`.

<details><summary>Regla de cálculo en notación R</summary>

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

Horas trabajadas a la semana
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_horas_semanal(tbl, min_edad=15)
```


En el periodo 2000-2005 se imputó cero (0) para algunos casos que no aplicaban
esta función toma cuenta de esa situación eliminando todos los valores
asignados en cero (0).


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_CATEGORIA_OCUP_PRINC`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_perceptores_ingresos(min_edad) %>% dplyr::mutate(horas_semanal = dplyr::case_when(EFT_HORAS_SEM_OCUP_PRINC > 
        0 & perceptores_ingresos == 1 ~ EFT_HORAS_SEM_OCUP_PRINC))
}
```

</details>

## ft_ing_alqui_renta_propiedades

Ingreso monetario no laboral por alquiler o renta de prepiedades para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_alqui_renta_propiedades(tbl)
```


Ingreso monetario no laboral por alquiler o renta de prepiedades para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_MONTO_ALQUILER_ING_NAC`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    EFT_MONTO_ALQUILER_ING_NAC <- NULL
    tbl %>% dplyr::mutate(ing_alqui_renta_propiedades = dplyr::if_else(is.na(EFT_MONTO_ALQUILER_ING_NAC), 
        0, EFT_MONTO_ALQUILER_ING_NAC))
}
```

</details>

## ft_ing_alquiler_anual

Ingreso monetario no laboral anual por alquiler para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_alquiler_anual(tbl)
```


Ingreso monetario no laboral anual por alquiler para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ANIO_PASADO_MONTO_ALQUILER`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_alquiler_anual = dplyr::case_when(is.na(EFT_ANIO_PASADO_MONTO_ALQUILER) ~ 
        0, TRUE ~ EFT_ANIO_PASADO_MONTO_ALQUILER/12))
}
```

</details>

## ft_ing_ayuda_gobierno

Ingreso monetario no laboral por ayuda del gobierno para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_ayuda_gobierno(tbl)
```


Ingreso monetario no laboral por ayuda del gobierno para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_MONTO_GOBIERNO_ING_NAC`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    EFT_MONTO_GOBIERNO_ING_NAC <- NULL
    tbl %>% dplyr::mutate(ing_ayuda_gobierno = dplyr::if_else(is.na(EFT_MONTO_GOBIERNO_ING_NAC), 0, EFT_MONTO_GOBIERNO_ING_NAC))
}
```

</details>

## ft_ing_beneficios_marginales

Ingreso monetario laboral por beneficios marginales para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_beneficios_marginales(tbl)
```


Ingreso monetario laboral por beneficios marginales para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ULT_DOCE_BENEFICIOS_MARG`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_beneficios_marginales = dplyr::case_when(is.na(EFT_ULT_DOCE_BENEFICIOS_MARG) ~ 
        0, TRUE ~ EFT_ULT_DOCE_BENEFICIOS_MARG/12))
}
```

</details>

## ft_ing_bonificaciones

Ingreso monetario laboral por bonificaciones para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_bonificaciones(tbl)
```


Ingreso monetario laboral por bonificaciones para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ULT_DOCE_BONIFICACION`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_bonificaciones = dplyr::case_when(is.na(EFT_ULT_DOCE_BONIFICACION) ~ 0, 
        TRUE ~ EFT_ULT_DOCE_BONIFICACION/12))
}
```

</details>

## ft_ing_comisiones

Ingreso monetario laboral por comisiones para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_comisiones(tbl)
```


Ingreso monetario laboral por comisiones para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_MES_PASADO_COMISIONES`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_comisiones = dplyr::case_when(is.na(EFT_MES_PASADO_COMISIONES) ~ 0, TRUE ~ 
        EFT_MES_PASADO_COMISIONES))
}
```

</details>

## ft_ing_dividendos

Ingreso monetario laboral por dividendos para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_dividendos(tbl)
```


Ingreso monetario laboral por dividendos para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ULT_DOCE_DIVIDENDOS`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_dividendos = dplyr::case_when(is.na(EFT_ULT_DOCE_DIVIDENDOS) ~ 0, TRUE ~ 
        EFT_ULT_DOCE_DIVIDENDOS/12))
}
```

</details>

## ft_ing_especie_alimentos

Ingreso no monetario laboral en alimentos para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_especie_alimentos(tbl)
```


Ingreso no monetario laboral en alimentos para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PAGO_ALIMENTOS_MONTO`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_alimentos = dplyr::case_when(is.na(EFT_PAGO_ALIMENTOS_MONTO) ~ 
        0, !is.na(EFT_PAGO_ALIMENTOS_MONTO) ~ EFT_PAGO_ALIMENTOS_MONTO))
}
```

</details>

## ft_ing_especie_auto

Ingreso no monetario no laboral por autoconsumo o autosuministro para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_especie_auto(tbl)
```


Ingreso no monetario no laboral por autoconsumo o autosuministro para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_BIENES_CONSUMO_ANUAL`, `EFT_BIENES_CONSUMO_MENSUAL`.

<details><summary>Regla de cálculo en notación R</summary>

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

Ingreso no monetario no laboral por ayuda de empresa, familiares u ONG para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_especie_ayuda_ong(tbl)
```


Ingreso no monetario no laboral por ayuda de empresa, familiares u ONG para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_AYUDA_FAMILIARES_ANUAL`, `EFT_AYUDA_FAMILIARES_MENSUAL`, `EFT_ESPECIE_EMPRESAS_ANO_VAL`, `EFT_ESPECIE_EMPRESAS_MES_VAL`, `EFT_ESPECIE_FAMILIARES_ANO_VAL`, `EFT_ESPECIE_FAMILIARES_MES_VAL`, `EFT_ESPECIE_GOBIERNO_ANO_VAL`, `EFT_ESPECIE_GOBIERNO_MES_VAL`, `EFT_ESPECIE_OTROS_VAL`.

<details><summary>Regla de cálculo en notación R</summary>

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

Ingreso no monetario laboral en celulares para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_especie_celulares(tbl)
```


Ingreso no monetario laboral en celulares para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_PAGO_COMUNICACION_MONTO`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_celulares = dplyr::case_when(is.na(EFT_PAGO_COMUNICACION_MONTO) ~ 
        0, TRUE ~ EFT_PAGO_COMUNICACION_MONTO))
}
```

</details>

## ft_ing_especie_otros

Ingreso no monetario laboral en otros servicios para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_especie_otros(tbl)
```


Ingreso no monetario laboral en otros servicios para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_PAGO_OTROS_MONTO`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_otros = dplyr::case_when(is.na(EFT_PAGO_OTROS_MONTO) ~ 0, TRUE ~ 
        EFT_PAGO_OTROS_MONTO))
}
```

</details>

## ft_ing_especie_transporte

Ingreso no monetario laboral en transporte para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_especie_transporte(tbl)
```


Ingreso no monetario laboral en transporte para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_PAGO_TRANSPORTE_MONTO`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_transporte = dplyr::case_when(is.na(EFT_PAGO_TRANSPORTE_MONTO) ~ 
        0, TRUE ~ EFT_PAGO_TRANSPORTE_MONTO))
}
```

</details>

## ft_ing_especie_vestido

Ingreso no monetario laboral en vestido o calzado para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_especie_vestido(tbl)
```


Ingreso no monetario laboral en vestido o calzado para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_PAGO_VESTIDO_MONTO`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_vestido = dplyr::case_when(is.na(EFT_PAGO_VESTIDO_MONTO) ~ 0, TRUE ~ 
        EFT_PAGO_VESTIDO_MONTO/12))
}
```

</details>

## ft_ing_especie_viviendas

Ingreso no monetario laboral en vivienda para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_especie_viviendas(tbl)
```


Ingreso no monetario laboral en vivienda para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_PAGO_VIVIENDAS_MONTO`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_especie_viviendas = dplyr::case_when(is.na(EFT_PAGO_VIVIENDAS_MONTO) ~ 
        0, TRUE ~ EFT_PAGO_VIVIENDAS_MONTO))
}
```

</details>

## ft_ing_ext_intereses_alquiler

Ingreso monetario no laboral por intereses o alquileres del exterior para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_ext_intereses_alquiler(tbl, ing_ext=None)
```


Ingreso monetario no laboral por intereses o alquileres del exterior para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_MONTO_ING_INTERES_MES`, `EFT_MONEDA_ING_INTERES_MES`.

## ft_ing_ext_pension

Ingreso monetario no laboral por pensión del exterior para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_ext_pension(tbl, ing_ext=None)
```


Ingreso monetario no laboral por pensión del exterior para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_MONTO_ING_PENSION_MES`, `EFT_MONEDA_ING_PENSION_MES`.

## ft_ing_gobierno_anual

Ingreso monetario no laboral anual por ayuda gobierno para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_gobierno_anual(tbl)
```


Ingreso monetario no laboral anual por ayuda gobierno para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ANIO_PASADO_MONTO_GOBIERNO`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    EFT_ANIO_PASADO_MONTO_GOBIERNO <- NULL
    tbl %>% dplyr::mutate(ing_gobierno_anual = dplyr::if_else(is.na(EFT_ANIO_PASADO_MONTO_GOBIERNO), 
        0, EFT_ANIO_PASADO_MONTO_GOBIERNO/12))
}
```

</details>

## ft_ing_horas_extras

Ingreso monetario laboral por horas extras para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_horas_extras(tbl)
```


Ingreso monetario laboral por horas extras para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_MES_PASADO_HORAS_EXTRAS`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_horas_extras = dplyr::case_when(is.na(EFT_MES_PASADO_HORAS_EXTRAS) ~ 0, 
        TRUE ~ EFT_MES_PASADO_HORAS_EXTRAS))
}
```

</details>

## ft_ing_imputado_vivienda_propia

Ingreso no monetario no laboral imputado por uso de vivienda propia para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_imputado_vivienda_propia(tbl)
```


Ingreso no monetario no laboral imputado por uso de vivienda propia para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_PARENTESCO_CON_JEFE`, `EFT_MONTO_PROBABLE_ALQ`.

## ft_ing_interes_anual

Ingreso monetario no laboral anual por intereses para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_interes_anual(tbl)
```


Ingreso monetario no laboral anual por intereses para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ANIO_PASADO_MONTO_INTERES`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_interes_anual = dplyr::case_when(is.na(EFT_ANIO_PASADO_MONTO_INTERES) ~ 
        0, TRUE ~ EFT_ANIO_PASADO_MONTO_INTERES/12))
}
```

</details>

## ft_ing_intereses_dividendo

Ingreso monetario no laboral por intereses o dividendos para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_intereses_dividendo(tbl)
```


Ingreso monetario no laboral por intereses o dividendos para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_MONTO_INTERES_ING_NAC`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_intereses_dividendo = dplyr::case_when(is.na(EFT_MONTO_INTERES_ING_NAC) ~ 
        0, TRUE ~ EFT_MONTO_INTERES_ING_NAC))
}
```

</details>

## ft_ing_ocup_prin

Ingreso monetario laboral por salario ocupación principal para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_ocup_prin(tbl)
```


Ingreso monetario laboral por salario ocupación principal para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_PRINC`.

<details><summary>Regla de cálculo en notación R</summary>

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

Ingreso monetario laboral por salario ocupación secundaria para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_ocup_secun(tbl)
```


Ingreso monetario laboral por salario ocupación secundaria para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_DIAS_SEM_OCUP_SECUN`, `EFT_HORAS_SEM_OCUP_SECUN`, `EFT_ING_OCUP_SECUN`, `EFT_PERIODO or PERIALFA`, `EFT_PERIODO_ING_OCUP_SECUN`.

<details><summary>Regla de cálculo en notación R</summary>

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

Ingreso mensual por persona del hogar

```python
ft.ft_ing_pc_pobreza_monetaria(tbl, ing_ext=None, remesas=None, keep=False, reuse=False)
```


Ingreso mensual por persona del hogar


**Columnas requeridas:** `EFT_ANIO_PASADO_MONTO_ALQUILER`, `EFT_ANIO_PASADO_MONTO_GOBIERNO`, `EFT_ANIO_PASADO_MONTO_INTERES`, `EFT_ANIO_PASADO_MONTO_PENSION`, `EFT_ANIO_PASADO_MONTO_REMESAS`, `EFT_AYUDA_FAMILIARES_ANUAL`, `EFT_AYUDA_FAMILIARES_MENSUAL`, `EFT_BIENES_CONSUMO_ANUAL`, `EFT_BIENES_CONSUMO_MENSUAL`, `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_DIAS_SEM_OCUP_SECUN`, `EFT_ESPECIE_EMPRESAS_ANO_VAL`, `EFT_ESPECIE_EMPRESAS_MES_VAL`, `EFT_ESPECIE_FAMILIARES_ANO_VAL`, `EFT_ESPECIE_FAMILIARES_MES_VAL`, `EFT_ESPECIE_GOBIERNO_ANO_VAL`, `EFT_ESPECIE_GOBIERNO_MES_VAL`, `EFT_ESPECIE_OTROS_VAL`, `EFT_FRECUENCIA_AGO`, `EFT_FRECUENCIA_JUL`, `EFT_FRECUENCIA_PER4`, `EFT_FRECUENCIA_PER5`, `EFT_FRECUENCIA_PER6`, `EFT_FRECUENCIA_SEP`, `EFT_HOGAR`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_HORAS_SEM_OCUP_SECUN`, `EFT_ING_OCUP_PRINC`, `EFT_ING_OCUP_SECUN`, `EFT_MES_PASADO_COMISIONES`, `EFT_MES_PASADO_HORAS_EXTRAS`, `EFT_MES_PASADO_PROPINAS`, `EFT_MIEMBRO`, `EFT_MONEDA_AGO`, `EFT_MONEDA_ING_INTERES_MES`, `EFT_MONEDA_ING_PENSION_MES`, `EFT_MONEDA_ING_REMESA_SEM`, `EFT_MONEDA_JUL`, `EFT_MONEDA_PER4`, `EFT_MONEDA_PER5`, `EFT_MONEDA_PER6`, `EFT_MONEDA_SEP`, `EFT_MONTO_AGO`, `EFT_MONTO_ALQUILER_ING_NAC`, `EFT_MONTO_EQUIV_REGALO`, `EFT_MONTO_GOBIERNO_ING_NAC`, `EFT_MONTO_ING_INTERES_MES`, `EFT_MONTO_ING_PENSION_MES`, `EFT_MONTO_ING_REMESA_SEM`, `EFT_MONTO_INTERES_ING_NAC`, `EFT_MONTO_JUL`, `EFT_MONTO_PENSION_ING_NAC`, `EFT_MONTO_PER4`, `EFT_MONTO_PER5`, `EFT_MONTO_PER6`, `EFT_MONTO_PROBABLE_ALQ`, `EFT_MONTO_REMESAS_ING_NAC`, `EFT_MONTO_SEP`, `EFT_PAGO_ALIMENTOS_MONTO`, `EFT_PAGO_COMUNICACION_MONTO`, `EFT_PAGO_OTROS_MONTO`, `EFT_PAGO_TRANSPORTE_MONTO`, `EFT_PAGO_VESTIDO_MONTO`, `EFT_PAGO_VIVIENDAS_MONTO`, `EFT_PARENTESCO_CON_JEFE`, `EFT_PERIODO`, `EFT_PERIODO or PERIALFA`, `EFT_PERIODO_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_SECUN`, `EFT_RECIBIO_ING_REMESA_SEM`, `EFT_RECIBIO_REMESA`, `EFT_ULT_DOCE_BENEFICIOS_MARG`, `EFT_ULT_DOCE_BONIFICACION`, `EFT_ULT_DOCE_DIVIDENDOS`, `EFT_ULT_DOCE_REGALIA_PASCUAL`, `EFT_ULT_DOCE_UTILIDADES_EMP`, `EFT_ULT_DOCE_VACACIONES_PAGAS`, `EFT_VIVIENDA`, `EFT_ZONA`.

## ft_ing_pension_anual

Ingreso monetario no laboral anual por pensión para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_pension_anual(tbl)
```


Ingreso monetario no laboral anual por pensión para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ANIO_PASADO_MONTO_PENSION`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_pension_anual = dplyr::case_when(is.na(EFT_ANIO_PASADO_MONTO_PENSION) ~ 
        0, TRUE ~ EFT_ANIO_PASADO_MONTO_PENSION/12))
}
```

</details>

## ft_ing_pension_jubilacion

Ingreso monetario no laboral por pensión o jubilación para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_pension_jubilacion(tbl)
```


Ingreso monetario no laboral por pensión o jubilación para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_MONTO_PENSION_ING_NAC`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_pension_jubilacion = dplyr::case_when(is.na(EFT_MONTO_PENSION_ING_NAC) ~ 
        0, TRUE ~ EFT_MONTO_PENSION_ING_NAC))
}
```

</details>

## ft_ing_propinas

Ingreso monetario laboral por propinas para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_propinas(tbl)
```


Ingreso monetario laboral por propinas para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_MES_PASADO_PROPINAS`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_propinas = dplyr::case_when(is.na(EFT_MES_PASADO_PROPINAS) ~ 0, TRUE ~ 
        EFT_MES_PASADO_PROPINAS))
}
```

</details>

## ft_ing_regalia_pascual

Ingreso monetario laboral por regalía pascual para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_regalia_pascual(tbl)
```


Ingreso monetario laboral por regalía pascual para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ULT_DOCE_REGALIA_PASCUAL`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_regalia_pascual = dplyr::case_when(is.na(EFT_ULT_DOCE_REGALIA_PASCUAL) ~ 
        0, TRUE ~ EFT_ULT_DOCE_REGALIA_PASCUAL/12))
}
```

</details>

## ft_ing_regalos_ext

Ingreso no monetario no laboral por regalos del exterior para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_regalos_ext(tbl, ing_ext=None)
```


Ingreso no monetario no laboral por regalos del exterior para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_MONTO_EQUIV_REGALO`.

## ft_ing_remesas_anual

Ingreso monetario no laboral anual por remesas para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_remesas_anual(tbl)
```


Ingreso monetario no laboral anual por remesas para el cálculo de pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ANIO_PASADO_MONTO_REMESAS`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_remesas_anual = dplyr::case_when(is.na(EFT_ANIO_PASADO_MONTO_REMESAS) ~ 
        0, TRUE ~ EFT_ANIO_PASADO_MONTO_REMESAS/12))
}
```

</details>

## ft_ing_remesas_ext

Ingreso monetario no laboral por remesas del exterior para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]

```python
ft.ft_ing_remesas_ext(tbl, remesas=None, ing_ext=None)
```


Ingreso monetario no laboral por remesas del exterior para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


**Columnas requeridas:** `EFT_PERIODO`, `EFT_VIVIENDA`, `EFT_HOGAR`, `EFT_MIEMBRO`, `EFT_RECIBIO_REMESA`, `EFT_MONTO_SEP`, `EFT_MONEDA_SEP`, `EFT_FRECUENCIA_SEP`, `EFT_MONTO_AGO`, `EFT_MONEDA_AGO`, `EFT_FRECUENCIA_AGO`, `EFT_MONTO_JUL`, `EFT_MONEDA_JUL`, `EFT_FRECUENCIA_JUL`, `EFT_MONTO_PER4`, `EFT_MONEDA_PER4`, `EFT_FRECUENCIA_PER4`, `EFT_MONTO_PER5`, `EFT_MONEDA_PER5`, `EFT_FRECUENCIA_PER5`, `EFT_MONTO_PER6`, `EFT_MONEDA_PER6`, `EFT_FRECUENCIA_PER6`, `EFT_RECIBIO_ING_REMESA_SEM`, `EFT_MONTO_ING_REMESA_SEM`, `EFT_MONEDA_ING_REMESA_SEM`.

## ft_ing_remesas_nac

Ingreso monetario no laboral por remesas nacionales para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_remesas_nac(tbl)
```


Ingreso monetario no laboral por remesas nacionales para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_MONTO_REMESAS_ING_NAC`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_remesas_nac = dplyr::case_when(is.na(EFT_MONTO_REMESAS_ING_NAC) ~ 0, TRUE ~ 
        EFT_MONTO_REMESAS_ING_NAC))
}
```

</details>

## ft_ing_total_pobreza_monetaria

Ingreso individual mensual usado por la pobreza histórica

```python
ft.ft_ing_total_pobreza_monetaria(tbl, ing_ext=None, remesas=None, keep=False, reuse=False)
```


Ingreso individual mensual usado por la pobreza histórica


**Columnas requeridas:** `EFT_ANIO_PASADO_MONTO_ALQUILER`, `EFT_ANIO_PASADO_MONTO_GOBIERNO`, `EFT_ANIO_PASADO_MONTO_INTERES`, `EFT_ANIO_PASADO_MONTO_PENSION`, `EFT_ANIO_PASADO_MONTO_REMESAS`, `EFT_AYUDA_FAMILIARES_ANUAL`, `EFT_AYUDA_FAMILIARES_MENSUAL`, `EFT_BIENES_CONSUMO_ANUAL`, `EFT_BIENES_CONSUMO_MENSUAL`, `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_DIAS_SEM_OCUP_SECUN`, `EFT_ESPECIE_EMPRESAS_ANO_VAL`, `EFT_ESPECIE_EMPRESAS_MES_VAL`, `EFT_ESPECIE_FAMILIARES_ANO_VAL`, `EFT_ESPECIE_FAMILIARES_MES_VAL`, `EFT_ESPECIE_GOBIERNO_ANO_VAL`, `EFT_ESPECIE_GOBIERNO_MES_VAL`, `EFT_ESPECIE_OTROS_VAL`, `EFT_FRECUENCIA_AGO`, `EFT_FRECUENCIA_JUL`, `EFT_FRECUENCIA_PER4`, `EFT_FRECUENCIA_PER5`, `EFT_FRECUENCIA_PER6`, `EFT_FRECUENCIA_SEP`, `EFT_HOGAR`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_HORAS_SEM_OCUP_SECUN`, `EFT_ING_OCUP_PRINC`, `EFT_ING_OCUP_SECUN`, `EFT_MES_PASADO_COMISIONES`, `EFT_MES_PASADO_HORAS_EXTRAS`, `EFT_MES_PASADO_PROPINAS`, `EFT_MIEMBRO`, `EFT_MONEDA_AGO`, `EFT_MONEDA_ING_INTERES_MES`, `EFT_MONEDA_ING_PENSION_MES`, `EFT_MONEDA_ING_REMESA_SEM`, `EFT_MONEDA_JUL`, `EFT_MONEDA_PER4`, `EFT_MONEDA_PER5`, `EFT_MONEDA_PER6`, `EFT_MONEDA_SEP`, `EFT_MONTO_AGO`, `EFT_MONTO_ALQUILER_ING_NAC`, `EFT_MONTO_EQUIV_REGALO`, `EFT_MONTO_GOBIERNO_ING_NAC`, `EFT_MONTO_ING_INTERES_MES`, `EFT_MONTO_ING_PENSION_MES`, `EFT_MONTO_ING_REMESA_SEM`, `EFT_MONTO_INTERES_ING_NAC`, `EFT_MONTO_JUL`, `EFT_MONTO_PENSION_ING_NAC`, `EFT_MONTO_PER4`, `EFT_MONTO_PER5`, `EFT_MONTO_PER6`, `EFT_MONTO_PROBABLE_ALQ`, `EFT_MONTO_REMESAS_ING_NAC`, `EFT_MONTO_SEP`, `EFT_PAGO_ALIMENTOS_MONTO`, `EFT_PAGO_COMUNICACION_MONTO`, `EFT_PAGO_OTROS_MONTO`, `EFT_PAGO_TRANSPORTE_MONTO`, `EFT_PAGO_VESTIDO_MONTO`, `EFT_PAGO_VIVIENDAS_MONTO`, `EFT_PARENTESCO_CON_JEFE`, `EFT_PERIODO`, `EFT_PERIODO or PERIALFA`, `EFT_PERIODO_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_SECUN`, `EFT_RECIBIO_ING_REMESA_SEM`, `EFT_RECIBIO_REMESA`, `EFT_ULT_DOCE_BENEFICIOS_MARG`, `EFT_ULT_DOCE_BONIFICACION`, `EFT_ULT_DOCE_DIVIDENDOS`, `EFT_ULT_DOCE_REGALIA_PASCUAL`, `EFT_ULT_DOCE_UTILIDADES_EMP`, `EFT_ULT_DOCE_VACACIONES_PAGAS`, `EFT_VIVIENDA`, `EFT_ZONA`.

## ft_ing_utilidades_empresariales

Ingreso monetario laboral por utilidades empresariales para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_utilidades_empresariales(tbl)
```


Ingreso monetario laboral por utilidades empresariales para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ULT_DOCE_UTILIDADES_EMP`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_utilidades_empresariales = dplyr::case_when(is.na(EFT_ULT_DOCE_UTILIDADES_EMP) ~ 
        0, TRUE ~ EFT_ULT_DOCE_UTILIDADES_EMP/12))
}
```

</details>

## ft_ing_vacaciones

Ingreso monetario laboral por vacaciones para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ing_vacaciones(tbl)
```


Ingreso monetario laboral por vacaciones para el cálculo de la pobreza monetaria
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_ULT_DOCE_VACACIONES_PAGAS`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% dplyr::mutate(ing_vacaciones = dplyr::case_when(is.na(EFT_ULT_DOCE_VACACIONES_PAGAS) ~ 0, 
        TRUE ~ EFT_ULT_DOCE_VACACIONES_PAGAS/12))
}
```

</details>

## ft_ingreso_laboral_mensual

Ingreso laboral mensual
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ingreso_laboral_mensual(tbl, min_edad=15)
```


Ingreso laboral mensual
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_CATEGORIA_OCUP_PRINC`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_PRINC`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

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

Población ocupada
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_ocupado(tbl, min_edad=15)
```


Población ocupada
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

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

Población Económicamente Activa (PEA) abierta
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_pea_abierta(tbl, min_edad=15)
```


Población Económicamente Activa (PEA) abierta
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% ft_desempleo_abierto(min_edad) %>% dplyr::mutate(pea_abierta = dplyr::case_when(ocupado == 
        1 ~ 1, desempleo_abierto == 1 ~ 1, pet == 1 ~ 0))
}
```

</details>

## ft_pea_ampliada

Población Económicamente Activa (PEA) ampliada
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_pea_ampliada(tbl, min_edad=15)
```


Población Económicamente Activa (PEA) ampliada
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% ft_desempleo_ampliado(min_edad) %>% dplyr::mutate(pea_ampliada = dplyr::case_when(ocupado == 
        1 ~ 1, desempleo_ampliado == 1 ~ 1, pet == 1 ~ 0))
}
```

</details>

## ft_perceptores_ingresos

Perceptores de ingresos
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_perceptores_ingresos(tbl, min_edad=15)
```


Perceptores de ingresos
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_CATEGORIA_OCUP_PRINC`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_ocupado(min_edad) %>% dplyr::mutate(perceptores_ingresos = dplyr::case_when(ocupado == 
        1 & EFT_CATEGORIA_OCUP_PRINC != 7 ~ 1, ocupado == 1 ~ 0))
}
```

</details>

## ft_peri_vars

Separar y validar el periodo semestral de la ENFT

```python
ft.ft_peri_vars(tbl, rm=False, ano=True, semestre=True, periodo=True)
```


Acepta S/AAAA, AAAA/S o AAAAS; reconoce EFT_PERIODO o PERIALFA.
Valida cada fila incluso cuando se combinan formatos. No modifica la columna
original salvo que rm sea TRUE. Solo recalcula las salidas solicitadas.


**Columnas requeridas:** `EFT_PERIODO or PERIALFA`.

## ft_pet

Población en edad de trabajar (PET)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_pet(tbl, min_edad=15)
```


Población en edad de trabajar (PET)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_EDAD`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    ft_check_age(min_edad)
    tbl %>% dplyr::mutate(pet = dplyr::case_when(EFT_EDAD >= min_edad ~ 1, EFT_EDAD < min_edad ~ 0))
}
```

</details>

## ft_poblacion_inactiva

Población inactiva (No PEA)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_poblacion_inactiva(tbl, min_edad=15)
```


Población inactiva (No PEA)
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_pea_ampliada(min_edad) %>% dplyr::mutate(poblacion_inactiva = dplyr::case_when(pea_ampliada == 
        1 ~ 0, pet == 1 ~ 1))
}
```

</details>

## ft_pobreza_monetaria

Pobreza monetaria histórica de la ENFT, 2005-2016

```python
ft.ft_pobreza_monetaria(tbl, ing_ext=None, remesas=None, keep=False, reuse=False)
```


Implementación histórica de enftr, revisada para preservar ingresos desconocidos,
corregir meses de remesas y validar claves. No está certificada como reproducción
del programa oficial. Las líneas incluidas son nominales y específicas de zona
y semestre. No aplique esta función a la ENCFT ni a períodos posteriores a 2016.


**Columnas requeridas:** `EFT_ANIO_PASADO_MONTO_ALQUILER`, `EFT_ANIO_PASADO_MONTO_GOBIERNO`, `EFT_ANIO_PASADO_MONTO_INTERES`, `EFT_ANIO_PASADO_MONTO_PENSION`, `EFT_ANIO_PASADO_MONTO_REMESAS`, `EFT_AYUDA_FAMILIARES_ANUAL`, `EFT_AYUDA_FAMILIARES_MENSUAL`, `EFT_BIENES_CONSUMO_ANUAL`, `EFT_BIENES_CONSUMO_MENSUAL`, `EFT_DIAS_SEM_OCUP_PRINC`, `EFT_DIAS_SEM_OCUP_SECUN`, `EFT_ESPECIE_EMPRESAS_ANO_VAL`, `EFT_ESPECIE_EMPRESAS_MES_VAL`, `EFT_ESPECIE_FAMILIARES_ANO_VAL`, `EFT_ESPECIE_FAMILIARES_MES_VAL`, `EFT_ESPECIE_GOBIERNO_ANO_VAL`, `EFT_ESPECIE_GOBIERNO_MES_VAL`, `EFT_ESPECIE_OTROS_VAL`, `EFT_FRECUENCIA_AGO`, `EFT_FRECUENCIA_JUL`, `EFT_FRECUENCIA_PER4`, `EFT_FRECUENCIA_PER5`, `EFT_FRECUENCIA_PER6`, `EFT_FRECUENCIA_SEP`, `EFT_HOGAR`, `EFT_HORAS_SEM_OCUP_PRINC`, `EFT_HORAS_SEM_OCUP_SECUN`, `EFT_ING_OCUP_PRINC`, `EFT_ING_OCUP_SECUN`, `EFT_MES_PASADO_COMISIONES`, `EFT_MES_PASADO_HORAS_EXTRAS`, `EFT_MES_PASADO_PROPINAS`, `EFT_MIEMBRO`, `EFT_MONEDA_AGO`, `EFT_MONEDA_ING_INTERES_MES`, `EFT_MONEDA_ING_PENSION_MES`, `EFT_MONEDA_ING_REMESA_SEM`, `EFT_MONEDA_JUL`, `EFT_MONEDA_PER4`, `EFT_MONEDA_PER5`, `EFT_MONEDA_PER6`, `EFT_MONEDA_SEP`, `EFT_MONTO_AGO`, `EFT_MONTO_ALQUILER_ING_NAC`, `EFT_MONTO_EQUIV_REGALO`, `EFT_MONTO_GOBIERNO_ING_NAC`, `EFT_MONTO_ING_INTERES_MES`, `EFT_MONTO_ING_PENSION_MES`, `EFT_MONTO_ING_REMESA_SEM`, `EFT_MONTO_INTERES_ING_NAC`, `EFT_MONTO_JUL`, `EFT_MONTO_PENSION_ING_NAC`, `EFT_MONTO_PER4`, `EFT_MONTO_PER5`, `EFT_MONTO_PER6`, `EFT_MONTO_PROBABLE_ALQ`, `EFT_MONTO_REMESAS_ING_NAC`, `EFT_MONTO_SEP`, `EFT_PAGO_ALIMENTOS_MONTO`, `EFT_PAGO_COMUNICACION_MONTO`, `EFT_PAGO_OTROS_MONTO`, `EFT_PAGO_TRANSPORTE_MONTO`, `EFT_PAGO_VESTIDO_MONTO`, `EFT_PAGO_VIVIENDAS_MONTO`, `EFT_PARENTESCO_CON_JEFE`, `EFT_PERIODO`, `EFT_PERIODO or PERIALFA`, `EFT_PERIODO_ING_OCUP_PRINC`, `EFT_PERIODO_ING_OCUP_SECUN`, `EFT_RECIBIO_ING_REMESA_SEM`, `EFT_RECIBIO_REMESA`, `EFT_ULT_DOCE_BENEFICIOS_MARG`, `EFT_ULT_DOCE_BONIFICACION`, `EFT_ULT_DOCE_DIVIDENDOS`, `EFT_ULT_DOCE_REGALIA_PASCUAL`, `EFT_ULT_DOCE_UTILIDADES_EMP`, `EFT_ULT_DOCE_VACACIONES_PAGAS`, `EFT_VIVIENDA`, `EFT_ZONA`.

## ft_regiones_desarrollo

Regiones de desarrollo según decreto 710-04
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_regiones_desarrollo(tbl)
```


Regiones de desarrollo según decreto 710-04
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_PROVINCIA`.

<details><summary>Regla de cálculo en notación R</summary>

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

Regiones de desarrollo según decreto 685-00
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_regiones_desarrollo_685_00(tbl)
```


Regiones de desarrollo según decreto 685-00
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_PROVINCIA`.

<details><summary>Regla de cálculo en notación R</summary>

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

Regiones de desarrollo según decreto 710-04
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_regiones_desarrollo_710_04(tbl)
```


Regiones de desarrollo según decreto 710-04
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_PROVINCIA`.

<details><summary>Regla de cálculo en notación R</summary>

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

Registrar una edicion documentada de ENFT

```python
ft.ft_register_dict(con, dictionary, version, valid_from=None, valid_to=None, **kwargs)
```


Registrar una edicion documentada de ENFT


## ft_sector_ocupacion

Sector de ocupación
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_sector_ocupacion(tbl, min_edad=15)
```


Sector de ocupación
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]


**Columnas requeridas:** `EFT_AYUDO_FAM_SEM_ANT`, `EFT_BUSCO_TRAB_MES_ANT`, `EFT_BUSCO_TRAB_SEM_ANT`, `EFT_CANT_PERS_TRAB`, `EFT_CATEGORIA_OCUP_PRINC`, `EFT_COSIO_LAVO_SEM_ANT`, `EFT_CULTIVO_SEM_ANT`, `EFT_EDAD`, `EFT_ELAB_PROD_SEM_ANT`, `EFT_OCUPACION_PRINC`, `EFT_TIENE_COND_JORNADA`, `EFT_TRABAJO_SEM_ANT`, `EFT_TUVO_ACT_ECON_SEM_ANT`.

<details><summary>Regla de cálculo en notación R</summary>

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

Asigna etiquetas de datos a las variables especificadas

```python
ft.ft_setLabels(tbl, dict=None, vars=None)
```


htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


## ft_set_Dict

Asigna etiquetas de datos a las variables especificadas

```python
ft.ft_set_Dict(tbl, dictionary=None, subset=None, *, version=None, at=None, con=None, **kwargs)
```


htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


## ft_set_labels

Asigna etiquetas de datos a las variables especificadas

```python
ft.ft_set_labels(tbl, dict=None, vars=None)
```


htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


## ft_useLabels

Utiliza las etiquetas de datos de una variable/dataset

```python
ft.ft_useLabels(tbl, dict=None, vars=None, **kwargs)
```


htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


## ft_use_labels

Utiliza las etiquetas de datos de una variable/dataset

```python
ft.ft_use_labels(tbl, dict=None, vars=None, **kwargs)
```


htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


## ft_version

Identificar la estructura de los datos ENFT

```python
ft.ft_version(tbl)
```


Distingue nombres de columnas, no revisiones del diccionario ni metodologias.
Una tabla con ambas columnas de periodo es ambigua y se rechaza.


**Columnas requeridas:** `EFT_PERIODO or PERIALFA`.

## ft_with_Dict

Utiliza las etiquetas de datos de una variable/dataset

```python
ft.ft_with_Dict(tbl, dictionary=None, subset=None, **kwargs)
```


htmlhttps://lifecycle.r-lib.org/articles/stages.html#experimentallifecycle-experimental.svgoptions: alt='[Experimental]'[Experimental]


## ft_zona

Zona de residencia
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_zona(tbl)
```


La base de datos de ne ENFT en su primera versión imputaba las zonas de
residencia con los valores de 0 y 1, para compatibilidad con la segunda
versión y la encuesta continua (ENCFT) se crea una variable zona que imputa
los valores como 1 y 2.


**Columnas requeridas:** `EFT_PERIODO + EFT_ZONA or PERIALFA + S1_P4`.

## ft_zona_desarrollo_fronterizo

Zona Especial de Desarrollo Fronterizo de la República Dominicana
htmlhttps://lifecycle.r-lib.org/articles/stages.html#stablelifecycle-stable.svgoptions: alt='[Stable]'[Stable]

```python
ft.ft_zona_desarrollo_fronterizo(tbl)
```


Vea Ley 28-01 de la República Dominicana.


**Columnas requeridas:** `EFT_PROVINCIA`.

<details><summary>Regla de cálculo en notación R</summary>

```r
{
    tbl %>% ft_regiones_desarrollo_710_04() %>% dplyr::mutate(zona_desarrollo_fronterizo = dplyr::case_when(as.numeric(EFT_PROVINCIA) %in% 
        as.numeric(c("16", "10", "07", "05", "15", "26", "03")) ~ 1, TRUE ~ 0))
}
```

</details>

`EnftDataFrame` expone los mismos cálculos como métodos encadenables. Use corchetes para leer columnas cuyo nombre coincida con un método.
