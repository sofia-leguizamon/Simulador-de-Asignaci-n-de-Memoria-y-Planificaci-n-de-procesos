
#cracion de un proceso base y vacio, como si fuera una clase
#por cada proceso se debe ingresaro leer desde un archivo el Id de proceso, tamaño del proceso, tiempo de arribo y tiempo de irrupción.
def crearProceso(id,tamaño):
    a=dict()
    a["id"] = id
    a["tamaño"] = tamaño
    a["enUso"] = False
    a["ta"] = None
    a["ti"] = None
    return a

#Crea unos procesos de prueva y los pone en una lista
def listaDeProcesosNuevosPorDefault():
    ln=list()
    ln.append(crearProceso(1,40))
    ln.append(crearProceso(2,140))
    ln.append(crearProceso(3,200))
    ln.append(crearProceso(4,93))
    ln.append(crearProceso(5,42))
    #muestra los procesos creados
    for i in range(len(ln)):
        print(ln[i])
    return ln

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
    '''for i in range(4):
        print(nuev[i])'''
    
    return nuev

def ponerProcesoEnMemoria(memoria,proceso):
    return 0

def sacarProcesoDeMemoria(memoria,proceso):
    return 0



'''----------------------------------------------------------------------------------------------------------'''
''' aqui ya no hay funciones'''


memoria=crearMemoria()  #definimos la memoria

nuevos=list()           #lista de los procesos que recien llegan , todabia no se cumple su TA
listos=list()           #lista de los procesos que ya podrian entrar en memoria, ya se cumplio su TA
suspendidos=list()      #lista de los procesos que estan en espera de libear espacio en memoria
corriendo=None          #proceso que se esta corriendo

nuevos=listaDeProcesosNuevosPorDefault()




'''
------------------------------------------------------------------------------------------------------
---------para implementar futuras funciones---------
------------------------------------------------------------------------------------------------------
-una funcion que implemente el worst-fit para la memoria y el proceso
-un algoritmo que realice la planificacion SJF

-menu de opciones de ingrso de procesos, si quiere por un archivo o manual o default

-cargar proceso manualmente
-cargar procesos por un archivo externo

-------procesos-------
-mostrar la tabla de los procesos cargados(los que estarian en la lista de nuevos)
-mostrar el proceso que esta corriendo
-El estado de la cola de procesos listos.
-Listado de procesos que no se encuentran en estado de listo ni ejecución (informar el estado en que se
encuentran)


-------memoria-------
-mostrar La tabla de particiones de memoria, la cual deberá contener 
    (Id de partición, dirección de comienzo de partición, 
    tamaño de la partición, id de proceso asignado a la partición, 
    fragmentación interna)




fijarse una vez que se pueda:
-¿como implementar lo de multiprogramacion 5?
-¿como dar la posibilidad de ingresar un proceso, cuando ocurra un cambio en la memoria,
    creo que tambien deberiamos dar la opcion de no ingresar ningun proceso mas, 
    para que no este molestando a cada rato
-¿como medir el tiempo dentro del algoritmo?
    podriamos definir una variable T que se vaya incrementando en cada iteracion del codigo


------------------------------------------------------------------------------------------------------
'''