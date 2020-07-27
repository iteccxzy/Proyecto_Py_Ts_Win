 -- Table: public.tutorias

-- DROP TABLE public.tutorias;

CREATE TABLE public.tutorias
(
    resultado_id integer,
    fecha date,
    hora time without time zone,
    confirmacion_id integer NOT NULL,
    tutoria_id integer NOT NULL DEFAULT nextval('tutorias_tutoria_id_seq'::regclass),
    zoom_user character varying COLLATE pg_catalog."default",
    CONSTRAINT tutorias_pkey PRIMARY KEY (tutoria_id),
    CONSTRAINT confirmaciones_fkey FOREIGN KEY (confirmacion_id)
        REFERENCES public.confirmaciones (confirmacion_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT resultados_fkey FOREIGN KEY (resultado_id)
        REFERENCES public.resultados (resultado_id) MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.tutorias
    OWNER to postgres;