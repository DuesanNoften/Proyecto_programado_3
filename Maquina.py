import pygame
from Menu_class import *
from funcionalidad import *
from Dinero_class import *
import datetime
import random
import time
import threading
pygame.init()

#Iniciando clock
clock = pygame.time.Clock()

#Creando la variable saldo, para su uso
global saldo
saldo=0

#Creando la variable global posvx y posvy
global posvx, posvy
posvx=50
posvy=600


#Iniciando pantalla
pantalla = pygame.display.set_mode((700,300))
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
papel_font = "garamond"
    
#Advice Machine
running = True

#Iniciando Idioma 
idioma = 'esp'

#Cargando mensajes
mensajes = abrir_mensajes()
chistes = []
dichos = []
consejos = []
jokes = []
sayings = []
advices = []
for mensaje in mensajes:
    if mensaje:
        tipo = mensaje[0]
        if tipo == "1":
            chistes.append(mensaje)
        elif tipo == "2":
            dichos.append(mensaje)
        elif tipo == "3":
            consejos.append(mensaje)
        elif tipo == "4":
            jokes.append(mensaje)
        elif tipo == "5":
            sayings.append(mensaje)
        elif tipo == "6":
            advices.append(mensaje)
        else:
            pass


#Iniciando comandos
lista_comandos = [Menu("Administracion",["Ctrñ:","Resetear","Reporte","Apagar"]),
                  Menu("Idioma",["Español","English"]),
                  Menu("Mensaje",["Consejo","Chiste","Dicho"])]

seleccionando = False
comando_actual = 1
estado_actual = 0
monto = 20

#Funcionalidades
#apagar():para el ciclo
def apagar():
    global running
    running= False
#traducir_ingles(): cambia a lenguaje de los comandos a ingles
def traducir_ingles():
    global lista_comandos
    global idioma
    idioma = 'ing'
    lista_comandos = [Menu("Administration",["Pswd:","Reset","Report","Shut Down"]),
                      Menu("Language",["Español","English"]),
                      Menu("Message",["Advice","Joke","Saying"])]
    lista_comandos[0].buscar_estado("Shut Down").set_funcionalidad(apagar,[])
    lista_comandos[0].buscar_estado("Reset").set_funcionalidad(reiniciar_ventas,[])
    lista_comandos[1].buscar_estado("Español").set_funcionalidad(traducir_espanol,[])
    lista_comandos[1].buscar_estado("English").set_funcionalidad(traducir_ingles,[])
    lista_comandos[0].buscar_estado("Pswd:").set_funcionalidad(contrasena,[])
    lista_comandos[2].buscar_estado("Joke").set_funcionalidad(imprimir,[jokes,'1'])
    lista_comandos[2].buscar_estado("Advice").set_funcionalidad(imprimir,[advices,''])
    lista_comandos[2].buscar_estado("Saying").set_funcionalidad(imprimir,[sayings,''])
#traducir_espanol(): cambia a lenguaje de los comandos a espanol
def traducir_espanol():
    global lista_comandos
    global idioma
    idioma = 'esp'
    lista_comandos = [Menu("Administracion",["Ctrñ:","Resetear","Reporte","Apagar"]),
                  Menu("Idioma",["Español","English"]),
                  Menu("Mensaje",["Consejo","Chiste","Dicho"])]
    lista_comandos[0].buscar_estado("Apagar").set_funcionalidad(apagar,[])
    lista_comandos[0].buscar_estado("Resetear").set_funcionalidad(reiniciar_ventas,[])
    lista_comandos[1].buscar_estado("Español").set_funcionalidad(traducir_espanol,[])
    lista_comandos[1].buscar_estado("English").set_funcionalidad(traducir_ingles,[])
    lista_comandos[0].buscar_estado("Ctrñ:").set_funcionalidad(contrasena,[])
    lista_comandos[2].buscar_estado("Chiste").set_funcionalidad(imprimir,[chistes,'esp'])
    lista_comandos[2].buscar_estado("Dicho").set_funcionalidad(imprimir,[dichos,'esp'])
    lista_comandos[2].buscar_estado("Consejo").set_funcionalidad(imprimir,[consejos,'esp'])
    
