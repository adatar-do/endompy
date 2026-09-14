"""ENHOGAR 2018: local labour proxies and versioned dictionaries."""
from functools import wraps as _wraps
import warnings as _warnings
from .core import (pet,ocupado,desocupado,pea,inactivo,fuerza_trabajo_potencial,
    enhogar_edition,get_enhogar_edition,guess_enhogar_edition,enhogar_example)
from .dictionaries import (get_dict,dict_versions,register_dict,set_labels,use_labels,browse_dict,
    dict_modules,dictionary_coverage)

__all__=['pet','ocupado','desocupado','pea','inactivo','fuerza_trabajo_potencial',
    'enhogar_edition','get_enhogar_edition','guess_enhogar_edition','enhogar_example',
    'get_dict','dict_versions','register_dict','set_labels','use_labels','browse_dict',
    'dict_modules','dictionary_coverage']
for _name in tuple(__all__):
    if 'enhogar_' not in _name:
        _alias='ehg_'+('dict' if _name=='get_dict' else _name)
        globals()[_alias]=globals()[_name]; __all__.append(_alias)


def _deprecated(function,alias):
    @_wraps(function)
    def wrapper(*args,**kwargs):
        _warnings.warn(alias+' is deprecated; use '+function.__name__,DeprecationWarning,stacklevel=2)
        return function(*args,**kwargs)
    return wrapper


for _old,_new in [('setLabels','set_labels'),('useLabels','use_labels')]:
    globals()[_old]=_deprecated(globals()[_new],_old)
    globals()['ehg_'+_old]=globals()[_old]; __all__ += [_old,'ehg_'+_old]

from .dataframe import EnhogarDataFrame
__all__.append('EnhogarDataFrame')
