from flask_sqlalchemy import SQLAlchemy

# Instanciando SQLAlchemy.
db = SQLAlchemy()

### MODELOS ###

# Creando el modelo de la base de datos.

class Registro_gastos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(12))
    concepto = db.Column(db.String(50))
    monto = db.Column(db.Integer)
    total = db.Column(db.Integer)