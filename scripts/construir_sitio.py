#!/usr/bin/env python3
"""Construye la investigación y el sitio Quarto para GitHub Pages."""
from pathlib import Path
import subprocess,sys,shutil,os
ROOT=Path(__file__).resolve().parents[1]
for script in ['preparar_datos.py','construir_web.py','preparar_quarto.py']:
 subprocess.run([sys.executable,str(ROOT/'scripts'/script)],cwd=ROOT,check=True)
quarto=os.environ.get('QUARTO_BIN') or shutil.which('quarto')
if not quarto:raise SystemExit('Instala Quarto CLI o define QUARTO_BIN con la ruta de su ejecutable.')
subprocess.run([quarto,'render',str(ROOT/'07_sitio_web/quarto')],cwd=ROOT,check=True)
shutil.copytree(ROOT/'07_sitio_web/quarto/_site',ROOT/'docs',dirs_exist_ok=True)
(ROOT/'docs/.nojekyll').touch()
print('Sitio completo construido en docs/.')
