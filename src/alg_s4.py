# # Algoritmia
# ## Práctica 4

# El objetivo de esta práctica es trabajar con grafos.
# Se pide la implementación de las funciones que aparecen a continuación.

# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# El grafo se puede representar como un diccionario de diccionarios o como una matriz de adyacencia.
# Para esta práctica se usará la representación de diccionario de diccionarios.

# NOTA: Los grafos son dirigidos y pesados.

import heapq
from typing import Optional


grafo_de_ejemplo: dict[str, dict[str, int]] = {
    "a": {"b": 1, "c": 2},
    "b": {"a": 3, "d": 6},
    "c": {"a": 5, "b": 2},
    "d": {},
}


# Funciones genéricas de grafos
def numero_nodos(grafo: dict) -> int:
    """Número de nodos en el grafo.

    Args:
        grafo (dict): Grafo

    Returns:
        int: Número de nodos
    """
    return len(grafo)


def numero_arcos(grafo: dict) -> int:
    """Número de arcos en el grafo.

    Args:
        grafo (dict): Grafo

    Returns:
        int: Número de arcos
    """
    total = 0
    for nodo in grafo:
        total += len(grafo[nodo])
    return total

    # return sum(len(grafo[nodo]) for nodo in grafo)


def peso_total(grafo: dict) -> int:
    """Suma de los pesos de los arcos del grafo.

    Args:
        grafo (dict): Grafo

    Returns:
        int: Suma de los pesos
    """
    total = 0
    for nodo in grafo:
        for destino in grafo[nodo]:
            total += grafo[nodo][destino]
    return total


def peso_total_profesor(grafo: dict) -> int:
    """Suma de los pesos de los arcos del grafo.

    Args:
        grafo (dict): Grafo

    Returns:
        int: Suma de los pesos
    """
    adj = 0
    for _, vecinos in grafo.items():
        adj += sum(vecinos.values())
    return adj


def arco(grafo: dict, origen: str, destino: str) -> Optional[int]:
    """Si hay un arco de origen a destino, devuelve su peso.
    Si no hay, devuelve None.

    Args:
        grafo (dict): Grafo
        origen (str): Origen del arco
        destino (str): Destino del arco

    Returns:
        Optional[int]: Peso del arco o None si no existe
    """
    if origen in grafo and destino in grafo[origen]:
        return grafo[origen][destino]
    return None

    # return grafo.get(origen, {}).get(destino, None)


# Operaciones de modificación


def inserta_nodo(grafo: dict, nodo: str) -> dict:
    """Inserta el nodo en el grafo.
    Si ya estaba, no se modifica.
    Devuelve el propio grafo.

    Args:
        grafo (dict): Grafo
        nodo (str): Nodo a insertar

    Returns:
        dict: Grafo
    """
    grafo.setdefault(nodo, {})
    return grafo


def inserta_nodo_profesor(grafo: dict, nodo: str) -> dict:
    """Inserta el nodo en el grafo.
    Si ya estaba, no se modifica.
    Devuelve el propio grafo.

    Args:
        grafo (dict): Grafo
        nodo (str): Nodo a insertar

    Returns:
        dict: Grafo
    """
    if nodo not in grafo:
        grafo[nodo] = {}
    return grafo


def inserta_arco(grafo: dict, origen: str, destino: str, peso: int = 1) -> dict:
    """Inserta el arco en el grafo.
    Si ya estaba se actualiza el peso.
    Devuelve el propio grafo.

    Args:
        grafo (dict): Grafo
        origen (str): Origen del arco
        destino (str): Destino del arco
        peso (int, optional): Peso del arco. Defaults to 1.

    Returns:
        dict: Grafo
    """
    grafo = inserta_nodo(grafo, origen)
    grafo = inserta_nodo(grafo, destino)
    grafo[origen][destino] = peso
    return grafo


# Operaciones de consulta
def grado(grafo: dict, nodo: str, salida: bool = True) -> int:
    """Devuelve el grado de salida o entrada de un nodo del grafo.
    Estos grados son el número de arcos que salen o llegan al nodo.

    Args:
        grafo (dict): Grafo
        nodo (str): Nodo
        salida (bool, optional): Salida del nodo. Defaults to True. Si es False, se refiere a la entrada.

    Returns:
        int: Grado
    """
    if salida:
        return len(grafo[nodo]) if nodo in grafo else 0

    # Grado de entrada
    count = 0
    for origen in grafo:
        if nodo in grafo[origen]:
            count += 1
    return count

    # return sum(1 for origen in grafo if nodo in grafo[origen])


