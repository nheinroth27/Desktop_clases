#En el archivpero persona.py, crear un clase persona con atributo nombre
#Despues instanciar un objeto de tipo persona

class Persona:
    nombre = None
    edad = 27

    def __init__ (self, name, years):
        self.nombre = name
        self.edad = years
        print ("Soy una persona, me lllamo", self.nombre, "y tengo", self.edad)
    
    def get_edad (self):
        return self.edad
    
    def set_edad (self, cantidad):
        self.edad = cantidad

    def cumple (self):
        self.edad += 1

persona1 = Persona ("Jose", 27)        
