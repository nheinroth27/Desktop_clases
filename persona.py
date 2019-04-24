#En el archivpero persona.py, crear un clase persona con atributo nombre
#Despues instanciar un objeto de tipo persona

class Persona:
    nombre = ""
    nacionalidad = ""
    remera = ""

    def __init__ (self, name, country:
        self.nombre = name
        self.nacionalidad = country 
        print ("Soy una persona, me lllamo", self.nombre, "y soy", self.nacionalidad)
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self):
        


persona1 = Persona ("Lucas", "paraguayo")