def pesos_adyacentes(grafo: dict, nodo: str, salida: bool = True) -> int:
    """Devuelve la suma de los pesos de los arcos adyacentes al nodo,
    de salida o entrada.

    Args:
        grafo (dict): Grafo
        nodo (str): Nodo
        salida (bool, optional): Salida del nodo. Defaults to True. Si es False, se refiere a la entrada.

    Returns:
        int: Suma de pesos
    """
    if salida:
        return sum(grafo[nodo].values()) if nodo in grafo else 0

    # Suma de pesos de arcos de entrada
    total = 0
    for origen in grafo:
        if nodo in grafo[origen]:
            total += grafo[origen][nodo]
    return total

    # return sum(grafo[origen][nodo] for origen in grafo.values()


def coste_camino(grafo: dict, camino: list[str]) -> Optional[int]:
    """Devuelve el coste del camino en el grafo.
    El camino viene dado como una secuencia de nodos.
    Si esa secuencia no forma un camino, devuelve None.

    Args:
        grafo (dict): Grafo
        camino (list[str]): Recorrido de nodos

    Returns:
        int: Coste del camino
    """
    if len(camino) <= 1:
        return 0

    coste = 0
    for i in range(len(camino) - 1):
        origen = camino[i]
        destino = camino[i + 1]
        peso = arco(grafo, origen, destino)
        if peso is None:
            return None
        coste += peso
    return coste


def coste_camino_profesor(grafo: dict, camino: list[str]) -> Optional[int]:
    """Devuelve el coste del camino en el grafo.
    El camino viene dado como una secuencia de nodos.
    Si esa secuencia no forma un camino, devuelve None.

    Args:
        grafo (dict): Grafo
        camino (list[str]): Recorrido de nodos

    Returns:
        int: Coste del camino
    """
    coste = 0
    for i in range(len(camino) - 1):
        if camino[i + 1] not in grafo.get(camino[i], {}):
            return None
        coste += grafo[camino[i]][camino[i + 1]]
    return coste


###################
# Habiendo creado las funciones anteriores, se pide implementar los siguientes métodos:


def prim(grafo: dict, inicial: Optional[str] = None) -> dict:
    """Implementa el algoritmo de Prim para obtener el árbol de expansión mínima de un grafo usando colas de prioridad.
    Devuelve en el formato del grafo el árbol.

    Se recuerda que un árbol es un grafo sin bucles y conectado.

    El grafo que se va a recibir siempre será conexo y sin direcciones.

    Args:
        grafo (dict): Grafo
        inicial (str, optional): Nodo inicial. Defaults to None.

    Returns:
        dict: Árbol de expansión mínima

    Complexity:
        O(n log n)
    """
    # Si no se proporciona nodo inicial, tomar el primero
    if inicial is None:
        inicial = list(grafo.keys())[0]

    # Crear árbol vacío
    arbol = {nodo: {} for nodo in grafo}

    # Conjunto de nodos visitados
    visitados = {inicial}

    # Repetir hasta que todos los nodos estén en el árbol
    while len(visitados) < len(grafo):
        arco_minimo = (None, None, float("inf"))  # (origen, destino, peso)

        # Buscar el arco de menor peso entre visitados y no visitados
        for nodo in visitados:
            for vecino, peso in grafo[nodo].items():
                if vecino not in visitados and peso < arco_minimo[2]:
                    arco_minimo = (nodo, vecino, peso)

        # Añadir el arco mínimo al árbol
        origen, destino, peso = arco_minimo
        arbol[origen][destino] = peso
        arbol[destino][origen] = peso  # Ya que es un grafo no dirigido

        # Añadir el nuevo nodo a visitados
        visitados.add(destino)

    return arbol


def prim_profesor(grafo: dict, inicial: Optional[str] = None) -> dict:
    """Implementa el algoritmo de Prim para obtener el árbol de expansión mínima de un grafo. Devuelve en el formato del grafo el árbol.

    Se recuerda que un árbol es un grafo sin bucles y conectado.

    El grafo que se va a recibir siempre será conexo y sin direcciones.

    Args:
        grafo (dict): Grafo
        inicial (str, optional): Nodo inicial. Defaults to None.

    Returns:
        dict: Árbol de expansión mínima
    """
    # Si no se proporciona nodo inicial, tomar el primero
    if inicial is None:
        inicial = list(grafo.keys())[0]

    arbol = {x: dict() for x in grafo.keys()}
    vistos = set()
    candidatos: dict[str, tuple[Optional[str], float]] = {
        x: (None, float("inf")) for x in grafo.keys()
    }
    vistos.add(inicial)

    while len(vistos) < len(grafo):
        for adyacente, peso in grafo[inicial].items():
            if adyacente not in vistos and peso < candidatos[adyacente][1]:
                candidatos[adyacente] = (inicial, float(peso))

        mejor = min(candidatos, key=lambda x: candidatos[x][1])
        arbol[mejor][candidatos[mejor][0]] = candidatos[mejor][1]
        arbol[candidatos[mejor][0]][mejor] = candidatos[mejor][1]
        nodo = mejor
        vistos.add(nodo)
        candidatos.pop(nodo)

    return arbol


