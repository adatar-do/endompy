"""
EndomDataFrame - Base class for survey DataFrames

Provides a base DataFrame class that integrates with labelerpy
for data labeling functionality.
"""

import pandas as pd

# Try to import labelerpy to register the pandas accessor if available.
try:
    import labelerpy  # noqa: F401
    HAS_LABELERPY = True
except ImportError:
    HAS_LABELERPY = False


class EndomDataFrame(pd.DataFrame):
    """
    Base DataFrame class for Dominican survey data.
    
    Inherits from pandas.DataFrame and optionally integrates with
    labelerpy for data labeling functionality. Survey-specific
    DataFrame classes (like EncftDataFrame) should inherit from this class.
    
    If labelerpy is installed, pandas DataFrames provide:
    - df.labeler.set_dict(): Apply a data dictionary to the DataFrame
    - df.labeler.with_dict(): Replace values with their labels
    
    Examples
    --------
    >>> from endompy import EndomDataFrame
    >>> df = EndomDataFrame({'X': [1, 2, 3]})
    >>> 
    >>> # With labelerpy installed:
    >>> from labelerpy import Dict
    >>> dict = Dict(metadata={"name": "Test"}, variables={"X": {"label": "Variable X"}})
    >>> df = df.labeler.set_dict(dict)
    """
    
    # Preserve these attributes during pandas operations
    _metadata = ["_endom_attrs"]
    
    def __init__(self, data=None, *args, **kwargs):
        """
        Initialize an EndomDataFrame.
        
        Parameters
        ----------
        data : array-like, dict, DataFrame, optional
            Data to create the DataFrame from.
        *args, **kwargs
            Additional arguments passed to pd.DataFrame.
        """
        super().__init__(data, *args, **kwargs)
        self._endom_attrs = {}
    
    @property
    def _constructor(self):
        """Return constructor for pandas operations."""
        return EndomDataFrame
    
    @property
    def _constructor_sliced(self):
        """Return constructor for Series (slicing)."""
        return pd.Series
    
    @classmethod
    def has_labelerpy(cls) -> bool:
        """Check if labelerpy is available."""
        return HAS_LABELERPY
