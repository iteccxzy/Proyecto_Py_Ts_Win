 -- FUNCTION: public.semana()

-- DROP FUNCTION public.semana();

CREATE FUNCTION public.semana()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$begin

insert into tutorias ( confirmacion_id, zoom_user, fecha, hora)

select  confirmaciones.confirmacion_id, zoom,  fecha_inicio, horarios.hora
from confirmaciones
join horarios on horarios.horario_id= confirmaciones.horario_id
left join tutorias on tutorias.confirmacion_id=confirmaciones.confirmacion_id
left join resultados on resultados.resultado_id=tutorias.resultado_id
order by  confirmaciones.confirmacion_id desc
limit 1;

insert into tutorias ( confirmacion_id, zoom_user, fecha, hora)

select  confirmaciones.confirmacion_id, zoom,  fecha_inicio + interval '7 day', horarios.hora
from confirmaciones
join horarios on horarios.horario_id= confirmaciones.horario_id
left join tutorias on tutorias.confirmacion_id=confirmaciones.confirmacion_id
left join resultados on resultados.resultado_id=tutorias.resultado_id
order by  confirmaciones.confirmacion_id desc
limit 1
;

insert into tutorias ( confirmacion_id, zoom_user, fecha, hora)

select  confirmaciones.confirmacion_id, zoom,  fecha_inicio + interval '14 day', horarios.hora
from confirmaciones
join horarios on horarios.horario_id= confirmaciones.horario_id
left join tutorias on tutorias.confirmacion_id=confirmaciones.confirmacion_id
left join resultados on resultados.resultado_id=tutorias.resultado_id
order by  confirmaciones.confirmacion_id desc
limit 1
;

insert into tutorias ( confirmacion_id, zoom_user, fecha, hora)

select  confirmaciones.confirmacion_id, zoom,  fecha_inicio + interval '21 day', horarios.hora
from confirmaciones
join horarios on horarios.horario_id= confirmaciones.horario_id
left join tutorias on tutorias.confirmacion_id=confirmaciones.confirmacion_id
left join resultados on resultados.resultado_id=tutorias.resultado_id
order by  confirmaciones.confirmacion_id desc
limit 1

;
insert into tutorias ( confirmacion_id, zoom_user, fecha, hora)

select  confirmaciones.confirmacion_id, zoom,  fecha_inicio + interval '28 day', horarios.hora
from confirmaciones
join horarios on horarios.horario_id= confirmaciones.horario_id
left join tutorias on tutorias.confirmacion_id=confirmaciones.confirmacion_id
left join resultados on resultados.resultado_id=tutorias.resultado_id
order by  confirmaciones.confirmacion_id desc
limit 1

;
insert into tutorias ( confirmacion_id, zoom_user, fecha, hora)

select  confirmaciones.confirmacion_id, zoom,  fecha_inicio + interval '35 day', horarios.hora
from confirmaciones
join horarios on horarios.horario_id= confirmaciones.horario_id
left join tutorias on tutorias.confirmacion_id=confirmaciones.confirmacion_id
left join resultados on resultados.resultado_id=tutorias.resultado_id
order by  confirmaciones.confirmacion_id desc
limit 1

;
insert into tutorias ( confirmacion_id, zoom_user, fecha, hora)

select  confirmaciones.confirmacion_id, zoom,  fecha_inicio + interval '42 day', horarios.hora
from confirmaciones
join horarios on horarios.horario_id= confirmaciones.horario_id
left join tutorias on tutorias.confirmacion_id=confirmaciones.confirmacion_id
left join resultados on resultados.resultado_id=tutorias.resultado_id
order by  confirmaciones.confirmacion_id desc
limit 1

;
insert into tutorias ( confirmacion_id, zoom_user, fecha, hora)

select  confirmaciones.confirmacion_id, zoom,  fecha_inicio + interval '49 day', horarios.hora
from confirmaciones
join horarios on horarios.horario_id= confirmaciones.horario_id
left join tutorias on tutorias.confirmacion_id=confirmaciones.confirmacion_id
left join resultados on resultados.resultado_id=tutorias.resultado_id
order by  confirmaciones.confirmacion_id desc
limit 1
;

 RETURN NULL;
end
$BODY$;

ALTER FUNCTION public.semana()
    OWNER TO postgres;
