import random
from math import exp
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


def costo(tablero,N):
  cont = 0
  for i in range(0,N):
    for j in range(i+1,N):
      if tablero[j]==tablero[i]:
        cont += 1
      if tablero[j]+j==tablero[i]+i or tablero[j]-j==tablero[i]-i:
        cont += 1
  return cont


def simulated_annealing(t,N,respuesta):
    inicial=respuesta
    # Para evitar recuento cuando no encontramos un mejor estado.
    costo_respuesta = costo(imprimir(respuesta),N)
    cont=0
    sch=0.99
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
        delta = costo(imprimir(sucesor),N) - costo_respuesta
        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            respuesta = deepcopy(sucesor)
            costo_respuesta = costo(imprimir(respuesta),N)
        if costo_respuesta == 0 or cont>500:
            return(imprimir(respuesta),imprimir(inicial),cont,costo_respuesta)


def imprimir(tablero):
    #Imprime el tablero
    retornado=[]
    for x in range(0,len(tablero)):
      retornado.append(tablero[x])
    return retornado