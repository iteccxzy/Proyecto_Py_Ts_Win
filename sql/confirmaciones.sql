 -- Table: public.confirmaciones

-- DROP TABLE public.confirmaciones;

CREATE TABLE public.confirmaciones
(
    materia_id integer NOT NULL,
    carrera_id integer NOT NULL,
    horario_id integer,
    fecha_inicio timestamp without time zone,
    docente_id integer NOT NULL,
    bimestre_id integer NOT NULL,
    confirmacion_id integer NOT NULL DEFAULT nextval('confirmaciones_confirmacion_id_seq'::regclass),
    zoom character varying COLLATE pg_catalog."default",
    CONSTRAINT confirmaciones_pkey PRIMARY KEY (confirmacion_id),
    CONSTRAINT bims_fkey FOREIGN KEY (bimestre_id)
        REFERENCES public.bimestres (bim_id) MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID,
    CONSTRAINT carreras_fkey FOREIGN KEY (carrera_id)
        REFERENCES public.carreras (carrera_id) MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID,
    CONSTRAINT docentes_fkey FOREIGN KEY (docente_id)
        REFERENCES public.docentes (docente_id) MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID,
    CONSTRAINT horarios_fkey FOREIGN KEY (horario_id)
        REFERENCES public.horarios (horario_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT materias_fkey FOREIGN KEY (materia_id)
        REFERENCES public.materias (materia_id) MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.confirmaciones
    OWNER to postgres;

-- Trigger: insert_semana

-- DROP TRIGGER insert_semana ON public.confirmaciones;

CREATE TRIGGER insert_semana
    AFTER INSERT
    ON public.confirmaciones
    FOR EACH ROW
    EXECUTE PROCEDURE public.semana();