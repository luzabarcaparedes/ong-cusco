#!/usr/bin/env python3
"""Valida referencias y genera SQL local. No se conecta a servicios."""
from pathlib import Path
from datetime import date, time
from zoneinfo import ZoneInfo
import json, hashlib, re, argparse
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--dataset', default='02_datos/cooperacion_consolidada_2026-10-22.json')
parser.add_argument('--scope', default='consolidado', choices=['consolidado','europa','ampliacion'])
args=parser.parse_args()
path=ROOT/args.dataset
research_dir=ROOT/'01_investigacion' if args.scope=='consolidado' else ROOT/'01_investigacion'/('europa' if args.scope=='europa' else 'america_asia_oceania')
research_dir.mkdir(parents=True,exist_ok=True)
data=json.loads(path.read_text())
collections=['sources','organizations','opportunities','contacts','people','projects','country_coverage']
ids={}
for kind in collections:
 rows=data[kind]
 assert len({r['id'] for r in rows})==len(rows), f'ID duplicado en {kind}'
 ids[kind]={r['id'] for r in rows}
 for r in rows:
  assert not any(isinstance(v,str) and '\x00' in v for v in r.values()), 'NUL no permitido'
for kind in collections:
 for r in data[kind]:
  if r.get('source_id'): assert r['source_id'] in ids['sources'], (kind,r['id'],'fuente')
  if r.get('organization_id'): assert r['organization_id'] in ids['organizations'], (kind,r['id'],'organización')
  for x in r.get('extra_source_ids',[]): assert x in ids['sources']
for s in data['sources']:
 assert s['url'].startswith(('http://','https://'))
 date.fromisoformat(s['checked_on'])
cutoff=date.fromisoformat(data['meta']['as_of'])
valid={'abierta','recepcion_anual','anunciada_condicionada','cerrada','resultados_publicados','por_verificar'}
for r in data['opportunities']:
 assert r['status'] in valid
 if r.get('deadline_date'):
  d=date.fromisoformat(r['deadline_date'])
  assert not (r['status']=='abierta' and d<cutoff), ('Abierta con fecha pasada',r['id'])
 if r.get('deadline_time'): time.fromisoformat(r['deadline_time'])
 if r.get('deadline_timezone'): ZoneInfo(r['deadline_timezone'])
 if r.get('deadline_conflict'):
  assert r['deadline_precision']=='fecha_prudente_por_conflicto_no_resuelto'
  for key in ['embassy_date','portal_date']: date.fromisoformat(r['deadline_conflict'][key])
 if r.get('amount_min') is not None and r.get('amount_max') is not None:
  assert 0<=r['amount_min']<=r['amount_max']
for c in data['contacts']:
 if c.get('email'): assert re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',c['email']), c['id']
# Esquema explícito: los detalles JSONB conservan campos no normalizados.
columns={
 'sources':['id','title','url','checked_on'],
 'organizations':['id','name','country_code','source_id'],
 'opportunities':['id','organization_id','title','status','deadline_date','deadline_time','deadline_timezone','amount_min','amount_max','currency','verified_on','source_id'],
 'contacts':['id','organization_id','label','email','phone','source_id','verified_on'],
 'people':['id','organization_id','name','role','source_id','verified_on'],
 'projects':['id','organization_id','title','geography','status','source_id','verified_on'],
 'country_coverage':['id','country','status','source_id','verified_on']}
def literal(v):
 if v is None: return 'NULL'
 if isinstance(v,bool): return 'TRUE' if v else 'FALSE'
 if isinstance(v,(int,float)): return str(v)
 return "'"+str(v).replace("'","''")+"'"
sql=['-- Generado desde JSON, no editar manualmente.','BEGIN;','SET LOCAL standard_conforming_strings = on;']
for table in collections:
 cols=columns[table]
 for row in data[table]:
  values=[literal(row.get(c)) for c in cols]+[literal(json.dumps(row,ensure_ascii=False))+'::jsonb']
  names=cols+['details']
  updates=', '.join(c+'=EXCLUDED.'+c for c in names if c!='id')
  sql.append('INSERT INTO ong.'+table+' ('+', '.join(names)+') VALUES ('+', '.join(values)+') ON CONFLICT (id) DO UPDATE SET '+updates+';')
