from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
import controlador_usuario
import controlador_conductor
import controlador_vehiculo
from flask_recaptcha import ReCaptcha


app = Flask(__name__, template_folder="Vistas")
# recaptcha = ReCaptcha(app=app)

# app.config.update(dict(
#     RECAPTCHA_ENABLED = True,
#     RECAPTCHA_SITE_KEY = "6LfiqtgfAAAAAJmtvXyZlHEDLHRxtGMHAunlOvGy",
#     RECAPTCHA_SECRET_KEY = "6LfiqtgfAAAAAFZHcqVfxs0mWZBjT6vH656uK6ID",
# ))
 
# recaptcha = ReCaptcha()
# recaptcha.init_app(app)
 
# app.config['SECRET_KEY'] = 'demolan'


#############################################################################
#VISTAS_LOGIN
@app.route("/")
def home():
    return render_template('login.html')

@app.route("/recuperar%password")
def home_recu_passw():
    return render_template("recuperar_password.html")

#############################################################################
#VISTAS_ADMIN

@app.route("/home")
def Index():
    return render_template("index.html")

@app.route('/manage')
def mante_usr():
    usuario = controlador_usuario.obtener_usuario()
    return render_template('frmusr.html', usuario=usuario)
    
@app.route("/agregar_usuario")
def formulario_agregar_usuario():
    return render_template("agregar_usuario.html")
    

@app.route("/frmeditpass/<int:id>")
def resset_password(id):
    usuario = controlador_usuario.obtener_usuario_por_id(id)
    return render_template("reset_pass.html", usuario=usuario)

@app.route("/formulario_editar_usuario/<int:id>")
def editar_usuario(id):
    usuario = controlador_usuario.obtener_usuario_por_id(id)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route('/', methods=["POST"])
def eliminar_usuario():
    controlador_usuario.eliminar_usuario(request.form["id"])
    return redirect('manage')

@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    id = request.form["id"]
    dni = request.form["dni"]
    fullname = request.form["fullname"]
    username = request.form["username"]
    correo = request.form["correo"]
    telefono = request.form["telefono"]
    
    controlador_usuario.actualizar_usuario(dni, fullname, username, correo,telefono, id)
    return redirect("/manage")

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    dni = request.form["dni"]
    fullname = request.form["fullname"]
    username = request.form["username"]
    password = request.form["password"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    controlador_usuario.insertar_usuario(dni, fullname, username, password, telefono,correo)
    return redirect("/manage")


#############################################################################
#VISTAS_mechan
#funcion listado
@app.route('/manage_conductor')
def manageconductor():
    conductor = controlador_conductor.obtener_conductor()
    return render_template('conductor/frmconductor.html', conductor=conductor)

@app.route("/agregar_conductor")
def formulario_agregar_conductor():
    return render_template("conductor/agregar_conductor.html")

@app.route("/guardar_conductor", methods=["POST"])
def guardar_conductor():
    dni = request.form["dni"]
    nombre = request.form["nombre"]
    celular = request.form["celular"]
    controlador_conductor.insertar_conductor(dni, nombre, celular)
    return redirect('/manage_conductor')

@app.route('/delect_conductor', methods=["POST"])
def eliminar_Conductor():
    controlador_conductor.eliminar_Conductor(request.form["id"])
    return redirect('/manage_conductor')
    # return render_template('frmconductor.html')

@app.route("/formulario_editar_conductor/<int:id>")
def editar_conductor(id):
    conductor = controlador_conductor.obtener_conductor_por_id(id)
    return render_template("conductor/editar_conductor.html", conductor=conductor)


@app.route("/actualizar_conductor", methods=["POST"])
def actualizar_conductor():
    id = request.form["id"]
    dni = request.form["dni"]
    nombre = request.form["nombre"]
    celular = request.form["celular"]
    controlador_conductor.actualizar_conductor( dni, nombre, celular, id)
    return redirect('/manage_conductor')

#############################################################################
#FORMULARIO GUIVAR


@app.route('/adm_vehiculo')
def mante_vehiculo():
    vehiculo = controlador_vehiculo.obtener_vehiculo()
    return render_template('vehiculo/frmvehiculo.html', vehiculo=vehiculo)


@app.route("/agregar_vehiculo")
def formulario_agregar_vehiculo():
    return render_template("vehiculo/agregar_vehiculo.html")


@app.route("/formulario_editar_vehiculo/<int:id>")
def editar_vehiculo(id):
    vehiculo = controlador_vehiculo.obtener_vehiculo_por_id(id)
    return render_template("vehiculo/editar_vehiculo.html", vehiculo=vehiculo)

@app.route('/adm_vehiculo', methods=["POST"])
def eliminar_vehiculo():
    controlador_vehiculo.eliminar_Vehiculo(request.form["id"])
    return redirect('/adm_vehiculo')

@app.route("/actualizar_vehiculo", methods=["POST"])
def actualizar_vehiculo():
    id = request.form["id"]
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    color = request.form["color"]
    numero_unidad = request.form["numero_unidad"]
    placa = request.form["placa"]
    
    controlador_vehiculo.actualizar_vehiculo(marca,modelo,color,numero_unidad,placa, id)
    return redirect("/adm_vehiculo")







@app.route("/guardar_vehiculo", methods=["POST"])
def guardar_vehiculo():
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    color = request.form["color"]
    numero_unidad = request.form["numero_unidad"]
    placa = request.form["placa"]
    controlador_vehiculo.insertar_vehiculo(marca, modelo, color, numero_unidad, placa)
    return redirect("/adm_vehiculo")




#############################################################################

# DEFINIENDO ERRORES - EXCEPCIONES

@app.errorhandler(404)
def pagina_no_encontrada(Error_404):
    return render_template('error_404.html',Error_404="Página no encontrada..."), 404

@app.errorhandler(500)
def pagina_no_encontrada(Error_500):
    return render_template('error_500.html')


   
#####:::::::: Config::::::::####  
if __name__ == "__main__":
    app.run(debug=True,
    host="0.0.0.0",
    port="8443")
#####::::::::::::::::::::####