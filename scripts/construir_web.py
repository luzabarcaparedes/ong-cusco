#!/usr/bin/env python3
"""Construye la landing estática para GitHub Pages. Sin dependencias externas."""
from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'02_datos/cooperacion_consolidada_2026-10-22.json').read_text())
orgs={row['id']:row for row in data['organizations']};sources={row['id']:row for row in data['sources']}
countries={row['id']:row['country'] for row in data['country_coverage']}
countries.update({'INT':'Regional / internacional','EU':'Unión Europea','PE':'Perú'})
entries=[]
for row in data['opportunities']:
 org=orgs[row['organization_id']]; mode=row.get('instrument_type','subvencion')
 if any(token in mode for token in ['beca','credito_tecnologico','aporte_tecnologico']):group='tecnologia'
 elif any(token in mode for token in ['articulacion','cooperacion','alianza','inversion_publica','invitacion_red','investigacion']):group='alianzas'
 else:group='proyectos'
 entries.append({'id':row['id'],'title':row['title'],'organization':org['name'],'country':countries.get(org['country_code'],org['country_code']),'group':group,'status':row['status'],'summary':row.get('eligibility') or row.get('ngo_new') or org['route'],'geography':row.get('geography',''),'eligibility':row.get('ngo_new','Elegibilidad por verificar.'),'restrictions':row.get('restrictions',''),'deadline_date':row.get('deadline_date'),'deadline_precision':row.get('deadline_precision'),'deadline_conflict':row.get('deadline_conflict'),'verified_on':row['verified_on'],'source_url':sources[row['source_id']]['url']})
rank={'abierta':0,'recepcion_anual':1,'anunciada_condicionada':2,'por_verificar':3,'cerrada':4,'resultados_publicados':5}
entries.sort(key=lambda r:(rank.get(r['status'],6),r['deadline_date'] or '9999',r['title']))
public={'as_of':data['meta']['as_of'],'note':'Estados observados, no monitoreo en tiempo real. Revalidar bases y elegibilidad. No incluye contactos personales.','entries':entries}
out=ROOT/'docs';out.mkdir(exist_ok=True);(out/'data').mkdir(exist_ok=True)
for file in (ROOT/'07_sitio_web/src').iterdir():
 if file.is_file():shutil.copyfile(file,out/file.name)
html=(out/'index.html').read_text().replace('__ENTITIES__',str(len(data['organizations']))).replace('__REFERENCES__',str(len(data['sources']))).replace('__OPPORTUNITIES__',str(len(entries)))
(out/'index.html').write_text(html)
(out/'data/catalogo.json').write_text(json.dumps(public,ensure_ascii=False,indent=2)+'\n')
(out/'.nojekyll').write_text('')
print('Landing construida en docs/:',len(entries),'fichas;',len(data['organizations']),'entidades;',len(data['sources']),'referencias.')
