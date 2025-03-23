#Escribir un programa que identifique si un números es perfecto: Nota.- Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos (excluyendo al propio número) ejemplo: para el número 6: generar sus divisores enteros
x=int(input("numero:..."))
suma = 0
suma=sum(i for i in range(1,x) if x%i==0)

print("espefecto" if suma == x else "no es perfecto")