
def abrir_mensajes():
    archivo=open("mensajes.txt","r")
    texto_archivo=archivo.read()
    archivo.close()
    texto_archivo=string_remove(texto_archivo,["-"," "])
    texto_separado=texto_archivo.split("\n")
    for i in range(0,len(texto_separado)):
        if texto_separado[i]:
            texto_separado[i] = string_replace(texto_separado[i],"\t","$").split("$")
    print(texto_separado)
    return texto_separado

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

