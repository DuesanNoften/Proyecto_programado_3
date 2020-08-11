

class Estado():
    def __init__(self,nombre):
        self.nombre = nombre
        self.funcionalidad = None

    def get_nombre(self):
        return self.nombre

    def get_funcionalidad(self):
        return self.funcionalidad

    def set_funcionalidad(self,funcion,args):
        self.funcionalidad = funcion
        self.args = args

    def do_funcionalidad(self):
        if self.funcionalidad == None:
            return None
        else:
            if self.args:
                return self.funcionalidad(self.args)
            else:
                return self.funcionalidad()


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

    def buscar_estado(self,nombre):
        for estado in self.estados:
            if nombre == estado.get_nombre():
                return estado

    def set_estado(self,indice,nuevo_estado):
        self.estados[indice] = Estado(nuevo_estado)

    def transicion1(self):
        self.tmp = [self.nombre,self.estados]
        self.nombre = "Cambiar"
        self.estados = [Estado("Seleccionar")]

    def transicion2(self):
        self.tmp = [self.nombre,self.estados]
        self.nombre = "Change"
        self.estados = [Estado("Select")]

    def reset(self):
        self.nombre,self.estados = self.tmp

    def get_tmp(self):
        return self.tmp

