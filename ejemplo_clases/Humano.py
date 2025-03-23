class Persona():
    edad=0
    estatura=0
    genero=''
    
    #constructor
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print(f' hola soy {self.nombre}')
        print('te comento que')
        print(f' tengo {self.edad}')
        print(f' tengo {self.estatura}')
        print(f' tengo el genero {self.genero}')
    def completar(self,edad, estatura, genero):
        self.edad = edad
        self.estatura = estatura
        self.genero = genero
