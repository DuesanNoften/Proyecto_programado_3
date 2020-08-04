import pygame 

pygame.init()

#Iniciando pantalla
pantalla = pygame.display.set_mode((500,300))
pygame.display.set_caption("Advice Machine")

#Advice Machine
running = True

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
    
    #Creando linea de comandos
    impresora = pygame.Surface((300,170))
    impresora.fill((189,189,189))
    impresora_rect = impresora.get_rect()
    impresora_rect.topleft = (170,100)

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
            
    pygame.display.update()
    
pygame.display.quit()
