# # Algoritmia
# ## Práctica 3

# El objetivo de esta práctica es trabajar con los algoritmos de la mochila y dar la vuelta.

# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.


from collections.abc import Generator
import heapq


def dar_la_vuelta(cambio: float, valores_monedas: list) -> Generator[float, None, None]:
    """Se recibe una cantidad de dinero y una lista de monedas. Se devuelve un generador de las monedas que se necesitan para dar ese cambio de forma que se minimice el número de monedas.

    Se han de devolver las monedas de mayor a menor valor.

    Nota: Para evitar el problema de los decimales en python se puede usar la función round() para redondear a dos decimales.

    Args:
        cambio (float): Cantidad de dinero a devolver.
        valores_monedas (list): Lista de monedas disponibles.

    Yields:
        Generator (float, None, None): Generador de monedas.

    Complexity:
        O(n)
    """
    monedas = sorted(valores_monedas, reverse=True)
    restante = round(cambio, 2)
    while restante > 0:
        for moneda in monedas:
            if moneda <= round(restante, 2):
                yield moneda
                restante = round(restante - moneda, 2)
                break


# Implementa dar la vuelta utilizando las recomendaciones de la diapositiva 5 de la presentación del tema 2 y comprueba si es más rápido que la implementación básica.

def algoritmo_mochila_voraz(objetos: dict, peso_soportado: int) -> list:
    """Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se
    maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.

    Args:
        objetos (dict): Diccionario de objetos.
        peso_soportado (int): Peso máximo soportado.

    Returns:
        list: Lista de claves de los objetos seleccionados.

    Complexity:
        O(n log n)
    """
    items_ordenados = sorted(
        objetos.items(), key=lambda kv: kv[1][1] / kv[1][0], reverse=True
    )
    seleccionados = []
    for clave, (peso, _) in items_ordenados:
        if peso <= peso_soportado:
            seleccionados.append(clave)
            peso_soportado -= peso
    return seleccionados


def algoritmo_mochila_voraz_partidos(objetos: dict, peso_soportado: int) -> list:
    """Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se
    maximice el valor usando un algoritmo voraz. Los objetos pueden partirse.

    Args:
        objetos (dict): Diccionario de objetos.
        peso_soportado (int): Peso máximo soportado.

    Returns:
        list: Lista de claves de los objetos seleccionados.

    Complexity:
        O(n log n)
    """
    items_ordenados = sorted(
        objetos.items(), key=lambda kv: kv[1][1] / kv[1][0], reverse=True
    )
    seleccionados = []
    peso_actual = 0
    for clave, (peso, _) in items_ordenados:
        if peso_actual + peso <= peso_soportado:
            seleccionados.append(clave)
            peso_actual += peso
        else:
            fraccion = (peso_soportado - peso_actual) / peso
            seleccionados.append((clave, fraccion))
            break
    return seleccionados

def algoritmo_mochila_voraz_colas_prioridad(objetos: dict, peso_soportado: int) -> list:
    """Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se
    maximice el valor usando un algoritmo voraz con colas de prioridad. Los objetos no pueden partirse.

    Args:
        objetos (dict): Diccionario de objetos.
        peso_soportado (int): Peso máximo soportado.

    Returns:
        list: Lista de claves de los objetos seleccionados.

    Complexity:
        O(n log n)
    """
    # Crear una cola de prioridad con los objetos ordenados por valor/peso
    cola_prioridad = [(-v / p, p, k) for k, (p, v) in objetos.items()]
    heapq.heapify(cola_prioridad)
    
    seleccionados = []
    peso_actual = 0
    while cola_prioridad and peso_soportado > 0:
        _, peso, clave = heapq.heappop(cola_prioridad)
        if peso <= peso_soportado:
            seleccionados.append(clave)
            peso_actual += peso
        else:
            fraccion = (peso_soportado - peso_actual) / peso
            seleccionados.append((clave, fraccion))
            break
    
    return seleccionados

def algoritmo_mochila_voraz_profesor(objetos: dict, peso_soportado: int) -> dict:
    """Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se
    maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.

    Args:
        objetos (dict): Diccionario de objetos.
        peso_soportado (int): Peso máximo soportado.

    Returns:
        dict: Lista de claves de los objetos seleccionados.
    """
    items_ordenados = sorted(
        objetos.items(), key=lambda kv: kv[1][1] / kv[1][0], reverse=True
    )
    peso = 0
    seleccionados = {}

    for k, (p, _) in items_ordenados:
        if peso + p <= peso_soportado:
            seleccionados[k] = 1
            peso += p
        else:
            peso_restante = peso_soportado - peso
            cabe = peso_restante / p
            seleccionados[k] = cabe
            break

    for k, _ in items_ordenados:
        if k not in seleccionados:
            seleccionados[k] = 0

    return seleccionados
