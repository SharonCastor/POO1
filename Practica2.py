#Figuras
import math

class Figura:
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

class Pentagono(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        apotema = (self.lado / (2 * math.tan(math.pi / 5)))
        return (5 * self.lado * apotema) / 2
    
    def calcular_perimetro(self):
        return 5 * self.lado

# Ejemplo de uso
triangulo = Triangulo(10, 5, 10, 8, 6)
cuadrado = Cuadrado(4)
pentagono = Pentagono(6)

print("Área del triángulo:", triangulo.calcular_area())
print("Perímetro del triángulo:", triangulo.calcular_perimetro())
print("Área del cuadrado:", cuadrado.calcular_area())
print("Perímetro del cuadrado:", cuadrado.calcular_perimetro())
print("Área del pentágono:", pentagono.calcular_area())
print("Perímetro del pentágono:", pentagono.calcular_perimetro())


from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':
    ALLOWED_IP = '10.2.80.150'
    app.run(host = '0.0.0.0', port = 5000)