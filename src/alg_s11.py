# # Algoritmia
# ## Práctica 11
# En esta práctica se resolverá el problema de los árboles binarios de búsqueda.

from typing import Optional


class ArbolBusquedaOptimo:
    """
    Clase para árboles de búsquedas construidos a partir de las probabilidades
    de búsqueda de sus claves y pseudoclaves.
    Las pseudoclaves representan las búsquedas de elementos que no están en el
    árbol.
    """

    def __init__(
        self, claves: list, probab_claves: list, probab_pseudo: Optional[list] = None
    ):
        """
        Constructor a partir de una secuencia con las claves, sus probabilidades
        y las probabilidades de buscar elementos que no están.
        
        Args:
            claves (list): Claves del árbol.
            probab_claves (list): Probabilidades de búsqueda de las claves.
            probab_pseudo (Optional[list], optional): Probabilidades de las pseudoclaves. Defaults to None.
        Raises:
            ValueError: Si la longitud de claves y probab_claves no es la misma.
            ValueError: Si la longitud de probab_pseudo no es len(claves) + 1.
        """
        if len(claves) != len(probab_claves):
            raise ValueError("La longitud de claves y probab_claves debe ser la misma")
        
        # Si no se proporcionan probabilidades para las pseudoclaves, se asume 0
        if probab_pseudo is None:
            probab_pseudo = [0] * (len(claves) + 1)
        elif len(probab_pseudo) != len(claves) + 1:
            raise ValueError("La longitud de probab_pseudo debe ser len(claves) + 1")

        self.claves = claves
        self.probab_claves = probab_claves
        self.probab_pseudo = probab_pseudo
        
        # Construir matrices para la programación dinámica
        n = len(claves)
        
        # w[i][j] = suma de probabilidades de las claves i hasta j y pseudoclaves i hasta j+1
        self.w = [[0 for _ in range(n+1)] for _ in range(n+2)]
        
        # c[i][j] = coste mínimo del subárbol que contiene las claves i hasta j
        self.c = [[0.0 for _ in range(n+1)] for _ in range(n+2)]
        
        # r[i][j] = raíz del subárbol óptimo que contiene las claves i hasta j
        self.r = [[0 for _ in range(n+1)] for _ in range(n+2)]
        
        # Estructura del árbol: clave -> (hijo_izquierdo, hijo_derecho)
        self.estructura = {}
        
        # Profundidad de cada nodo en el árbol
        self.prof = {}
        
        # Costo esperado de cada subárbol
        self.costes = {}
        
        # Para simplificar los índices, usamos 1-indexación para las claves
        # Construimos el árbol
        if n > 0:
            self._construir_arbol_optimo()
            
            # Calcular profundidades
            self._calcular_profundidades(self.raiz(), 0)
            
            # Calcular costes esperados
            self._calcular_costes()

    def _construir_arbol_optimo(self) -> None:
        """
        Construye el árbol de búsqueda óptimo utilizando programación dinámica.
        Esta implementación sigue el algoritmo de Knuth para árboles de búsqueda óptimos.
        
        Returns:
            None
        """
        n = len(self.claves)
        
        # Inicializar los valores para los subárboles vacíos: sólo pseudoclaves
        for i in range(1, n + 2):
            self.w[i][i-1] = self.probab_pseudo[i-1]
            self.c[i][i-1] = self.probab_pseudo[i-1]  # El coste incluye la pseudoclave
        
        # Construir subárboles de tamaño creciente
        for distancia in range(1, n + 1):
            for i in range(1, n - distancia + 2):
                j = i + distancia - 1
                
                # Calcular el peso total del subárbol
                self.w[i][j] = self.w[i][j-1] + self.probab_claves[j-1] + self.probab_pseudo[j]
                
                # Inicializar con valor infinito
                self.c[i][j] = float('inf')
                
                # Encontrar la raíz óptima probando cada clave como raíz
                for k in range(i, j + 1):
                    t = self.c[i][k-1] + self.c[k+1][j] + self.w[i][j]
                    
                    if t < self.c[i][j]:
                        self.c[i][j] = t
                        self.r[i][j] = k
        
        # Construir la estructura del árbol
        self._construir_estructura(1, n)

    def _construir_estructura(self, i: int, j: int) -> Optional[str]:
        """
        Construye recursivamente la estructura del árbol a partir de la matriz r.
        
        Args:
            i (int): Índice inicial de claves.
            j (int): Índice final de claves.
        Returns:
            Optional[str]: Clave de la raíz del subárbol construido.
        """
        if i > j:
            return None
        
        k = self.r[i][j]
        
        # La clave en la posición k-1 será la raíz de este subárbol
        clave = self.claves[k-1]
        
        # Construir subárboles izquierdo y derecho
        izq = self._construir_estructura(i, k-1)
        der = self._construir_estructura(k+1, j)
        
        # Guardar estructura
        self.estructura[clave] = (izq, der)
        
        return clave
    
    def _calcular_profundidades(self, clave: Optional[str], nivel: int) -> None:
        """
        Calcula la profundidad de cada nodo en el árbol.
        
        Args:
            clave (Optional[str]): Clave del nodo actual.
            nivel (int): Nivel de profundidad actual.
        Returns:
            None
        """
        if clave is None:
            return
        
        self.prof[clave] = nivel
        
        # Procesar hijos
        if clave in self.estructura:
            izq, der = self.estructura[clave]
            self._calcular_profundidades(izq, nivel + 1)
            self._calcular_profundidades(der, nivel + 1)
    
    def _calcular_costes(self) -> None:
        """
        Calcula los costes esperados para cada subárbol.
        
        Returns:
            None
        """
        n = len(self.claves)
        
        # Para cada clave, encontrar su posición i,j en la matriz r
        for clave in self.claves:
            idx = self.claves.index(clave) + 1  # 1-indexado
            
            # Buscar el rango donde esta clave es la raíz
            for i in range(1, n+1):
                for j in range(i, n+1):
                    if self.r[i][j] == idx:
                        self.costes[clave] = self.c[i][j]
                        break

    def __len__(self) -> int:
        """
        Número de claves en el árbol.
        
        Returns:
            int: Número de claves.
        """
        return len(self.claves)

    def __iter__(self):
        """
        Iterador sobre las claves del árbol.
        
        Returns:
            Iterator: Iterador de claves.
        """
        return iter(self.claves)

    def __contains__(self, clave: str) -> bool:
        """
        Indica si una clave está en el árbol.
        
        Args:
            clave (str): Clave a comprobar.
        Returns:
            bool: True si la clave está en el árbol, False en caso contrario.
        """
        return clave in self.claves

    def __getitem__(self, i: int) -> str:
        """
        Devuelve la clave i-ésima.
        
        Args:
            i (int): Índice de la clave.
        Returns:
            str: Clave correspondiente al índice.
        """
        return self.claves[i]

    def raiz(self) -> Optional[str]:
        """
        Devuelve la clave de la raíz del árbol.
        
        Returns:
            Optional[str]: Clave de la raíz o None si el árbol está vacío.
        """
        n = len(self.claves)
        if n == 0:
            return None
        
        idx = self.r[1][n]
        return self.claves[idx-1] if idx > 0 else None

    def profundidad(self, clave: Optional[str] = None) -> Optional[int]:
        """
        Devuelve la profundidad del árbol si clave es None, si no devuelve la
        profundidad de la clave. Si la clave no está devuelve None.
        
        Args:
            clave (Optional[str], optional): Clave a consultar. Defaults to None.
        Returns:
            Optional[int]: Profundidad del árbol o de la clave.
        """
        if clave is None:
            return max(self.prof.values()) if self.prof else 0
        
        return self.prof.get(clave, None)

    def hijos(self, clave: Optional[str] = None) -> tuple:
        """
        Devuelve un par con las claves del hijo izquierdo y derecho.
        Si el argumento clave es None devuelve los hijos de la raíz.
        En el resultado, None indica que no tiene ese hijo.
        
        Args:
            clave (Optional[str], optional): Clave a consultar. Defaults to None.
        Returns:
            tuple: (hijo_izquierdo, hijo_derecho)
        """
        if clave is None:
            clave = self.raiz()
        
        return self.estructura.get(clave, (None, None))

    def coste_esperado(self, clave: Optional[str] = None) -> float:
        """
        Devuelve el coste esperado de la búsqueda en el subárbol asociado a una
        clave. Si clave es None devuelve el coste del árbol completo.
        
        Args:
            clave (Optional[str], optional): Clave a consultar. Defaults to None.
        Returns:
            float: Coste esperado del subárbol o del árbol completo.
        """
        n = len(self.claves)
        
        # Para otros casos, usar el cálculo estándar
        if clave is None:
            return self.c[1][n] if n > 0 else 0
        
        if clave in self.costes:
            return self.costes[clave]
        
        # Si no está en costes pero está en el árbol, probablemente es una hoja
        idx = self.claves.index(clave) + 1
        
        # Para una hoja, el costo es la suma de su probabilidad y las pseudoclaves adyacentes
        return (self.probab_claves[idx-1] + 
                self.probab_pseudo[idx-1] + 
                self.probab_pseudo[idx])

    def __str__(self) -> str:
        """
        Devuelve una cadena con una representación del árbol.
        
        Returns:
            str: Representación del árbol.
        """
        def _str_rec(clave):
            if clave is None:
                return ""
            
            izq, der = self.estructura.get(clave, (None, None))
            
            resultado = "("
            if izq:
                resultado += _str_rec(izq)
            resultado += clave
            if der:
                resultado += _str_rec(der)
            resultado += ")"
            
            return resultado
        
        return _str_rec(self.raiz())