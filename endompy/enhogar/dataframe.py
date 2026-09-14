"""Chainable ENHOGAR tables using the same public calculations."""
from functools import wraps
import pandas as pd
from endompy.base import EndomDataFrame
from . import core, dictionaries


class EnhogarDataFrame(EndomDataFrame):
    """Local ENHOGAR 2018 table; rows, index and metadata survive calculations."""
    @property
    def _constructor(self): return EnhogarDataFrame
    @property
    def _constructor_sliced(self): return pd.Series


def _method(function):
    @wraps(function)
    def method(self,*args,**kwargs):
        result=function(self,*args,**kwargs)
        return EnhogarDataFrame(result).__finalize__(result)
    return method


for _name in ['pet','ocupado','desocupado','pea','inactivo','fuerza_trabajo_potencial']:
    setattr(EnhogarDataFrame,_name,_method(getattr(core,_name)))
for _name in ['set_labels','use_labels']:
    setattr(EnhogarDataFrame,_name,_method(getattr(dictionaries,_name)))
