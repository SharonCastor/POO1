#Figuras
import math

class Figuras:
    def cal_perimetro(numLados, lado):
        perimetro = numLados * lado
        return perimetro

    def cal_area(numLados, lado):
        if numLados == 4:  
            area = lado * lado
        elif numLados == 3: 
            area = (math.sqrt(3) / 4 ) * (lado ** 2 )
        elif numLados == 5: 
            area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (lado ** 2)
        else: area = 0
        return area

           
        




