"""a={
  "a":2
}
m=list()
for i in range(4):
  a["a"]=i
  print(a["a"])
  m.append(a)

print(m)
for j in range(15):
  for i in range(10):
    print("a", end=" ")
  print()

"""

def GeneralProcesos():
  lis=list()

  return lis



"""#asi, podemos obtener la direccion de memoria de una variable
a=list()
print(id(a))
b=list()
print(id(b))"""


#crear una lista vacia de x elemntos
"""l=list()
l=[None]*10
print(l)"""

#forma de ordenar una lista, segun una clave
"""tuplas_coches = [
        ('Rojo', '4859-A', 'A'),
        ('Azul', '2901-Z', 'M'),
        ('Gris', '1892-B', 'M')
    ]
# Ordenar los coches por matrícula
ordenados = sorted(tuplas_coches, key=lambda coe : coe[0])
print(ordenados)"""

"""
1-comenzar por la particion mas chica 
2-verificar su mayor espacio disponible de la particion
3-verificar si el proceso entra en la paraticion escogida
4-
"""


"""l=[None,None,None,None,None,1,None,None,None,None]
c=0
for i in range(len(l)):
  if l[i]==None:
    c=c+1
  else:
    c=0
print(c)"""


l=list()
l=[1]*3
a={
  1:l
}
b=dict()
b=a
b[1][0]=100
print(a)
print(b)

"""e=False
if not e:
  print("funciona")"""
#prueba de tiempo
"""import time
print("vendra un mensaje despues de 1.9 segundos")
time.s☺leep(1.9)
print("hola")
segund=time.time()
print(segund)

while segund!=segund+10:
  break"""

"""a,b=[3,4]
print(a)
print(b)

a=[3,4,3,5]
print(a)
del a[2]
print(a)
for i in a:
  print(i)


a=list()
if a==[]:
  print("funciona")"""

"""def Particion(nomb,cant):
  l=list()
  l=[None]*cant
  a=dict()
  a["nombre"] = nomb
  a["espacio"] = l
  a["libre"] = True
  a["DuracionDePro"] = None
  a["idcomienzo"] = id(a["espacio"][0])
  a["id"] = id(a)
  a["idproc"] = None
  a["fragmentI"] = None
  return a

b=Particion("p1",50)
print(b["id"])
print(b["idcomienzo"])
b["espacio"][0]=1
print(b["id"])
print(b["idcomienzo"])"""

