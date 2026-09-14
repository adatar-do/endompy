"""R parity plus independently derived ENFT contracts; no respondent data."""
import json
import sqlite3
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from endompy import EnftDataFrame, enftr as f
from endompy.enftr.rules import RULES
from endompy.enftr.poverty import _COMPONENTS, _table

HERE = Path(__file__).parent/'fixtures/enft'


def example(): return pd.DataFrame(json.loads((Path(f.__file__).parent/'resources/synthetic-members.json').read_text()))


@pytest.mark.parametrize('name',list(RULES))
def test_r_pipeline_reference(name):
    x = pd.DataFrame(json.loads((HERE/'branch-members.json').read_text()))
    x.index = ['repeated']*len(x)
    original = x.copy(deep=True)
    out = getattr(f,name)(x)
    expected = json.loads((HERE/(name+'.json')).read_text())
    for column,values in expected.items():
        np.testing.assert_allclose(pd.to_numeric(out[column]).to_numpy(dtype=float,na_value=np.nan),np.array(values,dtype=float),rtol=1e-10,atol=1e-10,equal_nan=True)
    pd.testing.assert_frame_equal(x,original)
    assert out.index.equals(x.index)


@pytest.mark.parametrize('name',['ing_ext_pension','ing_ext_intereses_alquiler','ing_regalos_ext','ing_remesas_ext','ing_imputado_vivienda_propia'])
def test_r_income_reference(name):
    out = getattr(f,name)(example())
    expected = json.loads((HERE/(name+'.json')).read_text())
    np.testing.assert_allclose(out[name],np.array(expected[name],dtype=float),rtol=1e-10,equal_nan=True)


def test_r_poverty_all_components():
    x = example(); x.index = pd.Index(['same']*len(x),name='original')
    out = f.pobreza_monetaria(x,keep=True)
    expected = json.loads((HERE/'poverty-members.json').read_text())
    for column in _COMPONENTS+['ing_total_pobreza_monetaria','ing_pc_pobreza_monetaria','pobreza_monetaria','lindigencia','lpobreza']:
        np.testing.assert_allclose(out[column].to_numpy(dtype=float,na_value=np.nan),np.array(expected[column],dtype=float),rtol=1e-10,equal_nan=True)
    for column in ['pobreza_estado','pobreza_metodo']: assert out[column].tolist() == expected[column]
    assert out.index.equals(x.index)
    assert f.pobreza_monetaria(x.iloc[:0]).empty


def test_periods_and_structures():
    x = pd.DataFrame({'EFT_PERIODO':['1/2005','2005/2','20061'],'ano':[0,0,0],'marker':['a','b','c']})
    assert f.peri_vars(x).periodo.tolist() == [20051,20052,20061]
    assert f.peri_vars(x,ano=False).ano.tolist() == [0,0,0]
    assert f.peri_vars(x,rm=True).marker.tolist() == ['a','b','c']
    for value in ['3/2005','2005/0','2005',None,True]:
        with pytest.raises(ValueError): f.peri_vars(pd.DataFrame({'EFT_PERIODO':[value]}))
    with pytest.raises(ValueError): f.version(pd.DataFrame({'PERIALFA':[1],'EFT_PERIODO':[1]}))
    assert f.zona(pd.DataFrame({'PERIALFA':['1/2000']*2,'S1_P4':[0,1]})).zona.tolist() == [1,2]
    with pytest.raises(ValueError): f.pet(example(),min_edad=-1)


def test_missing_coverage_and_line_boundaries():
    x = example().iloc[18:21].copy()
    x.iloc[0,x.columns.get_loc('EFT_ING_OCUP_PRINC')] = np.nan
    assert f.pobreza_monetaria(x).pobreza_estado.tolist() == ['missing_income']*3
    x['EFT_PERIODO'] = '1/2017'
    assert f.pobreza_monetaria(x).pobreza_estado.tolist() == ['outside_coverage']*3
    x = example().iloc[18:21].copy()
    for component in _COMPONENTS: x[component] = 0.0
    line = _table('lineas_oficial_zona').query("EFT_PERIODO == '1/2005' and EFT_ZONA == 0").iloc[0]
    for amount,code in [(0,1),(line.lindigencia,1),(line.lindigencia+.01,2),(line.lpobreza,2),(line.lpobreza+.01,3)]:
        x['ing_ocup_prin'] = amount
        assert f.pobreza_monetaria(x,reuse=True).pobreza_monetaria.tolist() == [code]*3
    with pytest.raises(ValueError): f.pobreza_monetaria(example(),reuse=['ing_ocup_prin'])


