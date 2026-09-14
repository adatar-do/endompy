"""Cross-language regression fixtures contain synthetic households only."""
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
import endompy.encftr as api
from endompy.encftr.rules import RESOURCES

REFERENCE = json.loads((Path(__file__).parent / "fixtures/r-reference.json").read_text(encoding="utf-8"))


@pytest.fixture
def members():
    return pd.read_json(RESOURCES / "synthetic-members.json")


@pytest.mark.parametrize("name", sorted(REFERENCE))
def test_r_parity(name, members):
    before = members.copy(deep=True)
    result = getattr(api, name)(members, **({"return_households": True, "include_details": True} if name == "iih" else {}))
    for col, values in REFERENCE[name].items():
        expected = pd.Series(values)
        actual = result[col].reset_index(drop=True)
        if col in ("calc_id", "macro_region_pobreza"):
            assert actual.fillna("NA").tolist() == expected.fillna("NA").tolist()
        else:
            np.testing.assert_allclose(actual.to_numpy(dtype=float, na_value=np.nan), pd.to_numeric(expected).to_numpy(dtype=float), rtol=1e-10, atol=1e-7, equal_nan=True, err_msg=col)
    pd.testing.assert_frame_equal(before, members)


@pytest.mark.parametrize("method", ["2012", "2022"])
def test_poverty_repeat_empty_and_index(members, method):
    fn = getattr(api, "pobreza_monetaria_" + method)
    members.index = [7] * len(members)
    first = fn(members, keep=True)
    second = fn(first, keep=True)
    for col in ("ing_total_pobreza_def", "ing_total_pobreza", "pobreza_monetaria"):
        pd.testing.assert_series_equal(first[col], second[col])
    assert first.index.tolist() == members.index.tolist()
    assert len(fn(members.iloc[:0])) == 0


def test_weights_and_education_boundaries():
    x = pd.DataFrame({"TRIMESTRE": [20231, 20232, 20232, 20234, 20241], "FACTOR_EXPANSION": [120, 240, 60, 90, 50]})
    assert api.factor_expansion_anual(x).factor_expansion_anual.tolist() == [40, 80, 20, 30, 50]
    assert api.factor_expansion_semestre(x).factor_expansion_semestre.tolist() == [60, 120, 30, 90, 50]
    for bad in (-1, float("inf"), True):
        with pytest.raises(ValueError): api.factor_expansion_anual(x.assign(FACTOR_EXPANSION=bad))
    school = pd.DataFrame({"NIVEL_ULTIMO_ANO_APROBADO": [3, 3, 5], "ULTIMO_ANO_APROBADO": [4, 6, 2], "ANO": [2021, 2022, 2022]})
    assert api.anos_educacion(school).anos_educacion.tolist() == [10, 12, 14]
    assert api.anos_educacion(school, secundaria_base="historica_por_ano").anos_educacion.tolist() == [12, 12, 14]


def test_households_do_not_mix_years_or_invent_heads():
    x = pd.DataFrame({"ANO": [2023, 2023, 2024], "TRIMESTRE": 1, "VIVIENDA": 1, "HOGAR": 1, "EDAD": [10, 30, 30]})
    assert api.tasa_dependencia(x).tasa_dependencia.tolist() == [100, 100, 0]
    heads = x.assign(PERIODO=[202301, 202301, 202401], PARENTESCO=[1, 2, 2], SEXO=[1, 2, 2])
    assert api.sexo_jefe(heads).sexo_jefe.iloc[:2].tolist() == [1, 1]
    assert pd.isna(api.sexo_jefe(heads).sexo_jefe.iloc[2])
    with pytest.raises(ValueError): api.sexo_jefe(heads.assign(PARENTESCO=1))


def test_unknown_dictionary_is_not_silently_replaced():
    assert len(api.get_dict()) == 636
    with pytest.raises(ValueError): api.get_dict("unpublished")
    with pytest.raises(ValueError): api.get_dict(at="2019-01-01")
    df = api.EncftDataFrame({"SEXO": [1, 2]}).set_dict()
    assert df.attrs
