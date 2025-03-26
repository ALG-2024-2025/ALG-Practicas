import time
import random
import heapq

# # Algoritmia
# ## Práctica 5

# En esta práctica se implementan las estructuras unión pertenencia y el algoritmo de Kruskal.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

union_pertenecia_ejemplo = """
# Ejemplo de uso de la estructura de unión-pertenencia
# 
# Creamos una partición con los elementos 0, 1, 2, 3, 4
# 
"""
# particion = Particion([0, 1, 2, 3, 4])
# print(len(particion))  # 5

disjuntos_ejemplo = """
# Ejemplo de uso de la estructura de unión-pertenencia
#
# Creamos una partición con los elementos 0, 1, 2, 3, 4
#
# Añadimos los elementos 5, 6, 7, 8, 9
#
# Unimos los elementos 0 y 1
#
# Unimos los elementos 2 y 3
"""

# particion = Particion([0, 1, 2, 3, 4])
# print(len(particion))  # 5
# particion = Particion([5, 6, 7, 8, 9])
# print(len(particion))  # 5
# particion.une(0, 1)
# particion.une(2, 3) # 3

class Particion:
    """
    Clase que implementa una partición de un conjunto en subconjuntos disjuntos.
    Una partición se corresponde con una estructura Unión-Pertenencia.
    """

    def __init__(self, iterable: iter):
        """Crea una partición con los elementos del iterable.
        Inicialmente cada elemento forma un subconjunto.

        Args:
            iterable (iter): Elementos iniciales.
        """
        self.padres = {x: x for x in iterable}  # Cada elemento es su propio padre
        self.tamanos = {x: 1 for x in iterable}  # Tamaño de cada subconjunto
        self.num_conjuntos = len(self.padres)
        self.total_elementos = len(self.padres)

    def __init__profesor(self, iterable: iter):
        """Crea una partición con los elementos del iterable.
        Inicialmente cada elemento forma un subconjunto.

        Args:
            iterable (iter): Elementos iniciales.
        """
        self.clase = {}
        self.altura = {}
        self.subconjuntos = 0
        for x in iterable:
            self.clase[x] = x
            self.altura[x] = 1
            self.subconjuntos += 1
            

    def __len__(self):
        """Devuelve el número de subconjuntos en la partición."""
        return self.num_conjuntos

    def numero(self, k: int = None) -> int:
        """Devuelve el número de elementos del subconjunto al que pertenece el 
        elemento k. 
        Si k es None devuelve el número   de elementos.

        Args:
            k (int, optional): Elemento a buscar. Defaults to None.

        Returns:
            int: Número de elementos del subconjunto.
        """
        if k is None:
            return self.total_elementos
        return self.tamanos[self.__getitem__(k)]
        

    def __getitem__(self, k: int) -> int:
        """Devuelve el subconjunto al que pertenece el elemento k.
        El subconjunto se identifica mediante uno de sus elementos.

        Args:
            k (int): Elemento a buscar.

        Returns:
            int: Elemento representante del subconjunto.
        """
        if self.padres[k] != k:
            self.padres[k] = self.__getitem__(self.padres[k])
        return self.padres[k]


    def __iter__(self) -> iter:
        """Devuelve un iterador sobre los subconjuntos.
        Cada subconjunto se identifica mediante uno de sus elementos.

        Returns:
            iter: Objeto iterable.

        Yields:
            Iterator[iter]: Iterador sobre los subconjuntos.
        """
        representantes = set()
        for elemento in self.padres:
            representante = self.__getitem__(elemento)
            if representante not in representantes:
                representantes.add(representante)
                yield representante
    
    def une(self, a: int, b: int):
        """Une los subconjuntos a los que pertencen a y b.

        Args:
            a (int): Valor de un elemento.
            b (int): Valor de un elemento.
        """
        raiz_a = self.__getitem__(a)
        raiz_b = self.__getitem__(b)
        
        if raiz_a == raiz_b:
            return
            
        # Unión por tamaño
        if self.tamanos[raiz_a] < self.tamanos[raiz_b]:
            self.padres[raiz_a] = raiz_b
            self.tamanos[raiz_b] += self.tamanos[raiz_a]
        else:
            self.padres[raiz_b] = raiz_a
            self.tamanos[raiz_a] += self.tamanos[raiz_b]
            
        self.num_conjuntos -= 1

    def une_profesor(self, a: int, b: int):
        """Une los subconjuntos a los que pertencen a y b.

        Args:
            a (int): Valor de un elemento.
            b (int): Valor de un elemento.
        """
        a = self[a]
        b = self[b]

        if a == b:
            return
        
        self.subconjuntos -= 1
        if self.altura[a] == self.altura[b]:
            self.altura[a] += 1
        if self.altura[a] < self.altura[b]:
            a, b = b, a
        else:
            self.clase[a] = b

