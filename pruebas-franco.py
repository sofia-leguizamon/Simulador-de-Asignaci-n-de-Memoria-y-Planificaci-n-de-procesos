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
print(c)