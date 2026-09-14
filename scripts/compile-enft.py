"""Compile only supported, exported ENFT calculation pipelines; fail on drift."""
from pathlib import Path
import json, re, shutil

ROOT = Path(__file__).resolve().parents[2]
source = json.loads((ROOT/'endompy/scripts/generated/enft-functions.json').read_text())
target = ROOT/'endompy/endompy/enftr'
resources = target/'resources'
resources.mkdir(parents=True, exist_ok=True)
exports = re.findall(r'export\((ft_\w+)\)', (ROOT/'enftr/NAMESPACE').read_text())
manual = {'ft_zona', 'ft_regiones_desarrollo', 'ft_compute_zona', 'ft_ing_imputado_vivienda_propia',
          'ft_ing_ext_pension', 'ft_ing_ext_intereses_alquiler', 'ft_ing_regalos_ext', 'ft_ing_remesas_ext'}

def op(node): return node.get('call', '').split('::')[-1]
def pipe(node):
    if node.get('symbol') == 'tbl': return []
    if op(node) == '%>%': return pipe(node['args'][0]) + step(node['args'][1])
    raise ValueError('Unsupported ENFT pipeline: '+str(node)[:160])
def step(node):
    name = op(node)
    if name in ('mutate', 'select') or name.startswith('ft_'):
        return [dict(op=name, args=node.get('args', []), names=node.get('names', []))]
    raise ValueError('Unsupported ENFT step: '+name)
def compile_function(name):
    fn = source[name]; steps = []
    for node in fn['body']['args']:
        name_op = op(node)
        if name_op == '<-' and node['args'][1] == {'value':None}: continue
        if name_op == 'ft_check_age': continue  # validated centrally with the same contract
        if name_op == '%>%': steps += pipe(node)
        else: raise ValueError(name+': unsupported statement '+name_op)
    return dict(parameters=fn['formals'], steps=steps)

rules = {name[3:]:compile_function(name) for name in exports if name in source and name not in manual}
(resources/'survey-rules.json').write_text(json.dumps(rules,ensure_ascii=False,indent=2),encoding='utf-8')
lines = ['"""ENFT indicators compiled from the reviewed R package. Do not edit by hand."""', 'from .rules import run_rule', '']
for name, spec in rules.items():
    params = [p if 'missing' in default else p+'='+repr(default.get('value')) for p, default in spec['parameters'].items()]
    kwargs = ''.join(', '+p.split('=')[0]+'='+p.split('=')[0] for p in params[1:])
    lines += [f'def {name}({", ".join(params)}):', f'    """Apply enftr::ft_{name}; preserve input rows, order and index.',
              '', '    See ENFT reference for required columns, codes and historical scope.', '    """',
              f'    return run_rule(tbl, "{name}"{kwargs})', '']
(target/'indicators.py').write_text('\n'.join(lines),encoding='utf-8')
shutil.copyfile(ROOT/'enftr/inst/dictionaries/baseline-1.json', resources/'baseline-1.json')
shutil.copyfile(ROOT/'enftr/inst/examples/synthetic-members.json', resources/'synthetic-members.json')
for file in ('dictionaries.py', 'labeling.py'):
    text = (ROOT/'endompy/endompy/encftr'/file).read_text().replace('ENCFT','ENFT').replace('encft','enft')
    (target/file).write_text(text,encoding='utf-8')
print('Compiled',len(rules),'ENFT pipelines with explicit unsupported-operation failures.')
