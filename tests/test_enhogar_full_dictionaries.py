import sqlite3
import pandas as pd
import pytest
from endompy import enhogar as e
from labelerpy import RevisionRegistry


def test_complete_revision_preserves_original_references():
    old=e.get_dict(2022,'baseline-1'); new=e.get_dict(2022)
    assert len(new)==603
    assert new.revision()['version']=='coverage-2'
    assert new.revision()['parent_version']=='baseline-1'
    for name,reference in old.revision()['variable_refs'].items():
        assert new.revision()['variable_refs'][name]==reference
    assert e.dict_versions(2022).version.tolist()==['baseline-1','coverage-2']
    assert e.dict_modules(2018).definitions.tolist()==[447]


@pytest.mark.parametrize('module,count',[('viviendas',10),('hogares',39),('personas',43),('elegidos',491),('geografia',9)])
def test_every_module_matches_official_inventory(module,count):
    dictionary=e.get_dict(2022,module=module)
    assert len(dictionary)==count
    assert dictionary.revision()['dictionary_id']=='enhogar-2022-'+module
    assert e.dict_versions(2022,module=module).version.tolist()==['redatam-1']
    provenance=e.dictionary_coverage(provenance=True)
    expected={v['name'] for v in provenance.values() if v['module']==module}
    assert set(dictionary)==expected
    coverage=e.dictionary_coverage()
    assert coverage['source_field_occurrences']==coverage['documented_field_occurrences']==592
    assert coverage['uncovered_fields']==[]


def test_weight_ambiguity_requires_module_and_preserves_codes():
    x=pd.DataFrame({'FEXP_VIV':[1,2],'GRUP_SEC':[1,5]})
    with pytest.raises(ValueError,match='Ambiguous'):
        e.set_labels(x,edition=2022)
    labelled=e.use_labels(x,vars=['GRUP_SEC'],edition=2022,module='hogares')
    assert labelled.GRUP_SEC.tolist()==['Muy bajo','Alto']
    assert x.GRUP_SEC.tolist()==[1,5]
    assert 'HOGAR.FEXP_VIV' in e.get_dict(2022)
    assert 'VIVIENDA.FEXP_VIV' in e.get_dict(2022)


def test_module_revision_isolation_and_single_definition_change():
    with sqlite3.connect(':memory:') as con:
        original=e.get_dict(2022,module='personas')
        registry=RevisionRegistry(con)
        registry.import_revision(original)
        draft=original.draft()
        draft['P202'].label='Sexo de la persona'
        revised=e.register_dict(con,draft,'review-2',edition=2022,module='personas',parent_version='redatam-1')
        assert e.get_dict(2022,version='review-2',con=con,module='personas').revision()['version']=='review-2'
        with pytest.raises(ValueError,match='exact version'):
            e.get_dict(2022,con=con,module='personas')
        a,b=original.revision()['variable_refs'],revised.revision()['variable_refs']
        assert sum(a[name]==b[name] for name in a)==42
        assert len(e.dict_versions(2022,con=con,module='hogares'))==0
        with pytest.raises(ValueError,match='module'):
            e.register_dict(con,draft,'wrong',edition=2022,module='hogares')
