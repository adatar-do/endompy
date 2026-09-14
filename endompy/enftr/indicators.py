"""ENFT indicators compiled from the reviewed R package. Do not edit by hand."""
from .rules import run_rule

def alfabeta(tbl, min_edad=15):
    """Apply enftr::ft_alfabeta; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "alfabeta", min_edad=min_edad)

def anos_educacion(tbl):
    """Apply enftr::ft_anos_educacion; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "anos_educacion")

def cantidad_personas_trabajan(tbl):
    """Apply enftr::ft_cantidad_personas_trabajan; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "cantidad_personas_trabajan")

def categoria_ocupacion_principal(tbl):
    """Apply enftr::ft_categoria_ocupacion_principal; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "categoria_ocupacion_principal")

def desempleo_abierto(tbl, min_edad=15):
    """Apply enftr::ft_desempleo_abierto; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "desempleo_abierto", min_edad=min_edad)

def desempleo_ampliado(tbl, min_edad=15):
    """Apply enftr::ft_desempleo_ampliado; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "desempleo_ampliado", min_edad=min_edad)

def desempleo_cesante_abierto(tbl, min_edad=15):
    """Apply enftr::ft_desempleo_cesante_abierto; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "desempleo_cesante_abierto", min_edad=min_edad)

def desempleo_cesante_ampliado(tbl, min_edad=15):
    """Apply enftr::ft_desempleo_cesante_ampliado; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "desempleo_cesante_ampliado", min_edad=min_edad)

def desempleo_nuevo_abierto(tbl, min_edad=15):
    """Apply enftr::ft_desempleo_nuevo_abierto; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "desempleo_nuevo_abierto", min_edad=min_edad)

def desempleo_nuevo_ampliado(tbl, min_edad=15):
    """Apply enftr::ft_desempleo_nuevo_ampliado; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "desempleo_nuevo_ampliado", min_edad=min_edad)

def dias_semana_ocupacion_principal(tbl):
    """Apply enftr::ft_dias_semana_ocupacion_principal; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "dias_semana_ocupacion_principal")

def dominios_inferencia(tbl):
    """Apply enftr::ft_dominios_inferencia; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "dominios_inferencia")

def dominios_inferencia1(tbl):
    """Apply enftr::ft_dominios_inferencia1; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "dominios_inferencia1")

def dominios_inferencia2(tbl):
    """Apply enftr::ft_dominios_inferencia2; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "dominios_inferencia2")

def dominios_inferencia3(tbl):
    """Apply enftr::ft_dominios_inferencia3; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "dominios_inferencia3")

def grupo_ocupacion(tbl, min_edad=15):
    """Apply enftr::ft_grupo_ocupacion; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "grupo_ocupacion", min_edad=min_edad)

def grupo_rama(tbl):
    """Apply enftr::ft_grupo_rama; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "grupo_rama")

def horas_semanal(tbl, min_edad=15):
    """Apply enftr::ft_horas_semanal; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "horas_semanal", min_edad=min_edad)

def ing_alqui_renta_propiedades(tbl):
    """Apply enftr::ft_ing_alqui_renta_propiedades; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_alqui_renta_propiedades")

def ing_alquiler_anual(tbl):
    """Apply enftr::ft_ing_alquiler_anual; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_alquiler_anual")

def ing_ayuda_gobierno(tbl):
    """Apply enftr::ft_ing_ayuda_gobierno; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_ayuda_gobierno")

def ing_beneficios_marginales(tbl):
    """Apply enftr::ft_ing_beneficios_marginales; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_beneficios_marginales")

def ing_bonificaciones(tbl):
    """Apply enftr::ft_ing_bonificaciones; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_bonificaciones")

def ing_comisiones(tbl):
    """Apply enftr::ft_ing_comisiones; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_comisiones")

def ing_dividendos(tbl):
    """Apply enftr::ft_ing_dividendos; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_dividendos")

def ing_especie_alimentos(tbl):
    """Apply enftr::ft_ing_especie_alimentos; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_especie_alimentos")

def ing_especie_auto(tbl):
    """Apply enftr::ft_ing_especie_auto; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_especie_auto")

def ing_especie_ayuda_ong(tbl):
    """Apply enftr::ft_ing_especie_ayuda_ong; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_especie_ayuda_ong")

