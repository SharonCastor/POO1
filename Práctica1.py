#Figuras
import math

lados = float(input("¿Cuántos lados tiene tu figura? \n"))
distancia= float(input("¿Cuánto mide cada lado? \n"))

class figura:
    def area(lados,distancia):
        if lados <= 2 :
            print("Esta figura no existe")
            exit()
        elif lados == 3:
            mitadl=distancia/2
            h = math.sqrt((distancia*2) + (mitadl*2))
            area= (h*distancia)/2
        elif lados == 4:
            area=distancia*distancia
        elif lados>=5:
            area = (lados * distancia**2) / (4 * math.tan(math.pi / lados))
        return(area)
            


    def perimetro(lados,distancia):
        if lados>2:
            perimetro=lados*distancia
        return (perimetro)

figura.area(lados, distancia)
figura.perimetro(lados, distancia)
area=figura.area(lados, distancia)
perimetro=figura.perimetro(lados, distancia)
print(" ")
print("El area de su figura es: ",area)
print("El perimetro de su figura es: ",perimetro)