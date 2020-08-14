import pygame
"""
Clase dinero
Self.image=Es la imagen principal de la clase
self.lado= Es la imagen de el costado angosto de la moneda utilizado para cuando se inserta
self.valor= Es el valor con el que se reconoce la moneda en el programa
self.rect= Es el hitbox de self.image
self.rect= Es el hitbox de self.lado
self.posx=Es la posicion en x donde se genera la moneda
self.posy=Es la posicion en y donde se genera la moneda
"""
pygame.init()


class Dinero:
    def __init__ (self):
        self.valor=20
        self.image=pygame.image.load('moneda/moneda.png')
        self.rect=self.image.get_rect()
        self.lado=pygame.image.load('moneda/lado.png')
        self.rectl=self.lado.get_rect()
        self.posx=550
        self.posy=250
moneda=Dinero()
