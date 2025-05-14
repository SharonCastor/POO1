class Pisto:
    def __init__ (self, hielera, hielera2):
        self.__hielera = hielera
        self.hielera2 = hielera2
    
    def pistear1(self):
        self.__hielera = "Vaciar"
        return self.__hielera
    
    def pistear2(self):
        self.hielera2 = "Mah. esta vacía"
        return self.hielera2
    
fiesta =Pisto("Cartón en hielera","Unas cuantas frias")

print(fiesta.pistear1())
print(fiesta.pistear2)

