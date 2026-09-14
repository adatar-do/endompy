"""ENCFT calculations, dictionary revisions and a chainable pandas DataFrame.

Use explicit pobreza_monetaria_2012 or pobreza_monetaria_2022. Dictionary
revisions describe the questionnaire and are independent of poverty methodology.
"""
from . import core as _core, education as _education, indicators as _indicators
from . import poverty as _poverty, iih as _iih, icv as _icv
from .dictionaries import get_dict, dict_versions, register_dict
from .labeling import set_dict, with_dict, browse_dict

__all__ = ["get_dict", "dict_versions", "register_dict", "set_dict", "with_dict", "browse_dict"]
for _module in (_core, _education, _indicators, _poverty, _iih, _icv):
    for _name, _value in vars(_module).items():
        if not _name.startswith("_") and callable(_value) and getattr(_value, "__module__", None) == _module.__name__:
            if _name not in ("require_columns", "quarter_parts", "normalize_currency"):
                globals()[_name] = _value
                __all__.append(_name)

# Python entry points retain the R names for migration and paired scripts.
for _name in tuple(__all__):
    _alias = "ftc_" + {"get_dict": "dict", "set_dict": "set_Dict", "with_dict": "with_Dict"}.get(_name, _name)
    globals()[_alias] = globals()[_name]
    __all__.append(_alias)

from .dataframe import EncftDataFrame
__all__.append("EncftDataFrame")

import warnings as _warnings
from functools import wraps as _wraps


def _deprecated(function, alias):
    @_wraps(function)
    def wrapper(*args, **kwargs):
        _warnings.warn(alias + " is deprecated; use " + function.__name__ + ".", DeprecationWarning, stacklevel=2)
        return function(*args, **kwargs)
    return wrapper


_old_names = {"compute_" + name: name for name in ("alfabetizacion", "anos_educacion", "asistencia_escolar",
    "grupos_edad", "hacinamiento", "matriculacion_escolar", "sobreedad_escolar",
    "tasa_alfabetizacion_hogar", "tasa_dependencia", "trabajo_infantil")}
_old_names.update({"compute_factor_exp_anual": "factor_expansion_anual", "factor_exp_anual": "factor_expansion_anual",
                   "compute_region": "regiones_desarrollo", "pobreza_monetaria": "pobreza_monetaria_2012"})
for _alias, _name in _old_names.items():
    globals()[_alias] = _deprecated(globals()[_name], _alias)
    globals()["ftc_" + _alias] = globals()[_alias]
    __all__.extend([_alias, "ftc_" + _alias])


def set_labels(tbl, dictionary=None, vars=None):
    """Deprecated compatibility entry point; use set_dict(..., subset=...)."""
    _warnings.warn("Use set_dict.", DeprecationWarning, stacklevel=2)
    return set_dict(tbl, dictionary, subset=vars)


def use_labels(tbl, dictionary=None, vars=None, **kwargs):
    """Deprecated compatibility entry point; use with_dict(..., use_label=False)."""
    _warnings.warn("Use with_dict.", DeprecationWarning, stacklevel=2)
    return with_dict(tbl, get_dict() if dictionary is None else dictionary, subset=vars,
                     use_label=False, use_labels=True, **kwargs)


for _name, _function in {"ftc_set_labels": set_labels, "ftc_setLabels": set_labels,
                        "ftc_use_labels": use_labels, "ftc_useLabels": use_labels}.items():
    globals()[_name] = _function
    __all__.append(_name)
__all__.extend(["set_labels", "use_labels"])


def ftc0_compute_icv_siuben(tbl):
    """Deprecated encftr0 entry point; use icv_siuben."""
    _warnings.warn("Use icv_siuben.", DeprecationWarning, stacklevel=2)
    return icv_siuben(tbl)


def ftc0_setLabels(tbl, vars=None):
    """Deprecated encftr0 labeling; questionnaire and ICV labels, selected columns."""
    _warnings.warn("Use set_dict and set_labels_icv_siuben.", DeprecationWarning, stacklevel=2)
    return set_labels_icv_siuben(set_dict(tbl, subset=vars), vars=vars)


def ftc0_setLabels_icv_global(tbl):
    """Deprecated encftr0 ICV classification labeling."""
    _warnings.warn("Use set_labels_icv_siuben.", DeprecationWarning, stacklevel=2)
    return set_labels_icv_siuben(tbl, vars=["icv_global"])


def ftc0_useLabels(tbl, vars=None):
    """Deprecated encftr0 code-to-category conversion, respecting selected columns."""
    _warnings.warn("Use with_dict and use_labels_icv_siuben.", DeprecationWarning, stacklevel=2)
    labeled = set_labels_icv_siuben(set_dict(tbl, subset=vars), vars=vars)
    return with_dict(labeled, dictionary=None, subset=vars, use_label=False, use_labels=True)


__all__.extend(["ftc0_compute_icv_siuben", "ftc0_setLabels", "ftc0_setLabels_icv_global", "ftc0_useLabels"])
