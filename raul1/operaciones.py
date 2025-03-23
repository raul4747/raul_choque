#definiciones
#def sumar_gabriel(numero1, numero2):
#    resultado=numero1+numero2
#    return resultado

#res_suma=sumar_gabriel(5,3)
#print(res_suma)

#otros
def sumar_gabriel(a,b,c):
    suma=a+b+c
    mult=a*b*c
    return suma, mult

suma, mult=sumar_gabriel(5,3,2)
print(suma, mult)

