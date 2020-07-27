 -- Table: public.duraciones

-- DROP TABLE public.duraciones;

CREATE TABLE public.duraciones
(
    duracion_id integer NOT NULL,
    cantidad_bimestres integer NOT NULL,
    CONSTRAINT duraciones_pkey PRIMARY KEY (duracion_id)
)

TABLESPACE pg_default;

ALTER TABLE public.duraciones
    OWNER to postgres;