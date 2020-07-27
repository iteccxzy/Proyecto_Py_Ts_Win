 -- Table: public.carreras

-- DROP TABLE public.carreras;

CREATE TABLE public.carreras
(
    carrera_id integer NOT NULL,
    descripcion character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT carreras_pkey PRIMARY KEY (carrera_id)
)

TABLESPACE pg_default;

ALTER TABLE public.carreras
    OWNER to postgres;