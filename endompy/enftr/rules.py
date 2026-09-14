"""Closed ENFT pipeline executor using shared arithmetic and predicate semantics."""
import json
import inspect
from pathlib import Path
from .core import _require, _age
from ..encftr.rules import expression, _selection

RULES = json.loads((Path(__file__).parent/'resources/survey-rules.json').read_text(encoding='utf-8'))


def run_rule(tbl, name, **kwargs):
    _require(tbl)
    spec = RULES[name]
    env = {key:value.get('value') for key,value in spec['parameters'].items() if key != 'tbl'}
    env.update(kwargs)
    if 'min_edad' in env: _age(env['min_edad'])
    # A private positional index avoids alignment surprises with repeated caller indexes.
    df = tbl.copy(deep=True)
    index = df.index.copy(); df.index = range(len(df))
    for step in spec['steps']:
        op, args, names = step['op'], step['args'], step['names']
        if op == 'mutate':
            for node, column in zip(args,names): df[column] = expression(node,df,env)
        elif op == 'select':
            for node in args:
                if node.get('call') == '-': df = df.drop(columns=_selection(node['args'][0],df,env))
                else: df = df[_selection(node,df,env)]
        elif op.startswith('ft_'):
            from . import core, indicators
            function = getattr(core,op[3:],None) or getattr(indicators,op[3:])
            positional, keywords = [], {}
            for node, key in zip(args,names):
                value = expression(node,df,env)
                if key: keywords[key] = value
                else: positional.append(value)
            df = function(df,*positional,**keywords)
        else: raise ValueError('Unsupported bundled ENFT operation: '+op)
    df.index = index
    return df
