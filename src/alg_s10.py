# # Algoritmia
# ## Práctica 10
# En esta práctica se resolverá el problema de los caminos mínimos entre todos los nodos de un grafo.
# Y la multiplicación de matrices.
from typing import Optional, List


class CaminosMinimosFloyd:
    """
    Clase para representar los caminos mínimos entre todos los nodos de un grafo.
    Los caminos deben calcularse con el algoritmo de Floyd.
    El espacio de almacenamiento debe ser O(n^2), siendo n el número de nodos.
    """

    def __init__(self, grafo: dict):
        """Constructor que recibe el grafo sobre el que calcular los caminos
        mínimos.
        El grafo que se recibe es un diccionario donde las claves son arcos
        (pares de nodos) y los valores son el peso de los arcos.

        Args:
            grafo (dict): Grafo representado como un diccionario de arcos y pesos.
        """
        # Extraer todos los nodos del grafo
        nodos = set()
        for origen, destino in grafo:
            nodos.add(origen)
            nodos.add(destino)
        self.nodos = sorted(list(nodos))  # Ordenamos para tener un orden fijo

        # Construir diccionarios
        self.nodo_a_indice = {}
        self.indice_a_nodo = {}
        for i, nodo in enumerate(self.nodos):
            self.nodo_a_indice[nodo] = i
            self.indice_a_nodo[i] = nodo
        n = len(self.nodos)

        # Inicializar matrices D y P
        INF = float("inf")
        self.D = [[INF for _ in range(n)] for _ in range(n)]  # Matriz de distancias
        self.P: List[List[Optional[int]]] = [
            [None for _ in range(n)] for _ in range(n)
        ]  # Matriz de predecesores

        # Inicializar diagonal de D con ceros (distancia de un nodo a sí mismo)
        for i in range(n):
            self.D[i][i] = 0

        # Llenar matrices D y P con la información del grafo
        for (origen, destino), peso in grafo.items():
            i = self.nodo_a_indice[origen]
            j = self.nodo_a_indice[destino]
            self.D[i][j] = peso
            self.P[i][j] = i  # El predecesor de j en el camino desde i es i

        # Algoritmo de Floyd
        # D es la matriz de distancias mínimas
        # P es la matriz de predecesores
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.D[i][k] != INF and self.D[k][j] != INF:
                        if self.D[i][j] > self.D[i][k] + self.D[k][j]:
                            self.D[i][j] = self.D[i][k] + self.D[k][j]
                            self.P[i][j] = self.P[k][j]

    def distancia(self, origen: str, destino: str) -> Optional[float]:
        """Devuelve la distancia del camino mínimo ente origen y destino.
        Si no hay camino devuelve None.

        Args:
            origen (str): Origen del camino.
            destino (str): Destino del camino.

        Returns:
            Optional[float]: Distancia del camino mínimo o None si no hay camino.
        """
        if (origen not in self.nodo_a_indice) or (destino not in self.nodo_a_indice):
            return None

        i = self.nodo_a_indice[origen]
        j = self.nodo_a_indice[destino]

        if self.D[i][j] == float("inf"):
            return None

        return self.D[i][j]

    def camino(self, origen: str, destino: str) -> Optional[List[str]]:
        """Devuelve en una lista de nodos el camino mínimo entre origen y
        destino.
        Si no hay camino devuelve None.

        Args:
            origen (str): Origen del camino.
            destino (str): Destino del camino.

        Returns:
            Optional[List[str]]: Lista de nodos del camino mínimo o None si no hay camino.
        """
        if origen not in self.nodo_a_indice or destino not in self.nodo_a_indice:
            return None

        i = self.nodo_a_indice[origen]
        j = self.nodo_a_indice[destino]

        if self.D[i][j] == float("inf"):
            return None

        # Si origen y destino son el mismo nodo
        if origen == destino:
            return [origen]

        # Reconstruir el camino usando la matriz P
        camino = [destino]
        while i != j:
            j = self.P[i][j]
            if j is not None:
                camino.insert(0, self.indice_a_nodo[j])
            else:
                # Si j es None, hay un problema con el camino
                return None

        return camino


def multiplicacion_encadenada_matrices(dimensiones: List[int]) -> tuple:
    """Dadas las dimensiones de varias matrices a multiplicar, aplica el método
    de programación dinámica para para determinar en qué orden realizar las
    multiplicaciones.
    El número de matrices será la longitud de dimensiones menos uno.
    Las dimensiones de la matriz M_i están en las componentes i-1 e i de
    'dimensiones'.
    Devuelve el número de multiplicaciones de elementos a realizar y una
    cadena con la fórmula, incluyendo paréntesis (solo si son necesarios), en
    la que se realizarían las multiplicaciones.
    Por ejemplo '(M_1*(M_2*M_3))*M_4'.

    Args:
        dimensiones (List[int]): Lista de dimensiones de las matrices a multiplicar.

    Returns:
        tuple: Número de multiplicaciones y cadena con la fórmula de multiplicación.
    """
    n = len(dimensiones) - 1  # Número de matrices

    # Inicializar matrices para DP
    # M[i][j] = mínimo número de multiplicaciones para multiplicar matrices i a j
    # S[i][j] = posición del paréntesis para multiplicar matrices i a j
    M = [[0.0 for _ in range(n + 1)] for _ in range(n + 1)]
    S = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Calcular el costo mínimo para cada subcadena de matrices
    for longitud in range(2, n + 1):  # Longitud de la subcadena
        for i in range(1, n - longitud + 2):
            j = i + longitud - 1
            M[i][j] = float("inf")
            for k in range(i, j):
                # Costo = costo de multiplicar matrices i a k + costo de multiplicar matrices k+1 a j
                # + costo de multiplicar los dos resultados anteriores
                costo = (
                    M[i][k]
                    + M[k + 1][j]
                    + dimensiones[i - 1] * dimensiones[k] * dimensiones[j]
                )
                if costo < M[i][j]:
                    M[i][j] = costo
                    S[i][j] = k

    # Construir la fórmula parentizada
    def construir_formula(i, j):
        if i == j:
            return f"M_{i}"
        else:
            k = S[i][j]
            izquierda = construir_formula(i, k)
            derecha = construir_formula(k + 1, j)

            # Decidir si necesitamos paréntesis
            if i == k and k + 1 == j:  # Caso base: solo dos matrices
                return f"{izquierda}*{derecha}"
            elif i == k:  # Si la parte izquierda es una sola matriz
                return f"{izquierda}*({derecha})"
            elif k + 1 == j:  # Si la parte derecha es una sola matriz
                return f"({izquierda})*{derecha}"
            else:  # Ambas partes son complejas
                return f"({izquierda})*({derecha})"

    formula = construir_formula(1, n)

    return (M[1][n], formula)
