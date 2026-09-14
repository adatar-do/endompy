"""Historical ENFT income model, 2005-2016; not an official-method certification."""
import json
from functools import lru_cache
from pathlib import Path
import numpy as np
import pandas as pd
from .core import _require, _numeric, _parts, peri_vars

_RESOURCES = Path(__file__).parent/'resources'
_KEYS = ['EFT_PERIODO','EFT_VIVIENDA','EFT_HOGAR','EFT_MIEMBRO']
_COMPONENTS = json.loads((_RESOURCES/'components.json').read_text(encoding='utf-8'))
_METHOD = 'enftr-historical-2005-2016-v2'


@lru_cache(maxsize=None)
def _table(name):
    return pd.DataFrame(json.loads((_RESOURCES/(name+'.json')).read_text(encoding='utf-8')))


def _canonical(tbl, unique=False):
    _require(tbl,_KEYS)
    column, year, half = _parts(tbl)
    if column != 'EFT_PERIODO': raise ValueError('This calculation requires the EFT_ structure.')
    result = tbl.copy(deep=True).reset_index(drop=True)
    result['EFT_PERIODO'] = [f'{s}/{y}' for y,s in zip(year,half)]
    if result[_KEYS].isna().any().any(): raise ValueError('Missing member keys are not allowed.')
    if any(result[c].astype(str).str.strip().eq('').any() for c in _KEYS): raise ValueError('Empty member keys are not allowed.')
    if unique and result.duplicated(_KEYS).any(): raise ValueError('Duplicate period/dwelling/household/member keys.')
    return result


def _ids(tbl, keys=_KEYS):
    def normalize(v):
        if isinstance(v,(int,float,np.integer,np.floating)) and v == int(v): return str(int(v))
        return str(v)
    return [tuple(normalize(v) for v in row) for row in tbl[keys].itertuples(index=False,name=None)]


def _rate(year,month,currency):
    rates = _table('tdc_oficial')
    found = rates.loc[(rates.date.str[:7] == f'{int(year):04d}-{int(month):02d}') & (rates.cod_moneda2 == currency),'value']
    if len(found) != 1 or not np.isfinite(found.iloc[0]) or found.iloc[0] <= 0:
        raise ValueError('Missing exchange rate for currency/month; check tdc_oficial coverage.')
    return float(found.iloc[0])


def _ipc(year,month):
    table = _table('ipc_oficial')
    found = table.loc[table.date.str[:7] == f'{int(year):04d}-{int(month):02d}','ipc']
    if len(found) != 1 or not np.isfinite(found.iloc[0]) or found.iloc[0] <= 0: raise ValueError('Missing CPI for month.')
    return float(found.iloc[0])


def _attach(tbl,events,values,output):
    target = _canonical(tbl,True)
    ids, event_ids = _ids(target), _ids(events)
    if not set(event_ids).issubset(set(ids)): raise ValueError('External table contains members absent from tbl.')
    sums = {}
    for key,value in zip(event_ids,values): sums[key] = sums.get(key,0) + (np.nan if pd.isna(value) else float(value))
    out = tbl.copy(deep=True)
    out[output] = np.array([sums.get(key,0) for key in ids],dtype=float)
    return out


def _external(tbl,ing_ext,amount,currency,output):
    events = _canonical(tbl if ing_ext is None else ing_ext)
    _numeric(events,[amount]+([currency] if currency else []))
    _,years,halves = _parts(events)
    values = events[amount].to_numpy(dtype=float,na_value=np.nan).copy()
    for i,value in enumerate(values):
        if pd.isna(value): continue
        if value <= 0: values[i] = 0
        elif currency: values[i] *= _rate(years[i],3 if halves[i] == 1 else 9,events[currency].iloc[i])
    return _attach(tbl,events,values,output)


def ing_ext_pension(tbl,ing_ext=None):
    """Sum monthly external pension transactions in DOP; unknown amounts remain missing."""
    return _external(tbl,ing_ext,'EFT_MONTO_ING_PENSION_MES','EFT_MONEDA_ING_PENSION_MES','ing_ext_pension')


def ing_ext_intereses_alquiler(tbl,ing_ext=None):
    """Sum monthly external interest/rent transactions using survey-month exchange rates."""
    return _external(tbl,ing_ext,'EFT_MONTO_ING_INTERES_MES','EFT_MONEDA_ING_INTERES_MES','ing_ext_intereses_alquiler')


def ing_regalos_ext(tbl,ing_ext=None):
    """Sum external gifts already valued in DOP; absent transactions contribute zero."""
    return _external(tbl,ing_ext,'EFT_MONTO_EQUIV_REGALO',None,'ing_regalos_ext')


