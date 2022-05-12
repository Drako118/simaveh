from cado.cnx_db import obtener_conexion


#listar_conductor
def obtener_conductor():
    conexion = obtener_conexion()
    conductor = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, dni, nombre, celular FROM conductor")
        conductor = cursor.fetchall()
    conexion.close()
    return conductor

#eliminar_conductor
def eliminar_Conductor(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM conductor WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_conductor_por_id(id):
    conexion = obtener_conexion()
    conductor = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT  dni, nombre, celular FROM conductor WHERE id = %s", (id,))
        conductor = cursor.fetchone()
    conexion.close()
    return conductor


def actualizar_conductor(dni, nombre, celular, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE conductor SET dni = %s, nombre = %s, celular = %s, WHERE id = %s",
                        (dni, nombre, celular, id))                      
    conexion.commit()
    conexion.close()


def insertar_conductor(dni, nombre, celular):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO conductor(dni, nombre, celular) VALUES (%s, %s, %s)",
                       (dni, nombre, celular))
    conexion.commit()
    conexion.close()




