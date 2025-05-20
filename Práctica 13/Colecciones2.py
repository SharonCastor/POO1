#Colecciones, add, remove, discard
#Sharon Alessandra Castor Vaquera
#01-abril-2025

conj = {12, 2, 17, 35, 8}
print("Conjunto inical: ",conj)

conj.add(5)
print("Conjunto despues de agregar 5: ", conj)

conj.remove(12)
print("Conjunto después de eliminar 12: ", conj)

conj.discard(1)
print("Conjunto después de intenta eliminar 1: ",conj)

print("¿Existe el valor 1 en mi conjunto? ", 1 in conj)

conj.add(2)
print("Conjunto después de intentar agregar 2 de nuevo: ",conj)