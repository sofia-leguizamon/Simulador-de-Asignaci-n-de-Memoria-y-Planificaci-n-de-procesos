#prueba para habrir un archivo existente ingresando el nombre por cmd
a=input("ingrese el nombre del archivo que quiere abrir: ")
a.rstrip("\n")      #esto es para eliminar el salto de linea del ingreso del texto
arch1=open(a,"r")   #abro el archivo con nombre "a" como read

for linea in arch1:
    print(linea)
