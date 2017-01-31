from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class Formulario(Form):
	sentimiento = StringField(validators=[DataRequired()])

class ProductoForm(Form):
	nombre = StringField('Nombre', validators=[DataRequired()])
	telefono = StringField('Telefono', validators=[DataRequired()])


class Registro(Form):
	nombreCompleto = StringField('Nombre Completo', validators=[DataRequired()])
	telefono = StringField('Telefono', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	password = StringField('Password', validators=[DataRequired()])
