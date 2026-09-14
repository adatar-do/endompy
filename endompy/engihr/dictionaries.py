"""Module-scoped ENGIH revisions interoperable with labeler and engihr in R."""
from labelerpy import Dict, RevisionRegistry
from labelerpy.labeling import ensure_dict
import pandas as pd
from .metadata import RESOURCE, _module, _metadata_version


def _identity(dictionary, module, edition, at=None, required=False):
    revision = dictionary.revision(at=at)
    metadata = dictionary.metadata.to_dict()
    if required or "module" in metadata:
        if metadata.get("module") != module:
            raise ValueError("Dictionary module does not match requested module")
    if required or "edition" in metadata:
        if metadata.get("edition") != edition:
            raise ValueError("Dictionary edition does not match requested edition")
    if required and (revision is None or revision["dictionary_id"] != "engih-2018-" + module):
        raise ValueError("Dictionary identity does not match module/edition")
    return dictionary


def get_dict(module="personas", edition=2018, version=None, at=None, con=None):
    """Select coverage-2, an explicit baseline-1, or an exact registry revision/applicability date."""
    _module(module, edition)
    if con is not None:
        dictionary = RevisionRegistry(con).load("engih-2018-" + module, version=version, at=at)
    else:
        version = _metadata_version(version)
        dictionary = Dict.from_json(RESOURCE / "dictionaries" / (module + "-" + version + ".json"))
    return _identity(dictionary, module, edition, at, required=True)


def dict_versions(module="personas", edition=2018, con=None):
    """List revision identity, parent, dates, author, message and content fingerprint."""
    _module(module, edition)
    if con is not None:
        return RevisionRegistry(con).list_versions("engih-2018-" + module)
    fields = ["dictionary_id", "version", "parent_version", "created_at", "author", "message",
        "valid_from", "valid_to", "content_hash"]
    revisions = [get_dict(module, edition, version).revision() for version in ("baseline-1", "coverage-2")]
    return pd.DataFrame([{key: revision[key] for key in fields} for revision in revisions])


def register_dict(con, dictionary, version, module="personas", edition=2018,
                  valid_from=None, valid_to=None, **kwargs):
    """Register a Dict draft, reusing unchanged definitions and caller-owned transactions."""
    _module(module, edition)
    if not isinstance(dictionary, Dict) or not dictionary.is_valid():
        raise ValueError("dictionary must be a valid Dict draft")
    metadata = dictionary.metadata.to_dict()
    if metadata.get("module") != module or metadata.get("edition") != edition:
        raise ValueError("Dictionary module/edition metadata must match")
    return RevisionRegistry(con).register(dictionary, version, dictionary_id="engih-2018-" + module,
        valid_from=valid_from, valid_to=valid_to, **kwargs)


def _resolve(dictionary, module, edition, version, at, con):
    _module(module, edition)
    if dictionary is None:
        return get_dict(module, edition, version, at, con)
    if version is not None or con is not None:
        raise ValueError("Supply either dictionary or a registry/version selection")
    dictionary = ensure_dict(dictionary)
    if not dictionary.is_valid():
        raise ValueError("Invalid dictionary or revision integrity mismatch")
    return _identity(dictionary, module, edition, at)
