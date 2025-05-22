#Práctica 3

# Clase base (superclase)
class Figura:
    def calcular_area(self):
        pass  # Método que será sobrescrito en las subclases

# Clases hijas (subclases) con diferentes implementaciones
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio * self.radio

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# Función que usa polimorfismo
def imprimir_area(figura):
    print(f"El área es: {figura.calcular_area()}")

# Creación de objetos de diferentes clases
mi_cuadrado = Cuadrado(4)
mi_circulo = Circulo(3)
mi_triangulo = Triangulo(5, 2)

# Llamamos a la función con diferentes objetos
imprimir_area(mi_cuadrado)  # "El área es: 16"
imprimir_area(mi_circulo)   # "El área es: 28.2744"
imprimir_area(mi_triangulo) # "El área es: 5"