# Plan para desarrollar el sitio institucional

Propuesta de trabajo del 22 de octubre de 2026. El sitio actual es un prototipo público generado con Quarto y publicado en GitHub Pages. El plan separa la presentación institucional del observatorio de cooperación, conservando la investigación como respaldo. Los tiempos son rangos de planificación, no fechas comprometidas ni servicios ya implementados.

## Objetivo y públicos

Que un oficial de cooperación, especialista o posible aliado entienda en pocos minutos qué problema queremos abordar, dónde, con qué enfoque, en qué etapa estamos y qué colaboración buscamos. La comunidad debe poder comprender la propuesta sin lenguaje de convocatorias. El equipo necesita una herramienta privada para investigar y gestionar relaciones; no todo su contenido corresponde al sitio público.

## Arquitectura propuesta

| Sección | Contenido | Condición de publicación |
|---|---|---|
| Inicio | Propósito, dos programas, territorio, forma de colaboración y estado institucional | La agenda se identifica como propuesta |
| Quiénes somos | Nombre, constitución, gobierno, equipo y experiencia individual verificada | Publicar datos profesionales consentidos; no DNI, domicilios ni expediente notarial |
| Enfoque y programas | Problemas, población, método, límites y resultados esperados | Sustento y capacidades verificables; separar metas de logros |
| Proyectos | Fichas con estados idea, diseño, formulado, ejecución y cierre | No llamar ejecutado a un concepto ni mostrar beneficiarios ficticios |
| Cooperación y evidencia | Catálogo filtrable, bases, fechas, fuentes y notas de análisis | Diferenciar convocatoria, programa bilateral, crédito tecnológico y alianza |
| Territorio y conocimiento | Diagnósticos, notas de contexto y aprendizajes propios o citados | Año, geografía y derechos de uso claros |
| Transparencia | Documentos institucionales públicos, políticas y rendiciones | Publicar al existir y pasar revisión; no simular certificados |
| Colaborar y contacto | Tipos de alianza, perfil breve y canal institucional | Correo y responsable definidos antes de activar formulario |

## Fases y entregables

### Fase 1 Enfoque y contenido base

**Duración orientativa: una a dos semanas.** Revisar y decidir las dos líneas propuestas; seleccionar criterios territoriales y revisar el lenguaje con posibles usuarios. Completar perfil de trabajo, mapa de contenidos y guía editorial. Registrar qué afirmaciones tienen evidencia y qué capacidades están pendientes. Responsable sugerido: dirección promotora, con apoyo de especialistas por identificar.

**Salida verificable:** agenda aprobada por la promotora, ficha de audiencia, inventario de contenidos y lista de datos faltantes. La portada actual ya permite revisar la propuesta, sin sustituir esa validación.

### Fase 2 Identidad y diseño

**Duración orientativa: una a dos semanas, tras la decisión de enfoque.** Elegir nombre y revisar disponibilidad jurídica y digital; definir identidad visual y dominio si se desea. Diseñar navegación, portada y plantilla de proyecto para móvil y escritorio. La futura marca no debe confundirse con “Proyecto Cusco”, denominación descriptiva usada en el prototipo.

**Salida verificable:** sistema visual y prototipo navegable revisados, con textos finales de presentación. No comprar dominio ni contratar servicios sin decidir titular y costo.

### Fase 3 Sitio institucional inicial

**Duración orientativa: dos a tres semanas, con identidad y contenido disponibles.** Implementar Inicio, Quiénes somos, Programas, Proyectos, Evidencia y Contacto. Preparar español primero; inglés después de revisar la traducción. Los contenidos en quechua requieren colaboración lingüística competente. Revisar accesibilidad, navegación con teclado, móvil, carga, metadatos y enlaces.

**Salida verificable:** versión pública con contenido aprobado, contacto real y ficha institucional descargable. Si falta un dato, omitirlo o indicar su estado; no rellenar con texto que sugiera operación inexistente.

### Fase 4 Observatorio y herramienta privada

**Duración orientativa: dos a cuatro semanas adicionales; depende del alcance y del equipo.** Mantener la consulta pública estática si basta. Para edición multiusuario y seguimiento de relaciones, desplegar PostgreSQL en un entorno privado, ejecutar y probar migraciones, definir acceso, backups y responsables. Preparar un backend que publique solo los campos aprobados.

**Salida verificable:** datos migrados y probados, recuperación de backup demostrada, permisos revisados y flujo de publicación controlado. GitHub Pages seguirá siendo una capa estática: no almacena claves de base de datos ni sustituye un backend.

### Fase 5 Operación y mejora

**Cadencia a definir según capacidad.** Asignar una persona a la revisión editorial y otra al mantenimiento técnico, o documentar una sola responsable inicial. Proponer revisión semanal de plazos próximos y mensual del resto; esta cadencia todavía no es una automatización activa. Mantener historial de cambios, incidencias y correcciones.

**Salida verificable:** calendario y responsables acordados, fecha de última revisión visible y procedimiento para retirar contenido desactualizado.

## Modelo mínimo de contenido

- Programa: objetivo, necesidad y fuente, población propuesta, geografía, actividades, capacidades requeridas y resultados esperados.
- Proyecto: estado, problema, evidencia, roles, indicadores, presupuesto cuando exista, financiación confirmada o pendiente y fecha de actualización.
- Oportunidad: cooperante, país de origen, territorio elegible, instrumento, estado observado, cierre y zona horaria, requisitos, montos, bases y calidad de acceso a la fuente.
- Evidencia: institución autora, título, URL, fecha de publicación y consulta, ámbito y afirmación respaldada.
- Contacto privado: institución, rol profesional, fuente pública, vigencia y registro de comunicaciones autorizadas. No publicar agendas personales ni documentos de identidad.

## Reglas editoriales para el público de cooperación

Presentar por separado lo que proponemos, lo que estamos preparando y lo que efectivamente hemos ejecutado. Cada resultado publicado debe tener soporte. Los logos de financiadores, testimonios, fotografías identificables y nombres de socios requieren autorización y relación real. Una cita de un programa no debe parecer respaldo institucional.

Mostrar la capacidad verificable del equipo sin trasladar automáticamente su experiencia individual a la ONG. Evitar promesas sobre traducción, IA sin conexión o despliegue territorial que no hayan sido probadas. Priorizar utilidad y lenguaje claro sobre palabras de moda de cada donante.

## Decisiones necesarias

Nombre y dominio; identidad pública; contacto y responsable; equipo y experiencia acreditable; territorio del primer diagnóstico; población prioritaria; presupuesto de desarrollo y mantenimiento; modalidad de edición y tratamiento de datos. No se necesita decidir ahora una plataforma compleja para seguir mejorando el prototipo.

## Criterios de aceptación

La portada explica enfoque, territorio, etapa y colaboración sin atribuciones falsas. Cada oportunidad enlaza su fuente y conserva sus restricciones. Las fichas permiten distinguir un proyecto propio de un antecedente ajeno. El sitio funciona en móvil y con teclado, sin enlaces rotos. No expone documentos notariales ni claves. La actualización del contenido tiene responsable y el sistema privado se prueba antes de almacenar datos de seguimiento.
