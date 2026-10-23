# Preparación para PostgreSQL

Se entrega esquema, carga inicial reproducible, consultas y una instantánea JSON consolidada como fuente editable. **No hay servidor instalado ni base creada.** Esta fase prepara la migración; no implementa el aplicativo.

Modelo: fuentes, organizaciones, oportunidades, contactos institucionales, personas, proyectos, cobertura por país e interacciones. Las relaciones principales tienen claves foráneas; los campos descriptivos adicionales se conservan en JSONB. Cada oportunidad incluye fecha de verificación y estado observado. Las instantáneas completas quedan en `research_batches`, identificadas por SHA-256.

## Regeneración local

Desde la carpeta raíz, con Python 3.9 o posterior y base de zonas horarias:

```sh
python3 scripts/preparar_datos.py
```

El validador revisa IDs, referencias, fechas, zonas horarias, montos y correos; genera carga SQL y documentos derivados. No hace solicitudes de red ni envía información.

## Carga futura

Una vez exista una base dedicada y una conexión autorizada, ejecutar desde la raíz con `psql` y su configuración de conexión segura. No guardar contraseñas en archivos del proyecto:

```sh
psql -X -v ON_ERROR_STOP=1 -f 03_base_datos/schema.sql
psql -X -v ON_ERROR_STOP=1 -f 03_base_datos/seed_consolidado.sql
```

La carga actualiza registros por ID y no elimina registros ausentes del JSON. No ejecutarla en una base ajena al proyecto. Esquema y seed tienen transacciones separadas. Antes de cambios futuros de esquema se requieren migraciones versionadas: `CREATE TABLE IF NOT EXISTS` no modifica tablas ya creadas.

## Verificación y límites

Se validaron datos y generación local. No se ejecutó el SQL en PostgreSQL: no se encontraron servidor ni cliente `psql` en el entorno. Falta prueba de migración real, roles, permisos, copias de seguridad y despliegue. No hay infraestructura remota provisionada.

`status` es el estado al corte, no un monitoreo en vivo. La vista `opportunity_dashboard` añade una bandera de calendario; no transforma automáticamente una convocatoria anunciada en abierta, ni acredita prórrogas. Las zonas son IANA y se mantienen horas originales. Una fecha sin hora permanece sin hora.

La fecha suiza se deriva de una regla de fin de mes y conserva esa precisión en `details`. Una persona identificada históricamente conserva esa salvedad. No hay tabla de beneficiarios ni información sensible comunitaria en esta base inicial.

## Ampliación a otros continentes

El script usa por defecto `02_datos/cooperacion_consolidada_2026-10-22.json`. Genera `seed_consolidado.sql`, fuentes/cobertura en `01_investigacion` y directorio global. Conserva `seed_europa.sql` como entrega histórica. No cargar ambos esperando conjuntos independientes: comparten IDs y se actualizan por clave.

Para validar/regenerar un lote separado sin reemplazar el directorio global:

```sh
python3 scripts/preparar_datos.py --dataset 02_datos/america_asia_oceania_2026-10-22.json --scope ampliacion
```

Los mecanismos nuevos conservan `instrument_type`, presencia, región y salvedades en JSONB. Se distinguen becas personales, cooperación técnica y subvenciones; no contar todos los registros como concursos. Australia conserva conflicto de fecha y una meta prudente del 8/11/2026; el portal muestra 9/11 a las 09:00 PET. La fecha principal no es una confirmación de cierre oficial.
