import psycopg2


def consulta_principal():
    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")
    cursor = db.cursor()

    # realizamos la consulta sql

    cursor.execute('''
                      select ca.descripcion , ma.descripcion, doc.nombre, doc.apellidos, fecha, hora, zoom_user

from tutorias tu
join  confirmaciones co on co.confirmacion_id= tu.confirmacion_id
join materias ma on ma.materia_id=co.materia_id
join carreras ca on ca.carrera_id=co.carrera_id
join docentes doc on doc.docente_id=co.docente_id

where fecha=CURRENT_DATE''')

    return cursor.fetchall()


def consulta_carga_ts_carrera():

    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")
    cursor = db.cursor()

    # realizamos la consulta sql

    cursor.execute('''
                       select  descripcion from carreras''')

    data = []
    res = cursor.fetchall()
    for i in range(len(res)):
        data += (list(res[i]))

    return data


def consulta_carga_ts_materia(m):

    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")
    cursor = db.cursor()

    temp = str(m)
    print(temp)
    cursor.execute("SELECT MATERIAS.DESCRIPCION \
        FROM MATERIAS JOIN CARRERAS ON CARRERAS.CARRERA_ID=MATERIAS.CARRERA_ID WHERE CARRERAS.DESCRIPCION = '%s'" % (temp))

    data = []
    res = cursor.fetchall()
    for i in range(len(res)):
        data += (list(res[i]))

    return data


def consulta_carga_ts_docente():

    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")
    cursor = db.cursor()

    # realizamos la consulta sql

    cursor.execute('''
                      select  concat (nombre, ' ',  apellidos) from docentes''')

    data = []
    res = cursor.fetchall()
    for i in range(len(res)):
        data += (list(res[i]))

    return data


def consulta_carga_ts_bimestre():

    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")
    cursor = db.cursor()

    # realizamos la consulta sql

    cursor.execute('''
        select  descripcion from bimestres
            where agno= extract(year from NOW())
                ''')

    data = []
    res = cursor.fetchall()
    for i in range(len(res)):
        data += (list(res[i]))

    return data


def consulta_guardar_ts(_materia, _carrera, _fecha, _hora, _docente, _bim, _zoom):

    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")
    cursor = db.cursor()

    cursor.execute('call public.insert_confirmacion(%s, %s, %s, %s,%s, %s, %s);', [
                   _materia, _carrera, _fecha, _hora, _docente, _bim, _zoom, ])

    db.commit()

    cursor.close()
    db.close()


def consulta_busqueda_ts(m):
    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")
    cursor = db.cursor()

    # realizamos la consulta sql

    cursor.execute('''
                      select ca.descripcion , ma.descripcion, doc.nombre, doc.apellidos,
                      fecha, hora, zoom_user, tu.tutoria_id

from tutorias tu
join  confirmaciones co on co.confirmacion_id= tu.confirmacion_id
join materias ma on ma.materia_id=co.materia_id
join carreras ca on ca.carrera_id=co.carrera_id
join docentes doc on doc.docente_id=co.docente_id

where fecha='%s'
''' % (m))

    return cursor.fetchall()


def consulta_del_ts(j):
    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")
    cursor = db.cursor()

    # realizamos la consulta sql

    cursor.execute('''
                    delete from tutorias where tutoria_id='%s'
        ''' % (j))

    db.commit()

    cursor.close()
    db.close()


def consulta_edit(a, b, c):

    db = psycopg2.connect(user="postgres",
                          password="",
                          host="localhost",
                          port="5432",
                          database="tutorias")

    cursor = db.cursor()


    cursor.execute('call public.update_ts(%s, %s, %s);', [
                   a,b,c, ])

    db.commit()

    cursor.close()
    db.close()
    


