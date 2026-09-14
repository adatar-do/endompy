"""Chainable ENCFT DataFrame; calculations are also available as pure functions."""
from functools import wraps
import pandas as pd
from endompy.base import EndomDataFrame


class EncftDataFrame(EndomDataFrame):
    """A pandas DataFrame with ENCFT calculations and dictionary labeling.

    Examples
    --------
    >>> x = EncftDataFrame({'FACTOR_EXPANSION': [100, 200]})
    >>> x.factor_expansion_anual(periods=4)['factor_expansion_anual'].tolist()
    [25.0, 50.0]
    """
    _metadata = ["_encft_attrs", "_endom_attrs"]

    def __init__(self, data=None, *args, **kwargs):
        super().__init__(data, *args, **kwargs)
        self._encft_attrs = {}

    @property
    def _constructor(self):
        return EncftDataFrame

    @property
    def _constructor_sliced(self):
        return pd.Series

    def set_dict(self, dict=None, **kwargs):
        """Apply ENCFT dictionary metadata; accepts version, at and con."""
        from .labeling import set_dict
        return set_dict(self, dictionary=dict, **kwargs)


def _method(function):
    @wraps(function)
    def method(self, *args, **kwargs):
        result = function(self, *args, **kwargs)
        return EncftDataFrame(result).__finalize__(result)
    return method


# Bind the same reviewed functions; each wrapper preserves metadata and subclass.
from importlib import import_module
for _module in (import_module("endompy.encftr." + name) for name in ("core", "education", "indicators", "poverty", "iih", "icv")):
    for _name, _value in vars(_module).items():
        if not _name.startswith("_") and callable(_value) and getattr(_value, "__module__", None) == _module.__name__:
            if _name not in ("require_columns", "quarter_parts", "normalize_currency", "variables_iih", "variables_icv_siuben", "dict_icv_siuben"):
                setattr(EncftDataFrame, _name, _method(_value))