def dijkstra(grafo: dict, inicial: str) -> dict:
    """Implementa el algoritmo de Dijkstra
    Devuelve un diccionario con la distancia mínima desde el nodo inicial a cada uno de los nodos del grafo.

    Args:
        grafo (dict): Grafo
        inicial (str): Nodo inicial

    Returns:
        dict: Distancias mínimas

    Complexity:
        O(n^2)
    """
    # Inicializar distancias y predecesores
    distancias = {nodo: (None, float("inf")) for nodo in grafo}
    distancias[inicial] = (None, 0)

    # Conjunto de nodos no visitados
    no_visitados = set(grafo.keys())

    while no_visitados:
        # Encontrar el nodo no visitado con la menor distancia
        nodo_actual = min(no_visitados, key=lambda x: distancias[x][1])

        # Si la distancia es infinito, no hay más caminos posibles
        if distancias[nodo_actual][1] == float("inf"):
            break

        # Eliminar el nodo actual de no_visitados
        no_visitados.remove(nodo_actual)

        # Actualizar las distancias de los nodos adyacentes
        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancias[nodo_actual][1] + peso

            if nueva_distancia < distancias[vecino][1]:
                distancias[vecino] = (nodo_actual, nueva_distancia)

    return distancias


def dijkstra_profesor(grafo: dict, inicial: str) -> dict:
    """Implementa el algoritmo de Dijkstra
    Devuelve un diccionario con la distancia mínima desde el nodo inicial a cada uno de los nodos del grafo.

    Args:
        grafo (dict): Grafo
        inicial (str): Nodo inicial

    Returns:
        dict: Distancias mínimas
    """
    # Inicializar distancias y predecesores
    distancias: dict[str, tuple[Optional[str], float]] = {
        nodo: (None, float("inf")) for nodo in grafo.keys()
    }
    padre: dict[str, Optional[str]] = {x: None for x in grafo.keys()}
    visto = set()

    distancias[inicial] = (None, 0)
    cola = [(0, inicial)]
    heapq.heappush(cola, (0, inicial))

    while cola:
        _, nodo = heapq.heappop(cola)
        if nodo in visto:
            continue
        visto.add(nodo)

        for adyacente, peso in grafo[nodo].items():
            if adyacente not in visto:
                nueva_distancia = distancias[nodo][1] + peso
                if nueva_distancia < distancias[adyacente][1]:
                    distancias[adyacente] = (nodo, nueva_distancia)
                    heapq.heappush(cola, (nueva_distancia, adyacente))

    return {x: (padre[x], distancias[x][1]) for x in grafo.keys()}


def obten_camino_minimo(
    inicial: str, final: str, caminos_pre_calculados: dict
) -> Optional[list[str]]:
    """Devuelve el camino mínimo entre dos nodos, a partir de la información obtenida con Dijkstra.
    Si no hay camino, devuelve None.

    Args:
        inicial (str): Nodo inicial
        final (str): Nodo final
        caminos_pre_calculados (dict): Resultado de Dijkstra

    Raises:
        Exception: Los nodos iniciales o finales no están en el grafo
        Exception: El nodo inicial no es el nodo fuente de los caminos pre-calculados

    Returns:
        list[str]: Camino mínimo

    Complexity:
        O(n log n)
    """
    if inicial not in caminos_pre_calculados or final not in caminos_pre_calculados:
        raise Exception("Los nodos iniciales o finales no están en el grafo")

    # Verificar que el nodo inicial sea el nodo fuente de los caminos pre-calculados
    # El nodo fuente es el único que tiene None como predecesor y distancia 0
    if not (
        caminos_pre_calculados[inicial][0] is None
        and caminos_pre_calculados[inicial][1] == 0
    ):
        raise Exception(
            "El nodo inicial no es el nodo fuente de los caminos pre-calculados"
        )

    if caminos_pre_calculados[final][1] == float("inf"):
        return None

    # Reconstruir el camino desde el final hasta el inicio
    camino = [final]
    nodo_actual = final

    while nodo_actual != inicial:
        predecesor = caminos_pre_calculados[nodo_actual][0]
        if predecesor is None:
            # Si el predecesor es None y no hemos llegado al inicial, no hay camino
            if nodo_actual != inicial:
                return None
            break
        camino.append(predecesor)
        nodo_actual = predecesor

    # Invertir el camino para que vaya del inicio al final
    return list(reversed(camino))
