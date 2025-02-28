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




