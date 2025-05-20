from abc import ABC, abstractmethod

class Padres(ABC):
    @abstractmethod
    def rasgos(self):
        pass

class Hijo1(Padres):
    def rasgos(self):
        return "color de piel"

class Hijo2(Padres):
    def rasgos(self):
        return "color de ojos"

hijo1 = Hijo1()
hijo2 = Hijo2()

print("hijo 1 ", hijo1.rasgos())
print("hijo 2 ", hijo2.rasgos())

class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def hacer_sonido(self):
        return "sonido generico"
    
class perro(Animal):
    def hacer_sonido(self):
        return "guau guau"

perrito = perro("Blacky", "Husky") 
print(perrito.nombre)
print(perrito.raza)
print(perrito.hacer_sonido())
