"""Traditional Dominican ENFT: historical indicators, income and dictionary revisions."""
from . import core as _core, indicators as _indicators, poverty as _poverty
from .dictionaries import get_dict, dict_versions, register_dict
from .labeling import set_dict, with_dict, browse_dict
import warnings as _warnings
from functools import wraps as _wraps

__all__ = ['get_dict','dict_versions','register_dict','set_dict','with_dict','browse_dict']
for _module in (_core,_indicators,_poverty):
    for _name,_value in vars(_module).items():
        if not _name.startswith('_') and callable(_value) and getattr(_value,'__module__',None) == _module.__name__:
            globals()[_name] = _value
            __all__.append(_name)


def set_labels(tbl,dict=None,vars=None):
    """Compatibility labeling with the original R argument positions."""
    return set_dict(tbl,dict,subset=vars)


def use_labels(tbl,dict=None,vars=None,**kwargs):
    """Replace codes with value labels while preserving column names."""
    return with_dict(tbl,get_dict() if dict is None else dict,subset=vars,use_label=False,use_labels=True,**kwargs)


__all__ += ['set_labels','use_labels']
for _name in tuple(__all__):
    _alias = 'ft_'+{'get_dict':'dict','set_dict':'set_Dict','with_dict':'with_Dict'}.get(_name,_name)
    globals()[_alias] = globals()[_name]; __all__.append(_alias)


def _deprecated(function,alias):
    @_wraps(function)
    def wrapper(*args,**kwargs):
        _warnings.warn(alias+' is deprecated; use '+function.__name__+'.',DeprecationWarning,stacklevel=2)
        return function(*args,**kwargs)
    return wrapper


for _alias,_name in {'compute_peri_vars':'peri_vars',
                     'compute_zona':'zona','regiones_desarrollo':'regiones_desarrollo_710_04',
                     'setLabels':'set_labels','useLabels':'use_labels'}.items():
    globals()[_alias] = _deprecated(globals()[_name],_alias)
    globals()['ft_'+_alias] = globals()[_alias]
    __all__ += [_alias,'ft_'+_alias]


def ano(tbl):
    """Deprecated year-only compatibility wrapper."""
    _warnings.warn('Use peri_vars.',DeprecationWarning,stacklevel=2)
    return peri_vars(tbl,semestre=False,periodo=False)


compute_ano = ft_compute_ano = ft_ano = ano
__all__ += ['ano','compute_ano','ft_ano','ft_compute_ano']

from .dataframe import EnftDataFrame
__all__.append('EnftDataFrame')
