lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num=input('ingresa el numero')
num=int(num)
for i in range (0, len(lista)):
    resultado = num*lista[i]#print(f'indice: {i}, valor:{lista[i]}')
    #print(resultado)
    print(lista[i],"x",num,"=",resultado)