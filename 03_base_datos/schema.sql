-- PostgreSQL 14+. No instala servidor ni crea base de datos.
-- Ejecutar en una base dedicada al proyecto con rol autorizado.
BEGIN;
CREATE SCHEMA IF NOT EXISTS ong;
CREATE TABLE IF NOT EXISTS ong.sources (
 id text PRIMARY KEY,
 title text NOT NULL,
 url text NOT NULL CHECK (url ~ '^https?://'),
 checked_on date NOT NULL,
 details jsonb NOT NULL
);
CREATE TABLE IF NOT EXISTS ong.organizations (
 id text PRIMARY KEY,
 name text NOT NULL,
 country_code text NOT NULL,
 source_id text NOT NULL REFERENCES ong.sources(id),
 details jsonb NOT NULL
);
CREATE TABLE IF NOT EXISTS ong.opportunities (
 id text PRIMARY KEY,
 organization_id text NOT NULL REFERENCES ong.organizations(id),
 title text NOT NULL,
 status text NOT NULL CHECK (status IN ('abierta','recepcion_anual','anunciada_condicionada','cerrada','resultados_publicados','por_verificar')),
 deadline_date date,
 deadline_time time,
 deadline_timezone text,
 amount_min numeric CHECK (amount_min >= 0),
 amount_max numeric CHECK (amount_max >= 0),
 currency text,
 verified_on date NOT NULL,
 source_id text NOT NULL REFERENCES ong.sources(id),
 details jsonb NOT NULL,
 CHECK (amount_min IS NULL OR amount_max IS NULL OR amount_min <= amount_max)
);
CREATE TABLE IF NOT EXISTS ong.contacts (
 id text PRIMARY KEY,
 organization_id text NOT NULL REFERENCES ong.organizations(id),
 label text NOT NULL,
 email text,
 phone text,
 source_id text NOT NULL REFERENCES ong.sources(id),
 verified_on date NOT NULL,
 details jsonb NOT NULL
);
CREATE TABLE IF NOT EXISTS ong.people (
 id text PRIMARY KEY,
 organization_id text NOT NULL REFERENCES ong.organizations(id),
 name text NOT NULL,
 role text NOT NULL,
 source_id text NOT NULL REFERENCES ong.sources(id),
 verified_on date NOT NULL,
 details jsonb NOT NULL
);
CREATE TABLE IF NOT EXISTS ong.projects (
 id text PRIMARY KEY,
 organization_id text NOT NULL REFERENCES ong.organizations(id),
 title text NOT NULL,
 geography text NOT NULL,
 status text NOT NULL,
 source_id text NOT NULL REFERENCES ong.sources(id),
 verified_on date NOT NULL,
 details jsonb NOT NULL
);
CREATE TABLE IF NOT EXISTS ong.country_coverage (
 id text PRIMARY KEY,
 country text NOT NULL,
 status text NOT NULL,
 source_id text REFERENCES ong.sources(id),
 verified_on date NOT NULL,
 details jsonb NOT NULL
);
-- Historial de lotes: conserva cada instantánea JSON con fecha y huella.
CREATE TABLE IF NOT EXISTS ong.research_batches (
 sha256 text PRIMARY KEY,
 as_of date NOT NULL,
 imported_at timestamptz NOT NULL DEFAULT now(),
 snapshot jsonb NOT NULL
);
-- Relaciones adicionales entre registros y fuentes, con integridad referencial.
CREATE TABLE IF NOT EXISTS ong.opportunity_sources (
 opportunity_id text REFERENCES ong.opportunities(id),
 source_id text REFERENCES ong.sources(id),
 PRIMARY KEY (opportunity_id, source_id)
);
CREATE TABLE IF NOT EXISTS ong.interactions (
 id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 organization_id text NOT NULL REFERENCES ong.organizations(id),
 contact_id text REFERENCES ong.contacts(id),
 person_id text REFERENCES ong.people(id),
 occurred_at timestamptz NOT NULL,
 channel text NOT NULL,
 purpose text NOT NULL,
 outcome text,
 next_action text,
 followup_on date,
 document_path text
);
CREATE INDEX IF NOT EXISTS opportunities_deadline_idx ON ong.opportunities(deadline_date);
CREATE INDEX IF NOT EXISTS organizations_country_idx ON ong.organizations(country_code);
CREATE INDEX IF NOT EXISTS opportunities_org_idx ON ong.opportunities(organization_id);
CREATE INDEX IF NOT EXISTS contacts_org_idx ON ong.contacts(organization_id);
CREATE INDEX IF NOT EXISTS interactions_followup_idx ON ong.interactions(followup_on);
CREATE OR REPLACE VIEW ong.opportunity_dashboard AS
 SELECT o.id, g.name AS organization, g.country_code, o.title,
 o.status AS status_at_last_check, o.verified_on, o.deadline_date,
 o.deadline_time, o.deadline_timezone, o.amount_min, o.amount_max, o.currency,
 CASE WHEN o.deadline_date < CURRENT_DATE THEN 'plazo_fecha_pasado'
      WHEN o.status = 'abierta' THEN 'revalidar_antes_de_postular'
      ELSE o.status END AS calendar_flag,
 s.url AS primary_source_url, o.details->>'ngo_new' AS ngo_new,
 o.details->>'restrictions' AS restrictions,
 o.details->>'instrument_type' AS instrument_type,
 o.details->>'deadline_precision' AS deadline_precision,
 o.details->'deadline_conflict' AS deadline_conflict
 FROM ong.opportunities o JOIN ong.organizations g ON g.id=o.organization_id
 JOIN ong.sources s ON s.id=o.source_id;
COMMIT;