for row in data['opportunities']:
 sql.append('DELETE FROM ong.opportunity_sources WHERE opportunity_id='+literal(row['id'])+';')
 for src in [row['source_id']]+row.get('extra_source_ids',[]):
  sql.append('INSERT INTO ong.opportunity_sources VALUES ('+literal(row['id'])+', '+literal(src)+') ON CONFLICT DO NOTHING;')
digest=hashlib.sha256(path.read_bytes()).hexdigest()
sql.append('INSERT INTO ong.research_batches (sha256, as_of, snapshot) VALUES ('+literal(digest)+', '+literal(data['meta']['as_of'])+', '+literal(json.dumps(data,ensure_ascii=False))+'::jsonb) ON CONFLICT DO NOTHING;')
sql.append('COMMIT;')
(ROOT/('03_base_datos/seed_'+args.scope+'.sql')).write_text('\n'.join(sql)+'\n')
lines=['# Fuentes de investigación', '', 'Corte: '+data['meta']['as_of']+'. El tipo de acceso distingue lectura directa de extracto indexado. No se archivaron copias completas de las páginas.', '']
for r in data['sources']:
 lines += ['## '+r['id']+' — '+r['title'],'','['+r['title']+']('+r['url']+')','',f"Consulta: {r['checked_on']}. Tipo: {r['level']}. Acceso: {r['access']}.", '',r['note'],'']
(research_dir/'FUENTES.md').write_text('\n'.join(lines))
org_names={r['id']:r['name'] for r in data['organizations']}
src_urls={r['id']:r['url'] for r in data['sources']}
lines=['# Directorio público inicial','', 'Consultado el '+data['meta']['as_of']+'. Ningún contacto realizado. Reconfirmar los datos históricos antes de uso.', '', '| Organización / canal | Contacto público | Uso y fuente |','|---|---|---|']
for r in data['contacts']:
 channel=r.get('email') or r.get('phone') or r.get('url') or 'Formulario en página oficial'
 lines.append('| '+org_names[r['organization_id']]+' / '+r['label']+' | '+channel+' | '+r['purpose']+' — [fuente]('+src_urls[r['source_id']]+') |')
lines += ['','## Personas y cargos publicados','','No se atribuye responsabilidad sobre subvenciones por el solo cargo. No hay correos personales inferidos.','']
for r in data['people']:
 lines += ['- **'+r['name']+'** — '+r['role']+'. '+r['note']+' [Fuente]('+src_urls[r['source_id']]+')']
directory_name='DIRECTORIO_PUBLICO.md' if args.scope=='consolidado' else 'DIRECTORIO_'+args.scope.upper()+'.md'
(ROOT/'05_relacionamiento'/directory_name).write_text('\n'.join(lines)+'\n')
lines=['# Cobertura por país — '+args.scope, '', 'Control de alcance: no confundir búsqueda pendiente con ausencia de fondos. UE se registra separadamente. Se incluye un alcance ampliado de trabajo, sin pretensión de clasificación política oficial.', '', '| País | Estado de revisión | Fuente inicial |','|---|---|---|']
for r in data['country_coverage']:
 src='[Fuente]('+src_urls[r['source_id']]+')' if r.get('source_id') else 'Sin fuente suficiente'
 lines.append('| '+r['country']+' | '+r['status'].replace('_',' ')+' | '+src+' |')
(research_dir/'COBERTURA_PAISES.md').write_text('\n'.join(lines)+'\n')
print('Validación correcta. Registros:', {k:len(data[k]) for k in collections})
print('SQL de carga, fuentes, directorio y cobertura regenerados. No ejecutado contra PostgreSQL.')