def test_keys_and_external_transactions():
    x = example().iloc[18:21].copy()
    with pytest.raises(ValueError,match='Duplicate'): f.pobreza_monetaria(pd.concat([x,x.iloc[:1]]))
    bad = x.copy(); bad.iloc[0,bad.columns.get_loc('EFT_ZONA')] = 1
    with pytest.raises(ValueError,match='zone'): f.pobreza_monetaria(bad)
    events = pd.concat([x.iloc[:1],x.iloc[:1]]); events['EFT_MONTO_EQUIV_REGALO'] = [10,20]
    assert f.ing_regalos_ext(x,events).ing_regalos_ext.tolist() == [30,0,0]
    events.iloc[1,events.columns.get_loc('EFT_MONTO_EQUIV_REGALO')] = np.nan
    assert pd.isna(f.ing_regalos_ext(x,events).ing_regalos_ext.iloc[0])
    events['EFT_MIEMBRO'] = 99
    with pytest.raises(ValueError,match='absent'): f.ing_regalos_ext(x,events)
    x['lindigencia'] = -1; x['lpobreza'] = -1
    assert (f.pobreza_monetaria(x).lindigencia > 0).all()


def test_previous_year_remittance_and_unknown_fx():
    x = example().iloc[36:39].copy()
    for slot in ['SEP','AGO','JUL','PER4','PER5','PER6']: x['EFT_MONTO_'+slot] = 0.0
    x.iloc[0,x.columns.get_loc('EFT_MONTO_PER4')] = 120
    fx = _table('tdc_oficial').query("date == '2007-12-31' and cod_moneda2 == 1").value.iloc[0]
    ipc = _table('ipc_oficial').set_index('date').ipc
    expected = 120*fx*ipc['2008-03-31']/ipc['2007-12-31']/6
    assert f.ing_remesas_ext(x).ing_remesas_ext.iloc[0] == pytest.approx(expected)
    x['EFT_MONTO_UNRELATED'] = 999999
    assert f.ing_remesas_ext(x).ing_remesas_ext.iloc[0] == pytest.approx(expected)
    x.iloc[0,x.columns.get_loc('EFT_MONEDA_PER4')] = 999
    with pytest.raises(ValueError,match='exchange rate'): f.ing_remesas_ext(x)


def test_dictionaries_and_dataframe():
    d = f.get_dict()
    assert d.revision()['dictionary_id'] == 'enft'
    with pytest.raises(ValueError): f.get_dict(at='2005-01-01')
    with sqlite3.connect(':memory:') as con:
        one = f.register_dict(con,d.draft(),'v1',valid_from='2005-01-01',valid_to='2005-12-31')
        draft = one.draft(); draft['EFT_ZONA'].label = 'Revised zone'
        two = f.register_dict(con,draft,'v2',parent_version='v1',valid_from='2006-01-01',valid_to='2006-12-31')
        assert f.get_dict(con=con,at='2006-06-01').revision()['version'] == 'v2'
        assert one.revision()['variable_refs']['EFT_EDAD'] == two.revision()['variable_refs']['EFT_EDAD']
        assert one.revision()['variable_refs']['EFT_ZONA']['definition_hash'] != two.revision()['variable_refs']['EFT_ZONA']['definition_hash']
    x = EnftDataFrame(example())
    assert isinstance(x.peri_vars().ocupado().pobreza_monetaria(),EnftDataFrame)
    with pytest.warns(UserWarning):
        assert len(x.set_dict()) == len(x)
