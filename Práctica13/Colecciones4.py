#Colecciones, diccionarios
#Sharon Alesandra Castor Vaquera
#01-abril-2025


Dic={"x":"equis","y": "ye","D":"De"}
Dic2=dict(x = "equis", y = "ye", D = "De")
print(Dic['x'])
print(Dic.get('x'))
print(Dic.get('z'))#None

#Modificar valor existente
Dic['x'] = "equisD"
Dic['z'] ="Zeta"

del Dic['y']
x = Dic.pop('y')
print(x)#"ye"

print ('x'in Dic)#true

llaves = Dic.keys()
print(llaves) #['x','y','D']
valores = Dic.values()
p = Dic.items()
