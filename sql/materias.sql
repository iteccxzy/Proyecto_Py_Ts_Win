 -- Table: public.materias

-- DROP TABLE public.materias;

CREATE TABLE public.materias
(
    materia_id integer NOT NULL,
    carrera_id integer NOT NULL,
    descripcion character varying(255) COLLATE pg_catalog."default" NOT NULL,
    duracion_id integer,
    CONSTRAINT materias_pkey PRIMARY KEY (materia_id),
    CONSTRAINT carreras_fkey FOREIGN KEY (carrera_id)
        REFERENCES public.carreras (carrera_id) MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID,
    CONSTRAINT duraciones_fkey FOREIGN KEY (duracion_id)
        REFERENCES public.duraciones (duracion_id) MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.materias
    OWNER to postgres;