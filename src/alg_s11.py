# # Algoritmia
# ## Práctica 11
# En esta práctica se resolverá el problema de los árboles binarios de búsqueda.
 
class ArbolBusquedaOptimo:
    """
    Clase para árboles de búsquedas construidos a partir de las probabilidades
    de búsqueda de sus claves y pseudoclaves.
    Las pseudoclaves representan las búsquedas de elementos que no están en el
    árbol.
    """
    
    def __init__(self, claves, probab_claves, probab_pseudo = None):
        """
        Constructor a partir de una secuencia con las claves, sus probabilidades 
        y las probabilidades de buscar elementos que no están.
        La longitud de claves y probab_claves tiene que ser la misma.
        Si probab_pseudo es None no se tienen en cuentas las búsquedas de 
        elementos que no están.
        Si prabab_pseudo no es None, su longitud debe ser la de claves más 1.
        """
        pass

    def __str__(self, clave=None):
        """
        Devuelve una cadena con una representación del árbol.
        Si clave es distinto de None se obtiene la cadena para el subárbol con
        clave como raíz.
        La cadena correspondiente a un nodo con dos hijos es 
        "(" + str(subarbol_izq) + str(clave) + str(subarbol_der) + ")".
        Para un subárbol vacío la cadena correspondiente es vacía.
        Por ejemplo, un nodo hoja se representa como "(" + str(clave) + ")".
        """
        pass
    
    def __len__(self):
        """Número de claves en el árbol."""
        pass
        
    def __contains__(self, clave):
        """Indica si una clave está en el árbol."""
        pass
    
    def __getitem__(self, i):
        """Devuelve la clave i-ésima."""
        pass

    def raiz(self):
        """Devuelve la clave de la raíz del árbol.""" 
        pass
        
    def profundidad(self, clave=None):
        """
        Devuelve la profundidad del árbol si clave es None, si no devuelve la 
        profundidad de la clave. 
        Si la clave no está devuelve None.
        """
        pass


    def hijos(self, clave=None):
        """
        Devuelve un par con las claves del hijo izquierdo y derecho.
        Si el argumento clave es None devuelve los hijos de la raíz.
        En el resultado, None indica que no tiene ese hijo.
        """
        pass

    
    def coste_esperado(self, clave=None):
        """
        Devuelve el coste esperado de la búsqueda en el subárbol asociado a una
        clave.
        Si clave es None devuelve el coste del árbol completo.
        """
        pass