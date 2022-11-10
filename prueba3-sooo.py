from tabulate import tabulate
import re

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
    ln.append(crearProceso(idAutoIncr,20,2,3))
    idAutoIncr+=1
    '''
    ln.append(crearProceso(idAutoIncr,93,2,7))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,77,3,3))
    idAutoIncr+=1'''
    return ln

#pide y verifica el ingreso de un proceso por pantalla, debolviendp dicho proceso como un diccionario ya definido
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
    return p

#creacion de la memoria, devuelve una lista con las particiones
def crearMemoria():
    #deficinicion de la particion
    particion = {
        "nombre":None,      #nombre de la particion 
        "tamaño":None,      #tamaño de la particion
        "enUso":False,      #si tiene un proceso o no en ella
        "fragI":0,          #fragmentacion Interna
        "fragE":False,      #fragmentacion Externa
        "Proceso":None ,    #es el procesos que se encunetre en la particion
        "idMemo":None,
        "ejecutando":False   #si el proceso que esta en esa particion esta en ejecucion      
    }
    #creacion de la lista que va a tener las particiones
    nuev=list()
    #creacion de las particiones y agregacion a la lista
    for i in range(4):
        nuev.append(dict(particion))
    #cargo los datos de cada particion:
    nuev[0]["nombre"]="Sist. Op.  "
    nuev[0]["tamaño"]=100
    nuev[0]["enUso"]=True
    nuev[0]["idMemo"]=1
    nuev[0]["ejecutando"]=True

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
    return nuev
    
#carga en la particion, el proceso seleccionado ()
def ponerProcesoEnMemoria(partic,proce): 
    #'partic' sera una particion de la memoria
    #'proce' un proceso de la cola de listos
    partic["enUso"]= True
    partic["fragI"]= partic["tamaño"]-proce["tamaño"]
    partic["Proceso"]= proce
    return partic

def sacarProcesoDeMemoria(partic):
    global terminados
    partic["enUso"]= False
    partic["fragI"]= 0
    terminados.append(partic["Proceso"])
    partic["Proceso"]= None
    partic["ejecutando"]=False
    return 0

#esta funcion coloca un proceso segun worst fitn en la memoria y devuelve un valor verdadero
# si lo coloco y uno falso si no
def algoritmoWorstFit(proceso): 
    global memoria
    for i in memoria:
        if  not(i["enUso"]) and proceso["tamaño"]<= i["tamaño"]:
            ponerProcesoEnMemoria(i,proceso)
            return True
    return False

#basicamente ordenamoms la lista de nuevos por el tiempo de irrupcion nomas
def AplicarAlgoritmoSJF():
    global nuevos
    nuevos=sorted(nuevos, key=lambda particion : particion['tamaño'],reverse=True)
    return 0

#esto es solo para mi para verificar las tablas- borar al final
def tabla(name,table):
    print("\n",name,"\n")
    for i in table:
        print(i)
    print()
    return 0 

#esta es la verificacion de fin del algoritmo
def terminoTodo():
    global nuevos,listos,suspendidos,corriendo
    return (len(nuevos)==0 and  len(listos)==0 and len(suspendidos)==0 and len(corriendo)==0)

def deNuevosAListos():
    global nuevos,listos,T,cambios
    con=0
    for i in range(len(nuevos)):
        if T>=nuevos[i-con]["ta"]:
            listos.append(nuevos[i-con])
            nuevos.remove(nuevos[i-con])
            con+=1
            cambios=True

def verificarProcesoFinalido():
    global memoria,T,Tp,cambios
    for part in memoria:
        if (part["Proceso"]!=None) and (part["ejecutando"]):
            if part["Proceso"]["ti"]+Tp-1==T:
                print("termino el proceso : ",part["Proceso"])
                sacarProcesoDeMemoria(part)
                cambios=True
    return 0

