# # Algoritmia
# ## Práctica 11
# En esta práctica se resolverá los problemas NP forma normal conjuntiva y reducción a clique.

import networkx as nx

class FormaNormalConjuntiva:
    """
    Clase que representa una expresión en forma normal conjuntiva.
    Las cláusulas son secuencias con dos elementos, el primero contiene las
    variables que están sin negar, el segundo las que están negadas.
    """

    def __init__(self, *clausulas):
        """Constructor. Si se reciben cláusulas se añaden a la expresión."""
        
        pass

    def num_variables(self):
        """Devuelve el número de variables que aparecen en la expresión."""
        
        pass
        
    def __len__(self):
        """Devuelve el número de clausulas."""
        
        pass
        
    def inserta_clausulas(self, *clausulas):
        """Inserta cláusulas adicionales al final de la expresión."""
        
        pass

    def __getitem__(self, i):
        """Devuelve la cláusula i-ésima. Para la primera, i=0."""
        
        pass
                
    def evalua(self, ciertas):
        """
        Evalua la expresión, es decir, devuelve True o False, dada una
        asignación de valores a las variables. La asignación se indica con el
        iterable "ciertas" en el que están las variables que están a cierto.
        El resto de variables se entiende que están a falso.
        """
        
        pass

    def asignacion_satisfacible(self):       
        """
        Si la expresión es satisfacible, devuelve una asignación que hace
        la expresión cierta. La asignación se indica como un iterable de las
        variables que están a cierto, el resto de variables estarán a falso.
        Si la expresión no es satisfacible devuelve None.
        """
        
        pass
            
def reduccion_a_clique(fnc):
    """
    Dada una expresión en forma normal conjuntiva, devuelve el grafo 
    correspondiente a la reducción al problema del k-clique.
    Los nodos son cadenas con el formato "(i:l)", donde i es el número de
    clásula y l representa el literal. El literal es la variable, precedido por
    '!' si está negada.
    """
    
    pass