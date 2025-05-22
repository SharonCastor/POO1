#Colecciones, tuplas, diccionario
#Sharon Alessandra Castor Vaquera
#27-marzo-2025


import numpy as np

valores_mixtos=[12, "Hola", 8.36, True, 12]
valores_iguales=np.array ([2, 5, 17, 2, 9])

tupla_mixtos = tuple(valores_mixtos)
tupla_iguales=tuple(valores_iguales)

conjunto_mixtos= tuple(valores_mixtos)
conjunto_iguales= tuple(valores_iguales)

diccionario= {
    "nombre":"Sharon",
    "edad": 18,
    "estatura": 1.58,
    "estudiante": True,
    "materias": ["POO1","Álgebra","Cálculo","IR"]}

print("Lista mixta:", valores_mixtos)
print("Lista enteros:", valores_iguales)
print("Tupla mixta:", tupla_mixtos)
print("Tupla enteros:", tupla_iguales)
print("Conjunto mixto:", conjunto_mixtos)
print("Conjunto enteros:", conjunto_iguales)
print("Diccionario:", diccionario)
