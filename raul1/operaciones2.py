#define una funcion para que opere de acuerdo a una condicion
def operaciones(a,b,ope):
    resultado=0
    if ope=="suma":
        resultado=a+b
    elif ope=="resta":
        resultado=a-b
    elif ope=="multiplicar":
        resultado=a*b
    else:
        print("operador no valido")
    return resultado
resultado=operaciones(5,3,"suma")
print("suma", resultado)
resultado=operaciones(5,3,"resta")
print("resta", resultado)
resultado=operaciones(5,3,"multiplicar")
print("multiplicacion", resultado)