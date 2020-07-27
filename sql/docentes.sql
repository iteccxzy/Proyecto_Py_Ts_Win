 -- Table: public.docentes

-- DROP TABLE public.docentes;

CREATE TABLE public.docentes
(
    docente_id integer NOT NULL,
    nombre character varying(255) COLLATE pg_catalog."default" NOT NULL,
    apellidos character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT docentes_pkey PRIMARY KEY (docente_id)
)

TABLESPACE pg_default;

ALTER TABLE public.docentes
    OWNER to postgres;