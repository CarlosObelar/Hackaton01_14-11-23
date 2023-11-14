from flask import Flask
from modelo import db, Registro_gastos

# Instanciando la clase flask.
app = Flask(__name__)

# Configurando la base de datos.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializando la base de datos.
db.init_app(app)

# Creando la base de datos.
# with app.app_context():
#     db.create_all()

# Agregando manualmente ciertos gastos mensuales comúnes.
with app.app_context():
    gasto_01 = Registro_gastos(fecha = "10/01/2023", concepto = "ANDE", monto = 200000)
    gasto_02 = Registro_gastos(fecha = "10/01/2023", concepto = "Internet", monto = 250000)
    
    db.session.add(gasto_01)
    db.session.add(gasto_02)
    db.session.commit()