#Práctica 3
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Atributo privado

    def obtener_edad(self):
        return self.__edad  # Método para acceder a la edad

    def cambiar_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad  # Modificamos la edad de forma segura
        else:
            print("Edad no válida.")

# Crear objeto
persona1 = Persona("Juan", 25)

# Intentamos acceder directamente al atributo (esto dará error)
# print(persona1.__edad)  #  No permitido

# Accedemos a la edad de manera segura
print(persona1.obtener_edad())  #  25

# Cambiamos la edad correctamente
persona1.cambiar_edad(30)
print(persona1.obtener_edad())  #  30