#Figuras
from math import sqrt
from math import pi
from math import tan

class figura:
    def cal_perimetro(numLados, lado):
        perimetro = numLados * lado
        return perimetro

    def cal_area(numLados, lado):
        if numLados == 4:  
            area = lado * lado
        elif numLados == 3: 
            area = (sqrt(3) / 4 ) * (lado ** 2 )
        elif numLados == 5: 
            area = (numLados * (lado)^2) / (4 * tan(pi / numLados))
        else: area = 0
        return area
    




           
        




