# ## Algoritmia
# ### Práctica 1
# El objetivo de esta práctica es trabajar con iteradores y generadores.


# Se pide la implementación de las funciones que aparecen a continuación.
#
# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada.
#
# Para cada función que se pide se proporciona una función con algunos tests.
#
# Al llamar a las funciones de test no debería saltar ninguna aserción.


# Importaciones
from itertools import repeat
import collections
from collections.abc import Iterable
from typing import Optional

# ### Iterador con sustitución


def iterador_con_sustitucion(iterable: Iterable, cambios: dict) -> Iterable:
    """Dado un iterable genera sus valores una vez aplicadas las sustituciones
    indicadas por el diccionario de cambios.
    Los valores no hay que devolverlos todos a la vez, se deben generar de uno
    en uno.

    Args:
        iterable (Iterable): Objeto iterable.
        cambios (dict): Diccionario de cambios.

    Returns:
        Iterable: Elementos del iterable con los cambios aplicados.
    """
    for x in iterable:
        yield cambios.get(x, x)


# ### Iterador anidado


def iterador_anidado(elemento: Iterable) -> Iterable:
    """Iterador que genera los valores en elemento recursivamente: si elemento no
    es iterable genera solo elemento, pero si elemento es iterable genera sus
    elementos de manera recursiva.
    Los valores se deben generar de uno en uno.

    Args:
        elemento (Iterable): Elemento a iterar.

    Returns:
        Iterable: Elementos del iterable.
    """

    def helper(el: Iterable, seen: set) -> Iterable:
        """Función auxiliar que genera los elementos de manera recursiva.

        Args:
            el (Iterable): Elemento a iterar.
            seen (set): Elementos ya vistos.

        Returns:
            Iterable: Elementos del iterable.
        """
        if id(el) in seen:
            yield el
        elif isinstance(el, Iterable):
            seen.add(id(el))
            for sub in el:
                yield from helper(sub, seen)
        else:
            yield el

    yield from helper(elemento, set())


def iterador_anidado_profesor(elemento: Iterable) -> Iterable:
    """Iterador que genera los valores en elemento recursivamente: si elemento no
    es iterable genera solo elemento, pero si elemento es iterable genera sus
    elementos de manera recursiva.
    Los valores se deben generar de uno en uno.

    Args:
        elemento (Iterable): Elemento a iterar.

    Returns:
        Iterable: Elementos del iterable.
    """
    if not isinstance(elemento, Iterable):
        yield elemento
    else:
        for sub in elemento:
            yield from iterador_anidado(sub)


# ### Generador de media móvil


def generador_media_movil(iterable: Iterable, longitud: int) -> Iterable:
    """Dado un iterable de valores numéricos, genera los valores de la media móvil
    de la longitud indicada.
    Por ejemplo, si la longitud es 3, generaría la media de los 3 primeros
    valores, de los valores del 2º al 4º, de los valores del 3º al 5º...
    Los valores se deben generar de uno en uno.

    Args:
        iterable (Iterable): Objeto iterable.
        longitud (int): Longitud de la media móvil.

    Returns:
        Iterable: Valores de la media móvil.
    """
    iterador = iter(iterable)
    ventana = collections.deque(maxlen=longitud)
    for _ in range(longitud):
        ventana.append(next(iterador))
    suma = sum(ventana)
    yield suma / longitud
    for elem in iterador:
        suma += elem - ventana.popleft()
        ventana.append(elem)
        yield suma / longitud


def generador_media_movil_profesor(iterable: Iterable, longitud: int) -> Iterable:
    """Dado un iterable de valores numéricos, genera los valores de la media móvil
    de la longitud indicada.
    Por ejemplo, si la longitud es 3, generaría la media de los 3 primeros
    valores, de los valores del 2º al 4º, de los valores del 3º al 5º...
    Los valores se deben generar de uno en uno.

    Args:
        iterable (Iterable): Objeto iterable.
        longitud (int): Longitud de la media móvil.

    Returns:
        Iterable: Valores de la media móvil.
    """
    suma = 0
    ventana = []  # Buffer
    for e in iterable:
        ventana.append(e)
        suma += e
        if len(ventana) > longitud:
            suma -= ventana.pop(0)
        if len(ventana) == longitud:
            yield suma / longitud


# ### Iterador Incluido


def iterador_incluido(itera_1: Iterable, itera_2: Iterable) -> bool:
    """Dado un primer iterador o iterable, comprueba que sus elementos están
    incluidos en el mismo orden en los elementos de un segundo iterador o
    iterable.

    Args:
        itera_1 (Iterable): Objeto iterable 1.
        itera_2 (Iterable): Objeto iterable 2.

    Returns:
        bool: True si los elementos de itera_1 están incluidos en itera_2 en el.
    """

    iter_1 = iter(itera_1)
    iter_2 = iter(itera_2)
    for elem_1 in iter_1:
        for elem_2 in iter_2:
            if elem_1 == elem_2:
                break
        else:
            return False
    return True


def iterador_incluido_profesor(itera_1: Iterable, itera_2: Iterable) -> bool:
    """Dado un primer iterador o iterable, comprueba que sus elementos están
    incluidos en el mismo orden en los elementos de un segundo iterador o
    iterable.

    Args:
        itera_1 (Iterable): Objeto iterable 1.
        itera_2 (Iterable): Objeto iterable 2.

    Returns:
        bool: True si los elementos de itera_1 están incluidos en itera_2 en el.
    """

    iter_1 = iter(itera_1)
    iter_2 = iter(itera_2)
    for elem_1 in iter_1:
        try:
            while next(iter_2) != elem_1:
                pass
        except StopIteration:
            return False
    return True