def ing_especie_celulares(tbl):
    """Apply enftr::ft_ing_especie_celulares; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_especie_celulares")

def ing_especie_otros(tbl):
    """Apply enftr::ft_ing_especie_otros; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_especie_otros")

def ing_especie_transporte(tbl):
    """Apply enftr::ft_ing_especie_transporte; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_especie_transporte")

def ing_especie_vestido(tbl):
    """Apply enftr::ft_ing_especie_vestido; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_especie_vestido")

def ing_especie_viviendas(tbl):
    """Apply enftr::ft_ing_especie_viviendas; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_especie_viviendas")

def ing_gobierno_anual(tbl):
    """Apply enftr::ft_ing_gobierno_anual; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_gobierno_anual")

def ing_horas_extras(tbl):
    """Apply enftr::ft_ing_horas_extras; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_horas_extras")

def ing_interes_anual(tbl):
    """Apply enftr::ft_ing_interes_anual; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_interes_anual")

def ing_intereses_dividendo(tbl):
    """Apply enftr::ft_ing_intereses_dividendo; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_intereses_dividendo")

def ing_ocup_prin(tbl):
    """Apply enftr::ft_ing_ocup_prin; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_ocup_prin")

def ing_ocup_secun(tbl):
    """Apply enftr::ft_ing_ocup_secun; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_ocup_secun")

def ing_pension_anual(tbl):
    """Apply enftr::ft_ing_pension_anual; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_pension_anual")

def ing_pension_jubilacion(tbl):
    """Apply enftr::ft_ing_pension_jubilacion; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_pension_jubilacion")

def ing_propinas(tbl):
    """Apply enftr::ft_ing_propinas; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_propinas")

def ing_regalia_pascual(tbl):
    """Apply enftr::ft_ing_regalia_pascual; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_regalia_pascual")

def ing_remesas_anual(tbl):
    """Apply enftr::ft_ing_remesas_anual; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_remesas_anual")

def ing_remesas_nac(tbl):
    """Apply enftr::ft_ing_remesas_nac; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_remesas_nac")

def ing_utilidades_empresariales(tbl):
    """Apply enftr::ft_ing_utilidades_empresariales; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_utilidades_empresariales")

def ing_vacaciones(tbl):
    """Apply enftr::ft_ing_vacaciones; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ing_vacaciones")

def ingreso_laboral_mensual(tbl, min_edad=15):
    """Apply enftr::ft_ingreso_laboral_mensual; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ingreso_laboral_mensual", min_edad=min_edad)

def ocupado(tbl, min_edad=15):
    """Apply enftr::ft_ocupado; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "ocupado", min_edad=min_edad)

def pea_abierta(tbl, min_edad=15):
    """Apply enftr::ft_pea_abierta; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "pea_abierta", min_edad=min_edad)

def pea_ampliada(tbl, min_edad=15):
    """Apply enftr::ft_pea_ampliada; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "pea_ampliada", min_edad=min_edad)

def perceptores_ingresos(tbl, min_edad=15):
    """Apply enftr::ft_perceptores_ingresos; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "perceptores_ingresos", min_edad=min_edad)

def pet(tbl, min_edad=15):
    """Apply enftr::ft_pet; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "pet", min_edad=min_edad)

def poblacion_inactiva(tbl, min_edad=15):
    """Apply enftr::ft_poblacion_inactiva; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "poblacion_inactiva", min_edad=min_edad)

def regiones_desarrollo_685_00(tbl):
    """Apply enftr::ft_regiones_desarrollo_685_00; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "regiones_desarrollo_685_00")

def regiones_desarrollo_710_04(tbl):
    """Apply enftr::ft_regiones_desarrollo_710_04; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "regiones_desarrollo_710_04")

def sector_ocupacion(tbl, min_edad=15):
    """Apply enftr::ft_sector_ocupacion; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "sector_ocupacion", min_edad=min_edad)

def zona_desarrollo_fronterizo(tbl):
    """Apply enftr::ft_zona_desarrollo_fronterizo; preserve input rows, order and index.

    See ENFT reference for required columns, codes and historical scope.
    """
    return run_rule(tbl, "zona_desarrollo_fronterizo")
