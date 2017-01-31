from app import app
from flask import render_template
from api.api import Feeling

from forms.forms import Formulario, ProductoForm, Registro
import json
from firebase import firebase


@app.route("/", methods=('GET','POST'))
def index():
	myForm = Formulario()
	myVideo = Feeling()
	contexto = myVideo.obtenVideo(myForm.sentimiento.data)
	#link= myVideo.url
	return render_template("index.html", data=contexto, form=myForm)
'''
@app.route("/producto", methods=('GET','POST'))
def producto():
	formulario = ProductoForm()
	fbase = firebase.FirebaseApplication('https://demoflask-d2c73.firebaseio.com/', None)
	if formulario.validate_on_submit():
		fbase.post('/producto',{'nombre':formulario.nombre.data,'telefono':formulario.telefono.data})
	result = fbase.get('/producto', None)
	return render_template("producto.html", data = result, form=formulario)

'''

@app.route("/producto", methods=('GET','POST'))
def producto():
	registro = Registro()
	fbase = firebase.FirebaseApplication('https://demoflask-d2c73.firebaseio.com/', None)
	if registro.validate_on_submit():
		fbase.post('/producto',{'nombre':registro.nombreCompleto.data,'telefono':registro.telefono.data, 'email':registro.email.data, 'password':registro.password.data})
	result = fbase.get('/producto', None)
	return render_template("producto.html", data = result, form=registro)

'''	
	
	myForm = Formulario()
	if myForm.validate_on_submit():
		myVideo = Feeling()
		contexto = myVideo.obtenVideo(myForm.sentimiento.data) #data es de WTForm
		if contexto != False:
			return render_template("index.html", data=contexto, form=myForm)
		else: 
			return render_template("404.html")
	else:
		return render_template("index.html", data=Feeling(), form=myForm)

'''


'''
@app.route("/")
def index():
	myVideo = Feeling()
	contexto = myVideo.obtenVideo("happy")
	link= myVideo.url
	return render_template("index.html", data=link)
'''