from enum import Enum
class Consecutivo(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3

print(Consecutivo.Lunes)
print(Consecutivo.Lunes.value)

print(type(Consecutivo.Lunes))
print(type(Consecutivo.Lunes.value))