def ing_imputado_vivienda_propia(tbl):
    """Assign the household mean imputed rent once, to its unique head."""
    work = _canonical(tbl,True)
    _numeric(work,['EFT_MONTO_PROBABLE_ALQ','EFT_PARENTESCO_CON_JEFE'])
    ids = _ids(work,_KEYS[:3]); groups = {}
    for i,key in enumerate(ids): groups.setdefault(key,[]).append(i)
    values = np.zeros(len(work))
    for indexes in groups.values():
        head = work.loc[indexes,'EFT_PARENTESCO_CON_JEFE']
        if head.isna().any() or (head == 1).sum() != 1: raise ValueError('Exactly one head per household is required.')
        rent = work.loc[indexes,'EFT_MONTO_PROBABLE_ALQ']
        values[head.index[head == 1][0]] = float(rent.mean()) if rent.notna().any() else np.nan
    out = tbl.copy(deep=True); out['ing_imputado_vivienda_propia'] = values
    return out


def ing_remesas_ext(tbl,remesas=None,ing_ext=None):
    """Convert six remittance slots using payment-month FX/CPI and survey-month CPI.

    For semester 1, PER4/PER5/PER6 refer to December/November/October of the prior year.
    Through 2007/1 multiply by frequency and divide by 12; from 2007/2 divide by 6.
    2000/1 uses external semester totals divided by 6. Coverage ends at 2016/2.
    """
    target = _canonical(tbl,True)
    events = _canonical(tbl if remesas is None else remesas,True)
    old = _canonical(tbl if ing_ext is None else ing_ext)
    _,year,half = _parts(events); periods = year*10+half
    events = events.loc[(periods >= 20002) & (periods <= 20162)].reset_index(drop=True)
    _,year,half = _parts(events); periods = year*10+half
    values = np.zeros(len(events))
    if len(events):
        _numeric(events,['EFT_RECIBIO_REMESA'])
        if (~events.EFT_RECIBIO_REMESA.dropna().isin([0,1,2])).any(): raise ValueError('Unknown remittance receipt code.')
        received = np.flatnonzero(events.EFT_RECIBIO_REMESA.eq(1).fillna(False).to_numpy(dtype=bool))
        values[events.EFT_RECIBIO_REMESA.isna()] = np.nan
        for slot_index,slot in enumerate(('SEP','AGO','JUL','PER4','PER5','PER6')):
            if not len(received): continue
            amount,currency,frequency = ['EFT_'+prefix+'_'+slot for prefix in ('MONTO','MONEDA','FRECUENCIA')]
            _numeric(events,[amount,currency]+([frequency] if (periods[received] <= 20071).any() else []))
            for i in received:
                value = events[amount].iloc[i]
                if pd.isna(value): values[i] = np.nan; continue
                if value <= 0: continue
                month = (3,2,1,12,11,10)[slot_index] if half[i] == 1 else (9,8,7,6,5,4)[slot_index]
                payment_year = year[i] - int(half[i] == 1 and slot_index >= 3)
                freq = events[frequency].iloc[i] if periods[i] <= 20071 else 1
                if not pd.isna(freq) and freq < 0: raise ValueError('Negative remittance frequency.')
                converted = value*_rate(payment_year,month,events[currency].iloc[i])*_ipc(year[i],3 if half[i] == 1 else 9)/_ipc(payment_year,month)
                values[i] += converted*(np.nan if pd.isna(freq) else freq)/(12 if periods[i] <= 20071 else 6)
    _,year,half = _parts(old)
    old = old.loc[year*10+half == 20001].reset_index(drop=True)
    old_values = np.zeros(len(old))
    if len(old):
        _numeric(old,['EFT_RECIBIO_ING_REMESA_SEM','EFT_MONTO_ING_REMESA_SEM','EFT_MONEDA_ING_REMESA_SEM'])
        for i,row in old.iterrows():
            flag = row.EFT_RECIBIO_ING_REMESA_SEM
            if pd.isna(flag): old_values[i] = np.nan
            elif flag == 1:
                value = row.EFT_MONTO_ING_REMESA_SEM
                old_values[i] = np.nan if pd.isna(value) else value/6
                if not pd.isna(value) and value > 0: old_values[i] *= _rate(2000,3,row.EFT_MONEDA_ING_REMESA_SEM)
    out = _attach(tbl,pd.concat([events[_KEYS],old[_KEYS]],ignore_index=True),np.concatenate([values,old_values]),'ing_remesas_ext')
    _,year,half = _parts(target)
    out.loc[(year*10+half < 20001) | (year*10+half > 20162),'ing_remesas_ext'] = np.nan
    return out


def _option(value,name):
    if isinstance(value,bool): return
    if not isinstance(value,(list,tuple)) or any(not isinstance(x,str) or x not in _COMPONENTS for x in value) or len(set(value)) != len(value):
        raise ValueError(name+' must be bool or unique component names.')


