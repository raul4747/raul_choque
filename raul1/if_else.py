num=input('aca va el numero')
num=int(num)
if num < 0:
    print (f'El numero {num} es negativo')
elif num == 0: 
    print (f'El numero {num} es cero')
elif num>=1 and num<=10:
    print (f'El numero {num} es positivo y esta entre 1 a 10')
elif num in range(11,21):  
    print('el numero esta entre 11 y 21')
else:
    print('el numero es mayor a 20')