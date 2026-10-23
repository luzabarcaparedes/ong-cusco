# Sitio del Mapa Integrado de Cooperación

El sitio principal se genera con Quarto desde `quarto/`. Incluye portada de recomendaciones, mapa estratégico, catálogo de 45 mecanismos con filtro por país del cooperante, tipo, estado y periodo; primero abiertas/anunciadas y luego anteriores, informes por región, conceptos de proyectos y fuentes, con navegación y búsqueda de texto. La presentación de la iniciativa permanece en `docs/iniciativa/`. “Proyecto Cusco” es una denominación descriptiva; la ONG todavía no tiene nombre definitivo ni constitución.

## Reconstrucción

Requisitos: Python 3.9 o posterior y Quarto CLI (probado con 1.10.19). Desde la raíz:

```sh
python3 scripts/construir_sitio.py
```

Los QMD se regeneran desde los informes Markdown; editar los MD originales y reconstruir. El catálogo parte de la instantánea consolidada JSON. Los archivos HTML de `docs/` se publican en GitHub Pages, rama `main`, carpeta `/docs`; no requieren ejecutar Quarto en el servidor.

No hay formularios, analítica, credenciales ni conexión a PostgreSQL. Los estados corresponden al corte de investigación; los plazos pasados se señalan sin detectar prórrogas. Las fichas públicas no incluyen personas/contactos; el directorio institucional permanece en el repositorio.
