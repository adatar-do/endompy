"""ENGIH 2018 metadata and revisions, matching engihr 0.3.0 in R."""
from functools import wraps as _wraps
import warnings as _warnings
from .metadata import modules, schema, catalog, source_issues, example, dictionary_coverage
from .dictionaries import get_dict, dict_versions, register_dict
from .labeling import set_labels, use_labels, validate
from .dataframe import EngihDataFrame

__all__ = ["modules", "schema", "catalog", "source_issues", "example", "get_dict",
    "dictionary_coverage", "dict_versions", "register_dict", "set_labels", "use_labels", "validate", "EngihDataFrame"]
for _name in tuple(__all__[:-1]):
    _alias = "egi_" + ("dict" if _name == "get_dict" else _name)
    globals()[_alias] = globals()[_name]
    __all__.append(_alias)


def _deprecated(function, alias):
    @_wraps(function)
    def wrapper(*args, **kwargs):
        _warnings.warn(alias + " is deprecated; use " + function.__name__, DeprecationWarning, stacklevel=2)
        return function(*args, **kwargs)
    return wrapper


for _old, _new in (("setLabels", "set_labels"), ("useLabels", "use_labels")):
    globals()[_old] = _deprecated(globals()[_new], _old)
    globals()["egi_" + _old] = globals()[_old]
    __all__ += [_old, "egi_" + _old]