# ### Secuencia generalizada de Fibonacci
# En la secuencia de Fibonacci, cada valor se obtiene sumando los dos anteriores. Se considera una generalización en la que cada valor se obtiene sumando los *k* anteriores:
# - F(0) = ... = F(k-1) = 1
# - F(n) = F(n-1) + ... + F(n-k+1)


def fibonacci_generalizado(k: int, iniciales: Optional[Iterable] = None) -> Iterable:
    """Genera indefinidamente valores de la secuencia generalizada de Fibonacci.
    Cada valor, salvo los iniciales, es la suma de los k anteriores.
    Los valores iniciales, que deben ser k, son los valores de F(0) ... F(k-1).
    El valor por defecto de los valores iniciales es 1.
    El espacio de memoria utilizado debería ser O(k).

    Args:
        k (int): Número de valores anteriores a sumar.
        iniciales (Iterable, optional): Valores iniciales. Defaults to None.

    Returns:
        Iterable: Valores de la secuencia generalizada de Fibonacci.

    Complexity:
        O(k)
    """
    if iniciales is None:
        iniciales = [1] * k
    numeros = list(iniciales)
    yield from numeros
    while True:
        siguiente = sum(numeros)
        yield siguiente
        numeros.append(siguiente)
        numeros.pop(0)


# ### Iterador repetido


def iter_repetido(itera: Iterable, repeticiones: Iterable) -> Iterable:
    """Genera los elementos del primer argumento tantas veces como el elemento
    correspondiente del segundo argumento.
    Se espera que los elementos del segundo argumento sean números naturales.
    El primer elemento del primer argumento se genera tantas veces como el
    primer elemento del segundo argumento, ... el elemento i-ésimo del primer
    argumento se genera tantas veces como el elemento i-ésimo del segundo
    argumento...
    Si el número de elementos de los dos argumentos fuera diferente, se
    generarán elementos hasta que uno se quede sin elementos.

    Args:
        itera (Iterable): Objeto iterable.
        repeticiones (Iterable): Objeto iterable con las repeticiones.

    Returns:
        Iterable: Elementos del primer argumento repetidos según el segundo.
    """
    iter_1 = iter(itera)
    iter_2 = iter(repeticiones)
    for rep in iter_2:
        try:
            item = next(iter_1)
        except StopIteration:
            return
        yield from repeat(item, rep)


def iter_repetido_profesor(itera: Iterable, repeticiones: Iterable) -> Iterable:
    """Genera los elementos del primer argumento tantas veces como el elemento
    correspondiente del segundo argumento.
    Se espera que los elementos del segundo argumento sean números naturales.
    El primer elemento del primer argumento se genera tantas veces como el
    primer elemento del segundo argumento, ... el elemento i-ésimo del primer
    argumento se genera tantas veces como el elemento i-ésimo del segundo
    argumento...
    Si el número de elementos de los dos argumentos fuera diferente, se
    generarán elementos hasta que uno se quede sin elementos.

    Args:
        itera (Iterable): Objeto iterable.
        repeticiones (Iterable): Objeto iterable con las repeticiones.

    Returns:
        Iterable: Elementos del primer argumento repetidos según el segundo.
    """
    for e, r in zip(itera, repeticiones):
        yield from repeat(e, r)


# ### Mezcla de iteradores ordenados


def iter_mezcla(iter_1: Iterable, iter_2: Iterable) -> Iterable:
    """Dados dos iteradores o iterables, suponiendo que ambos generan valores en
    orden, se generan los elementos de ambos de manera ordenada.
    La cantidad de memoria usada debe ser O(1).

    Args:
        iter_1 (Iterable): Primer iterable.
        iter_2 (Iterable): Segundo iterable.

    Returns:
        Iterable: Elementos de ambos iterables de manera ordenada.
    """
    iter_1 = iter(iter_1)
    iter_2 = iter(iter_2)
    elem_1 = next(iter_1, None)
    elem_2 = next(iter_2, None)

    while elem_1 is not None and elem_2 is not None:
        if elem_1 <= elem_2:
            yield elem_1
            elem_1 = next(iter_1, None)
        else:
            yield elem_2
            elem_2 = next(iter_2, None)

    while elem_1 is not None:
        yield elem_1
        elem_1 = next(iter_1, None)
    while elem_2 is not None:
        yield elem_2
        elem_2 = next(iter_2, None)


def iter_mezcla_profesor(iter_1: Iterable, iter_2: Iterable) -> Iterable:
    """Dados dos iteradores o iterables, suponiendo que ambos generan valores en
    orden, se generan los elementos de ambos de manera ordenada.
    La cantidad de memoria usada debe ser O(1).

    Args:
        iter_1 (Iterable): Primer iterable.
        iter_2 (Iterable): Segundo iterable.

    Returns:
        Iterable: Elementos de ambos iterables de manera ordenada.
    """
    iter_1 = iter(iter_1)
    iter_2 = iter(iter_2)
    elem_1 = next(iter_1, None)
    elem_2 = next(iter_2, None)

    while elem_1 is not None and elem_2 is not None:
        if elem_1 <= elem_2:
            yield elem_1
            elem_1 = next(iter_1, None)
        else:
            yield elem_2
            elem_2 = next(iter_2, None)

    if elem_1 is not None:
        yield elem_1
        yield from iter_1
    elif elem_2 is not None:
        yield elem_2
        yield from iter_2
