import sqlite3
import pytest
from endompy import encftr


def test_one_changed_variable_reuses_the_other_635_definitions():
    with sqlite3.connect(":memory:") as con:
        first = encftr.register_dict(con, encftr.get_dict().draft(), "example-1",
            valid_from="2020-01-01", valid_to="2020-12-31")
        draft = first.draft()
        draft["SEXO"].label = "Sexo de la persona"
        second = encftr.register_dict(con, draft, "example-2",
            valid_from="2021-01-01", valid_to="2021-12-31")
        a, b = first.revision()["variable_refs"], second.revision()["variable_refs"]
        assert sum(a[name]["definition_hash"] == b[name]["definition_hash"] for name in a) == 635
        assert encftr.get_dict(at="2021-04-01", con=con).revision()["version"] == "example-2"
        assert len(encftr.dict_versions(con)) == 2
        assert encftr.get_dict(version="example-1", con=con)["SEXO"].label == first["SEXO"].label
        with pytest.raises(ValueError): encftr.register_dict(con, draft, "example-2")
        with pytest.raises(ValueError): encftr.get_dict(at="2022-01-01", con=con)
