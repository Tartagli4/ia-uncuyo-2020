import time
import temple
import hill
import genetico

def algoritmo(n):
  costonulo=0
  tiempo=0
  for x in range(0,29):
    start = time.time()
    if n==1:
      respuesta=temple.crear(N)
      temperatura= 4000
      respuesta,inicial,cont,costo=temple.simulated_annealing(temperatura,N,respuesta)
    if n==2:
      respuesta,costo,cont,inicial=hill.hillClimbing(N)
    if n==3:
      poblacion=[]
      inicial=hill.crear(N)
      for i in range(10):
	      poblacion.append(genetico.intercambio(5, inicial))
      respuesta=genetico.algoritmo_genetico(poblacion)
      costo=hill.amenazas(respuesta,N)
    t=(time.time() - start)
    if costo==0:
      costonulo+=1
    tiempo=tiempo+t
  tiempromedio=tiempo/30
  print("Tiempo promedio: ",tiempromedio)
  print("Cantidad de veces que se llego a un estado optimo:", costonulo)
  print("Ultimo estado inicial: ", inicial )
  print("Ultimo estado final: ", respuesta)
N = 9
algoritmo(1)
#n=1 temple simulado
#n=2 Hill Climbing
#n=3 Algoritmo genetico
