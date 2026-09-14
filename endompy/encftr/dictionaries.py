"""ENCFT dictionary editions, independent from poverty methodologies."""

from pathlib import Path

from labelerpy import Dict, RevisionRegistry
import pandas as pd


def get_dict(version=None, at=None, con=None):
    """Load an exact ENCFT revision, or a documented edition applicable at a date.

    The bundled ``baseline-1`` has no asserted historical date applicability.
    A SQLite connection can contain user-registered, dated survey editions.
    Ambiguous or unknown dates raise ValueError. Returned dictionaries are detached.
    """
    if con is not None:
        return RevisionRegistry(con).load("encft", version=version, at=at)
    version = "baseline-1" if version is None else version
    if not isinstance(version, str) or version != "baseline-1":
        raise ValueError("Revision not bundled; use dict_versions() or supply con.")
    result = Dict.from_json(Path(__file__).parent / "resources" / "baseline-1.json")
    result.revision(at=at)
    return result


def dict_versions(con=None):
    """List revision metadata, including explicit applicability and content hash."""
    if con is not None:
        return RevisionRegistry(con).list_versions("encft")
    revision = get_dict().revision()
    fields = ["dictionary_id", "version", "parent_version", "created_at", "author",
              "message", "valid_from", "valid_to", "content_hash"]
    return pd.DataFrame([{key: revision[key] for key in fields}])


def register_dict(con, dictionary, version, valid_from=None, valid_to=None, **kwargs):
    """Register a complete documented edition, reusing unchanged definitions.

    ``kwargs`` accepts parent_version, author, message and explicit renames.
    The caller retains ownership of the SQLite connection and transaction.
    """
    return RevisionRegistry(con).register(dictionary, version, dictionary_id="encft",
        valid_from=valid_from, valid_to=valid_to, **kwargs)
