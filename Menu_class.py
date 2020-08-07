

class Estado():
    def __init__(self,nombre):
        self.nombre = nombre
        self.funcionalidad = None

    def get_nombre(self):
        return self.nombre

    def set_funcionalidad(self,funcion):
        self.funcionalidad = funcion


class Menu():
    def __init__(self,nombre,estados):
        self.nombre = nombre
        self.estados = []
        for estado in estados:
            self.estados.append(Estado(estado))

    def get_nombre(self):
        return self.nombre

    def get_estado(self,indice):
        return self.estados[indice]

    def set_estado(self,indice,nuevo_estado):
        self.estado[indice] = nuevo_estado

    def transicion1(self):
        self.tmp = [self.nombre,self.estados]
        self.nombre = "Cambiar"
        self.estados = [Estado("Seleccionar")]

    def reset(self):
        self.nombre,self.estados = self.tmp

    def get_tmp(self):
        return self.tmp

