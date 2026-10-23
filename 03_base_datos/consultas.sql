-- Oportunidades con estado observado y advertencias de actualidad
SELECT * FROM ong.opportunity_dashboard ORDER BY deadline_date NULLS LAST;

-- Directorio de cooperación con trazabilidad
SELECT g.name, c.label, c.email, c.phone, c.verified_on, s.url,
 c.details->>'purpose' AS purpose
FROM ong.contacts c JOIN ong.organizations g ON g.id=c.organization_id
JOIN ong.sources s ON s.id=c.source_id ORDER BY g.name;

-- Antecedentes que mencionan Cusco: revisar el estado y la salvedad
SELECT g.name, p.title, p.geography, p.status, p.details->>'note' AS note, s.url
FROM ong.projects p JOIN ong.organizations g ON g.id=p.organization_id
JOIN ong.sources s ON s.id=p.source_id
WHERE p.geography ILIKE '%Cusco%';

-- Países que requieren más investigación
SELECT country, status FROM ong.country_coverage ORDER BY status, country;

-- Seguimientos registrados por el equipo (vacío al iniciar)
SELECT g.name, i.followup_on, i.next_action
FROM ong.interactions i JOIN ong.organizations g ON g.id=i.organization_id
WHERE i.followup_on <= CURRENT_DATE ORDER BY i.followup_on;
