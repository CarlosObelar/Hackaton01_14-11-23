from flask import Flask, render_template, request, redirect, url_for
from modelo import db, Registro_gastos

# Instanciando la clase flask.
app = Flask(__name__)

# Configurando la base de datos.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializando la base de datos.
db.init_app(app)

### RUTAS ###

# Ruta principal - Landing Page.
@app.route("/")
def index():
    return render_template("landing_page.html")

## RUTAS DEL CRUD ###

# CRUD - READ.
@app.route("/home")
def home():
    
    gastos = Registro_gastos.query.all()
    total = sum(g.monto for g in gastos)
    
    # Cambiando el formato de los montos en Guaraníes.
    gastos_formateados = [{"id": g.id, "fecha": g.fecha, "concepto": g.concepto, "monto": "{:,.0f} Gs".format(g.monto)} for g in gastos]
    total_formateado = "{:,.0f} Gs".format(total)
    
    return render_template("home.html", gastos=gastos_formateados, total=total_formateado)

# CRUD - CREATE.
@app.route("/crear", methods=["POST"])
def crear():
    if request.method == "POST":
        
        # Obteniendo los datos del formulario.
        fecha = request.form.get("fecha")
        concepto = request.form.get("concepto")
        monto = request.form.get("monto")
        
        # Creando el objeto "gasto".
        gasto = Registro_gastos(fecha=fecha, concepto=concepto, monto=monto)
        
        # Agregando a la base de datos.
        db.session.add(gasto)
        
        # Guardando los cambios realizados.
        db.session.commit()
                
        return redirect(url_for("home"))
    
# CRUD - UPDATE
@app.route("/actualizar/<id>", methods = ["GET", "POST"])
def actualizar(id):
    
    # Obteniendo el personaje a actualizar.
    gasto = Registro_gastos.query.get(id)
    if request.method == "POST":
        
        # Obteniendo los datos del formulario.
        gasto.fecha = request.form.get("fecha")
        gasto.concepto = request.form.get("concepto")
        gasto.monto = request.form.get("monto")
        
        # Agregando las actualizaciones de los gastos a la base de datos.
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("actualizar.html", gasto=gasto)

# CRUD - DELETE
@app.route("/eliminar/<id>")
def eliminar(id):
    
    # Obteniendo el gasto a eliminar.
    gastos = Registro_gastos.query.get(id)
    
    # Eliminando el gasto seleccionado.
    db.session.delete(gastos)
    
    # Guardando los cambios realizados.
    db.session.commit()
    
    return redirect(url_for("home"))




### BREAKPOINT ###
if __name__ == "__main__":
    app.run(debug = True)