 -- Table: public.resultados

-- DROP TABLE public.resultados;

CREATE TABLE public.resultados
(
    resultado_id integer NOT NULL,
    descripcion character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT resultados_pkey PRIMARY KEY (resultado_id)
)

TABLESPACE pg_default;

ALTER TABLE public.resultados
    OWNER to postgres;