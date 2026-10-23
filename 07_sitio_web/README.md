# Landing de Proyecto Cusco

Presentación de una iniciativa en formación y explorador de fuentes. “Proyecto Cusco” es una denominación descriptiva del sitio, no el nombre legal definitivo de la futura ONG.

- Código editable: `src/index.html`, `src/styles.css`, `src/app.js`, `src/favicon.svg`.
- Publicación estática: carpeta `/docs` del repositorio, rama `main`.
- Catálogo público: fichas resumidas y fuentes; no incluye el directorio de personas/contactos.
- Sin formularios de captación de datos, analítica ni servicios de terceros en la página.
- Tipografías del sistema, ilustración vectorial local y sin dependencias de ejecución.

Desde la raíz:

```sh
python3 scripts/preparar_datos.py
python3 scripts/construir_web.py
python3 -m http.server 8080 --directory docs
```

Visitar `http://localhost:8080`. Los cambios del catálogo se hacen en la instantánea consolidada JSON, seguida de reconstrucción. No editar `docs/data/catalogo.json` manualmente.

Los estados son observaciones de investigación. La página marca como pasado un plazo anterior al día actual de Perú, pero no detecta prórrogas, nuevas ediciones o cancelaciones. La fecha de corte sigue siendo visible. El conflicto de cierre DAP Australia se muestra expresamente.

Para GitHub Pages: publicar desde rama `main`, carpeta `/docs`. El sitio es estático y no necesita secretos ni claves API. El directorio completo de investigación permanece en Markdown dentro del repositorio.
