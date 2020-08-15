#abrir_mensajes(): abre el archivo mensajes y hace la division de los datos
def abrir_mensajes():
    archivo=open("mensajes.txt","r")
    texto_archivo=archivo.read()
    archivo.close() 
    texto_archivo=string_remove(texto_archivo,["-"," "])
    texto_separado=texto_archivo.split("\n")
    for i in range(0,len(texto_separado)):
        if texto_separado[i]:
            texto_separado[i] = string_replace(texto_separado[i],"\t","$").split("$")
    return texto_separado

# string_remove(string,elementos)
#E: un string y los elementos que quieren ser eliminados de esta (lista)
#S: el string sin los elementos eliminados
#R: -
def string_remove(string,elementos):
    len_str = len(string)
    nuevo_str=''
    i=0
    while i != len_str:
        valor=True
        for elemento in elementos:
            if string[i] == elemento:
                valor=False
        if valor:
            nuevo_str+=string[i]
        else:
            pass
        i+=1
        
    return nuevo_str

#string_replace(string,remplazado,remplazador)
#E: un string, un elemento que se sea remplazar, y el elemento por el cual se va a reemplazar
#S: el string con el elemento remplazadoren vez del elemento a remplazar(si se repite varias veces se reemplaza una vez)
#R: -
def string_replace(string,remplazado,remplazador):
    len_str = len(string)
    nuevo_str=''
    if string[0] == remplazado:
        nuevo_str+=remplazador
    else:
        nuevo_str+=string[0]
    i=1
    elemento_anterior=string[0]
    while i != len_str:
        if elemento_anterior == remplazado and string[i] == elemento_anterior:
            i+=1
            continue
        else:
            if string[i] == remplazado:
                nuevo_str+=remplazador
            else:
                nuevo_str+=string[i]
        elemento_anterior=string[i]
        i+=1
    return nuevo_str

#abrir_ventas(): abre el archivo ventas y hace la division de los datos
def abrir_ventas():
    archivo=open("ventas.txt","r")
    texto_archivo=archivo.read()
    archivo.close()
    texto_archivo = texto_archivo.split('\n')
    return texto_archivo

#reiniciar_ventas(): abre el archivo ventas y borra la ventas realizadas
def reiniciar_ventas():
    archivo=open("ventas.txt","r")
    texto_archivo=archivo.read()
    archivo.close()
    texto_archivo = texto_archivo.split('\n')
    nuevo_texto = []
    espacio = True
    for texto in texto_archivo:
        if texto:
            if texto[0].isnumeric() and espacio:
                nuevo_texto.append('')
                espacio = False
                continue
            elif texto[0].isnumeric():
                continue
            else:
                nuevo_texto.append(texto)
    print(nuevo_texto)
    largo = len(nuevo_texto)
    archivo = open("ventas.txt","w")
    for i in range(0,largo):
        if i != largo-1:
            archivo.write(nuevo_texto[i]+'\n')
        else:
            archivo.write(nuevo_texto[i])
    archivo.close()

    texto_mensajes = abrir_mensajes()
    archivo = open("mensajes.txt",'r+')
    texto_archivo=archivo.read()
    texto_archivo = texto_archivo.split('\n')
    print(texto_mensajes)
    for i in range(3,len(texto_archivo)-1):
        print(texto_mensajes[i])
        mensaje = texto_mensajes[i]
        nuevo_str  = (mensaje[0]
                      +'\t'
                      +mensaje[1]
                      +'\t'
                      +mensaje[2]
                      +'\t\t\t\t\t'
                      +mensaje[3]
                      +'\t'
                      +'0'
                      +'\t'
                      +mensaje[5])
        texto_archivo[i] = nuevo_str
    print(texto_archivo)
    archivo.seek(0,0)
    largo = len(texto_archivo)
    for i in range(0,largo):
        if i != largo-1:
            archivo.write(texto_archivo[i]+'\n')
        else:
            archivo.write(texto_archivo[i])
    archivo.close()

def actualizar_ventas(tipo,codigo):
    texto = abrir_mensajes()
    for i in range(0,len(texto)):
        if texto[i]:
            if texto[i][0]==tipo and texto[i][1]==codigo:
                indice = i
    archivo = open("mensajes.txt",'r+')
    texto_archivo=archivo.read()
    texto_archivo = texto_archivo.split('\n')
    mensaje = texto[indice]
    nuevas_ventas = str(int(mensaje[4])+1)
    nuevo_str  = (mensaje[0]
                  +'\t'
                  +mensaje[1]
                  +'\t'
                  +mensaje[2]
                  +'\t\t\t\t\t'
                  +mensaje[3]
                  +'\t'
                  +f'{nuevas_ventas}'
                  +'\t'
                  +mensaje[5])
    texto_archivo[indice] = nuevo_str
    print(mensaje,texto_archivo[indice],texto_archivo)
    archivo.seek(0,0)
    largo = len(texto_archivo)
    for i in range(0,largo):
        if i != largo-1:
            archivo.write(texto_archivo[i]+'\n')
        else:
            archivo.write(texto_archivo[i])
    archivo.close()


    
    
    
