from cado.cnx_db import obtener_conexion


#listar_usuario
def obtener_usuario():
    conexion = obtener_conexion()
    usuario = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, dni, fullname, username,correo,telefono FROM usuarios")
        usuario = cursor.fetchall()
    conexion.close()
    return usuario

#eliminar_usuario
def eliminar_usuario(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT  dni, fullname, username, correo , telefono FROM usuarios WHERE id = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario


def actualizar_usuario(dni, fullname, username, correo, telefono, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET dni = %s, fullname = %s, username = %s,   correo = %s , telefono = %s WHERE id = %s",
                        (dni, fullname, username,correo, telefono, id))
    conexion.commit()
    conexion.close()


def insertar_usuario(dni ,fullname,username,password,telefono,correo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(dni ,fullname,username,password,telefono, correo) VALUES (%s, %s, %s,%s, %s, %s)",
                       (dni ,fullname,username,password,telefono, correo))
    conexion.commit()
    conexion.close()




