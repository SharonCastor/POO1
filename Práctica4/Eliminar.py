#Práctica 4 (Arreglos)

class Lista:
    def __init__(self):
        self.arregloLista = [2, 3, 5]

    def eliminar(self, indice):
        if 0 <= indice < len(self.arregloLista):  # Se corrigió 'inidce' a 'indice'
            self.arregloLista.pop(indice)  # 'pop()' solo recibe el índice
            print(f"El nuevo arreglo es {self.arregloLista}")
        else:
            print("Índice inexistente")

# Crear instancia de la clase
lista = Lista()

# Pedir el índice al usuario y eliminar el elemento
indice = int(input("Ingresa el índice a remover: "))
lista.eliminar(indice)
#Arreglos
class lista:
  def __init__(self):
    self.arregloLista =[2,3,5]

    def eliminar(self, indice,v):
      if 0 <= inidce < len(self.arregloLista):
      self.arregloLista.pop(indice,v)
      print(f"El nuevo arreglo es {self.arregloLista}")

      else:
        print("indice inexistente")
lista =lista()
inidce=int(input("ingrese el indice a remover"))
lista.eliminar(inidce)





