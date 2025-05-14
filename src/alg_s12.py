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
        self._clausulas = []
        self._variables = set()
        if clausulas:
            self.inserta_clausulas(*clausulas)

    def num_variables(self):
        """Devuelve el número de variables que aparecen en la expresión."""
        return len(self._variables)
        
    def __len__(self):
        """Devuelve el número de clausulas."""
        return len(self._clausulas)
        
    def inserta_clausulas(self, *clausulas):
        """Inserta cláusulas adicionales al final de la expresión."""
        for clausula in clausulas:
            self._clausulas.append(clausula)
            # Extraer variables de la cláusula (sin negar y negadas)
            for literal_list in clausula:
                for literal in literal_list:
                    # Para las variables negadas, quitamos el signo de negación
                    var = literal.replace('!', '')
                    self._variables.add(var)

    def __getitem__(self, i):
        """Devuelve la cláusula i-ésima. Para la primera, i=0."""
        return self._clausulas[i]
                
    def evalua(self, ciertas):
        """
        Evalua la expresión, es decir, devuelve True o False, dada una
        asignación de valores a las variables. La asignación se indica con el
        iterable "ciertas" en el que están las variables que están a cierto.
        El resto de variables se entiende que están a falso.
        """
        # Convertir el iterable a conjunto para búsqueda O(1)
        ciertas = set(ciertas)
        
        # Evaluamos cada cláusula
        for pos, neg in self._clausulas:
            # Una cláusula es verdadera si al menos un literal es verdadero
            # Un literal positivo es verdadero si la variable está en "ciertas"
            # Un literal negado es verdadero si la variable NO está en "ciertas"
            
            clausula_verdadera = False
            
            # Comprobar literales positivos
            for var in pos:
                if var in ciertas:
                    clausula_verdadera = True
                    break
                    
            # Si ya es verdadera, no necesitamos comprobar los negativos
            if clausula_verdadera:
                continue
                
            # Comprobar literales negativos
            for var in neg:
                if var not in ciertas:
                    clausula_verdadera = True
                    break
                    
            # Si alguna cláusula es falsa, toda la expresión es falsa
            if not clausula_verdadera:
                return False
                
        # Si todas las cláusulas son verdaderas, la expresión es verdadera
        return True
    
    def evalua_profesor(self, ciertas):
        """
        Evalua la expresión, es decir, devuelve True o False, dada una
        asignación de valores a las variables. La asignación se indica con el
        iterable "ciertas" en el que están las variables que están a cierto.
        El resto de variables se entiende que están a falso.
        """
        for cierta in self._clausulas:
            satisfecha = False
            for v in cierta[0]:
                if v in ciertas:
                    satisfecha = True
                    break
            if not satisfecha:
                for v in cierta[1]:
                    if v not in ciertas:
                        satisfecha = True
                        break
            if not satisfecha:
                return False
        return True

    def asignacion_satisfacible(self):       
        """
        Si la expresión es satisfacible, devuelve una asignación que hace
        la expresión cierta. La asignación se indica como un iterable de las
        variables que están a cierto, el resto de variables estarán a falso.
        Si la expresión no es satisfacible devuelve None.
        """
        variables = list(self._variables)
        n = len(variables)
        
        # Probamos todas las posibles combinaciones de asignaciones
        # 2^n posibilidades donde n es el número de variables
        for i in range(2**n):
            # Creamos una asignación basada en la representación binaria de i
            asignacion = []
            for j in range(n):
                if (i >> j) & 1:  # Si el j-ésimo bit está activo
                    asignacion.append(variables[j])
            
            # Evaluamos la expresión con esta asignación
            if self.evalua(asignacion):
                return asignacion
                
        # Si no encontramos ninguna asignación satisfacible
        return None
            
def reduccion_a_clique(fnc):
    """
    Dada una expresión en forma normal conjuntiva, devuelve el grafo 
    correspondiente a la reducción al problema del k-clique.
    Los nodos son cadenas con el formato "(i:l)", donde i es el número de
    clásula y l representa el literal. El literal es la variable, precedido por
    '!' si está negada.
    """
    g = nx.Graph()
    
    # Crear lista de nodos para cada cláusula
    nodos_por_clausula = []
    for i in range(len(fnc)):
        positivos, negativos = fnc[i]
        nodos = []
        
        # Añadir nodos para literales positivos
        for var in positivos:
            nodo = f"{i}:{var}"
            g.add_node(nodo)
            nodos.append((nodo, var, False))  # (nodo, variable, negado)
            
        # Añadir nodos para literales negativos
        for var in negativos:
            nodo = f"{i}:!{var}"
            g.add_node(nodo)
            nodos.append((nodo, var, True))   # (nodo, variable, negado)
            
        nodos_por_clausula.append(nodos)
        
    # Añadir aristas entre nodos de diferentes cláusulas si no son contradictorios
    for i in range(len(nodos_por_clausula)):
        for j in range(i+1, len(nodos_por_clausula)):
            for nodo_i, var_i, neg_i in nodos_por_clausula[i]:
                for nodo_j, var_j, neg_j in nodos_por_clausula[j]:
                    # No conectar si son literales contradictorios (misma variable, uno negado y otro no)
                    if not (var_i == var_j and neg_i != neg_j):
                        g.add_edge(nodo_i, nodo_j)
    
    return g