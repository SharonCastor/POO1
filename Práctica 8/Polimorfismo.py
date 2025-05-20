class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

def sonido_animal(animal: Animal):
    print(animal.hacer_sonido())

mi_perro = Perro()
mi_gato = Gato()

print(sonido_animal(mi_perro))
print(sonido_animal(mi_gato))