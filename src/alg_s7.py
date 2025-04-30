# # Algoritmia
# ## Práctica 7
# En esta práctica se resolverá el problema de ordenación Divide y Vencerás

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# NO se deberá utilizar el método sort de las listas de Python. Se deberán implementar los algoritmos de ordenación.
import time
import random
from typing import Any, Callable


def ordena(
    secuencia: list,
    key_function: Callable = lambda x: x,
    reverse: bool = False,
    tipo: str = "mergesort",
) -> list:
    """Ordena la secuencia dada.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    El parámetro tipo indica el algoritmo de ordenación a usar. Puede ser "mergesort" o "quicksort".

    Args:
        secuencia (list): Secuencia a ordenar.
        key_function (callable, optional): Función para obtener el valor a comparar de cada elemento. Defaults to lambda x: x.
        reverse (bool, optional): Indica si el orden es descendente. Defaults to False.
        tipo (str, optional): Algoritmo de ordenación a usar. Defaults to "MERGESORT".

    Returns:
        list: Secuencia ordenada.

    Raises:
        ValueError: Si el tipo de ordenación no es válido.
    """
    if tipo.lower() == "mergesort":
        mergesort(secuencia, key_function, reverse)
    elif tipo.lower() == "quicksort":
        quicksort(secuencia, key_function, reverse)
    else:
        raise ValueError("Tipo de ordenación no válido")

    return secuencia


