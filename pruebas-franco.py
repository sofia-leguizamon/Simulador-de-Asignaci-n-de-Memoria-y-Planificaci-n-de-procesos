'''import os
import time
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
for i in range(24):
    print(i,"repiteeeeeeeeeeeeeeeeeeeeeeeee")
    time.sleep(1)
clearConsole()  #este comando junto con la linea de codigo 1 y 5 limpian la pantalla en ejecucion
time.sleep(5)   #este comando "pausa" el programa
print("pantalla limpia")
'''


'''
a=[0,1,2,3,4,5]
b=a[3]
a.pop(3)
print(a)
print(b)
c=[]
c.append(b)
print(c)
b=a[1]
print(b)
print(c)'''

import os
from traceback import print_tb
#prueba de archivos, crea y escritura de un archivo
'''
archivo=open("hola.txt","w")
archivo.write("esta es una  prueba de escritura: \n \n")
for i in range(10):
    print(i)
    #archivo.write("for vuelta : ",str(i),"\n")
    archivo.write(str(i))
    archivo.write("\n")    
d=dict()
d[1]= 1
d["ha"]="hello"
d["w"]=34
print(d)
archivo.write("\n")
archivo.write("guardar diccionario: \n")
archivo.write(str(d))
archivo.close()
'''

#archivos lectura de datos
archivoEntrada=open("pruebaDeArchivo.txt","r")
a=dict()
archivoEntrada.readline()      #salto la primera linea del txt, ya que explica las columnas nomas
for linea in archivoEntrada:
    #se aplical la funcion split a una linea del txt, esta funcion corta los caracteres cuando encuentra
    #espacios en blanco, cada elemento cortado lo coloco en una varible
    #nota: si se agrega una columna en el txt tenemos que agregar una nueva variable
    m,n,o=linea.split()
    
print(m)
print(n)
print(o)

