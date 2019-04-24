class Dinosaurio:
    patas = 4
    nombre = None
    def __init__ (self, canti_patas, un_nombre):
        self.patas = canti_patas
        self.nombre = un_nombre
        print ("Hola soy un dinosaurio y tengo",self.patas,"patas. Me llamo", self.nombre)
    
    def get_patas (self):
        return self.patas
    
    def set_patas (self,cantidad):
        self.patas = cantidad

    def cortar_patas (self):
        self.patas -= 1

dino1 = Dinosaurio(4, "Jose")