def CorrerProcesoDeM():
    global memoria,ayudaMemoria,T,Tp,cambios
    #verifico que no haya un proceso en ejecucion
    for part in memoria:
        if part["idMemo"]!=1 and part["ejecutando"]:
            return 0
    cont=0
    #verifico que haya procesos cargados en memoria
    for part in memoria:
        if part["Proceso"]==None:
            cont+=1
        if cont==4:
            return 0

    x=10000
    s=0
    cont=0
    for part in memoria:
        if (part["idMemo"]!=1)and(part["Proceso"]!=None):
            if part["Proceso"]["ti"] < x:
                x=part["Proceso"]["ti"]
                s=cont
        cont+=1
    memoria[s]["ejecutando"]=True
    Tp=T
    cambios=True
    return 0






'''----------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------'''
''' aqui ya no hay funciones -- codigo madre'''





T=0 #tiempo de la cpu, esta va  a ser la medida de tiempo que vamos a tener en la misma corrida
Tp=0#Variable axiliar que nos permitira saber si comenzo a ejecutarse el 

Multiprogramacion=5             #esta variable solo va a tener valores del 0 al 5

cambios=False       #boolean que indica si hubo cambios true para si false para no

idAutoIncr=0 #se define el id de que se va a ir incrementando por cada proceso que entre en la corrida

memoria=crearMemoria()  #definimos la memoria
memoria=sorted(memoria, key=lambda particion : particion['tamaño'],reverse=True)
#esta funcion ordena el arreglo de diccionarios y los ordena de mayor a menor segun indique el campo ["tamaño"]
#esto se hace para facilitar la incercion del worst-fit, gracias al reverse=True


#LAS DISTINTAS COLAS DE PROCESOS
nuevos=list()           #lista de los procesos que recien llegan, todavia no se cumple su TA
listos=list()           #lista de los procesos que ya podrian entrar en memoria, ya se cumplio su TA
suspendidos=list()      #lista de los procesos que estan en espera de libear espacio en memoria
corriendo=list()        #proceso que se esta corriendo
terminados=list()       #procesos que ya han terminado, que ya se corrieron 


nuevos=listaDeProcesosNuevosPorDefault()

'''print();print();print()
if algoritmoWorstFit(nuevos[4]):
    print("proceso colocado")

ingresarUnProcesoPorPantalla()'''

print(nuevos,"\n")
print(nuevos[0])
print(nuevos[0]["ta"])
def imprimirTabladeProcesos (diccionario):
    print("-------------------------------")
    print("| ID  |  tamaño  |  TA  |  TI |")
    print("-------------------------------")
    for p in diccionario:
        print("| ", p["id"] ,"  |  ", p["tamaño"],"  |  ",  p["ta"],"  |  ", p["ti"]," |"  )
    print("-------------------------------")
    return 0

def imprimirTabladeMemoria (memoria):
    print("-----------------------------------------------------------------------------------------")
    print("--------------------------- T A B L A  D E  M E M O R I A -------------------------------")
    print("-----------------------------------------------------------------------------------------")
    print("| ID  |  Dir. de comienzo de partición  |  Tamaño  |  Proceso  |  Frgmentacion Interna  |")
    print("-----------------------------------------------------------------------------------------")
    for m in memoria:
        print("| ", m["idMemo"] ," |  a solucionar                   |  ", m["tamaño"],"   |  ", m["Proceso"], "   |", m["fragI"],"                     |")
    print("-----------------------------------------------------------------------------------------")
    return 0
    
imprimirTabladeProcesos(nuevos)
imprimirTabladeMemoria(memoria)



def ponerEnTxt (): 
    global idAutoIncr, nuevos
    archivoEntrada=open("pruebaDeArchivo.txt","r")
    archivoEntrada.readline()      #salto la primera linea del txt, ya que explica las columnas nomas
    for linea in archivoEntrada:
         #se aplical la funcion split a una linea del txt, esta funcion corta los caracteres cuando encuentra
         #espacios en blanco, cada elemento cortado lo coloco en una varible
         #nota: si se agrega una columna en el txt tenemos que agregar una nueva variable
        m,n,o=linea.split()
        a=crearProceso(idAutoIncr, int(m), int(n), int(o))
        idAutoIncr+=1
        nuevos.append(a)
        print("PROCESO:", a)


ponerEnTxt()
imprimirTabladeProcesos(nuevos)