def ing_total_pobreza_monetaria(tbl,ing_ext=None,remesas=None,keep=False,reuse=False):
    """Sum 34 monthly individual components within 2005/1-2016/2.

    keep selects retained components; reuse explicitly trusts provided component values.
    By default components are recalculated. Requires unique people and complete households.
    """
    from . import indicators
    canonical = _canonical(tbl,True)
    _option(keep,'keep'); _option(reuse,'reuse')
    if isinstance(reuse,(list,tuple)) and any(c not in tbl for c in reuse): raise ValueError('Requested reusable component is absent.')
    selected = _COMPONENTS if keep is True else keep if keep is not False else []
    retained = [c for c in _COMPONENTS if c in tbl] if reuse is True else reuse if reuse is not False else []
    _,year,half = _parts(canonical)
    covered = (year*10+half >= 20051) & (year*10+half <= 20162)
    work = peri_vars(canonical.loc[covered].reset_index(drop=True))
    ext = _canonical(tbl if ing_ext is None else ing_ext)
    rem = _canonical(tbl if remesas is None else remesas,True)
    ids = set(_ids(canonical)); active_ids = set(_ids(work))
    if not set(_ids(ext)).issubset(ids) or not set(_ids(rem)).issubset(ids): raise ValueError('External table contains members absent from tbl.')
    ext = ext.loc[[i in active_ids for i in _ids(ext)]].reset_index(drop=True)
    rem = rem.loc[[i in active_ids for i in _ids(rem)]].reset_index(drop=True)
    for component in _COMPONENTS:
        if len(work) and component not in retained:
            if component in ('ing_ext_pension','ing_ext_intereses_alquiler','ing_regalos_ext'): work = globals()[component](work,ext)
            elif component == 'ing_remesas_ext': work = ing_remesas_ext(work,rem,ext)
            elif component == 'ing_imputado_vivienda_propia': work = ing_imputado_vivienda_propia(work)
            else: work = getattr(indicators,component)(work)
        if not len(work): work[component] = pd.Series(dtype=float)
        _numeric(work,[component])
    out = tbl.copy(deep=True)
    total = np.full(len(out),np.nan)
    total[covered] = work[_COMPONENTS].to_numpy(dtype=float,na_value=np.nan).sum(axis=1)
    out['ing_total_pobreza_monetaria'] = total
    for component in selected:
        value = np.full(len(out),np.nan); value[covered] = work[component].to_numpy(dtype=float,na_value=np.nan)
        out[component] = value
    return out


def ing_pc_pobreza_monetaria(tbl,ing_ext=None,remesas=None,keep=False,reuse=False):
    """Compute household mean across all members; any unknown total leaves it missing."""
    out = ing_total_pobreza_monetaria(tbl,ing_ext,remesas,keep,reuse)
    work = _canonical(out,True); groups = {}
    for i,key in enumerate(_ids(work,_KEYS[:3])): groups.setdefault(key,[]).append(i)
    value = np.full(len(out),np.nan)
    for indexes in groups.values():
        if 'EFT_ZONA' in work and work.loc[indexes,'EFT_ZONA'].nunique(dropna=False) != 1: raise ValueError('Inconsistent zone within household.')
        value[indexes] = work.loc[indexes,'ing_total_pobreza_monetaria'].mean(skipna=False)
    out['ing_pc_pobreza_monetaria'] = value
    return out


def pobreza_monetaria(tbl,ing_ext=None,remesas=None,keep=False,reuse=False):
    """Classify 2005-2016 ENFT households: 1 extreme, 2 moderate, 3 nonpoor, NA unknown.

    Includes explicit status and method identifier. This historical implementation has
    not been certified against the official ENFT production program.
    """
    out = ing_pc_pobreza_monetaria(tbl,ing_ext,remesas,keep,reuse)
    _numeric(out,['EFT_ZONA'])
    if out.EFT_ZONA.isna().any() or (~out.EFT_ZONA.isin([0,1])).any(): raise ValueError('Poverty requires nonmissing EFT_ZONA codes 0/1.')
    canonical = _canonical(out); _,year,half = _parts(canonical)
    table = _table('lineas_oficial_zona').set_index(['EFT_PERIODO','EFT_ZONA'])
    values = table.reindex(pd.MultiIndex.from_frame(canonical[['EFT_PERIODO','EFT_ZONA']]))
    for c in ['lindigencia','lpobreza']: out[c] = values[c].to_numpy(dtype=float)
    covered = (year*10+half >= 20051) & (year*10+half <= 20162)
    if out.loc[covered,['lindigencia','lpobreza']].isna().any().any(): raise ValueError('Missing poverty line within coverage.')
    income = out['ing_pc_pobreza_monetaria'].to_numpy(dtype=float)
    out['pobreza_monetaria'] = np.where(~covered | np.isnan(income),np.nan,np.where(income <= out.lindigencia,1,np.where(income <= out.lpobreza,2,3)))
    out['pobreza_estado'] = np.where(~covered,'outside_coverage',np.where(np.isnan(income),'missing_income','classified'))
    out['pobreza_metodo'] = _METHOD
    return out
