"""Expanded metadata preserves historical identities and exposes evidence bounds."""
from pathlib import Path
import pandas as pd
import pytest
from endompy import engihr as e


@pytest.mark.parametrize("module", e.modules()["module"])
def test_every_old_definition_is_reused_and_inventory_matches(module):
    old = e.get_dict(module, version="baseline-1").revision()
    dictionary = e.get_dict(module)
    current = dictionary.revision()
    assert current["parent_version"] == "baseline-1"
    assert {name: current["variable_refs"][name] for name in old["variable_refs"]} == old["variable_refs"]
    schema = e.schema(module)
    assert set(schema.loc[schema.documented, "field"]) == set(current["variable_refs"])
    assert e.dict_versions(module)["version"].tolist() == ["baseline-1", "coverage-2"]


def test_source_strength_and_unresolved_fields_are_explicit():
    coverage = e.dictionary_coverage()
    assert coverage["definition_status_counts"] == {"published_header": 523, "official_dictionary": 530, "questionnaire": 647}
    assert coverage["unresolved_fields"]["personas"] == ["HOLGURA", "PERDIDA_TURISMO"]
    assert len(e.dictionary_coverage(True)) == 1700
    assert len(e.dictionary_coverage(True, version="baseline-1")) == 530
    assert e.modules().documented.sum() == 1700
    assert e.modules(version="baseline-1").documented.sum() == 530
    field = e.dictionary_coverage(True)["personas.FACTOR_EXPANSION"]
    assert field["definition_status"] == "published_header"
    assert "no calculation" in field["definition_note"]
    with pytest.raises(ValueError, match="True or False"):
        e.dictionary_coverage(1)
    with pytest.raises(ValueError, match="Revision not bundled"):
        e.schema(version="latest")
    d = e.get_dict()
    assert "HOLGURA" not in d and "PERDIDA_TURISMO" not in d
    assert "piso" in d["A201_APTOS"].label.lower()
    assert "miembros" in d["A401A"].label.lower()
    monthly = [v.label.lower() for key, v in d.variables.items() if key.startswith("D802") and key.endswith("M1_1")]
    assert monthly and not any("enero" in label or "january" in label for label in monthly)


def test_unresolved_columns_are_preserved_without_fabricated_labels():
    data = pd.DataFrame({"HOLGURA": [1, 2], "PERDIDA_TURISMO": [3, 4]})
    labelled = e.set_labels(data)
    pd.testing.assert_frame_equal(labelled, data)
    assert not labelled.attrs.get("labeler_provenance")
