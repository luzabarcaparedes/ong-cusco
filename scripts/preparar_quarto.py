from pathlib import Path
import re,json,shutil
r=Path(__file__).resolve().parents[1];q=r/'07_sitio_web/quarto';q.mkdir(exist_ok=True)
reports={'index':'01_investigacion/RECOMENDACIONES.md','mapa':'01_investigacion/MAPA_FINANCIAMIENTO.md','europa':'01_investigacion/europa/INFORME_EUROPA_2026-10-22.md','america':'01_investigacion/america_norte/INFORME_EEUU_CANADA_2026-10-22.md','asia':'01_investigacion/asia/INFORME_ASIA_2026-10-22.md','oceania':'01_investigacion/oceania/ANEXO_FONDOS_2026-10-22.md','otras-fuentes':'01_investigacion/otras_fuentes/INFORME_COMPLEMENTARIO_2026-10-22.md','fuentes':'01_investigacion/FUENTES.md','proyectos':'04_cartera_proyectos/CONCEPTOS_INICIALES.md'}
reports['convocatorias']='01_investigacion/MAPA_FINANCIAMIENTO.md'
lookup={str((r/v).resolve()):k+'.qmd' for k,v in reports.items()}
lookup[str((r/'01_investigacion/MAPA_FINANCIAMIENTO.md').resolve())]='mapa.qmd'
for name,src in reports.items():
 p=r/src;s=p.read_text();title=s.splitlines()[0].removeprefix('# ');s='\n'.join(s.splitlines()[1:])
 def link(m):
  target=m[1]
  if '://' in target or target.startswith('#') or target.endswith('.qmd'):return m[0]
  dest=(p.parent/target.split('#')[0]).resolve();url=lookup.get(str(dest))
  if not url:url='https://github.com/luzabarcaparedes/ong-cusco/blob/main/'+str(dest.relative_to(r))
  return ']('+url+')'
 s=re.sub(r'\]\(([^)]+)\)',link,s)
 if name=='convocatorias':
  html=(r/'07_sitio_web/src/index.html').read_text();section=html[html.index('<section class="section wrap" id="mapa">'):html.index('<section class="research')];template=html[html.index('<template id="card-template">'):html.index('<script src=')]
  title='Oportunidades y mecanismos de apoyo'
  s='\nConsulta primero las oportunidades con recepción abierta y las anunciadas. Al final aparecen los ciclos anteriores y resultados. País corresponde al cooperante, no al territorio beneficiario. **Corte de investigación: 22 de octubre de 2026.**\n\n```{=html}\n'+section+template+'\n<script src="app.js" defer></script>\n```\n'
 if name=='index':
  s='\n```{=html}\n<div class="home-intro"><p class="eyebrow">CUSCO · PERÚ · INICIATIVA EN FORMACIÓN</p><p class="home-lead">Conectar necesidades locales con cooperación que pueda convertirse en proyectos.</p><p>55 entidades · 45 mecanismos · 126 referencias registradas</p></div>\n```\n'+s

 (q/(name+'.qmd')).write_text('---\ntitle: '+json.dumps(title,ensure_ascii=False)+('\ntoc: false\nsidebar: false' if name=='index' else '')+'\n---\n'+s+'\n')
(q/'_quarto.yml').write_text('''project:
  type: website
  output-dir: _site
  resources:
    - app.js
    - data/
website:
  title: "Mapa Integrado de Cooperación"
  site-url: https://luzabarcaparedes.github.io/ong-cusco/
  navbar:
    left:
      - href: index.qmd
        text: Recomendaciones
      - href: convocatorias.qmd
        text: Oportunidades
      - href: mapa.qmd
        text: Mapa estratégico
      - href: proyectos.qmd
        text: Proyectos
      - href: fuentes.qmd
        text: Fuentes
    right:
      - href: https://github.com/luzabarcaparedes/ong-cusco
        text: GitHub
  sidebar:
    style: docked
    contents:
      - index.qmd
      - convocatorias.qmd
      - mapa.qmd
      - europa.qmd
      - america.qmd
      - asia.qmd
      - oceania.qmd
      - otras-fuentes.qmd
      - proyectos.qmd
      - fuentes.qmd
  search: true
format:
  html:
    theme: cosmo
    lang: es
    toc: true
    css: custom.css
    link-external-newwindow: true
execute:
  enabled: false
''')
shutil.copyfile(r/'07_sitio_web/src/app.js',q/'app.js');(q/'data').mkdir(exist_ok=True);shutil.copyfile(r/'docs/iniciativa/data/catalogo.json',q/'data/catalogo.json')
(q/'custom.css').write_text('''body{background:#fbfaf6;color:#263e35}h1,h2,h3{font-family:Georgia,serif}.navbar{background:#263e35}.navbar a,.navbar .navbar-title{color:#fff!important}.catalog-controls{display:flex;flex-wrap:wrap;gap:1rem;margin:1.5rem 0}.catalog-controls input,.catalog-controls select{max-width:100%;padding:.6rem;border:1px solid #9aaa9e;border-radius:4px}.select-wrap{display:grid;font-size:.9rem}.catalog{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem}.source-card{padding:1.2rem;border:1px solid #ced6cc;border-radius:8px;background:white;overflow-wrap:anywhere}.source-card h3{font-size:1.25rem;margin-top:.7rem}.card-top{display:flex;justify-content:space-between;gap:.5rem;font-size:.8rem}.status-badge{background:#eee8dc;padding:.15rem .4rem;border-radius:4px}.status-badge.open{background:#dcebd6}.card-type,.card-org,.card-deadline,.catalog-note{font-size:.85rem}.card-type{color:#a75335;margin-top:.7rem}.source-card details{margin:1rem 0}.button,.text-button{padding:.6rem 1rem;border:1px solid #263e35;background:white;border-radius:4px;color:#263e35}.section-heading h2{display:none}.results-meta{display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem}.catalog-note{margin-top:1rem}.eyebrow{font-size:.8rem;letter-spacing:.08em}.search{align-self:end}.search span{display:none}[hidden]{display:none!important}@media(max-width:720px){.catalog{grid-template-columns:1fr}.catalog-controls{display:grid}.catalog-controls input{width:100%}}''')
with (q/'custom.css').open('a') as f:f.write('\n.catalog-group{grid-column:1/-1;margin:1.8rem 0 .2rem;font-size:1.35rem}.home-intro{padding:2rem 0;margin-bottom:2rem;border-bottom:1px solid #ced6cc}.home-lead{font-family:Georgia,serif;font-size:clamp(1.7rem,3vw,2.7rem);max-width:850px;line-height:1.22}.catalog-controls{background:#f0f2eb;padding:1rem;border-radius:8px}.catalog-controls>label{flex:1 1 180px}.catalog-controls select{width:100%}.source-card summary{cursor:pointer}.source-card{border-top:3px solid #8c9d84}.source-card .source-link{font-weight:600}.catalog-controls input:focus,.catalog-controls select:focus{outline:3px solid #a7c4ae;outline-offset:2px}\n')
print('Fuentes QMD generadas:',len(reports))
