from pathlib import Path
import re,json,shutil
r=Path(__file__).resolve().parents[1];q=r/'07_sitio_web/quarto';q.mkdir(exist_ok=True)
reports={'index':'01_investigacion/MAPA_FINANCIAMIENTO.md','europa':'01_investigacion/europa/INFORME_EUROPA_2026-10-22.md','america':'01_investigacion/america_norte/INFORME_EEUU_CANADA_2026-10-22.md','asia':'01_investigacion/asia/INFORME_ASIA_2026-10-22.md','oceania':'01_investigacion/oceania/ANEXO_FONDOS_2026-10-22.md','otras-fuentes':'01_investigacion/otras_fuentes/INFORME_COMPLEMENTARIO_2026-10-22.md','fuentes':'01_investigacion/FUENTES.md','proyectos':'04_cartera_proyectos/CONCEPTOS_INICIALES.md'}
lookup={str((r/v).resolve()):k+'.qmd' for k,v in reports.items()}
for name,src in reports.items():
 p=r/src;s=p.read_text();title=s.splitlines()[0].removeprefix('# ');s='\n'.join(s.splitlines()[1:])
 def link(m):
  target=m[1]
  if '://' in target or target.startswith('#'):return m[0]
  dest=(p.parent/target.split('#')[0]).resolve();url=lookup.get(str(dest))
  if not url:url='https://github.com/luabarcaparedes-art/ong-cusco/blob/main/'+str(dest.relative_to(r))
  return ']('+url+')'
 s=re.sub(r'\]\(([^)]+)\)',link,s)
 if name=='index':
  html=(r/'07_sitio_web/src/index.html').read_text();section=html[html.index('<section class="section wrap" id="mapa">'):html.index('<section class="research')];template=html[html.index('<template id="card-template">'):html.index('<script src=')]
  s='\nIniciativa social en formación desde Cusco, Perú. Nombre y constitución pendientes. Este sitio reúne investigación sobre cooperación, financiamiento y posibles alianzas.\n\n[Conocer la iniciativa](iniciativa/index.html){.btn .btn-outline-primary}\n\n## Explorar mecanismos de apoyo\n\n```{=html}\n'+section+template+'\n<script src="app.js" defer></script>\n```\n\n'+s
 (q/(name+'.qmd')).write_text('---\ntitle: '+json.dumps(title,ensure_ascii=False)+'\n---\n'+s+'\n')
(q/'_quarto.yml').write_text('''project:
  type: website
  output-dir: _site
  resources:
    - app.js
    - data/
website:
  title: "Mapa Integrado de Cooperación"
  site-url: https://luabarcaparedes-art.github.io/ong-cusco/
  navbar:
    left:
      - href: index.qmd
        text: Mapa y convocatorias
      - href: proyectos.qmd
        text: Proyectos
      - href: fuentes.qmd
        text: Fuentes
    right:
      - href: https://github.com/luabarcaparedes-art/ong-cusco
        text: GitHub
  sidebar:
    style: docked
    contents:
      - index.qmd
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
print('Fuentes QMD generadas:',len(reports))
