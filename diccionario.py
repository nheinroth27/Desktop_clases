'''diccionario = {} #Ejemplo de diccionario

nombre_de_diccionario = {"nombre_clave":"valor"}

print(dic_persona.get("estatura"))
if dic_persona.get("estatura"):
print("Si existe la clave")
'''


#Crear un diccionario persona con claves nombre, edad, estatura 
# e imprimir cada uno de los valores de las claves en un print diferente. Luego cambiar la edad a otro valor $
# e imprimir de nuevo. Lueeego agragar un par clave/valor


d_persona = {"nombre":"Sandra","edad":27,"estatura":1.70}

print (d_persona["nombre"])
print (d_persona["edad"])
print (d_persona["estatura"])
d_persona["edad"] = 17
print (d_persona["edad"])
d_persona ["club"] = "None"
print (d_persona)

#Luego agregar un par clave "hobbie" que contenga una lista de hobbies e imprimir todo el diccionario

d_persona ["hobbie"] = ["cocinar","bordar","cuidar las plantas"]

print(d_persona)

d_persona["edad"] = input("Define tu edad ")

print(d_persona["edad"])
