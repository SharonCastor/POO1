#Arreglos

class Lista:
    def __init__(self):
        self.arregloLista = [2,3,5]
    
    def eliminar(self, indice):
        if 0 <= indice < len(self.arregloLista):
            self.arregloLista.pop(indice)
            print("La nueva lista es ", self.arregloLista)
        else:
            print("indice no valido")
    
    def insertar(self):
        elemento = int(input("ingrese el nuevo elemento a insertar: "))
        self.arregloLista.append(elemento)
        print("La nueva lista es ", self.arregloLista)

    def modificar(self):
        indice = int(input("ingrese el indice del elemento a modificar: "))
        if 0 <= indice < len(self.arregloLista):
             nuevo_elemento = input("Ingrese el nuevo valor: ")
             if nuevo_elemento.isdigit():
                self.arregloLista[indice] = int(nuevo_elemento)
                print("La nueva lista es ", self.arregloLista)
             else:
                print("numero invalido")
        else:
            print("indice invalido")

lista = Lista()

indice = int(input("ingrese el indice del elemento a eliminar"))
lista.eliminar(indice)

print("inserta un nuevo elemento a la lista")
lista.insertar()

print("inserta el indice y el nuevo elemento que tomará")
lista.modificar()
