import numpy as np
import random
import copy

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
    return imprimir(tablero)

def imprimir(tablero):
    #Imprime el tablero
    retornado=[]
    for x in range(0,len(tablero)):
      retornado.append(tablero[x])
    return retornado

def vecinos(tablero,n):
  tablerOptimo=copy.deepcopy(tablero)
  amenazasOptimas = amenazas(tablerOptimo,n)
  vecino = copy.deepcopy(tablerOptimo)
  amenazasVecino = amenazas(vecino,n)
  for i in range(0,n):
    for j in range(0,n):
      if (j != tablero[i]):
        vecino[i] = j
        NeighbourValue = amenazas(vecino,n)
        if NeighbourValue <= amenazasOptimas:
          amenazasOptimas = amenazasVecino
          tablerOptimo = copy.deepcopy(vecino)
        vecino[i] = tablero[i]
  return tablerOptimo

def amenazas(tablero,N):
  cont = 0
  for i in range(0,N):
    for j in range(i+1,N):
      if tablero[j]==tablero[i]:
        cont += 1
      if tablero[j]+j==tablero[i]+i or tablero[j]-j==tablero[i]-i:
        cont += 1
  return cont

def hillClimbing(n):
  tablero=crear(n)
  inicio=tablero
  cont=0
  actual=tablero
  valor = amenazas(actual,n)
  while (cont<20):
    vecino=vecinos(actual,n)
    amenazasVecino = amenazas(vecino,n)
    if amenazasVecino<valor:
      actual=vecino
      valor=amenazasVecino
      cont += 1
    else:
      return (actual,valor,cont,tablero)