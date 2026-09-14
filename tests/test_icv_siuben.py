import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from endompy import EncftDataFrame
from endompy import encftr as encft

FIXTURE = Path(__file__).parent / "fixtures"


def example():
    resource = Path(encft.__file__).parent / "resources/synthetic-icv.json"
    return pd.DataFrame(json.loads(resource.read_text(encoding="utf-8")))


def test_historical_reference_and_all_categories():
    x = example()
    expected = pd.DataFrame(json.loads((FIXTURE / "icv-legacy-expected.json").read_text()))
    y = encft.icv_siuben(x)
    assert all(pd.api.types.is_numeric_dtype(y[name]) for name in expected.columns)
    np.testing.assert_allclose(y[expected.columns].to_numpy(dtype=float, na_value=np.nan),
                               expected.to_numpy(dtype=float), rtol=0, atol=1e-12, equal_nan=True)
    assert sorted(y.icv_global.unique()) == [1, 2, 3, 4]
    pd.testing.assert_frame_equal(y[x.columns], x)
    assert y.icv_metodo.eq("encftr0-0.0.2.9002").all()
    pd.testing.assert_frame_equal(encft.ftc_icv_siuben(x), y)
    pd.testing.assert_frame_equal(encft.compute_icv_siuben(x), y)


def test_years_households_and_dwelling_crowding():
    first = example().iloc[:3].assign(TRIMESTRE=1, ANO=2019)
    second = first.assign(ANO=2020, NIVEL_ULTIMO_ANO_APROBADO=6,
                          ULTIMO_ANO_APROBADO=4, SABE_LEER_ESCRIBIR=1)
    expected = pd.concat([encft.icv_siuben(first), encft.icv_siuben(second)])
    both = pd.concat([first, second])
    pd.testing.assert_frame_equal(encft.icv_siuben(both), expected)
    order = [5, 1, 3, 0, 4, 2]
    np.testing.assert_allclose(encft.icv_siuben(both.iloc[order]).icv_puntaje.astype(float),
                               expected.iloc[order].icv_puntaje.astype(float))
    shared = pd.concat([first, second.assign(ANO=2019, HOGAR=2)]).assign(CANT_DORMITORIOS_VIVIENDA=2)
    y = encft.icv_siuben(shared)
    assert y.hacina1.eq(3.4806).all()
    assert y.escoj1.iloc[0] != y.escoj1.iloc[3]


def test_copy_index_details_and_recalculation():
    x = EncftDataFrame(example().iloc[:3].assign(estufa=987))
    x.index = [7, 7, 2]
    x.attrs["source"] = "synthetic"
    y = x.icv_siuben(include_details=False)
    assert isinstance(y, EncftDataFrame)
    assert y.index.tolist() == [7, 7, 2]
    assert y.attrs["source"] == "synthetic"
    assert y.estufa.eq(987).all()
    assert set(y) - set(x) == set(encft.variables_icv_siuben()["output"])
    full = encft.icv_siuben(x)
    stale = full.copy()
    stale[["icv_global", "icv_puntaje", "equiv1"]] = -999
    pd.testing.assert_frame_equal(encft.icv_siuben(stale, include_details=False), full)
    assert len(encft.icv_siuben(x.iloc[:0])) == 0
    assert encft.icv_siuben(x.assign(MATERIAL_PISO=np.nan)).pisov1.eq(0).all()


@pytest.mark.parametrize("column,value,match", [
    ("PARENTESCO", 2, "head"), ("PARENTESCO", 1, "head"),
    ("HOGAR", np.nan, "identifiers"), ("ZONA", np.nan, "ZONA"),
    ("EDAD", np.inf, "EDAD"), ("EDAD", "forty", "EDAD"),
    ("ANO", 2020, "disagree"),
])
def test_invalid_inputs(column, value, match):
    with pytest.raises(ValueError, match=match):
        encft.icv_siuben(example().iloc[:3].assign(**{column: value}))


def test_labels_preserve_questionnaire_revision_and_subsets():
    before = encft.get_dict().revision()["content_hash"]
    x = pd.DataFrame({"icv_global": [1, 2, 3, 4, np.nan], "SEXO": [1, 2, 1, 2, 1]})
    y = encft.use_labels_icv_siuben(x)
    assert y.icv_global.cat.categories.tolist() == ["ICV 1", "ICV 2", "ICV 3", "ICV 4"]
    assert y.SEXO.tolist() == x.SEXO.tolist()
    assert pd.isna(y.icv_global.iloc[-1])
    skipped = encft.set_labels_icv_siuben(x, vars=["SEXO"])
    pd.testing.assert_series_equal(skipped.icv_global, x.icv_global)
    assert encft.get_dict().revision()["content_hash"] == before


def test_model_spec_is_detached_and_options_are_validated():
    spec = encft.variables_icv_siuben()
    spec["required"].clear()
    assert "EDAD" in encft.variables_icv_siuben()["required"]
    x = example().iloc[:3]
    with pytest.raises(ValueError, match="method"):
        encft.icv_siuben(x, method="current")
    with pytest.raises(ValueError, match="include_details"):
        encft.icv_siuben(x, include_details=None)
    with pytest.raises(ValueError, match="EDAD"):
        encft.icv_siuben(x.drop(columns="EDAD"))
    with pytest.raises(ValueError, match="PARENTESCO"):
        encft.icv_siuben(x.assign(PARENTESCO=[1, np.nan, 3]))
    assert encft.icv_siuben(x.assign(MATERIAL_PISO=np.nan)).pisov1.tolist() == [0, 0, 0]


def test_legacy_migration_aliases():
    x = example().iloc[:3]
    with pytest.warns(DeprecationWarning):
        y = encft.ftc0_compute_icv_siuben(x)
    pd.testing.assert_frame_equal(y, encft.icv_siuben(x))
    with pytest.warns(DeprecationWarning):
        labels = encft.ftc0_setLabels(y, vars=["icv_global"])
    with pytest.warns(DeprecationWarning):
        selected = encft.ftc0_setLabels_icv_global(y)
    pd.testing.assert_frame_equal(labels, selected)
    with pytest.warns(DeprecationWarning):
        converted = encft.ftc0_useLabels(y, vars=["icv_global"])
    assert converted.icv_global.cat.categories.tolist() == ["ICV 1", "ICV 2", "ICV 3", "ICV 4"]
