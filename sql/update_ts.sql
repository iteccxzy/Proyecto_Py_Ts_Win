 -- PROCEDURE: public.update_ts(date, time without time zone, integer)

-- DROP PROCEDURE public.update_ts(date, time without time zone, integer);

CREATE OR REPLACE PROCEDURE public.update_ts(
	fecha_ date,
	hora_ time without time zone,
	id_ integer)
LANGUAGE 'sql'

AS $BODY$update tutorias set hora = hora_ , fecha=fecha_ where tutoria_id=id_$BODY$;
