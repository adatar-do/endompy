"""ENGIH contracts and differential checks against a fresh engihr oracles for historical and expanded revisions."""
from pathlib import Path
import json
import sqlite3
import numpy as np
import pandas as pd
import pytest
from labelerpy import Dict, RevisionRegistry
from endompy import EngihDataFrame, engihr as e

FIXTURES = Path(__file__).parent / "fixtures/engih"
MODULES = list(e.modules()["module"])


def read(name):
    return json.loads((FIXTURES / (name + ".json")).read_text(encoding="utf-8"))


@pytest.mark.parametrize("version", ["baseline-1", "coverage-2"])
@pytest.mark.parametrize("module", MODULES)
def test_every_module_matches_fresh_r_labels_levels_missingness_validation_and_provenance(module, version):
    directory = FIXTURES if version == "baseline-1" else FIXTURES.parent / "engih-full"
    oracle = json.loads((directory / (module + ".json")).read_text(encoding="utf-8"))
    x = pd.DataFrame(oracle["input"])
    original = x.copy(deep=True)
    x.index = pd.Index([i // 2 for i in range(len(x))], name="repeated")
    original.index = x.index
    dictionary = e.get_dict(module, version=version)
    assert dictionary.revision() == oracle["revision"]
    labelled = e.set_labels(x, dictionary, module=module)
    assert labelled.attrs.get("labeler_provenance") == oracle["provenance"]
    # Provenance is checked above. Compare data separately so pandas 3 does not
    # deepcopy the entire 1,130-variable dictionary on every column inspection.
    labelled_values = labelled.copy(deep=False)
    labelled_values.attrs = {}
    pd.testing.assert_frame_equal(labelled_values, original)
    assert not x.attrs
    presented = e.use_labels(x, dictionary, module=module)
    pd.testing.assert_index_equal(presented.index, x.index)
    presented_values = presented.copy(deep=False)
    presented_values.attrs = {}
    for name, values in oracle["display"].items():
        actual = presented_values[name].astype(object).where(presented_values[name].notna(), None).tolist()
        assert actual == values, name
    levels = oracle["levels"] or {}
    for name, expected in levels.items():
        assert list(presented_values[name].cat.categories) == expected, name
    assert [name for name in presented_values if isinstance(presented_values[name].dtype, pd.CategoricalDtype)] == list(levels)
    pd.testing.assert_frame_equal(e.validate(x, dictionary, module=module), pd.DataFrame(oracle["validation"]), check_dtype=False)
    pd.testing.assert_frame_equal(e.schema(module, version=version), pd.DataFrame(oracle["schema"]), check_dtype=False)
    pd.testing.assert_frame_equal(x, original)


def test_metadata_catalogs_and_source_decisions_match_r():
    oracle = read("metadata")
    # jsonlite emits R's named row index as _row; pandas keeps it as an index.
    expected_modules = pd.DataFrame(oracle["modules"]).drop(columns=["_row"], errors="ignore")
    pd.testing.assert_frame_equal(e.modules(version="baseline-1"), expected_modules, check_dtype=False)
    pd.testing.assert_frame_equal(e.source_issues(), pd.DataFrame(oracle["issues"]), check_dtype=False)
    for catalog, values in oracle["catalogs"].items():
        pd.testing.assert_frame_equal(e.catalog(catalog), pd.DataFrame(values), check_dtype=False)
    assert e.modules()["fields"].sum() == 1702
    assert e.modules(version="baseline-1")["documented"].sum() == 530
    assert e.schema(version="baseline-1")["documented"].sum() == 386
    assert e.get_dict()["A101"].labels is None
    assert e.get_dict()["A102"].labels is None
    assert not e.schema(version="baseline-1").set_index("field").loc["FACTOR_EXPANSION", "documented"]


@pytest.mark.parametrize("edition", [2022, "2018", True, None, [2018], float("nan")])
def test_unsupported_or_ambiguous_editions_fail(edition):
    with pytest.raises(ValueError, match="Only ENGIH 2018"):
        e.get_dict(edition=edition)


def test_registry_reuses_definitions_reloads_and_preserves_caller_transactions(tmp_path):
    database = tmp_path / "registry.sqlite"
    with sqlite3.connect(database) as con:
        baseline = e.get_dict("b1", version="baseline-1")
        RevisionRegistry(con).import_revision(baseline)
        with pytest.raises(ValueError, match="exact version"):
            e.get_dict("b1", con=con)
        draft = baseline.draft()
        field = "FREC_COMPRA_ALIMENTOS"
        draft[field].label = "Frecuencia revisada"
        revised = e.register_dict(con, draft, "review-2", module="b1", valid_from="2020-01-01", valid_to="2020-12-31")
        before, after = baseline.revision()["variable_refs"], revised.revision()["variable_refs"]
        assert before[field]["variable_id"] == after[field]["variable_id"]
        assert before[field]["definition_hash"] != after[field]["definition_hash"]
        assert {k: v for k, v in before.items() if k != field} == {k: v for k, v in after.items() if k != field}
        assert e.get_dict("b1", con=con, version="baseline-1").to_dict() == baseline.to_dict()
        assert e.get_dict("b1", con=con, at="2020-06-01").to_dict() == revised.to_dict()
        with pytest.raises(ValueError, match="apply|applicab"):
            e.get_dict("b1", con=con, version="review-2", at="2021-01-01")
        with pytest.raises(ValueError, match="immutable"):
            e.register_dict(con, draft, "review-2", module="b1")
        with pytest.raises(ValueError, match="module/edition"):
            e.register_dict(con, draft, "wrong", module="personas")
        con.execute("BEGIN")
        e.register_dict(con, revised.draft(), "temporary", module="b1")
        assert len(e.dict_versions("b1", con=con)) == 3
        con.rollback()
        assert len(e.dict_versions("b1", con=con)) == 2
        con.execute("SELECT 1")
    with sqlite3.connect(database) as con:
        assert e.get_dict("b1", version="review-2", con=con).revision() == revised.revision()


def test_revision_identity_integrity_and_selector_conflicts():
    with pytest.raises(ValueError, match="Unknown module"):
        e.get_dict("../personas")
    with pytest.raises(ValueError, match="Unknown catalog"):
        e.catalog("bad")
    with pytest.raises(ValueError, match="Revision not bundled"):
        e.get_dict(version="missing")
    with pytest.raises(ValueError, match="interval|applicab|valid"):
        e.get_dict(at="2018-01-01")
    with pytest.raises(ValueError, match="module"):
        e.set_labels(e.example(), e.get_dict("b1"))
    with pytest.raises(ValueError, match="either"):
        e.set_labels(e.example(), e.get_dict(), version="baseline-1")
    corrupt = e.get_dict("b1")
    corrupt["TENDRA_GASTO_EXTRA"].label = "changed without a draft"
    with pytest.raises(ValueError, match="integrity|fingerprint"):
        e.set_labels(pd.DataFrame({"TENDRA_GASTO_EXTRA": [1]}), corrupt, module="b1")


def test_selection_empty_tables_and_chaining_preserve_the_table():
    x = EngihDataFrame(e.example())
    x.index = [8, 8, 1, 1, 4]
    original = x.copy(deep=True)
    out = x.set_labels(vars=["A201"])
    assert isinstance(out, EngihDataFrame)
    assert list(out.attrs["labeler_provenance"]) == ["A201"]
    assert isinstance(out.use_labels(vars=["A201"]), EngihDataFrame)
    assert type(out.validate()) is pd.DataFrame
    pd.testing.assert_frame_equal(e.set_labels(x, vars=[]), original)
    empty = pd.DataFrame({"A201": pd.Series([], dtype=float)})
    assert e.use_labels(empty).empty
    assert e.validate(pd.DataFrame()).columns.tolist() == ["field", "status", "n", "missing", "unknown"]
    pd.testing.assert_frame_equal(x, original)


@pytest.mark.parametrize("vars", ["A201", ["missing"], ["A201", "A201"], [None], 7])
def test_bad_subsets_fail(vars):
    with pytest.raises(ValueError, match="vars"):
        e.set_labels(e.example(), vars=vars)


@pytest.mark.parametrize("tbl", [[1], pd.DataFrame([[1, 2]], columns=["A201", "A201"]), pd.DataFrame({"": [1]}), pd.DataFrame({1: [1]})])
def test_invalid_tables_fail(tbl):
    with pytest.raises((ValueError, TypeError), match="DataFrame|Column"):
        e.validate(tbl)


@pytest.mark.parametrize("values", [pd.Series(["1", "2"]), pd.Series([True, False]), pd.Series([1, "2"], dtype=object), pd.Series(pd.Categorical([1, 2]))])
def test_incompatible_codes_are_never_coerced(values):
    x = pd.DataFrame({"A201": values})
    assert e.validate(x).loc[0, "status"] == "type_mismatch"
    with pytest.raises(ValueError, match="Incompatible code type"):
        e.set_labels(x)


@pytest.mark.parametrize("dtype", ["float64", "Int64", "object", "boolean"])
def test_all_missing_columns_and_nullable_values_keep_missingness(dtype):
    x = pd.DataFrame({"A201": pd.Series([None, None], dtype=dtype)})
    pd.testing.assert_frame_equal(e.set_labels(x), x)
    assert e.use_labels(x)["A201"].isna().all()


def test_unknown_codes_strict_mode_legacy_aliases_and_display_collision():
    x = pd.DataFrame({"A201": [1234, None]})
    assert e.validate(x).loc[0, "unknown"] == 1
    assert e.use_labels(x).loc[0, "A201"] == "1234"
    with pytest.raises(ValueError, match="Unknown codes"):
        e.set_labels(x, strict=True)
    with pytest.raises(ValueError, match="strict"):
        e.set_labels(x, strict=1)
    custom = {"X": {"lab": "Question", "labs": {"Shown": "a", "Second": "b"}}}
    values = pd.DataFrame({"X": ["a", "Shown", None, "other"]})
    out = e.use_labels(values, custom)
    assert out["X"].cat.categories.tolist() == ["Shown", "Second", "[unlabelled code: Shown]", "other"]
    assert out.loc[1, "X"] == "[unlabelled code: Shown]"
    with pytest.warns(DeprecationWarning):
        pd.testing.assert_frame_equal(e.egi_setLabels(values, custom), e.set_labels(values, custom))
    with pytest.warns(DeprecationWarning):
        pd.testing.assert_frame_equal(e.egi_useLabels(values, custom), out)
    assert e.egi_dict is e.get_dict and e.egi_validate is e.validate


def test_get_dict_returns_detached_objects_and_does_not_cross_editions():
    first = e.get_dict()
    first["A101"].label = "caller mutation"
    assert e.get_dict()["A101"].label != "caller mutation"
    other = Dict(metadata={"name": "custom", "edition": 2022}, variables={"A201": {"label": "Other edition"}})
    with pytest.raises(ValueError, match="module|edition"):
        e.set_labels(e.example(), other)
