"""Convenience DataFrame with the same ENGIH contracts as the functional API."""
from functools import wraps
import pandas as pd
from endompy.base import EndomDataFrame
from . import labeling


class EngihDataFrame(EndomDataFrame):
    """Local ENGIH table. Choose module explicitly for non-Personas worksheets."""
    @property
    def _constructor(self):
        return EngihDataFrame

    @property
    def _constructor_sliced(self):
        return pd.Series

    def validate(self, *args, **kwargs):
        """Return an ordinary per-field diagnostic table, not respondent rows."""
        return labeling.validate(self, *args, **kwargs)


def _method(function):
    @wraps(function)
    def method(self, *args, **kwargs):
        return function(self, *args, **kwargs)
    return method


for _name in ("set_labels", "use_labels"):
    setattr(EngihDataFrame, _name, _method(getattr(labeling, _name)))
