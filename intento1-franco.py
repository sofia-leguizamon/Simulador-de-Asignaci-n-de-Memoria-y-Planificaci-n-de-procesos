
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
    ln.append(crearProceso(idAutoIncr,50,0,4))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,20,0,3))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,93,1,2))
    idAutoIncr+=1
    '''ln.append(crearProceso(idAutoIncr,77,0,3))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,20,0,3))
    idAutoIncr+=1
    ln.append(crearProceso(idAutoIncr,30,2,3))
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
    nuev[0]["nombre"]="sistema operativo"
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
    #'proce' un proceso de la cola de listosYsuspend
    partic["enUso"]= True
    partic["fragI"]= partic["tamaño"]-proce["tamaño"]
    partic["Proceso"]= proce
    return partic

def sacarProcesoDeMemoria(partic):
    global terminados,Multiprogramacion
    partic["enUso"]= False
    partic["fragI"]= 0
    terminados.append(partic["Proceso"])
    Multiprogramacion+=1        #aca sumo uno a la multi porque termino un proces
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

#esto es solo para mi para verificar las tablas- borar al final
def tabla(name,table):
    print("\n",name,"\n")
    for i in table:
        print(i)
    print()
    return 0 

#pasa los proces de la cola de listosYsuspend a la cola de nuevos si se cumple su tiempo de arribo
def deNuevosAlistosYsuspend():
    global nuevos,listosYsuspend,T,cambios,Multiprogramacion
    con=0
    for i in range(len(nuevos)):
        if T>=nuevos[i-con]["ta"] and Multiprogramacion>0: #verifico aca tambien lo de la multi programacion
            listosYsuspend.append(nuevos[i-con])
            nuevos.remove(nuevos[i-con])
            con+=1
            cambios=True
            Multiprogramacion-=1    #aca resto 1 porque pasa un proceso de la cola de nuevos a listosYsuspend

#esta funcion verifica si termino algun proceso en el tiempo T
def verificarProcesoFinalido():
    global memoria,T,Tp,cambios
    for part in memoria:
        if (part["Proceso"]!=None) and (part["ejecutando"]):
            if part["Proceso"]["ti"]+Tp==T:
                print("termino el proceso : ",part["Proceso"])
                sacarProcesoDeMemoria(part)
                cambios=True
    return 0

#esta funcion selecciona un proceso de la memoria(el de menor tiempo de irrupion) y lo pone en ejecucion
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

#basicamente ordenamoms la lista de nuevos por el tiempo de irrupcion nomas
def AplicarAlgoritmoSJF():
    global listosYsuspend,nuevos,memoria,cambios
    #0_ ordenar la cola de listosYsuspend de menor a mayor segun el ti
    listosYsuspend=sorted(listosYsuspend, key=lambda particion : particion['ti'])

    for part in memoria:
        if (not part["ejecutando"]):
            if part["Proceso"]==None:
                    return 0

    #1_verificar que el los proceso que esta afuera tenga un ti menor que cualquier procesos cargado en memoria
    if listosYsuspend!=[]:
        i=0; ban=True ;particionARemplazar=None
        for part in memoria:
            if (not part["ejecutando"]):
                if part["Proceso"]["ti"] <= listosYsuspend[0]["ti"]:
                    return 0
                #2_ seleccionar la la particion donde entre en tamaño, (siempre que no se este ejecutando)
                if ban and listosYsuspend[0]["tamaño"]<= part["tamaño"]:
                    particionARemplazar=i
                    ban=False
            i+=1
        if particionARemplazar==None: #si no  entra en en ninguna particion, debera salir de la funcions
            return 0
        #3_hacer el intercanvio del proceso que esta afuera con el que esta adentro
        x=memoria[particionARemplazar]["Proceso"]
        memoria[particionARemplazar]["Proceso"]=listosYsuspend[0]
        listosYsuspend.remove(listosYsuspend[0])
        listosYsuspend.append(x)
        cambios=True
        print(">--- aplicando SJF se cambio el proceso con ID:",x["id"],"y TI:",x["ti"]," de la ",memoria[particionARemplazar]["nombre"]," por el proceso con ID: ",memoria[particionARemplazar]["Proceso"]["id"],"y TI: ",memoria[particionARemplazar]["Proceso"]["ti"])    
    return 0


def imprimirTabladeProcesos (nombreDeLista, listaDeProcesos): #imprime una tabla con los procesos
    if nombreDeLista=="terminados" or nombreDeLista=="TERMINADOS":
        print("-----------TERMINADOS----------")
    else:
        print("------------",nombreDeLista,"-----------")
    print("| ID  |  tamaño  |  TA  |  TI |")
    print("-------------------------------")
    for p in listaDeProcesos:
        print("| ", p["id"] ,"  |  ", p["tamaño"],"  |  ",  p["ta"],"  |  ", p["ti"]," |"  )
    print("-------------------------------\n")
    return 0

def imprimirTabladeMemoria (memoria): #imprime la memoria
    print("--------------------------- T A B L A  D E  M E M O R I A -------------------------------")
    print("| ID  |  Dir. de comienzo de partición  |  Tamaño  | Id Proceso  |  Frgmentacion Interna  |")
    print("-----------------------------------------------------------------------------------------")
    memoria=sorted(memoria, key=lambda particion : particion["idMemo"],reverse=True)
    dirCdePar=[0,100,160,280]
    for i in range(4):
        if memoria[i]["Proceso"]!= None:
            print("| ", memoria[i]["idMemo"] ," |               ", dirCdePar[i] ,"             | ", memoria[i]["tamaño"],"   |  ", memoria[i]["Proceso"]["id"], "   |", memoria[i]["fragI"],"                     |")
        else:
            print("| ", memoria[i]["idMemo"] ," |               ", dirCdePar[i] ,"             | ", memoria[i]["tamaño"],"   |  no tiene   |", memoria[i]["fragI"],"                     |")    
    print("-----------------------------------------------------------------------------------------\n")
    return 0   


'''Toma un archivo previamente cargado y añade sus procesos, al diccionario de nuevos'''
def procesosDeUnArchivoExterno(): 
    global idAutoIncr, nuevos
    archivoEntrada=open("ArchivoDeProcesos.txt","r")
    archivoEntrada.readline()      #salto la primera linea del txt, ya que explica las columnas nomas
    for linea in archivoEntrada:
         #se aplical la funcion split a una linea del txt, esta funcion corta los caracteres cuando encuentra
         #espacios en blanco, cada elemento cortado lo coloco en una varible
        m,n,o=linea.split()
        a=crearProceso(idAutoIncr, int(m), int(n), int(o))
        idAutoIncr+=1
        nuevos.append(a)
    return 0

def MostrarProcesoEnEjecucion():
    global memoria
    for part in memoria:
        if part["idMemo"]!=1:
            if part["ejecutando"]:
                    print("|||||||||||||||||||||||| PROCESOS EN EJECUCION ||||||||||||||||||||||||||||||||||")
                    print("| ID PROCESO |  tamaño  |  TA  |  TI  |  NOMBRE PART    |ID PARTICION|")
                    print("|  ",part["Proceso"]["id"],"       | ",part["Proceso"]["tamaño"], "     | ",part["Proceso"]["ta"], "  |", part["Proceso"]["ti"],"   |  ", part["nombre"],"  | ",part["idMemo"],"       | ")
                    print("---------------------------------------------------------------------------------\n")
    return 0

def MostrarProcesosEnListos():
    global memoria
    print("-------------LISTOS------------")
    print("| ID  |  tamaño  |  TA  |  TI |")
    print("-------------------------------")
    for part in memoria:
        if (not part["ejecutando"]) and part["Proceso"]!=None:
            print("| ", part["Proceso"]["id"] ,"  |  ", part["Proceso"]["tamaño"],"  |  ",  part["Proceso"]["ta"],"  |  ", part["Proceso"]["ti"]," |"  )
    print("-------------------------------\n")
    return 0




'''----------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------------------------------'''
''' aqui ya no hay funciones -- codigo madre'''





T=0     #tiempo de la cpu, esta va  a ser la medida de tiempo que vamos a tener en la misma corrida
Tp=0    #Variable axiliar que nos permitira saber si comenzo a ejecutarse el 

Multiprogramacion=5             #esta bariable solo va a tener valores del 0 al 5

cambios=False       #boolean que indica si hubo cambios true para si false para no

idAutoIncr=0 #se define el id de que se va a ir incrementando por cada proceso que entre en la corrida

memoria=crearMemoria()  #definimos la memoria
memoria=sorted(memoria, key=lambda particion : particion['tamaño'],reverse=True)
#esta funcion ordena el arreglo de diccionarios y los ordena de mayor a menor segun indique el campo ["tamaño"]
#esto se hace para facilitar la incercion del worst-fit, gracias al reverse=True


#LAS DISTINTAS COLAS DE PROCEOSOS
nuevos=list()           #lista de los procesos que recien llegan , todabia no se cumple su TA
listosYsuspend=list()           #lista de los procesos que ya podrian entrar en memoria, ya se cumplio su TA
terminados=list()       #procesos que ya han terminado, que ya se corrieron 

#comienza el menu con las distintas opciones para el usuario
print("mensaje de bienvenida")
print("1 - correr simulacion con procesos por default ")
print("2 - correr simulacion con procesos que esten cargados en un archivo externo: 'ArchivoDeProcesos.txt'. ")
while True:
    try:
        ax=int(input("ingrese una de las opciones: "))
        if ax==1:
            nuevos=listaDeProcesosNuevosPorDefault()
            break
        elif ax==2:
            procesosDeUnArchivoExterno()
            break
        else:
            print("opcion invalida, pruebe de nuevo...")
    except:
        print("error:solo numeros por favor")


imprimirTabladeProcesos("NUEVOS",nuevos)
imprimirTabladeMemoria(memoria)
MostrarProcesosEnListos()

#CODIGO MADRE
while True:
    print(">------------------------------tiempo= ",T,"-- multiProg=",Multiprogramacion,"------------------------------<\n")
    #1. por cada unidad de tiempo que pase verifica que haya procesos que se puedan agregar a la lista de listosYsuspend y salgan de la lista de nuevos
    
    verificarProcesoFinalido()  #se hace esta verificacion porque cuando un proceso termina ya tiene que ingresar otro
    deNuevosAlistosYsuspend()
    AplicarAlgoritmoSJF()
    
    #2. por cada unidad de tiempo verifica que no se puedan colocar procesos de la lista de listosYsuspend en la memoria
    listaMomentania=[]
    for p in listosYsuspend:
        if algoritmoWorstFit(p):
            print(">--------------------EL PROCESO CON ID: ",p["id"]," FUE COLOCADO EN MEMORIA--------------------<")
            listaMomentania.append(p)
            cambios=True
        '''else:
            print("proceso  ",p," --> NO PUDO SER COLOCADO")'''
    #los porcesos colocados se borran de la cola de listosYsuspend y quedan en la memoria
    for r in listaMomentania:
        listosYsuspend.remove(r)
    
    #3. por cada unidad de tiempo veridica si se puede correr un proceso o si un proceso finalizo
    CorrerProcesoDeM()
    verificarProcesoFinalido()

    #imprime por pantalla cosas si hubo algun cambio
    if cambios:
        cambios=False
        input("mostramos cambios...(precione cualquier tecla)")
        imprimirTabladeMemoria(memoria)
        imprimirTabladeProcesos("NUEVOS",nuevos)
        MostrarProcesosEnListos()
        imprimirTabladeProcesos("LIS/SUS",listosYsuspend)
        imprimirTabladeProcesos("TERMINADOS",terminados)
        MostrarProcesoEnEjecucion()

        input("presione cualquier tecla para continuar")
    
    T+=1
    #esta es la verificacion de fin del algoritmo(codigo madre)
    if len(terminados)==idAutoIncr:
        break
    #esto va a terminar cuando todos  los procesos esten terminados, osea que las otras listas esten vacias

print("gracias por vernos hasta el final")
print("esto fue el grupo 2... ")
