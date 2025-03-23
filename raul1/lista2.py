datos = [2, 'dos', 4, 'dos', 6, 'tres', 4, 'uno', 'dos']
print(datos)

print(datos.index('dos'))  # Muestra la posición de la primera ocurrencia de 'dos'
print(datos.count('dos'))  # Cuenta cuántas veces aparece 'dos' en la lista
datos.pop(8)
print(datos)
#datos.reverse()
#print(datos)
indice=datos.index('dos',2,6)
print(indice)
print(f'''{datos.index(4)}-{datos.index(4,datos.index(4)+1,-1)}''')
#datos.sort()
print(datos)
repeticion=datos.count('dos')
print(repeticion)

try:
    datos.sort()
except:
    print("ojo algo esta mal...")
print("continua el codigo")
print(datos)