# Sugerencia: Implementar con las diveras técncias de unión-pertenencia vistas en clase y probar los tiempos de ejecución.

# Hacer con montículo

def kruskal(grafo: dict) -> dict:
    """Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.

    Args:
        grafo (dict): Grafo en formato de diccionario.

    Returns:
        dict: Árbol de expansión mínima en formato de diccionario.

    Complexity:
        O(n log n)
    """
    # Ordenamos los arcos por peso
    arcos_ordenados = sorted(grafo.items(), key=lambda item: item[1])
    
    # Obtenemos todos los nodos del grafo
    nodos = set()
    for u, v in grafo.keys():
        nodos.add(u)
        nodos.add(v)
    
    # Inicializamos la partición
    particion = Particion(nodos)
    
    # Árbol de expansión mínimo
    arbol = {}
    
    # Procesamos los arcos en orden de peso creciente
    for (u, v), peso in arcos_ordenados:
        # Si los nodos están en diferentes componentes
        if particion[u] != particion[v]:
            # Añadimos el arco al árbol
            arbol[(u, v)] = peso
            # Unimos las componentes
            particion.une(u, v)
    
    return arbol

def kruskal_monticulo(grafo: dict) -> dict:
    """Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.

    Args:
        grafo (dict): Grafo en formato de diccionario.

    Returns:
        dict: Árbol de expansión mínima en formato de diccionario.

    Complexity:
        O(n log n)
    """
    # Crear montículo con los arcos y sus pesos
    arcos_heap = [(peso, u, v) for (u, v), peso in grafo.items()]
    heapq.heapify(arcos_heap)
    
    # Obtenemos todos los nodos del grafo
    nodos = set()
    for u, v in grafo.keys():
        nodos.add(u)
        nodos.add(v)
    
    # Inicializamos la partición
    particion = Particion(nodos)
    
    # Árbol de expansión mínimo
    arbol = {}
    
    # Procesamos los arcos en orden de peso creciente usando el montículo
    while arcos_heap:
        peso, u, v = heapq.heappop(arcos_heap)
        # Si los nodos están en diferentes componentes
        if particion[u] != particion[v]:
            # Añadimos el arco al árbol
            arbol[(u, v)] = peso
            # Unimos las componentes
            particion.une(u, v)
    
    return arbol

def kruskal_profesor(grafo: dict) -> dict:
    """Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.

    Args:
        grafo (dict): Grafo en formato de diccionario.

    Returns:
        dict: Árbol de expansión mínima en formato de diccionario.
    """
    
    nodos = set()
    resultados = list()
    for y in grafo:
        peso = grafo[y]
        resultados.append((y, peso))
        nodos = nodos.union(set(y))

    candidatos = sorted(resultados, key=lambda x: x[1])
    particion = Particion(nodos)
    arbol = dict()
    for y, peso in candidatos:
        u, v = y
        if particion[u] != particion[v]:
            arbol[y] = peso
            particion.une(u, v)

    return arbol