def mergesort(secuencia: list, key_function: Callable, reverse: bool):
    """Ordena la secuencia dada con el algoritmo mergesort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Args:
        secuencia (list): Secuencia a ordenar.
        key_function (callable): Función para obtener el valor a comparar de cada elemento.
        reverse (bool): Indica si el orden es descendente.

    Complexity:
        O(n log n)
    """
    if len(secuencia) <= 1:
        return

    mid = len(secuencia) // 2
    left = secuencia[:mid]
    right = secuencia[mid:]

    mergesort(left, key_function, reverse)
    mergesort(right, key_function, reverse)

    left_index = right_index = merged_index = 0

    while left_index < len(left) and right_index < len(right):
        if (
            key_function(left[left_index]) <= key_function(right[right_index])
        ) != reverse:
            secuencia[merged_index] = left[left_index]
            left_index += 1
        else:
            secuencia[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1

    # Copia los elementos restantes de la lista, si los hay
    secuencia[merged_index:] = left[left_index:] or right[right_index:]


def mergesort_profesor(secuencia: list, key_function: Callable, reverse: bool):
    """Ordena la secuencia dada con el algoritmo mergesort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Args:
        secuencia (list): Secuencia a ordenar.
        key_function (callable): Función para obtener el valor a comparar de cada elemento.
        reverse (bool): Indica si el orden es descendente.

    Complexity:
        O(n log n)
    """
    function = key_function
    if reverse:

        def function(x):
            return -key_function(x)

        # function = lambda x: -key_function(x)

    return _mergesort_profesor(secuencia, function)


def _mergesort_profesor(secuencia: list, key_function: Callable):
    """Ordena la secuencia dada con el algoritmo mergesort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Args:
        secuencia (list): Secuencia a ordenar.
        key_function (callable): Función para obtener el valor a comparar de cada elemento.
        reverse (bool): Indica si el orden es descendente.

    Complexity:
        O(n log n)
    """
    if len(secuencia) <= 1:
        return secuencia

    mitad = len(secuencia) // 2
    izquierda = secuencia[:mitad]
    derecha = secuencia[mitad:]

    izquierda = _mergesort_profesor(izquierda, key_function)
    derecha = _mergesort_profesor(derecha, key_function)

    return _fusion_profesor(izquierda, derecha, key_function)


def _fusion_profesor(izquierda: list, derecha: list, key_function: Callable):
    """Fusiona dos listas ordenadas en una sola lista ordenada.

    Args:
        izquierda (list): Lista izquierda a fusionar.
        derecha (list): Lista derecha a fusionar.
        key_function (callable): Función para obtener el valor a comparar de cada elemento.
    """
    iter_izq = iter(izquierda)
    iter_der = iter(derecha)
    res = []

    elem_izq = next(iter_izq, None)
    elem_der = next(iter_der, None)
    while len(res) < len(izquierda) + len(derecha):
        if elem_izq is None:
            res.append(elem_der)
            elem_der = next(iter_der, None)
        elif elem_der is None:
            res.append(elem_izq)
            elem_izq = next(iter_izq, None)
        elif key_function(elem_izq) <= key_function(elem_der):
            res.append(elem_izq)
            elem_izq = next(iter_izq, None)
        else:
            res.append(elem_der)
            elem_der = next(iter_der, None)
    return res


def quicksort(secuencia: list, key_function: Callable, reverse: bool):
    """Ordena la secuencia dada con el algoritmo quicksort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Puedes utilizar el método de partición que quieras.

    Args:
        secuencia (list): Secuencia a ordenar.
        key_function (callable): Función para obtener el valor a comparar de cada elemento.
        reverse (bool): Indica si el orden es descendente.

    Complexity:
        Worst case: O(n^2)
        Average case: O(n log n)
    """

    def _insertion_sort(low, high):
        for i in range(low + 1, high + 1):
            key_item = secuencia[i]
            j = i - 1
            # Insertion sort in ascending or descending order based on reverse flag
            while (
                j >= low
                and (key_function(secuencia[j]) > key_function(key_item)) != reverse
            ):
                secuencia[j + 1] = secuencia[j]
                j -= 1
            secuencia[j + 1] = key_item

    def _median_of_three(low, high):
        mid = (low + high) // 2
        # Sort low, mid, high elements to put median at mid position
        if (key_function(secuencia[low]) > key_function(secuencia[mid])) != reverse:
            secuencia[low], secuencia[mid] = secuencia[mid], secuencia[low]
        if (key_function(secuencia[low]) > key_function(secuencia[high])) != reverse:
            secuencia[low], secuencia[high] = secuencia[high], secuencia[low]
        if (key_function(secuencia[mid]) > key_function(secuencia[high])) != reverse:
            secuencia[mid], secuencia[high] = secuencia[high], secuencia[mid]
        # Move median to high-1 position (standard practice)
        secuencia[mid], secuencia[high - 1] = secuencia[high - 1], secuencia[mid]
        return high - 1

    def _partition(low, high):
        # Use median-of-three pivot selection for better performance
        if high - low > 2:
            pivot_idx = _median_of_three(low, high)
        else:
            pivot_idx = high

        pivot = secuencia[pivot_idx]

        # Swap pivot with the last element if not already there
        if pivot_idx != high:
            secuencia[pivot_idx], secuencia[high] = (
                secuencia[high],
                secuencia[pivot_idx],
            )

        i = low - 1
        for j in range(low, high):
            if (key_function(secuencia[j]) <= key_function(pivot)) != reverse:
                i += 1
                secuencia[i], secuencia[j] = secuencia[j], secuencia[i]
        secuencia[i + 1], secuencia[high] = secuencia[high], secuencia[i + 1]
        return i + 1

    def _quicksort(low, high):
        # Use insertion sort for small subarrays (much faster for small n)
        if high - low < 10:
            _insertion_sort(low, high)
            return

        # Only proceed if there's something to sort
        while low < high:
            p = _partition(low, high)

            # Tail recursion optimization: handle the smaller partition recursively
            # and iterate on the larger partition
            if p - low < high - p:
                _quicksort(low, p - 1)
                low = p + 1  # Iterate on the right part
            else:
                _quicksort(p + 1, high)
                high = p - 1  # Iterate on the left part

    if len(secuencia) > 1:
        _quicksort(0, len(secuencia) - 1)


def quicksort_profesor(secuencia: list, key_function: Callable, reverse: bool):
    """Ordena la secuencia dada con el algoritmo quicksort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Puedes utilizar el método de partición que quieras.

    Args:
        secuencia (list): Secuencia a ordenar.
        key_function (callable): Función para obtener el valor a comparar de cada elemento.
        reverse (bool): Indica si el orden es descendente.

    Complexity:
        Worst case: O(n^2)
        Average case: O(n log n)
    """
    function = key_function
    if reverse:

        def function(x):
            return -key_function(x)

        # function = lambda x: -key_function(x)

    return _quicksort_profesor(secuencia, function)


def _quicksort_profesor(secuencia: list, key_function: Callable):
    """Ordena la secuencia dada con el algoritmo quicksort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Puedes utilizar el método de partición que quieras.

    Args:
        secuencia (list): Secuencia a ordenar.
        key_function (callable): Función para obtener el valor a comparar de cada elemento.
        reverse (bool): Indica si el orden es descendente.

    Complexity:
        Worst case: O(n^2)
        Average case: O(n log n)
    """
    if len(secuencia) <= 1:
        return secuencia

    pivote = secuencia[0]
    izquierda, derecha = _particion_profesor(secuencia[1:], pivote, key_function)

    return (
        _quicksort_profesor(izquierda, key_function)
        + [pivote]
        + _quicksort_profesor(derecha, key_function)
    )


def _particion_profesor(secuencia: list, pivote: Any, key_function: Callable):
    """Ordena la secuencia dada con el algoritmo quicksort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Puedes utilizar el método de partición que quieras.

    Args:
        secuencia (list): Secuencia a ordenar.
        key_function (callable): Función para obtener el valor a comparar de cada elemento.
        reverse (bool): Indica si el orden es descendente.

    Complexity:
        Worst case: O(n^2)
        Average case: O(n log n)
    """
    izquierda = []
    derecha = []

    for elem in secuencia:
        if key_function(elem) <= key_function(pivote):
            izquierda.append(elem)
        else:
            derecha.append(elem)

    return izquierda, derecha


# Sugerencia: Prueba los tiempos de los distitnos algoritmos de ordenación, así como sus variantes.

# Sugerencia: Comprueba formalmente y experimentalmente los tiempos de ordenación de los algoritmos para conjuntos ya ordenados, conjuntos ordenados en orden inverso y conjuntos aleatorios.

# Sugerencia: Prueba los tiempos comparando tu implementación con la del Timsort incluida en la función sorted de Python.


def main():
    # Generar lista base de prueba
    n = 10000
    base_list = [random.randint(0, 10000) for _ in range(n)]
    test_cases = {
        "Random": base_list,
        "Sorted": sorted(base_list),
        "Reverse": sorted(base_list, reverse=True),
    }

    # Diccionario de algoritmos a probar
    algorithms = {
        "MergeSort": lambda lst: ordena(lst, tipo="mergesort"),
        "QuickSort": lambda lst: ordena(lst, tipo="quicksort"),
        "Timsort (Python sorted)": lambda lst: sorted(lst),
    }

    for case, data in test_cases.items():
        print(f"\nTest case: {case}")
        results = {}
        for name, algo in algorithms.items():
            input_data = data.copy()
            start = time.perf_counter()
            algo(input_data)
            elapsed = time.perf_counter() - start
            results[name] = elapsed

        best_time = min(results.values())
        for name, elapsed in results.items():
            percentage = (elapsed / best_time) * 100
            print(f"{name}: {elapsed:.6f} seconds -> {percentage:.2f}% of best")


if __name__ == "__main__":
    main()
