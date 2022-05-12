from cado.cnx_db import obtener_conexion


#listar_usuario
def obtener_usuario():
    conexion = obtener_conexion()
    usuario = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, dni, fullname, username, telefono, correo FROM usuarios")
        usuario = cursor.fetchall()
    conexion.close()
    return usuario

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
            "SELECT  dni, fullname, username,password, telefono, correo FROM usuario WHERE id = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario


def actualizar_usuario(dni, fullname, username, password, telefono, correo, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET dni = %s, fullname = %s, username = %s, password = %s, telefono = %s, correo = %s WHERE id = %s",
                       (dni, fullname, username, password, telefono, correo,id))
    conexion.commit()
    conexion.close()


# def insertar_usuario(tipo_persona,dni_ruc,nombres_usr,password,repassword,nombre,ape_paterno,ape_materno,razon_social,correo_usr,telefono_usr,direccion_usr):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("INSERT INTO usuarios(tipo_persona,dni_ruc,nombres_usr,nombre,password,repassword,ape_paterno,ape_materno,razon_social,correo_usr,telefono_usr,direccion_usr) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s, %s)",
#                        (tipo_persona,dni_ruc,nombres_usr,password,repassword,nombre,ape_paterno,ape_materno,razon_social,correo_usr,telefono_usr,direccion_usr))
#     conexion.commit()
#     conexion.close()





# def eliminar_usuario(id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
#     conexion.commit()
#     conexion.close()


# def obtener_usuario_por_id(id):
#     conexion = obtener_conexion()
#     usuario = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             "SELECT id,tipo_persona, dni_ruc, nombres_usr,password,repassword,nombre, ape_paterno,ape_materno,razon_social,correo_usr, telefono_usr, direccion_usr FROM usuarios WHERE id = %s", (id,))
#         usuario = cursor.fetchone()
#     conexion.close()
#     return usuario


# # def actualizar_usuario(nombre, descripcion, precio, id):
# #     conexion = obtener_conexion()
# #     with conexion.cursor() as cursor:
# #         cursor.execute("UPDATE usuarios SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
# #                        (nombre, descripcion, precio, id))
# #     conexion.commit()
# #     conexion.close()


# def actualizar_usuario(tipo_persona, dni_ruc, nombres_usr,nombre, ape_paterno,ape_materno,razon_social,correo_usr, telefono_usr, direccion_usr,  id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("UPDATE usuarios SET tipo_persona = %s, dni_ruc = %s, nombres_usr = %s, nombre = %s, ape_paterno = %s, ape_materno = %s, razon_social = %s, correo_usr = %s, telefono_usr = %s, direccion_usr = %s WHERE id = %s",
#                        (tipo_persona, dni_ruc, nombres_usr,nombre,ape_paterno,ape_materno,razon_social, correo_usr, telefono_usr, direccion_usr , id))
#     conexion.commit()
#     conexion.close()


# def actualizar_pass_usr(password,repassword, id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("UPDATE usuarios SET password = %s, repassword = %s WHERE id = %s",
#                        (password,repassword, id))
#     conexion.commit()
#     conexion.close()
