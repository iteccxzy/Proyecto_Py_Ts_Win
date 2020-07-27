-- Table: public.bimestres

-- DROP TABLE public.bimestres;

CREATE TABLE public.bimestres
(
    bim_id integer NOT NULL,
    agno integer NOT NULL,
    descripcion character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT bimestres_pkey PRIMARY KEY (bim_id)
)

TABLESPACE pg_default;

ALTER TABLE public.bimestres
    OWNER to postgres;