from abc import ABC, abstractmethod
 
class FiguraGeometrica(ABC):
     @abstractmethod
     def calcular_area(self):
         pass
     @abstractmethod
     def calcular_perimetro(self):
         pass
     def describir(self):
         return f"Soy una figura con área {self.calcular_area()}"
     
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return 3.14 * self.radio**2
        
    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio
    
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
        
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)