# # Algoritmia
# ## Práctica 10
# En esta práctica se resolverá el problema de los caminos mínimos entre todos los nodos de un grafo.
# Y la multiplicación de matrices.
 
class CaminosMinimosFloyd:
    """
    Clase para representar los caminos mínimos entre todos los nodos de un grafo.
    Los caminos deben calcularse con el algoritmo de Floyd.
    El espacio de almacenamiento debe ser O(n^2), siendo n el número de nodos.
    """

    def __init__(self, grafo):
        """
        Constructor que recibe el grafo sobre el que calcular los caminos
        mínimos.
        El grafo que se recibe es un diccionario donde las claves son arcos 
        (pares de nodos) y los valores son el peso de los arcos.
        """

        # Definición de G, D y P a matrices
        pass
        
    def distancia(self, origen, destino):
        """
        Devuelve la distancia del camino mínimo ente origen y destino.
        Si no hay camino devuelve None.
        """
        pass
        
    def camino(self, origen, destino):
        """
        Devuelve en una lista de nodos el camino mínimo entre origen y
        destino.
        Si no hay camino devuelve None.
        """
        pass


def multiplicacion_encadenada_matrices(dimensiones):
    """
    Dadas las dimensiones de varias matrices a multiplicar, aplica el método
    de programación dinámica para para determinar en qué orden realizar las
    multiplicaciones.
    El número de matrices será la longitud de dimensiones menos uno.
    Las dimensiones de la matriz M_i están en las componentes i-1 e i de
    'dimensiones'.
    Devuelve el número de multiplicaciones de elementos a realizar y una
    cadena con la fórmula, incluyendo paréntesis (solo si son necesarios), en
    la que se realizarían las multiplicaciones.
    Por ejemplo '(M_1*(M_2*M_3))*M_4'.
    """
    pass