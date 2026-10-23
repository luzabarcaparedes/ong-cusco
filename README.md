# ONG — Proyecto en Cusco

Iniciativa por constituir; nombre pendiente. Inicio y corte de esta investigación: **22 de octubre de 2026**.

## Empezar aquí

- [Análisis de prioridades temáticas](01_investigacion/ANALISIS_PRIORIDADES_TEMATICAS.md).
- [Plan de desarrollo del sitio](07_sitio_web/PLAN_DESARROLLO_SITIO.md).

- [Recomendaciones y prioridades](01_investigacion/RECOMENDACIONES.md).
- [Catálogo por país y estado](https://luzabarcaparedes.github.io/ong-cusco/convocatorias.html).

Sitio generado con Quarto: portada institucional con dos programas propuestos, análisis temático, plan del sitio y catálogo ordenado por actualidad con filtro por país del cooperante, mapa estratégico e informes por región. [Instrucciones de reconstrucción](07_sitio_web/README.md).

- [Landing y catálogo público](https://luzabarcaparedes.github.io/ong-cusco/).
- [Otras fuentes: cooperación multilateral, empresas y fondos nacionales](01_investigacion/otras_fuentes/INFORME_COMPLEMENTARIO_2026-10-22.md).

- **[Mapa integrado: Europa, Estados Unidos, Canadá, Asia y anexo Oceanía](01_investigacion/MAPA_FINANCIAMIENTO.md)**.
- [Informe Estados Unidos y Canadá](01_investigacion/america_norte/INFORME_EEUU_CANADA_2026-10-22.md).
- [Informe Asia](01_investigacion/asia/INFORME_ASIA_2026-10-22.md).
- [Australia y Nueva Zelanda](01_investigacion/oceania/ANEXO_FONDOS_2026-10-22.md).
- [Datos consolidados](02_datos/cooperacion_consolidada_2026-10-22.json): 55 entidades, 45 registros de oportunidades/mecanismos, 34 canales y 15 personas. Las 126 referencias incluyen alguna duplicación documental; 30 antecedentes incluyen uno marcado como posible duplicado.
- [Fuentes consolidadas](01_investigacion/FUENTES.md) y [cobertura consolidada](01_investigacion/COBERTURA_PAISES.md).

- [Informe de cooperación europea](01_investigacion/europa/INFORME_EUROPA_2026-10-22.md): oportunidades, antecedentes de Cusco y estrategia de acceso.
- [Directorio público](05_relacionamiento/DIRECTORIO_PUBLICO.md): canales institucionales y personas con fuente.
- [Cobertura por país](01_investigacion/europa/COBERTURA_PAISES.md): distingue revisión parcial, búsqueda exploratoria y pendientes.
- [Fuentes](01_investigacion/europa/FUENTES.md): 52 referencias, acceso y fecha de consulta.
- [Datos estructurados](02_datos/europa_2026-10-22.json): 23 entidades, 11 convocatorias/ciclos, 14 canales, 7 personas y 9 antecedentes.
- [Preparación PostgreSQL](03_base_datos/README.md): esquema y carga inicial; todavía sin servidor instalado.
- [Conceptos de proyectos](04_cartera_proyectos/CONCEPTOS_INICIALES.md): cinco hipótesis para validar territorialmente.
- [Definición y secuencia del proyecto](00_gestion/PROYECTO.md).

## Lectura rápida

Chequia tiene convocatoria para proyectos 2027 con cierre próximo, pero exige entidad inscrita y excluye proyectos de capacitación. IKI Medium ofrece una vía mediante líder alemán. IKI Small anuncia convocatoria futura condicionada. El fondo cultural suizo solo corresponde si existe un vínculo cultural suizo. Las condiciones y las fuentes están en el informe.

La búsqueda europea es una **primera entrega parcial**, no un inventario exhaustivo. Hay 50 países en el control de cobertura y fuentes iniciales para 22. No encontrar una convocatoria no prueba inexistencia de fondos. No hay elegibilidad confirmada de la futura ONG en ningún programa.

## Organización de carpeta

| Carpeta | Uso |
|---|---|
| `00_gestion` | Propósito, método, decisiones y pendientes |
| `01_investigacion` | Informes y fuentes por continente |
| `02_datos` | Instantáneas JSON para consulta y migración |
| `03_base_datos` | PostgreSQL: esquema, seed y consultas |
| `04_cartera_proyectos` | Conceptos y futuras propuestas |
| `05_relacionamiento` | Directorio y futura documentación institucional |
| `06_constitucion` | Reservada para fase jurídica e identidad |
| `07_sitio_web` | Fuente de la landing y guía de construcción |
| `08_empresas` | Reservada para fondos empresariales |
| `09_otras_regiones` | Reservada para expansión territorial |
| `scripts` | Validación y generación de archivos derivados |

La instantánea consolidada JSON es la fuente editable de trabajo; el script la usa por defecto y regenera SQL, directorio, fuentes y cobertura. Las instantáneas europea y de ampliación se conservan como entregas originales. Si se edita un lote original, también debe actualizarse deliberadamente el consolidado; no hay fusión automática. Mantener IDs estables y agregar una instantánea por nuevo corte. No editar esos documentos derivados esperando que el cambio persista al regenerar.

No se ha contactado a terceros, presentado solicitudes ni configurado seguimiento automático. Se conserva la fecha de verificación para evitar presentar antecedentes como oportunidades vigentes.
