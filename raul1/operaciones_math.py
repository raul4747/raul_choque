def sumar(a,b,c): #funcion
    suma=a+b+c
    return suma

def operaciones(a,b,ope):#funcion
    if ope=="sumar":
        resultado=a+b
    elif ope=="resta":
        resultado=a-b
    elif ope=="multiplicar":
        resultado=a*b
    else:
        print("operador no valido")
    return resultado
def potencia_2(numero): #metodo
    resultado=numero**2
    print(f'la potencia de {numero} es {resultado}')