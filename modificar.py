#Práctica 4

class Arreglos:
    def __init__(self, v):  # Se espera que 'v' sea una lista
        self.arregloList = v

    def modificar(self):
        index = int(input("Lugar a cambiar: "))
        if 0 <= index < len(self.arregloList):  # Se corrigió la sintaxis de 'if'
            nuevoValor = int(input("Escribe el nuevo valor: "))
            self.arregloList[index] = nuevoValor
        else:
            print("Fuera de rango")  # Se corrigió 'esle' a 'else'

# Ejemplo de uso:
mi_arreglo = Arreglos([1, 2, 3, 4, 5])
mi_arreglo.modificar()
print(mi_arreglo.arregloList)

