 -- Table: public.horarios

-- DROP TABLE public.horarios;

CREATE TABLE public.horarios
(
    horario_id integer NOT NULL,
    dia character varying(255) COLLATE pg_catalog."default" NOT NULL,
    hora time without time zone NOT NULL,
    CONSTRAINT horarios_pkey PRIMARY KEY (horario_id)
)

TABLESPACE pg_default;

ALTER TABLE public.horarios
    OWNER to postgres;