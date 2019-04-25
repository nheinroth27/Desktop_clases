
import requests
from pprint import pprint #Para una impresion mas "linda"
API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Fight Club"
busqueda = URL + API_KEY + "&t=" + titulo

print(busqueda)



respuesta = requests.get(busqueda)
dic_peli = respuesta.json()
#texto = respuesta.text()
#print(texto)
print (dic_peli)
print ("")
print ("")
print ("El director de la pelicula", dic_peli["Title"],"fue",dic_peli["Director"])
print ("")
print ("")

#Ejercicio. Consultar el API de OMDB e imprimir el nombre de del Director de Fight CLub
#Crear una funcion que reciba como argumento el titulo de una pelicua y retorne los actores de esa peli

import requests
def act_peli (pelicula):
    API_KEY = "595695c3"
    URL = "http://www.omdbapi.com/?apikey="
    busqueda = URL + API_KEY + "&t=" + pelicula
    respuesta = requests.get(busqueda)
    dic_peli = respuesta.json()
    print ("En la pelicula",dic_peli["Title"],"estan",dic_peli["Actors"])

act_peli("Los Buscadores")