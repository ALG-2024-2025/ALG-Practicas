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

import random
import time


def subvector_suma_maxima_fuerza_bruta(vector: list) -> int:
    """Devuelve la suma máxima de un subvector contiguo del vector dado.

    Aproximación por fuerza bruta.

    Args:
        vector (list): Vector de números enteros (positivos y negativos).

    Returns:
        int: Suma máxima de un subvector contiguo.

    Complexity:
        O(n^2)
    """
    n = len(vector)
    if n == 0:
        return 0
    
    max_suma = vector[0]
    
    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += vector[j]
            max_suma = max(max_suma, suma_actual)
    
    return max_suma

def subvector_suma_maxima_fuerza_bruta_with_index(vector: list) -> tuple:
    """Devuelve la suma máxima de un subvector contiguo del vector dado.

    Aproximación por fuerza bruta.

    Args:
        vector (list): Vector de números enteros (positivos y negativos).

    Returns:
        tuple: Suma máxima de un subvector contiguo y los índices del subvector.

    Complexity:
        O(n^2)
    """
    n = len(vector)
    if n == 0:
        return 0, (-1, -1)
    
    max_suma = vector[0]
    start_index = 0
    end_index = 0
    
    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += vector[j]
            if suma_actual > max_suma:
                max_suma = suma_actual
                start_index = i
                end_index = j
    
    return max_suma, (start_index, end_index)

def subvector_suma_maxima_profesor(vector: list) -> int:
    """Devuelve la suma máxima de un subvector contiguo del vector dado.

    Aproximación por fuerza bruta.

    Args:
        vector (list): Vector de números enteros (positivos y negativos).

    Returns:
        int: Suma máxima de un subvector contiguo.

    Complexity:
        O(n^2)
    """
    max_sum = float('-inf')
    n = len(vector)
    # Opción 1
    for i in range(n):
        acum = 0
        for j in range(i, n):
            acum += vector[j]
            max_sum = max(max_sum, acum)
            
    # Opción 2
    for i in range(n):
        for j in range(i, n):
            suma = sum(vector[i : j + 1])
            max_sum = max(max_sum, suma)

    return max_sum 

def subvector_suma_maxima_divide_y_venceras(vector: list) -> int:
    """Devuelve la suma máxima de un subvector contiguo del vector dado.
    
    Aproximación Divide y Vencerás.

    Args:
        vector (list): Vector de números enteros (positivos y negativos).

    Returns:
        int: Suma máxima de un subvector contiguo.

    Complexity:
        O(n log n)
    """
    def max_crossing_subarray(arr: list, low: int, mid: int, high: int) -> int:
        """Devuelve la suma máxima de un subvector que pasa por el medio.

        Args:
            arr (list): Vector de números enteros (positivos y negativos).
            low (int): Índice bajo del subvector.
            mid (int): Índice medio del subvector.
            high (int): Índice alto del subvector.

        Returns:
            int: Suma máxima de un subvector que pasa por el medio.
        """
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, low - 1, -1):
            curr_sum += arr[i]
            left_sum = max(left_sum, curr_sum)

        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, high + 1):
            curr_sum += arr[i]
            right_sum = max(right_sum, curr_sum)

        return left_sum + right_sum

    def max_subarray(arr: list, low: int, high: int) -> int:
        """Devuelve la suma máxima de un subvector contiguo.

        Args:
            arr (list): Vector de números enteros (positivos y negativos).
            low (int): Índice bajo del subvector.
            high (int): Índice alto del subvector.

        Returns:
            int: Suma máxima de un subvector contiguo.
        """
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        left_sum = max_subarray(arr, low, mid)
        right_sum = max_subarray(arr, mid + 1, high)
        cross_sum = max_crossing_subarray(arr, low, mid, high)

        return max(left_sum, right_sum, cross_sum)

    if len(vector) == 0:
        return 0

    return max_subarray(vector, 0, len(vector) - 1)

def subvector_suma_maxima_divide_y_venceras_with_index(vector: list) -> tuple:
    """Devuelve la suma máxima de un subvector contiguo del vector dado.

    Aproximación Divide y Vencerás.

    Args:
        vector (list): Vector de números enteros (positivos y negativos).

    Returns:
        tuple: Suma máxima de un subvector contiguo y los índices del subvector.

    Complexity:
        O(n log n)
    """
    def max_crossing_subarray(arr: list, low: int, mid: int, high: int) -> tuple:
        """Devuelve la suma máxima de un subvector que pasa por el medio.

        Args:
            arr (list): Vector de números enteros (positivos y negativos).
            low (int): Índice bajo del subvector.
            mid (int): Índice medio del subvector.
            high (int): Índice alto del subvector.

        Returns:
            tuple: Suma máxima de un subvector que pasa por el medio y los índices del subvector.
        """
        left_sum = float('-inf')
        curr_sum = 0
        start_index = mid
        for i in range(mid, low - 1, -1):
            curr_sum += arr[i]
            if curr_sum > left_sum:
                left_sum = curr_sum
                start_index = i

        right_sum = float('-inf')
        curr_sum = 0
        end_index = mid + 1
        for i in range(mid + 1, high + 1):
            curr_sum += arr[i]
            if curr_sum > right_sum:
                right_sum = curr_sum
                end_index = i

        return left_sum + right_sum, (start_index, end_index)

    def max_subarray(arr: list, low: int, high: int) -> tuple:
        """Devuelve la suma máxima de un subvector contiguo.

        Args:
            arr (list): Vector de números enteros (positivos y negativos).
            low (int): Índice bajo del subvector.
            high (int): Índice alto del subvector.

        Returns:
            tuple: Suma máxima de un subvector contiguo y los índices del subvector.
        """
        if low == high:
            return arr[low], (low, low)

        mid = (low + high) // 2

        left_sum, left_indices = max_subarray(arr, low, mid)
        right_sum, right_indices = max_subarray(arr, mid + 1, high)
        cross_sum, cross_indices = max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum, left_indices
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum, right_indices

        return cross_sum, cross_indices
        
    if len(vector) == 0:
        return 0, (-1, -1)
    
    return max_subarray(vector, 0, len(vector) - 1)

# Sugerencia: analiza el tiempo de ejecución de cada una de las funciones anteriores.

# Sugerencia: crea una versión de estos algoritmos que además devuelva los índices del subvector de suma máxima.

def compare_times(func1: callable, func2: callable, vector: list):
    """
    Compara los tiempos de ejecución de dos funciones que resuelven el mismo problema.
    
    Args:
        func1 (callable): Primera función a comparar.
        func2 (callable): Segunda función a comparar.
        vector (list): Vector de números enteros (positivos y negativos).
    """
    start_time = time.time()
    func1(vector)
    time_func1 = time.time() - start_time

    start_time = time.time()
    func2(vector)
    time_func2 = time.time() - start_time

    print(f"Tiempo de ejecución de {func1.__name__}: {time_func1:.6f} segundos")
    print(f"Tiempo de ejecución de {func2.__name__}: {time_func2:.6f} segundos")

if __name__ == "__main__":
    vector = [random.randint(-100, 100) for _ in range(10000)]
    compare_times(subvector_suma_maxima_fuerza_bruta, subvector_suma_maxima_divide_y_venceras, vector)