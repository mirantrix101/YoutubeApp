import requests
import random



class Feeling(object):
	url = ""
	titulo = ""
	descripcion = ""
	resultado = ""
	

	def __init__(self):
		self.endpoint = "https://www.googleapis.com/youtube/v3/search"
		self.apikey = "AIzaSyCKxb2yYHm_CpF5iGLCX7C8LV3z32Nyv7I"

	
	def obtenVideo(self, sentimiento):
		parameters = {"part":"snippet", "key":self.apikey, "q":sentimiento}
		resultado = requests.get(self.endpoint, params=parameters).json()
		
		'''
		#random
		numbers= [0, 1, 2, 3, 4]
		randy = random.choice(numbers)
		arry = [randy]
		'''

		listado = resultado["items"][0]  #estudiar esta linea

		preVideo = "https://www.youtube.com/embed/"  #extra
		postVideo = "?rel=0&modestbranding=1&autohide=1&showinfo=0"

		self.url = preVideo+listado["id"]["videoId"]+postVideo
		self.titulo = listado["snippet"]["title"]
		self.descripcion = "Descripción: "+listado["snippet"]["description"]

		#Aquí pueden hacer un resultado con las 3 variables
		self.resultado = ""
		return self
