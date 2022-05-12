from cado.cnx_db import obtener_conexion


#listar_vehiculo
def obtener_vehiculo():
    conexion = obtener_conexion()
    vehiculo = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, marca, modelo, color, numero_unidad, placa FROM vehiculo")
        vehiculo = cursor.fetchall()
    conexion.close()
    return vehiculo

#eliminar_vehiculo
def eliminar_Vehiculo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM vehiculo WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_vehiculo_por_id(id):
    conexion = obtener_conexion()
    vehiculo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT marca, modelo, color,numero_unidad, placa FROM vehiculo WHERE id = %s", (id,))
        vehiculo = cursor.fetchone()
    conexion.close()
    return vehiculo


def actualizar_vehiculo(marca, modelo,color,numero_unidad, placa, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE vehiculo SET marca = %s, modelo = %s, color = %s,  numero_unidad = %s , placa = %s WHERE id = %s",
                        (marca, modelo,color,numero_unidad, placa, id))
    conexion.commit()
    conexion.close()


def insertar_vehiculo(marca, modelo, color, numero_unidad, placa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO vehiculo(marca, modelo, color, numero_unidad, placa) VALUES (%s, %s, %s,%s, %s)",
                       (marca, modelo, color, numero_unidad, placa))
    conexion.commit()
    conexion.close()





# def eliminar_vehiculo(id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("DELETE FROM vehiculos WHERE id = %s", (id,))
#     conexion.commit()
#     conexion.close()


# def obtener_vehiculo_por_id(id):
#     conexion = obtener_conexion()
#     vehiculo = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             "SELECT id,tipo_persona, dni_ruc, nombres_usr,password,repassword,nombre, ape_paterno,ape_materno,razon_social,correo_usr, telefono_usr, direccion_usr FROM vehiculos WHERE id = %s", (id,))
#         vehiculo = cursor.fetchone()
#     conexion.close()
#     return vehiculo


# # def actualizar_vehiculo(nombre, descripcion, precio, id):
# #     conexion = obtener_conexion()
# #     with conexion.cursor() as cursor:
# #         cursor.execute("UPDATE vehiculos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
# #                        (nombre, descripcion, precio, id))
# #     conexion.commit()
# #     conexion.close()


# def actualizar_vehiculo(tipo_persona, dni_ruc, nombres_usr,nombre, ape_paterno,ape_materno,razon_social,correo_usr, telefono_usr, direccion_usr,  id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("UPDATE vehiculos SET tipo_persona = %s, dni_ruc = %s, nombres_usr = %s, nombre = %s, ape_paterno = %s, ape_materno = %s, razon_social = %s, correo_usr = %s, telefono_usr = %s, direccion_usr = %s WHERE id = %s",
#                        (tipo_persona, dni_ruc, nombres_usr,nombre,ape_paterno,ape_materno,razon_social, correo_usr, telefono_usr, direccion_usr , id))
#     conexion.commit()
#     conexion.close()


# def actualizar_pass_usr(password,repassword, id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("UPDATE vehiculos SET password = %s, repassword = %s WHERE id = %s",
#                        (password,repassword, id))
#     conexion.commit()
#     conexion.close()
