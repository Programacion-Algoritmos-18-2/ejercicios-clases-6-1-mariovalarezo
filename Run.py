from MiArchivo.Archivo import *
from MiModelo.modelo import *


#Obtencion de la lista del txt
m = Mi_archivo()
listaN= m.obtener_informacion()
listaN = [l.split(",") for l in listaN]

#Creacion de lista  contenedora
lista = []


#Doble ciclo de for para separar todos los datos y agregarlos a la lista contenedora como un int
for d in listaN:
    for p in d:
        a = int(p)
        lista.append(a)
#Ordenar los datos de menor a mayor
lista.sort(key=int)
#envia la lista ordenada
b= Busqueda(lista)
#Imprime el metodo busquedaB el cual determina la posicion enviandole el elemento El elemento ejemplo es 4
print("El numero esta en la posicion: ",b.busuedaB(4))




m.cerrar_archivo()