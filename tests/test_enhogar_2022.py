"""2022 questionnaire contracts, independently expected outcomes and R parity."""
from itertools import product
from pathlib import Path
import json
import sqlite3
import numpy as np
import pandas as pd
import pytest
from endompy import EnhogarDataFrame, enhogar as e

EXPECTED={
 'pet':[1,1,1,1,1,1,0,1,1,1,1,1],
 'ocupado':[1,1,0,0,0,0,None,0,None,0,1,0],
 'desocupado':[0,0,1,0,0,0,None,0,0,None,0,0],
 'pea':[1,1,1,0,0,0,None,0,None,None,1,0],
 'inactivo':[0,0,0,1,1,1,None,1,None,None,0,1],
 'fuerza_trabajo_potencial':[0,0,0,1,1,0,None,0,0,0,0,None]}

def test_independent_2022_cases_and_chaining():
    x=e.enhogar_example(2022); x.index=['same']*len(x); original=x.copy(deep=True)
    out=e.fuerza_trabajo_potencial(e.inactivo(x))
    for name,values in EXPECTED.items():
        np.testing.assert_allclose(out[name].to_numpy(dtype=float,na_value=np.nan),np.array(values,dtype=float),equal_nan=True)
    pd.testing.assert_frame_equal(x,original)
    pd.testing.assert_frame_equal(pd.DataFrame(EnhogarDataFrame(x).inactivo().fuerza_trabajo_potencial()),out)
    assert out.index.equals(x.index)

def test_all_729_employment_combinations():
    rows=list(product([1,2,None],repeat=6))
    x=pd.DataFrame(rows,columns=['P50'+str(i) for i in range(1,7)]);x['P203']=30
    expected=[1 if 1 in row else 0 if all(v==2 for v in row) else np.nan for row in rows]
    np.testing.assert_allclose(e.ocupado(x)['ocupado'].to_numpy(dtype=float,na_value=np.nan),expected,equal_nan=True)

@pytest.mark.parametrize('name',EXPECTED)
def test_r_parity_and_empty_2022(name):
    x=e.enhogar_example(2022); fn=getattr(e,name)
    assert len(fn(x.iloc[:0]))==0
    with pytest.raises(ValueError,match='Conflicting'):fn(x,edition=2018)
    fixture=json.loads((Path(__file__).parent/'fixtures/enhogar/r-results-2022.json').read_text(encoding='utf-8'))
    for column,values in fixture[name].items():
        np.testing.assert_allclose(fn(x)[column].to_numpy(dtype=float,na_value=np.nan),np.array(values,dtype=float),equal_nan=True)

@pytest.mark.parametrize('name',['P50'+str(i) for i in range(1,7)]+['P508','P510','P511'])
def test_2022_codes_and_required_columns(name):
    x=e.enhogar_example(2022)
    with pytest.raises(ValueError,match='Missing'):e.fuerza_trabajo_potencial(x.drop(columns=name))
    x.loc[0,name]=9
    with pytest.raises(ValueError,match='Unsupported'):e.fuerza_trabajo_potencial(x)

def test_2022_search_uses_p508_and_respects_skips():
    x=e.enhogar_example(2022).iloc[[2]].copy()
    x['P507']=1; x['P508']=2
    assert e.desocupado(x)['desocupado'].iloc[0]==0
    x['P507']=96; x['P508']=1
    # P508=yes skips availability: unemployment must not require those fields.
    assert e.desocupado(x.drop(columns=['P510','P511']))['desocupado'].iloc[0]==1
    x['P501']=1; x['P508']=None
    assert e.desocupado(x)['desocupado'].iloc[0]==0

def test_age_99_is_valid_only_in_2022_and_minimum_ten():
    assert e.pet(pd.DataFrame({'P203':[99]}))['pet'].iloc[0]==1
    assert pd.isna(e.pet(pd.DataFrame({'H203':[99]}))['pet'].iloc[0])
    x=pd.DataFrame({'P203':[9,10,14,15,99,120,None]})
    np.testing.assert_allclose(e.pet(x,min_edad=10)['pet'].to_numpy(dtype=float,na_value=np.nan),[0,1,1,1,1,1,np.nan],equal_nan=True)

def test_edition_inference_interview_years_and_configuration():
    old=e.enhogar_edition(None)
    try:
        x=e.enhogar_example(2022)
        for y in [x,x.iloc[:0],x.drop(columns='HANO'),x.assign(HANO=2021)]:
            assert e.guess_enhogar_edition(y)==2022
            assert e.get_enhogar_edition(y)==2022
        assert e.get_enhogar_edition(pd.DataFrame({'HANO':[2021,2022]}))==2022
        with pytest.raises(ValueError,match='ambiguous'):e.get_enhogar_edition(pd.DataFrame({'HANO':[2021]}))
        assert len(e.set_labels(pd.DataFrame({'HANO':[2021]}),edition=2022))==1
        for y in [x.assign(H203=30),x.assign(H501=2),x.assign(HANO=2018),x.assign(HANO=None),x.assign(HANO=2023)]:
            with pytest.raises(ValueError):e.pet(y)
        assert e.enhogar_edition(2018) is None
        with pytest.raises(ValueError,match='Conflicting'):e.pet(x)
        assert e.pet(x,edition=2022)['pet'].iloc[0]==1
        assert e.guess_enhogar_edition(x)==2022
        assert e.get_enhogar_edition()==2018
    finally:e.enhogar_edition(old)

def test_dictionary_labels_and_revision_isolation():
    d=e.get_dict(2022,version='baseline-1'); assert len(d)==30
    assert d.revision()['dictionary_id']=='enhogar-2022'
    assert 'P508' in d and 'H507' not in d
    x=e.enhogar_example(2022)
    labeled=e.set_labels(x,['HZONA','P508'])
    np.testing.assert_array_equal(labeled['HZONA'],x['HZONA'])
    assert list(e.use_labels(x,['HZONA'])['HZONA'])==['Rural','Urbana']*6
    assert len(e.browse_dict(edition=2022,version='baseline-1'))==30
    with pytest.raises(ValueError):e.get_dict(2022,at='2022-01-01')
    with sqlite3.connect(':memory:') as con:
        a=e.register_dict(con,d.draft(),'example-1',edition=2022,valid_from='2022-01-01',valid_to='2022-06-30')
        draft=a.draft();draft['P508'].label='Busqueda revisada'
        b=e.register_dict(con,draft,'example-2',edition=2022,parent_version='example-1',valid_from='2022-07-01',valid_to='2022-12-31')
        ar,br=a.revision()['variable_refs'],b.revision()['variable_refs']
        assert sum(ar[k]['definition_hash']==br[k]['definition_hash'] for k in ar)==29
        assert e.get_dict(2022,con=con,at='2022-07-01').revision()['version']=='example-2'
        assert len(e.dict_versions(2022,con=con))==2
        assert len(e.dict_versions(2018,con=con))==0
        with pytest.raises(ValueError):e.get_dict(2018,version='example-1',con=con)
        with pytest.raises(ValueError):e.register_dict(con,draft,'example-2',edition=2022)
