"""Independent labour cases, validation and R/Python parity without respondent data."""
from itertools import product
import json
from pathlib import Path
import sqlite3
import numpy as np
import pandas as pd
import pytest
from endompy import EnhogarDataFrame, enhogar as e

FUNCTIONS=['pet','ocupado','desocupado','pea','inactivo','fuerza_trabajo_potencial']


def test_independent_cases():
    x=e.enhogar_example(); x.index=['repeat']*len(x); original=x.copy(deep=True)
    out=e.fuerza_trabajo_potencial(e.inactivo(x))
    expected={
        'pet':[1,1,1,1,1,1,0,None,1,1,1,1],
        'ocupado':[1,1,0,0,0,0,None,None,None,0,1,0],
        'desocupado':[0,0,1,0,0,0,None,None,0,None,0,0],
        'pea':[1,1,1,0,0,0,None,None,None,None,1,0],
        'inactivo':[0,0,0,1,1,1,None,None,None,None,0,1],
        'fuerza_trabajo_potencial':[0,0,0,1,1,0,None,None,0,0,0,None]}
    for name,values in expected.items():
        np.testing.assert_allclose(out[name].to_numpy(dtype=float,na_value=np.nan),np.array(values,dtype=float),equal_nan=True)
    pd.testing.assert_frame_equal(x,original)
    assert out.index.equals(x.index)
    pd.testing.assert_series_equal(e.inactivo(out)['inactivo'],out['inactivo'])
    chained=EnhogarDataFrame(x).inactivo().fuerza_trabajo_potencial()
    assert isinstance(chained,EnhogarDataFrame)
    pd.testing.assert_frame_equal(pd.DataFrame(chained),out)


def test_all_employment_combinations():
    rows=list(product([1,2,9,None],repeat=6))
    x=pd.DataFrame(rows,columns=['H50'+str(i) for i in range(1,7)]); x['H203']=30
    expected=[1 if 1 in row else 0 if all(v==2 for v in row) else np.nan for row in rows]
    np.testing.assert_allclose(e.ocupado(x)['ocupado'].to_numpy(dtype=float,na_value=np.nan),expected,equal_nan=True)


@pytest.mark.parametrize('name',FUNCTIONS)
def test_empty_and_r_parity(name):
    x=e.enhogar_example(); fn=getattr(e,name)
    assert len(fn(x.iloc[0:]))==12
    assert len(fn(x.iloc[:0]))==0
    with pytest.raises(ValueError,match='2018'):fn(x,edition=2019)
    expected=json.loads((Path(__file__).parent/'fixtures/enhogar/r-results.json').read_text(encoding='utf-8'))
    for col,values in expected[name].items():
        np.testing.assert_allclose(fn(x)[col].to_numpy(dtype=float,na_value=np.nan),np.array(values,dtype=float),equal_nan=True)


@pytest.mark.parametrize('name',['H501','H502','H503','H504','H505','H506','H507','H509','H510'])
def test_required_columns_and_invalid_codes(name):
    x=e.enhogar_example();x.loc[0,name]=8
    with pytest.raises(ValueError,match='Unsupported'): e.fuerza_trabajo_potencial(x)
    with pytest.raises(ValueError,match='Missing'): e.fuerza_trabajo_potencial(x.drop(columns=name))


@pytest.mark.parametrize('minimum',[9,None,np.inf,15.5,'15',True,[15,16]])
def test_min_age(minimum):
    with pytest.raises((ValueError,TypeError)): e.pet(e.enhogar_example(),min_edad=minimum)


@pytest.mark.parametrize('maximum',[14,None,-np.inf,65.5,'65',True,[65,66]])
def test_max_age(maximum):
    with pytest.raises((ValueError,TypeError)): e.pet(e.enhogar_example(),max_edad=maximum)


def test_schema_age_edition_and_labels():
    x=e.enhogar_example()
    with pytest.raises(TypeError): e.pet({'H203':[30]})
    with pytest.raises(ValueError): e.pet(pd.concat([x,x],axis=1))
    for v in [-1,121,np.inf,3.5,'30',True]:
        y=x.copy();y['H203']=v
        with pytest.raises((ValueError,TypeError)):e.pet(y)
    expected=[0,1,1,1,1,0,np.nan,np.nan]
    out=e.pet(pd.DataFrame({'H203':[9,10,14,15,65,66,99,None]}),10,65)
    np.testing.assert_allclose(out['pet'].to_numpy(dtype=float,na_value=np.nan),expected,equal_nan=True)
    old=e.enhogar_edition(None)
    try:
        assert e.get_enhogar_edition()==2018
        assert e.enhogar_edition(2018) is None
        assert e.guess_enhogar_edition(x)==2018
        for y in [x.iloc[:0],x.drop(columns='HANO')]:
            assert e.guess_enhogar_edition(y)==2018
        for y in [x.assign(HANO=2019),x.assign(HANO=None)]:
            with pytest.raises(ValueError):e.guess_enhogar_edition(y)
        with pytest.raises(ValueError):e.enhogar_edition(2019)
        assert e.get_enhogar_edition()==2018
    finally: e.enhogar_edition(old)
    labeled=e.set_labels(x,['HZONA'])
    np.testing.assert_array_equal(labeled['HZONA'],x['HZONA'])
    assert list(e.use_labels(x,['HZONA'])['HZONA'])==['Rural','Urbano']*6
    with pytest.raises(TypeError):e.ocupado(e.use_labels(x,['H501']))
    assert len(e.browse_dict())==447


def test_revision_reuses_unchanged_definitions():
    d=e.get_dict(); assert len(d)==447
    assert d.revision()['dictionary_id']=='enhogar-2018'
    for kwargs in [{'version':'missing'},{'at':'2018-06-01'},{'edition':2019}]:
        with pytest.raises(ValueError):e.get_dict(**kwargs)
    with sqlite3.connect(':memory:') as con:
        a=e.register_dict(con,d.draft(),'example-1',valid_from='2018-01-01',valid_to='2018-06-30')
        draft=a.draft();draft['HZONA'].label='Zona revisada'
        b=e.register_dict(con,draft,'example-2',parent_version='example-1',valid_from='2018-07-01',valid_to='2018-12-31')
        ar,br=a.revision()['variable_refs'],b.revision()['variable_refs']
        assert sum(ar[k]['definition_hash']==br[k]['definition_hash'] for k in ar)==446
        assert e.get_dict(con=con,at='2018-06-30').revision()['version']=='example-1'
        assert e.get_dict(con=con,at='2018-07-01').revision()['version']=='example-2'
        assert len(e.dict_versions(con=con))==2
        with pytest.raises(ValueError):e.register_dict(con,draft,'example-2')
        with pytest.raises(ValueError):e.get_dict(con=con,at='2019-01-01')


def test_legacy_aliases():
    x=e.enhogar_example()
    for name in FUNCTIONS: assert getattr(e,'ehg_'+name) is getattr(e,name)
    with pytest.warns(DeprecationWarning): e.ehg_setLabels(x,['HZONA'])
    with pytest.warns(DeprecationWarning): e.ehg_useLabels(x,['HZONA'])
