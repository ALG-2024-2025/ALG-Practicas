# # Algoritmia
# ## Práctica 7
# En esta práctica se resolverá el problema de subvector de suma máxima.

# Definición del problema:
# - Se tiene un vector de números, positivos y negativos.
# - Se debe encontrar el valor máximo que se puede obtener sumando los elementos de un subvector contiguo del vector dado.
# # Aproximación por fuerza bruta:
# # - Se consideran todos los subvectores posibles.
# # - Se calcula la suma de cada uno de ellos.
# # - Se devuelve la mayor suma obtenida.
# # Aproximación Divide y Vencerás:
# # - Se divide el vector en dos mitades.
# # - Se calcula la suma máxima de un subvector que está en la primera mitad.
# # - Se calcula la suma máxima de un subvector que está en la segunda mitad.
# # - Se calcula la suma máxima de un subvector que pasa por el medio.
# # - Se devuelve la mayor de las tres sumas anteriores.
# # - La suma máxima de un subvector que pasa por el medio se calcula sumando los elementos desde la mitad hacia la izquierda y desde la mitad hacia la derecha.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.


def subvector_suma_maxima_fuerza_bruta(vector):
    """
    Devuelve la suma máxima de un subvector contiguo del vector dado.
    
    Aproximación por fuerza bruta.
    """
    pass

def subvector_suma_maxima_divide_y_venceras(vector):
    """
    Devuelve la suma máxima de un subvector contiguo del vector dado.
    
    Aproximación Divide y Vencerás.
    """
    pass


# Sugerencia: analiza el tiempo de ejecución de cada una de las funciones anteriores.

# Sugerencia: crea una versión de estos algoritmos que además devuelva los índices del subvector de suma máxima.