#contrasena():
#E: lista de rectangulos
#S: Recibe contraseña por medio de colisiones con los rectangulos con el mouse y retorna un bool
#R: -
def contrasena(args):#argumentos:recs,menu,estado
    recs,menu,estado = args
    tmp = menu.get_estado(estado).get_nombre()
    ctrn_surface = pygame.Surface((275,75))
    ctrn_surface.fill((33,150,243))
    ctrn_rect = ctrn_surface.get_rect()
    ctrn_rect.topleft=(5,5)
    ctrn = ''
    correcta = False
    menu.set_estado(estado,menu.get_estado(estado).get_nombre()+ctrn)
    while len(ctrn) <= 5 and correcta == False:
        crear_texto(menu.get_estado(estado).get_nombre(),consola_font,(255,255,255),28,(1,1)," ",ctrn_surface)
        comandos.blit(ctrn_surface,ctrn_rect)
        contenedor.blit(comandos,comandos_rect)
        pantalla.blit(contenedor,contenedor_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if recs[0].collidepoint(mouse_pos):
                    ctrn += '1'
                    menu.set_estado(estado,tmp+ctrn)
                    break
                if recs[1].collidepoint(mouse_pos):
                    ctrn += '0'
                    menu.set_estado(estado,tmp+ctrn)
                    break
                
        if ctrn == '10110':
            correcta = True
            
        pygame.display.update()
        clock.tick(60)
 
    menu.set_estado(estado,tmp)
    ctrn_surface.fill((33,150,243))
    comandos.blit(ctrn_surface,ctrn_rect)
    return correcta

#imprimir(tipo)
#E: lista de los mensajes que se pueden imprimir
#S: Se escoge el mensaje con el precio mas cercano al monto actual y se imprime en la superficie
#R: -
def imprimir(args):#argumentos: tipo
    global saldo
    global monto
    global posvx,posvy
    tipo,idioma = args
    run=True
    if saldo > 0:
        #Consiguiendo el mensaje mas cercano
        precios = []
        for ele in tipo:
            if ele[3].isnumeric():
                if int(ele[3]) <= saldo:
                    precios.append(int(ele[3]))
        print(precios)
        if len(precios) != 1:
            global precio
            precio = comparar_precios(saldo,precios)
        else:
            precio = precios[0]-saldo
        print(saldo,precios,precio,precio+saldo)    
        while True:
            indice = random.choice(range(0,len(precios)))
            if precios[indice] == (-precio)+saldo:
                break
        mensaje = tipo[indice]
        print(mensaje)
        if saldo>=precio:
            pygame.mixer.music.load('moneda/sonido/monedas_1.mp3')
            saldo=precio
            if saldo>0:
                pygame.mixer.music.play()
                posvx=50
                posvy=255
            #Animacion imprimir
            marco = pygame.Surface((260,100))
            marco.fill((255,255,255))
            marco.set_colorkey((255,255,255))
            marco_rect = marco.get_rect()
            marco_rect.topleft = (20,45)
            papel = pygame.Surface((260,100))
            papel.fill((241,238,228))
            papel_rect = papel.get_rect()
            papel_y = -marco.get_height()
            papel_yreal = papel_y
            papel_rect.topleft = (0,papel_y)
            if idioma == 'esp':
                crear_texto("Click aqui",
                            papel_font,
                            (0,0,0),30,
                            (papel_rect.width//2,papel_rect.height//2),
                            'centro',papel)
            else:
                crear_texto("Click here",
                            papel_font,
                            (0,0,0),30,
                            (papel_rect.width//2,papel_rect.height//2),
                            'centro',papel)

            impresora = pygame.Surface((300,170))
            impresora.fill((189,189,189))
            pygame.draw.rect(impresora,(0,0,0),(20,35,260,25))
            superficie_rect = impresora.get_rect()
            superficie_rect.topleft = (180,110)

            running = True
            pygame.mixer.music.load('moneda/sonido/printer.mp3')
            pygame.mixer.music.play()
            while running:
                marco.fill((255,255,255))
                marco.set_colorkey((255,255,255))
                marco.blit(papel,papel_rect)
                impresora.blit(marco,marco_rect)
                pantalla.blit(impresora,superficie_rect)

                if papel_yreal < 0:
                    papel_yreal += 2
                    papel_y = int(papel_yreal)
                    papel_rect.topleft = (0,papel_y)
                else:
                    pass 

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = list(pygame.mouse.get_pos())
                        mouse_pos[0] -= 180
                        mouse_pos[1] -= 110
                        if marco_rect.collidepoint(mouse_pos):
                            running = False
                        
                pygame.display.update()
                clock.tick(60)
            #Imprimiendo mensaje
            marco = pygame.Surface((460,260))
            marco.fill((241,238,228))
            marco_rect = marco.get_rect()
            marco_rect.topleft = (20,20)
            papel = pygame.image.load(mensaje[5])
            papel = pygame.transform.scale(papel,(400,200))
            papel_rect = papel.get_rect()
            papel_rect.midtop = (marco_rect.midtop[0]-20,30)
            boton_salida = pygame.image.load('boton_salida.png').convert()
            boton_salida.set_colorkey((255,255,255))
            botons_rect = boton_salida.get_rect()
            botons_rect.topleft = (marco_rect.width -(botons_rect.width+10),5)

            running = True

            while running:
                marco.blit(boton_salida,botons_rect)
                marco.blit(papel,papel_rect)
                pantalla.blit(marco,marco_rect)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = list(pygame.mouse.get_pos())
                        mouse_pos[0] -= botons_rect.topleft[0]
                        mouse_pos[1] -= botons_rect.topleft[1]
                        if marco_rect.collidepoint(mouse_pos):
                            running = False

                pygame.display.update()
            print(saldo)
            #Guardando venta en tabla de ventas
            d=datetime.datetime.today()
            d=str(d)[:16]
            dt=d.split()
            t=dt[1]
            d=dt[0]
            texto_ventas = abrir_ventas()
            if not texto_ventas[4]:
                transaccion = 1
            else:
                transaccion = len(texto_ventas)-4
            string_venta = ''
            string_venta += (f'{transaccion}'
                             +'\t'
                             +'  '
                             +d
                             +'\t'
                             +t
                             +'\t'
                             +mensaje[0]
                             +'\t'
                             +mensaje[1]
                             +'\t'
                             +'\t'
                             +mensaje[3]
                             +'\t'
                             +str(int(mensaje[3])+saldo)
                             +'\t'
                             +'\t'
                             +str(saldo))
            no_espacio = True
            for i in range(0,len(texto_ventas)):
                if not texto_ventas[i]:
                    texto_ventas[i] = string_venta
                    no_espacio = False
                    break
            if no_espacio:
                tmp = texto_ventas[-1]
                texto_ventas[-1] = string_venta
                texto_ventas.append(tmp)
                
            archivo_venta = open("ventas.txt","w")
            largo = len(texto_ventas)
            for i in range(0,largo):
                if i != largo-1:
                    archivo_venta.write(texto_ventas[i]+'\n')
                else:
                    archivo_venta.write(texto_ventas[i])
            archivo_venta.close()
            print(run)
            print (saldo)
            saldo=0
    else:
        pass
    
#comparar_precio(monto,lista)
#E: un monti y la lista de mensajes
#S: la menor diferencia entre el precio de los mensajes y el monto
#R: -
def comparar_precios(monto,lista):
    #Hacer una pila de comparaciones
    if lista[1:] == []:
        return lista[0]
    else:
        return comparar_menor(abs(lista[0]-monto),comparar_precios(monto,lista[1:]))
#comparar_menor(): compara dos numeros y retorna el menor
def comparar_menor(x,y):
    if x > y:
        return y
    else:
        return x
    
#imprimir_reporte(args)
#E: idioma
#S: Imprime un reporte de las ventas
#R: -
def imprimir_reporte(args): #args():idioma
    #Animacion imprimir
    print('Wii')
    idioma = 'esp'
    marco = pygame.Surface((260,100))
    marco.fill((255,255,255))
    marco.set_colorkey((255,255,255))
    marco_rect = marco.get_rect()
    marco_rect.topleft = (20,45)
    papel = pygame.Surface((260,100))
    papel.fill((241,238,228))
    papel_rect = papel.get_rect()
    papel_y = -marco.get_height()
    papel_yreal = papel_y
    papel_rect.topleft = (0,papel_y)
    if idioma == 'esp':
        crear_texto("Click aqui",
        papel_font,
        (0,0,0),30,
        (papel_rect.width//2,papel_rect.height//2),
        'centro',papel)
    else:
        crear_texto("Click here",
        papel_font,
        (0,0,0),30,
        (papel_rect.width//2,papel_rect.height//2),
        'centro',papel)
    impresora = pygame.Surface((300,170))
    impresora.fill((189,189,189))
    pygame.draw.rect(impresora,(0,0,0),(20,35,260,25))
    superficie_rect = impresora.get_rect()
    superficie_rect.topleft = (180,110)

    running = True
    while running:
        marco.fill((255,255,255))
        marco.set_colorkey((255,255,255))
        marco.blit(papel,papel_rect)
        impresora.blit(marco,marco_rect)
        pantalla.blit(impresora,superficie_rect)

        if papel_yreal < 0:
            papel_yreal += 2
            papel_y = int(papel_yreal)
            papel_rect.topleft = (0,papel_y)
        else:
            pass 

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = list(pygame.mouse.get_pos())
                    mouse_pos[0] -= 180
                    mouse_pos[1] -= 110
                    if marco_rect.collidepoint(mouse_pos):
                        running = False
                        
        pygame.display.update()
        clock.tick(60)

    #Imprimiendo mensaje
    fondo = pygame.Surface((460,260))
    fondo.fill((241,238,228))
    fondo_rect = fondo.get_rect()
    fondo_rect.topleft = (20,20)

    marco = pygame.Surface((400,200))
    marco_rect = marco.get_rect()
    marco.fill((255,255,255))
    marco.set_colorkey((255,255,255))
    marco_rect.midtop = (marco_rect.midtop[0]+30,30)

    texto_imprimido = pygame.Surface((400,200))
    texto_imprimido.fill((255,255,255))
    texto_imprimido.set_colorkey((255,255,255))
    texto_rect = texto_imprimido.get_rect()
    texto_rect.topleft = (0,0)

    texto_archivo = abrir_mensajes()
    mensajes_vendidos = []
    for mensaje in texto_archivo:
        if mensaje:
            if mensaje[4] != '0' and mensaje[4].isnumeric():
                mensajes_vendidos.append(mensaje)

    texto_imprimir = [['Tipo','Codigo','Mensaje        ','Vendidos','Monto ventas']]
    for mensaje in mensajes_vendidos:
        texto_imprimir.append([mensaje[0],
                               mensaje[1],
                               mensaje[2],
                               mensaje[4],
                               str(int(mensaje[4])*int(mensaje[3]))])

    pos_y = 0
    for texto in texto_imprimir:
        if texto[0].isnumeric():
            string = ''
            for i in range(0,len(texto_imprimir[0])):
                diferencia = len(texto_imprimir[0][i])-len(texto[i])
                string+=texto[i]
                for j in range(0,diferencia+1):
                    string+=' '
                string+='     '
        else:
            string = (texto[0]
                      +'\t'
                      +texto[1]
                      +'\t'
                      +texto[2]
                      +'\t'
                      +texto[3]
                      +'\t'
                      +texto[4])
        crear_texto(string,papel_font,(0,0,0),15,(5,pos_y),'',texto_imprimido)
        pos_y += 15

    running = True

    while running:
        marco.blit(texto_imprimido,texto_rect)
        fondo.blit(marco,marco_rect)
        pantalla.blit(fondo,fondo_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            
        pygame.display.update()
        
#Asignando funcionalidades
lista_comandos[0].buscar_estado("Ctrñ:").set_funcionalidad(contrasena,[])
lista_comandos[0].buscar_estado("Apagar").set_funcionalidad(apagar,[])
lista_comandos[0].buscar_estado("Resetear").set_funcionalidad(reiniciar_ventas,[])
lista_comandos[1].buscar_estado("Español").set_funcionalidad(traducir_espanol,[])
lista_comandos[1].buscar_estado("English").set_funcionalidad(traducir_ingles,[])

#Maquina de Consejos
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
    hendija=pygame.Surface((100,90))
    hendija.fill((255,255,255))
    hendija.set_colorkey((255,255,255))
    hendija_rect=hendija.get_rect()
    hendija_rect.centerx= 70
    hendija_rect.centery= 80
    pygame.draw.circle(espacio_monedas,(224,224,224),(75,60),50,0)
    pygame.draw.rect(espacio_monedas,(0,0,0),(70,15,10,90))
    
    #Creando Impresora
    impresora = pygame.Surface((300,170))
    impresora.fill((189,189,189))
    impresora_rect = impresora.get_rect()
    impresora_rect.topleft = (170,100)

    #ubicando hitbox monedas
    moneda.vuelto_rect.centerx=100
    moneda.vuelto_rect.centery=260

    #Creando bandeja con dinero
    bandejas=pygame.Surface((300,290))
    bandejas.fill((87,87,88))
    bandejas_rect=bandejas.get_rect()
    bandejas_rect.topleft=(500,5)
    bandeja=pygame.Surface((180,270))
    bandeja.fill((50,59,86))
    bandeja_rect=bandeja.get_rect()
    bandeja_rect.topleft=(510,15)
    
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
    if saldo<=monto:
        crear_texto('Dinero:'+str(saldo)+'/'+str(monto),consola_font,
                    (255,255,255),10,(210,65),
                    " ",comandos)
    elif saldo<=monto+40:
        crear_texto('Dinero:'+str(saldo)+'/'+str(monto+40),consola_font,
                    (255,255,255),10,(210,65),
                    " ",comandos)
    else:
        crear_texto('Dinero:'+str(saldo)+'/'+str(monto+60),consola_font,
                    (255,255,255),10,(210,65),
                    " ",comandos)
    #Poniendo en pantalla
    contenedor.blit(boton1,boton1_rect)
    contenedor.blit(boton0,boton0_rect)
    contenedor.blit(impresora,impresora_rect)
    contenedor.blit(comandos,comandos_rect)
    contenedor.blit(espacio_monedas,espacio_monedas_rect)
    contenedor.blit(hendija,(80,25))
    bandeja.blit(moneda.image,(10,180))
    bandeja.blit(moneda.image,(40,150))
    bandeja.blit(moneda.image,(0,180))
    bandeja.blit(moneda.image,(90,180))
    bandeja.blit(moneda.image,(50,180))
    bandeja.blit(moneda.image,(70,150))
    bandeja.blit(moneda.image,(50,150))
    pantalla.blit(contenedor,contenedor_rect)
    pantalla.blit(moneda.lado,(moneda.posx,moneda.posy))
    pantalla.blit(bandejas,bandejas_rect)
    pantalla.blit(bandeja,bandeja_rect)
    
    pantalla.blit(moneda.vuelto,(posvx, posvy))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if hendija_rect.collidepoint(mouse_pos):
                if saldo<80:
                    pygame.mixer.music.load('moneda/sonido/MONEYWIN.wav')
                    pygame.mixer.music.play()
                    moneda.posx,moneda.posy=87,35
                    saldo += moneda.valor
                    print(saldo)
            if moneda.vuelto_rect.collidepoint(mouse_pos):
                posvx=50
                posvy=600
                
            if boton1_rect.collidepoint(mouse_pos):
                if seleccionando == False:
                    seleccionando = True
                    estado_tmp = estado_actual
                    estado_actual = 0
                    if idioma == 'esp':

                        lista_comandos[comando_actual].transicion1()

                    else:
                        lista_comandos[comando_actual].transicion2()
                    break
                else:
                    seleccionando = False
                    estado_actual = 0
                    lista_comandos[comando_actual].reset()
                    nombre_estado = lista_comandos[comando_actual].get_estado(estado_tmp).get_nombre()
                    if nombre_estado == "Ctrñ:" or nombre_estado == "Pswd:":
                        lista_comandos[0].buscar_estado(nombre_estado).set_funcionalidad(contrasena,[[boton1_rect,boton0_rect],
                                                                       lista_comandos[comando_actual],
                                                                       estado_tmp])
                        valor = lista_comandos[comando_actual].get_estado(estado_tmp).do_funcionalidad()
                        if valor:
                            estado_actual += 1
                            break
                    elif lista_comandos[comando_actual].get_estado(estado_tmp).get_funcionalidad() != None:
                       lista_comandos[comando_actual].get_estado(estado_tmp).do_funcionalidad()
                    if comando_actual != len(lista_comandos)-1:
                           comando_actual += 1
                    break
            if boton0_rect.collidepoint(mouse_pos):
                if seleccionando == False:
                    if comando_actual > 0:
                        comando_actual -= 1
                    else:
                        comando_actual += 1
                    estado_actual = 0
                    break
                else:
                    seleccionando = False
                    valor = len(lista_comandos[comando_actual].get_tmp()[1])
                    lista_comandos[comando_actual].reset()
                    nombre_estado = lista_comandos[comando_actual].get_estado(estado_tmp).get_nombre()
                    if nombre_estado == "Ctrñ:" or nombre_estado == "Pswd:":
                        pass
                    else:
                        if estado_tmp == valor-1:
                            estado_actual = 0
                        else:
                            estado_actual = estado_tmp + 1
                    break
        if event.type == pygame.MOUSEBUTTONUP:
            if saldo<=80:
                time.sleep(1.001)
                moneda.posx,moneda.posy=87,600
    pygame.display.update()
    clock.tick(60)
    
pygame.display.quit()
