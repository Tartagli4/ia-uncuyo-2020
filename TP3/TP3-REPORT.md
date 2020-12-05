  
Inteligencia Artificial 1: TP 3
Alumno: Tartaglia, Juan Ignacio Fecha de entrega: 2/11/2020

Realización del Algoritmo.
El primer paso para la realización del algoritmo fue investigar sobre el mismo. Para ello consulte distintas fuentes de información como videos de YouTube y la bibliografía dada por la catedra.

Una vez terminado el proceso de investigación e información del tema, decidí que la función de heurística [h(x)] estaría dada por la distancia euclidiana, ya que esta siempre nos va a dar una aproximación optimista con respecto a distancias, lo cual hace que la función sea admisible y consistente para el algoritmo.

Ya con la heurística preparada, se comenzó con la codificación del algoritmo, el cual esta basado en la utilización de la posición de la matriz como un "nodo". Se realizo de esta manera, ya que trabajando con nodos se pueden crear distintos atributos para esa posición de la matriz, como los valores de sus funciones (g, f y h) y su "padre".

Cada nodo tiene un padre, el cual hace referencia al nodo del cual vengo, por ejemplo si yo me encuentro en la posición (1,1) y me muevo a la posición (2,1), entonces el padre del mismo, será el que esta dado por la posición (1,1). Así mismo como un nodo tiene un padre, se crea el concepto de hijo.

Como los movimientos que puede realizar el algoritmo son izquierda, derecha, arriba y hacia abajo, defino en el algoritmo como hijos de un nodo, a los nodos que se encuentran realizando todos los movimientos posibles desde un mismo nodo.

Finalmente, el algoritmo se basa en el comienzo de un nodo dado en la posición inicial y luego, el movimiento hacia distintos nodos, hasta que lleguemos al nodo destino, en caso de que sea posible. Para realizar este movimiento de nodo inicial a nodo final, lo que se hace es analizar los nodos, tanto como sus hijos, su padre, si ya fue visitado anteriormente y si es el nodo final. Una vez realizado este análisis, se selecciona un nuevo nodo para continuar, si es que el algoritmo debe seguir avanzando, el cual será el que tenga el valor de f mas bajo que no haya sido visitado y así se repite hasta que el algoritmo finalice.
