import pygame
"""
Clase dinero
Se maneja en una ventana aparte y posee
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
