 -- PROCEDURE: public.insert_confirmacion(character varying, character varying, timestamp without time zone, integer, character varying, character varying, character varying)

-- DROP PROCEDURE public.insert_confirmacion(character varying, character varying, timestamp without time zone, integer, character varying, character varying, character varying);

CREATE OR REPLACE PROCEDURE public.insert_confirmacion(
	_materia character varying,
	_carrera character varying,
	_fecha timestamp without time zone,
	_hora integer,
	_docente character varying,
	_bim character varying,
	_zoom character varying)
LANGUAGE 'sql'

AS $BODY$INSERT INTO public.confirmaciones(
	materia_id, carrera_id, fecha_inicio, horario_id, docente_id, bimestre_id,zoom)
	
select materias.materia_id, 
carreras.carrera_id,  
_fecha, (Select Cast(_hora as INT)) ,

(select docente_id from docentes where concat(nombre, ' ', apellidos)= _docente ), 
(select bim_id from bimestres where descripcion=_bim),
_zoom
from materias 
join carreras on carreras.carrera_id=materias.carrera_id 
where materias.descripcion=_materia and carreras.descripcion=_carrera$BODY$;
