"""ENHOGAR dictionary revisions independent from questionnaire editions."""
from pathlib import Path
import json
import pandas as pd
from labelerpy import Dict, RevisionRegistry
from labelerpy.labeling import set_dict as _set_dict, with_dict as _with_dict
from .core import _edition, _year, _schema


def _spec(edition,module):
    edition=_year(edition)
    if not isinstance(module,str): raise ValueError('Invalid dictionary module')
    if edition==2018:
        if module!='all': raise ValueError('ENHOGAR 2018 only bundles module all')
        return dict(dictionary_id='enhogar-2018',default_version='baseline-1',versions=['baseline-1'],
                    files={'baseline-1':_schema(2018)['dictionary_file']},definitions=447)
    specs=json.loads((Path(__file__).parent/'resources/2022-dictionary-modules.json').read_text(encoding='utf-8'))
    if module not in specs: raise ValueError('Unknown ENHOGAR 2022 dictionary module')
    return specs[module]


def get_dict(edition=2018,version=None,at=None,con=None,module='all'):
    """Select an exact revision or a documented date. Baseline has no date interval."""
    spec=_spec(edition,module)
    if con is not None: result=RevisionRegistry(con).load(spec['dictionary_id'],version=version,at=at)
    else:
        if version is None: version=spec['default_version']
        if not isinstance(version,str) or version not in spec['versions']: raise ValueError('Revision not bundled')
        result=Dict.from_json(Path(__file__).parent/'resources'/spec['files'][version])
    if result.revision(at=at)['dictionary_id'] != spec['dictionary_id']:
        raise ValueError('Dictionary identity does not match edition/module')
    return result


def dict_versions(edition=2018,con=None,module='all'):
    """List immutable revision metadata, date intervals and content hashes."""
    spec=_spec(edition,module)
    if con is not None: return RevisionRegistry(con).list_versions(spec['dictionary_id'])
    fields=['dictionary_id','version','parent_version','created_at','author','message','valid_from','valid_to','content_hash']
    revisions=[get_dict(edition,version,module=module).revision() for version in spec['versions']]
    return pd.DataFrame([{key:revision[key] for key in fields} for revision in revisions])


def register_dict(con,dictionary,version,edition=2018,valid_from=None,valid_to=None,module='all',**kwargs):
    """Register a complete revision, reusing unchanged definitions and explicit renames."""
    spec=_spec(edition,module)
    if not isinstance(dictionary,Dict) or not dictionary.is_valid(): raise ValueError('dictionary must be a valid Dict draft')
    metadata=dictionary.metadata.to_dict()
    if 'module' in metadata and metadata['module']!=module: raise ValueError('Dictionary module does not match')
    if 'questionnaire_edition' in metadata and metadata['questionnaire_edition']!=edition: raise ValueError('Dictionary edition does not match')
    return RevisionRegistry(con).register(dictionary,version,dictionary_id=spec['dictionary_id'],valid_from=valid_from,valid_to=valid_to,**kwargs)


def set_labels(tbl,vars=None,edition=None,version=None,at=None,con=None,module='all'):
    """Attach labels and revision provenance; preserve the original numeric codes."""
    selected=_edition(tbl,edition)
    columns=tbl.columns if vars is None else vars
    if selected==2022 and module=='all' and set(columns)&{'FEXP_VIV','FPON_VIV','GRUP_SEC'}:
        raise ValueError('Ambiguous household/dwelling fields: select module hogares or viviendas')
    return _set_dict(tbl,get_dict(selected,version,at,con,module),subset=vars,dtypes=False,at=at)


def use_labels(tbl,vars=None,edition=None,version=None,at=None,con=None,module='all'):
    """Replace value codes for presentation, preserving original column names."""
    out=set_labels(tbl,vars,edition,version,at,con,module)
    if vars is not None: vars=[name for name in vars if name in out.columns]
    return _with_dict(out,subset=vars,use_label=False,use_labels=True)


def browse_dict(edition=2018,version=None,at=None,con=None,module='all'):
    """Return the selected dictionary as a local pandas table for notebooks."""
    return get_dict(edition,version,at,con,module).to_frame()


def dict_modules(edition=2018):
    """List dictionary modules, identities, default revisions and definitions."""
    edition=_year(edition)
    modules=['all'] if edition==2018 else ['all','viviendas','hogares','personas','elegidos','geografia']
    return pd.DataFrame([dict(module=module,**{key:_spec(edition,module)[key] for key in
                         ('dictionary_id','default_version','definitions')}) for module in modules])


def dictionary_coverage(provenance=False):
    """Public ONE 2022 inventory or per-field source traceability; no microdata."""
    if not isinstance(provenance,bool): raise ValueError('provenance must be boolean')
    name='2022-full-provenance.json' if provenance else '2022-full-coverage.json'
    return json.loads((Path(__file__).parent/'resources'/name).read_text(encoding='utf-8'))
