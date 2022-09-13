#cracion de un proceso base y vacio, como si fuera una clase
from tokenize import Octnumber


def crearProceso(nombre,tamaño):
    a=dict()
    a["nombre"] = nombre
    a["tamaño"] = tamaño
    a["enUso"] = False
    a["id"] = None
    a["ta"] = None
    a["ti"] = None
    return a
    

#creacion de la memoria, devuelve una lista con las particiones
def crearMemoria():
    #deficinicion de la particion
    particion = {
        "nombre":None,
        "tamaño":None,
        "enUso":False,
        "fragI":0
    }
    #creacion de la lista que va a tener las particiones
    nuev=list()
    #creacion de las particiones y agregacion a la lista
    for i in range(4):
        nuev.append(dict(particion))

    #cargo los datos de cada particion:
    nuev[0]["nombre"]="sistema operativo"
    nuev[0]["tamaño"]=100

    nuev[1]["nombre"]="particion 1"
    nuev[1]["tamaño"]=60

    nuev[2]["nombre"]="particion 2"
    nuev[2]["tamaño"]=120

    nuev[3]["nombre"]="particion 3"
    nuev[3]["tamaño"]=250

    #muestro por pantalla para verificar, sacar o comentar las prox 2 lines
    for i in range(4):
        print(nuev[i])
    
    return nuev













'''----------------------------------------------------------------------------------------------------------'''
''' aqui ya no hay funciones'''


memoria=crearMemoria()  #definimos la memoria

nuevos=list()           #lista de los procesos que recien llegan , todabia no se cumple su TA
listos=list()           #lista de los procesos que ya podrian entrar en memoria, ya se cumplio su TA
suspendidos=list()      #lista de los procesos que estan en espera de libear espacio en memoria
corriendo=None          #proceso que se esta corriendo




