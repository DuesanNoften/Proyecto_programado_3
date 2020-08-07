
class Menu():
    def __init__(self,nombre,estados):
        self.nombre = nombre
        self.estados = estados

    def get_nombre(self):
        return self.nombre

    def mostrar_estados(self):
        for estado in self.estados:
            print(estado)

    def get_estado(self,indice):
        return self.estados[indice]

    def set_estado(self,indice,nuevo_estado):
        self.estado[indice] = nuevo_estado

    def transicion1(self):
        self.tmp = [self.nombre,self.estados]
        self.nombre = "Cambiar"
        self.estados = ["Seleccionar"]

    def reset(self):
        self.nombre,self.estados = self.tmp