# Sugerencia: Prueba a implementar Kruskal para un grafo que esté en formato de matriz de adyacencia.

def prim(grafo: dict) -> dict:
    """Implementación del algoritmo de Prim para encontrar el árbol de expansión mínima.
    Los grafos son diccionarios donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.

    Args:
        grafo (dict): Grafo en formato de diccionario.

    Returns:
        dict: Árbol de expansión mínima en formato de diccionario.

    Complexity:
        O(n log n)
    """
    
    # Extraer todos los nodos del grafo
    nodos = set()
    for u, v in grafo.keys():
        nodos.add(u)
        nodos.add(v)
    
    if not nodos:
        return {}
    
    # Convertir el grafo a formato de listas de adyacencia
    adyacencia = {nodo: [] for nodo in nodos}
    for (u, v), peso in grafo.items():
        adyacencia[u].append((v, peso))
        adyacencia[v].append((u, peso))  # Para grafos no dirigidos
    
    # Elegimos un nodo arbitrario para comenzar
    inicio = next(iter(nodos))
    visitados = {inicio}
    arbol = {}
    
    # Cola de prioridad para los arcos fronteras (peso, nodo_destino, nodo_origen)
    arcos_frontera = [(peso, v, inicio) for v, peso in adyacencia[inicio]]
    heapq.heapify(arcos_frontera)
    
    while arcos_frontera and len(visitados) < len(nodos):
        peso, destino, origen = heapq.heappop(arcos_frontera)
        
        if destino in visitados:
            continue
        
        # Añadimos el nodo al conjunto de visitados
        visitados.add(destino)
        
        # Añadimos el arco al árbol (manteniendo el orden original de los nodos)
        if (origen, destino) in grafo:
            arbol[(origen, destino)] = peso
        else:
            arbol[(destino, origen)] = peso
        
        # Añadimos los arcos frontera desde el nuevo nodo
        for vecino, peso_vecino in adyacencia[destino]:
            if vecino not in visitados:
                heapq.heappush(arcos_frontera, (peso_vecino, vecino, destino))
    
    return arbol

# Sugerencia: Compara los tiempos de ejecución del algoritmo de Kruskal con los del algormitmo de Prim.

def comparar_tiempos(num_nodos_lista: list = [10, 50, 100, 500, 1000], repeticiones: int = 10):
    """
    Compara los tiempos de ejecución de los algoritmos de Kruskal y Prim.
    
    Args:
        num_nodos_lista: Lista con los diferentes tamaños de grafos a probar.
        repeticiones: Número de grafos aleatorios a generar para cada tamaño.
    """
    print(f"{'Nodos':<10}{'Kruskal (ms)':<15}{'Prim (ms)':<15}")
    print("-" * 40)
    
    for num_nodos in num_nodos_lista:
        tiempo_kruskal_total = 0
        tiempo_prim_total = 0
        
        for _ in range(repeticiones):
            # Crear un grafo completo aleatorio
            grafo = {}
            for i in range(num_nodos):
                for j in range(i+1, num_nodos):
                    peso = random.randint(1, 100)
                    grafo[(i, j)] = peso
            
            # Medir tiempo de Kruskal
            inicio = time.time()
            kruskal(grafo)
            fin = time.time()
            tiempo_kruskal_total += (fin - inicio) * 1000  # ms
            
            # Medir tiempo de Prim
            inicio = time.time()
            prim(grafo)
            fin = time.time()
            tiempo_prim_total += (fin - inicio) * 1000  # ms
        
        tiempo_kruskal_promedio = tiempo_kruskal_total / repeticiones
        tiempo_prim_promedio = tiempo_prim_total / repeticiones
        
        print(f"{num_nodos:<10}{tiempo_kruskal_promedio:<15.2f}{tiempo_prim_promedio:<15.2f}")

# Para ejecutar la comparación de tiempos, descomentar la siguiente línea:
comparar_tiempos()