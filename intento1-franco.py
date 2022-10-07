
#cracion de un proceso base y vacio, como si fuera una clase
#por cada proceso se debe ingresaro leer desde un archivo el Id de proceso, 
# tamaño del proceso, tiempo de arribo y tiempo de irrupción.
def crearProceso(id,tamaño,ta=0,ti=0):
    a=dict()
    a["id"] = id            #el numero de proceso
    a["tamaño"] = tamaño    #tamño de dicho proceso en kb
    a["ta"] = ta            #tiempo de arribo
    a["ti"] = ti            #tiempo de irrupcion
    return a

#Crea unos procesos de prueva y los pone en una lista
def listaDeProcesosNuevosPorDefault():
    global idAutoIncr
    ln=list()
    ln.append(crearProceso(idAutoIncr,40,0,3))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,140,0,4))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,200,2,3))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,93,2,7))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,77,3,3))
    idAutoIncr+=1
    #muestra los procesos creados
    print("los procesos por defaul creados son:")
    for i in range(len(ln)):
        print(ln[i])
    return ln

#
def ingresarUnProcesoPorPantalla():
    global idAutoIncr
    idp=idAutoIncr
    idAutoIncr+=1
    print()
    while True:
        try:
            tamp=int(input("Ingrese el tamaño del proceso: "))
            break
        except:
            print("Error al ingresar el tamaño, solo numeros enteros y sin otro tipo de caracteres")
            print("Trate de nuevo --> ")
    while True:
        try:
            tap=int(input("Ingrese el TA del proceso: "))
            break
        except:
            print("Error al ingresar el TA, solo numeros enteros y sin otro tipo de caracteres")
            print("Trate de nuevo --> ")
    while True:
        try:
            tip=int(input("Ingrese el TI del proceso: "))
            break
        except:
            print("Error al ingresar el TI, solo numeros enteros y sin otro tipo de caracteres")
            print("Trate de nuevo --> ")

    p=crearProceso(idp,tamp,tap,tip)
    print("el proceso ingresado fue: ")
    print(p)
    #aca tenemos que debolver el proceso recien cargado.
    return 0

#creacion de la memoria, devuelve una lista con las particiones
def crearMemoria():
    #deficinicion de la particion
    particion = {
        "nombre":None,      #nombre de la particion 
        "tamaño":None,      #tamaño de la particion
        "enUso":False,      #si tiene un proceso o no en ella
        "fragI":0,          #fragmentacion Interna
        "fragE":False,      #fragmentacion Externa
        "idProc":None ,     #es el id del procesos que se encunetre en la particion
        "idMemo":None      
    }
    #creacion de la lista que va a tener las particiones
    nuev=list()
    #creacion de las particiones y agregacion a la lista
    for i in range(4):
        nuev.append(dict(particion))

    #cargo los datos de cada particion:
    nuev[0]["nombre"]="sistema operativo"
    nuev[0]["tamaño"]=100
    nuev[0]["enUso"]=True
    nuev[0]["idMemo"]=1

    nuev[1]["nombre"]="particion 1"
    nuev[1]["tamaño"]=60
    nuev[1]["idMemo"]=2

    nuev[2]["nombre"]="particion 2"
    nuev[2]["tamaño"]=120
    nuev[2]["idMemo"]=3

    nuev[3]["nombre"]="particion 3"
    nuev[3]["tamaño"]=250
    nuev[3]["idMemo"]=4

    #muestro por pantalla para verificar, sacar o comentar las prox 3 lines
    
    print("la memoria quedaria asi:")
    for i in range(4):
        print(nuev[i])
    
    return nuev
    
#carga en la particion, el proceso seleccionado ()
def ponerProcesoEnMemoria(partic,proce): 
    #'partic' sera una particion de la memoria
    #'proce' un proceso de la cola de listos
    partic["enUso"]= True
    partic["fragI"]= partic["tamaño"]-proce["tamaño"]
    partic["idProc"]= proce["id"]
    return partic

def sacarProcesoDeMemoria(partic):
    partic["enUso"]= False
    partic["fragI"]= 0
    partic["idProc"]= None
    return 0

#esta funcion coloca un proceso segun worst fitn en la memoria
def algoritmoWorstFit(proceso): 
    global memoria
    for i in memoria:
        if  not(i["enUso"]) and proceso["tamaño"]<= i["tamaño"]:
            ponerProcesoEnMemoria(i,proceso)
            return True
        else:
            print("memoria ocupada")
    print("el procesos ",proceso["id"],"no se pudo colocar en memoria")
    return False

#basicamente ordenamoms la lista de nuevos por el tiempo de irrupcion nomas
def AplicarAlgoritmoSJF():
    global nuevos
    nuevos=sorted(nuevos, key=lambda particion : particion['tamaño'],reverse=True)
    return 0

def mostrarTablaDeMemoria():
    return 0



'''----------------------------------------------------------------------------------------------------------'''
''' aqui ya no hay funciones -- codigo madre'''
T=0 #tiempo de la cpu, esta va  a ser la medida de tiempo que vamos a tener en la misma corrida
Multiprogramacion=5             #esta bariable solo va a tener valores del 0 al 5

idAutoIncr=0 #se define el id de que se va a ir incrementando por cada proceso que entre en la corrida

memoria=crearMemoria()  #definimos la memoria
memoria=sorted(memoria, key=lambda particion : particion['tamaño'],reverse=True)
#esta funcion ordena el arreglo de diccionarios y los ordena de mayor a menor segun indique el campo ["tamaño"]
#esto se hace para facilitar la incercion del worst-fit, gracias al reverse=True


#LAS DISTINTAS COLAS DE PROCEOSOS
nuevos=list()           #lista de los procesos que recien llegan , todabia no se cumple su TA
listos=list()           #lista de los procesos que ya podrian entrar en memoria, ya se cumplio su TA
suspendidos=list()      #lista de los procesos que estan en espera de libear espacio en memoria
corriendo=None          #proceso que se esta corriendo
terminados=list()       #procesos que ya han terminado, que ya se corrieron 



nuevos=listaDeProcesosNuevosPorDefault()

'''print();print();print()
if algoritmoWorstFit(nuevos[4]):
    print("proceso colocado")

print();print();print()
for i in memoria:
    print(i)'''

ingresarUnProcesoPorPantalla()


#CODIGO MADRE
while True:
    
    
    break
    T+=1



'''
------------------------------------------------------------------------------------------------------
---------para implementar futuras funciones---------
------------------------------------------------------------------------------------------------------
-funcion que verifique que no haya dos procesos con el mismo id,
    notificar el errror y expluir procesos en caso afirmativo
    sofi---

-una funcion que implemente el worst-fit para la memoria y el proceso
    -----ya esta----

-un algoritmo que realice la planificacion SJF
    este algoritmo solo trabja en la cola de "listos" 
    -----ya esta----

-menu de opciones de ingrso de procesos, si quiere por un archivo o manual o default

-cargar proceso manualmente
    -----ya esta----

-cargar procesos por un archivo externo
    -----ya casiii esta----

-------procesos-------
-mostrar la tabla de los procesos cargados(los que estarian en la lista de nuevos)
-mostrar el proceso que esta corriendo (el proceso que esta en corriendo)
-El estado de la cola de procesos listos(lista de listos).
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
    --- ya esta ----


aclaracines del profe 15/09
-verificar errores de ingresos de datos en los procesos ... el profe puede poner en un TA 0-12'

------------------------------------------------------------------------------------------------------
'''