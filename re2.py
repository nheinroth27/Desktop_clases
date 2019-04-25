import requests

url = "https://dolar.melizeche.com/api/1.0"
respuesta = requests.get(url)
texto = respuesta.text
print (respuesta)
print(texto)
print(len(texto))

cotizacion = respuesta.json()
print(cotizacion)
print(len(texto))
print(type(cotizacion))