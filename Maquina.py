import pygame
from Menu_class import *

pygame.init()
#Iniciando clock
clock = pygame.time.Clock()

#Iniciando pantalla
pantalla = pygame.display.set_mode((500,300))
pygame.display.set_caption("Advice Machine")

#crear_texto
#E: texto, font, color, tamaño, posicion,posicion de rectangulo de referencia,superficie
#S: Se imprime el texto en la superficie con el font, color, tamaño y posicion
#R: -
def crear_texto(texto, tipo_font, color,tamano,posicion,posicion_rect,superficie):
    font = pygame.font.SysFont(tipo_font,tamano)
    impresion = font.render(texto, True, color)
    impresion_rect = impresion.get_rect()
    if posicion_rect.upper() == "CENTRO":
        impresion_rect.midtop = posicion
    elif posicion_rect.upper() == "DERECHA":
        impresion_rect.topright = posicion
    else:
        impresion_rect.topleft = posicion
    superficie.blit(impresion,impresion_rect)

#Iniciando font de consola
consola_font = "lucidaconsole"

#Advice Machine
running = True

#Iniciando comandos
lista_comandos = [Menu("Sistema",["Reset","Mostrar Ventas"]),
                  Menu("Idioma",["Español","Ingles"]),
                  Menu("Mensaje",["Consejo","Chiste","Dicho"])]

seleccionando = False
comando_actual = 1
estado_actual = 0

def prueba():
    print("Hola")

lista_comandos[comando_actual].get_estado(estado_actual).set_funcionalidad(prueba)

print(lista_comandos[comando_actual].get_estado(estado_actual))

while running:

    pantalla.fill((255,153,51))

    #Creando contenedor
    contenedor = pygame.Surface((480,280))
    contenedor.fill((38,50,56))
    contenedor_rect = contenedor.get_rect()
    contenedor_rect.topleft = (10,10)

    #Creando Espacio Monedas
    espacio_monedas =  pygame.Surface((150,260))
    espacio_monedas.fill((189,189,189))
    espacio_monedas_rect = espacio_monedas.get_rect()
    espacio_monedas_rect.topleft = (10,10)
    pygame.draw.circle(espacio_monedas,(224,224,224),(75,60),50,0)
    pygame.draw.rect(espacio_monedas,(0,0,0),(70,15,10,90))

    #Creando Impresora
    impresora = pygame.Surface((300,170))
    impresora.fill((189,189,189))
    impresora_rect = impresora.get_rect()
    impresora_rect.topleft = (170,100)
    
    #Creando Ranura de impresión
    pygame.draw.rect(impresora,(0,0,0),(20,35,260,25))

    #Creando ranura de vueltos
    pygame.draw.rect(espacio_monedas,(66,66,66),(5,120,140,130))

    #Creando linea de comandos
    comandos = pygame.Surface((280,80))
    comandos.fill((33,150,243))
    comandos_rect = comandos.get_rect()
    comandos_rect.topleft = (170,10)

    #Creando Botones
    boton0 = pygame.Surface((20,30))
    boton0.fill((255,51,0))
    boton0_rect = comandos.get_rect()
    boton0_rect.topleft = (455,15)

    boton1 = pygame.Surface((20,30))
    boton1.fill((0,255,51))
    boton1_rect = comandos.get_rect()
    boton1_rect.topleft = (455,55)

    #Colocando Texto
    crear_texto(lista_comandos[comando_actual].get_nombre(),
                consola_font,
                (255,255,255),
                28,(5,5),
                " ",comandos)
    
    crear_texto(lista_comandos[comando_actual].get_estado(estado_actual).get_nombre(),
                consola_font,
                (255,255,255),
                28,(5,45),
                " ",comandos)

    #Poniendo en pantalla
    contenedor.blit(boton1,boton1_rect)
    contenedor.blit(boton0,boton0_rect)
    contenedor.blit(impresora,impresora_rect)
    contenedor.blit(comandos,comandos_rect)
    contenedor.blit(espacio_monedas,espacio_monedas_rect)
    pantalla.blit(contenedor,contenedor_rect)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if boton1_rect.collidepoint(mouse_pos):
                if seleccionando == False:
                    seleccionando = True
                    estado_tmp = estado_actual
                    estado_actual = 0
                    lista_comandos[comando_actual].transicion1()
                    #print(lista_comandos[comando_actual].get_estado(estado_actual))
                    break
                else:
                    seleccionando = False
                    estado_actual = 0
                    lista_comandos[comando_actual].reset()
                    funcion =  lista_comandos[comando_actual].get_estado(estado_tmp).funcionalidad
                    if funcion != None:
                        funcion()
                    if comando_actual != len(lista_comandos)-1:
                        comando_actual += 1
                    break
            if boton0_rect.collidepoint(mouse_pos):
                if seleccionando == False:
                    if comando_actual > 0:
                        comando_actual -= 1
                    else:
                        comando_actual += 1
                    break
                else:
                    seleccionando = False
                    valor = len(lista_comandos[comando_actual].get_tmp()[1])
                    if estado_tmp == valor-1:
                        estado_actual = 0
                    else:
                        estado_actual = estado_tmp + 1
                    lista_comandos[comando_actual].reset()
                    break
              
    pygame.display.update()
    clock.tick(60)
    
pygame.display.quit()
