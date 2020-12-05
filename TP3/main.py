
import numpy as np
import random

class Node:
  #Creo una clase llamada nodo que lo que hace es darle a una posicion de la matriz distintos atributos como el "parent" del nodo, la localizacion del nodo y los valores de las funciones g, h y f. Donde parent es la posicion previa que visite en la matriz. Por ejemplo si me muevo de (1,1) a (2,2), el parent del nodo con posicion (2,2) tendra como parent a (1,1)

    def __init__(self, parent=None, position=None):
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = parent
        self.position = position

    #Defino la igualdad de nodos, que se da cuando tienen la misma ubicacion en la matriz.    
    def __eq__(self, other):
        return self.position == other.position

#Funcion que retorna el camino
def return_path(current_node,matrix):
    #Creo un arreglo vacio donde ingresare las tuplas a devolver.
    path = []
    current = current_node
    #Mientras tenga nodos, agrego al arreglo path las tuplas conlas posiciones.
    while current is not None:
        path.append(current.position)
        current = current.parent
    #Lo devuelvo al reves, ya que sino la posicion inicial (la ultima que inserto), quedaria en el final.
    return path[::-1]


def aStar(matrix, cost, start, end):
    #Algoritmo de busqueda A*.

    #Creo los nodos de origen y el final y los inicializo.
    startnode = Node(None, tuple(start))
    endnode = Node(None, tuple(end))

    #Creo un arreglo que contendra los nodos a visitar y otro que contendra los nodos visitados.
    to_visit = []  
    visited = [] 
    
    # Añado el nodo inicial
    to_visit.append(startnode)

    #Creo una codificacion para los movimientos permitidos.
    moves  =  [[-1, 0 ], # arriba
              [ 0, -1], # izquierda
              [ 1, 0 ], # abajo
              [ 0, 1 ]] # derecha

    #Guardo el tamaño de la matriz en 2 variables
    no_rows, no_columns = np.shape(matrix)
    
    # Lupeo mientras todavia tenga nodos para visitar
    
    while len(to_visit) > 0:
        # Saco un nodo de la lista a visitar
        current_node = to_visit[0]
        current_index = 0

        #Para cada nodo en la lista a visitar, el que tenga el menor valor de f, sera elegido para seguir analizan,do
        for index, item in enumerate(to_visit):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        #Saco el nodo actual de la lista de nodos a visitar y los inserto en la lista de visitados
        to_visit.pop(current_index)
        visited.append(current_node)

        # Si el nodo es igual al nodo de destino, entonces retorno la funcion que va a retornar las tuplas.
        if current_node == endnode:
            return return_path(current_node,matrix)

        #Genero la lista que contendra los "hijos" del nodo actual, en caso de que no sea el nodo final.
        children = []

        #Para cada movimiento lupeo.
        for new_position in moves: 

            # Consigo la posicion del nodo y lo inserto en una tupla.
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Me aseguro que la posicion que tengo no sobrepase las dimensiones de la matriz.
            if (node_position[0] > (no_rows - 1) or 
                node_position[0] < 0 or 
                node_position[1] > (no_columns -1) or 
                node_position[1] < 0):
                continue

            # Me fijo que si el nodo sobre el que estoy parado no sea un obstaculo
            if matrix[node_position[0]][node_position[1]] != 0:
                continue

            #Creo un nuevo nodo
            new_node = Node(current_node, node_position)

            #Meto ese nodo a la lista de hijos
            children.append(new_node)

        #Comienzo a revisar los hijos
        for child in children:
            
            # Me fijo que el nodo hijo no este en la lista de visitados
            if len([visited for visited in visited if visited == child]) > 0:
                continue

            #Actualizo los valores de f, g y h para el hijo.
            child.g = current_node.g + cost

            ##El calculo de la heuristica esta dado por la distancia euclidiana.
            child.h = (((child.position[0] - endnode.position[0]) ** 2) + 
                       ((child.position[1] - endnode.position[1]) ** 2)) 

            #Calculo f, ya habiendo calculado g y h
            child.f = child.g + child.h

            #El hijo ya esta en la lista de nodos a visitar y su g es menor
            if len([i for i in to_visit if child == i and child.g > i.g]) > 0:
                continue

            #Añado el hijo a la lista de nodos a visitar
            to_visit.append(child)


#Funcion que crea la matriz y le agrega obstaculos de manera aleatoria
def random_matrix(size,start,end):

  #Creo una matriz llena de ceros, dada el tamaño
  matrix=np.zeros((size,size))
  mylist = [0,1]

  #Mediante la funcion random.choices, agrego obstaculos en la matriz de forma aleatoria, de tal forma en la que es menos probable tener un obstaculo en la matriz y haya una buena distribucion.
  for x in range (0,size):
    for y in range(0,size):
      matrix[x][y]=random.choices(mylist, weights = [3, 1])[0]

  #Si las posiciones iniciales y la final fueron cambiadas por una bloqueada, la desbloqueo.
  matrix[start[0]][start[1]]=0
  matrix[end[0]][end[1]]=0

  return matrix

if __name__ == '__main__':
    start=[0, 0] #Posicion incial
    end=[34,72] # Posicion Final 
    cost=1 #Costo por moviemiento
    matrix=random_matrix(100,start,end)
    path=AStar(matrix,cost, start, end)
    print(path)
    print(np.matrix(matrix))
