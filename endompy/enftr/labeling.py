"""Survey-specific entry points to labelerpy metadata and value labels."""
from labelerpy.labeling import set_dict as _set_dict, with_dict as _with_dict
from .dictionaries import get_dict


def set_dict(tbl, dictionary=None, subset=None, *, version=None, at=None, con=None, **kwargs):
    """Apply an explicit dictionary or a bundled/registered questionnaire edition."""
    if dictionary is not None and (version is not None or con is not None):
        raise ValueError("Supply dictionary or version/con, not both.")
    if dictionary is None:
        dictionary = get_dict(version=version, at=at, con=con)
    return _set_dict(tbl, dictionary, subset=subset, at=at, **kwargs)


def with_dict(tbl, dictionary=None, subset=None, **kwargs):
    """Use variable and value labels, preserving unknown-code policy from labelerpy."""
    return _with_dict(tbl, dictionary, subset=subset, **kwargs)


def browse_dict(version=None, at=None, con=None):
    """Return the selected dictionary as a pandas table for notebooks or export."""
    return get_dict(version=version, at=at, con=con).to_frame()
