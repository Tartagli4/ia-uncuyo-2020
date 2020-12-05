import random
from math import exp
import time
from copy import deepcopy


def amenaza(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return (n - 1) * n / 2


def crear(n):
    #Creo el tablero
    tablero = {}
    temperatura = list(range(n))
    random.shuffle(temperatura)  # lo mezclo para que sea random
    columna = 0
    while len(temperatura) > 0:
        fila = random.choice(temperatura)
        tablero[columna] = fila
        temperatura.remove(fila)
        columna += 1
    del temperatura
    return tablero


def costo(tablero):
    #Calculo cuantos pares de reinas hay amenazados
    amenazas = 0
    tablerom = {}
    tableroa = {}

    for columna in tablero:
        temp_m = columna - tablero[columna]
        temp_a = columna + tablero[columna]
        if temp_m not in tablerom:
            tablerom[temp_m] = 1
        else:
            tablerom[temp_m] += 1
        if temp_a not in tableroa:
            tableroa[temp_a] = 1
        else:
            tableroa[temp_a] += 1

    for i in tablerom:
        amenazas += amenaza(tablerom[i])
    
    for i in tableroa:
        amenazas += amenaza(tableroa[i])
    
    return amenazas


def simulated_annealing(t,N,respuesta):
    inicial=respuesta
    solucion=False
    # Para evitar recuento cuando no encontramos un mejor estado.
    costo_respuesta = costo(respuesta)
    cont=0
    sch = 0.99
    while t > 0:
        cont=cont+1
        t*= sch
        sucesor = deepcopy(respuesta)
        while True:
            index_1 = random.randrange(0, N - 1)
            index_2 = random.randrange(0, N - 1)
            if index_1 != index_2:
                break
        sucesor[index_1], sucesor[index_2] = sucesor[index_2], \
            sucesor[index_1]  #intercambio las reinas seleccionadas
        delta = costo(sucesor) - costo_respuesta
        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            respuesta = deepcopy(sucesor)
            costo_respuesta = costo(respuesta)
        if costo_respuesta == 0:
            solucion = True
            return(imprimir(respuesta),imprimir(inicial),cont)


def imprimir(tablero):
    #Imprime el tablero
    retornado=[]
    for x in range(0,len(tablero)):
      retornado.append(tablero[x])
    return retornado

N = 9
temperatura= 4000
start = time.time()
respuesta=crear(N)
respuesta,inicial,contador=simulated_annealing(temperatura,N,respuesta)
print("Estado inicial:", inicial)
print("Estado Final:", respuesta)
print("Cantidad de estados recorridos:", contador)
print("Tiempo de ejecucción:", time.time() - start)
