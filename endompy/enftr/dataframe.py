"""Chainable traditional ENFT data frame with the same calculation functions."""
from functools import wraps
from importlib import import_module
import pandas as pd
from endompy.base import EndomDataFrame


class EnftDataFrame(EndomDataFrame):
    """Local member table for the traditional ENFT; distinct from EncftDataFrame."""
    @property
    def _constructor(self): return EnftDataFrame
    @property
    def _constructor_sliced(self): return pd.Series
    def set_dict(self,dict=None,**kwargs):
        """Apply the ENFT dictionary or a selected registered revision."""
        from .labeling import set_dict
        return set_dict(self,dict,**kwargs)


def _method(function):
    @wraps(function)
    def method(self,*args,**kwargs):
        result = function(self,*args,**kwargs)
        return EnftDataFrame(result).__finalize__(result)
    return method


for _module in (import_module('endompy.enftr.'+name) for name in ('core','indicators','poverty')):
    for _name,_value in vars(_module).items():
        if not _name.startswith('_') and _name != 'version' and callable(_value) and getattr(_value,'__module__',None) == _module.__name__:
            setattr(EnftDataFrame,_name,_method(_value))
