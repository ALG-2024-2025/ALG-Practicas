# # Algoritmia
# ## Práctica 9
# En esta práctica se resolverá el problema de Subsecuencia Común Más Larga (LCS) y el problema de la mochila 1-0.


# Subsecuencia Común Más Larga (LCS)


def es_subsecuencia(subsecuencia: str, cadena: str) -> bool:
    """Indica si el primer argumento es subsecuencia del segundo.

    Args:
        subsecuencia (str): Subsecuencia a comprobar.
        cadena (str): Cadena a comprobar.

    Returns:
        bool: True si subsecuencia es subsecuencia de cadena, False en caso contrario.

    Complexity:
        O(n)
    """
    sub_pos, str_pos = 0, 0
    while sub_pos < len(subsecuencia) and str_pos < len(cadena):
        if subsecuencia[sub_pos] == cadena[str_pos]:
            sub_pos += 1
        str_pos += 1
    return sub_pos == len(subsecuencia)


def es_subsecuencia_profesor(subsecuencia: str, cadena: str) -> bool:
    """Indica si el primer argumento es subsecuencia del segundo.

    Args:
        subsecuencia (str): Subsecuencia a comprobar.
        cadena (str): Cadena a comprobar.

    Returns:
        bool: True si subsecuencia es subsecuencia de cadena, False en caso contrario.

    Complexity:
        O(n)
    """
    iter1 = iter(subsecuencia)
    iter2 = iter(cadena)

    for c in iter2:
        try:
            c1 = next(iter1)
        except StopIteration:
            return True
        if c != c1:
            continue
    return False


def subsecuencia_comun_mas_larga(x: str, y: str) -> str:
    """Dadas dos cadenas x e y devuelve una que es subsecuencia de ambas y que
    tiene la longitud máxima de todas las subsecuencias comunes.

    Args:
        x (str): Cadena x.
        y (str): Cadena y.

    Returns:
        str: Subsecuencia común más larga de x e y.

    Complexity:
        O(m*n)
    """
    len_x, len_y = len(x), len(y)

    # Inicializar la matriz para programación dinámica
    dp = [[0 for _ in range(len_y + 1)] for _ in range(len_x + 1)]

    # Llenar la matriz
    for row in range(1, len_x + 1):
        for col in range(1, len_y + 1):
            if x[row - 1] == y[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    # Reconstruir la subsecuencia
    current_row, current_col = len_x, len_y
    longest_subsequence = []
    while current_row > 0 and current_col > 0:
        if x[current_row - 1] == y[current_col - 1]:
            longest_subsequence.append(x[current_row - 1])
            current_row -= 1
            current_col -= 1
        elif dp[current_row - 1][current_col] > dp[current_row][current_col - 1]:
            current_row -= 1
        else:
            current_col -= 1

    result = "".join(reversed(longest_subsequence))
    return result


def subsecuencias_comunes_mas_largas(x: str, y: str) -> set:
    """Dadas dos cadenas x e y devuelve un conjunto con todas las subsecuencias de
    ambas que tienen longitud máxima.

    Args:
        x (str): Cadena x.
        y (str): Cadena y.

    Returns:
        set: Conjunto con todas las subsecuencias comunes más largas de x e y.

    Complexity:
        O(m*n)
    """
    len_x, len_y = len(x), len(y)

    # Matriz para almacenar las longitudes de las LCS
    dp = [[0] * (len_y + 1) for _ in range(len_x + 1)]

    # Llenar la matriz
    for row in range(1, len_x + 1):
        for col in range(1, len_y + 1):
            if x[row - 1] == y[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    # Obtener la longitud máxima
    max_length = dp[len_x][len_y]

    # Conjunto para almacenar todas las LCS
    all_lcs = set()

    # Función recursiva para construir todas las LCS
    def generate_lcs(row: int, col: int, lcs: str = ""):
        """Genera todas las subsecuencias comunes más largas (LCS) de x e y.

        Args:
            row (int): Fila actual en la matriz dp.
            col (int): Columna de la matriz dp.
            lcs (str, optional): Subsecuencia común actual. Defaults to "".
        """
        if row == 0 or col == 0:
            # Si llegamos al final, agregamos la LCS al conjunto
            if len(lcs) == max_length:
                all_lcs.add("".join(reversed(lcs)))
            return

        if x[row - 1] == y[col - 1]:
            # Si los caracteres son iguales, los incluimos en la LCS
            generate_lcs(row - 1, col - 1, lcs + x[row - 1])
        else:
            # Exploramos ambos caminos si son óptimos
            if dp[row - 1][col] == dp[row][col]:
                generate_lcs(row - 1, col, lcs)
            if dp[row][col - 1] == dp[row][col]:
                generate_lcs(row, col - 1, lcs)

    generate_lcs(len_x, len_y)
    return all_lcs


def subsecuencias_comunes_mas_largas_profesor(x: str, y: str) -> set:
    """Dadas dos cadenas x e y devuelve un conjunto con todas las subsecuencias de
    ambas que tienen longitud máxima.

    Args:
        x (str): Cadena x.
        y (str): Cadena y.

    Returns:
        set: Conjunto con todas las subsecuencias comunes más largas de x e y.

    Complexity:
        O(m*n)
    """
    len_x, len_y = len(x), len(y)

    # Matriz para almacenar las longitudes de las LCS
    dp = [[0] * (len_y + 1) for _ in range(len_x + 1)]

    # Llenar la matriz
    for row in range(1, len_x + 1):
        for col in range(1, len_y + 1):
            if x[row - 1] == y[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    # Función recursiva para construir todas las LCS
    def subsecuencia_comun_mas_larga(row: int, col: int) -> set:
        if row == 0 or col == 0:
            return {""}
        if x[row - 1] == y[col - 1]:
            return {
                s + x[row - 1] for s in subsecuencia_comun_mas_larga(row - 1, col - 1)
            }
        if dp[row - 1][col] > dp[row][col - 1]:
            return subsecuencia_comun_mas_larga(row - 1, col)
        if dp[row][col - 1] > dp[row - 1][col]:
            return subsecuencia_comun_mas_larga(row, col - 1)
        return subsecuencia_comun_mas_larga(
            row - 1, col
        ) | subsecuencia_comun_mas_larga(row, col - 1)

    return subsecuencia_comun_mas_larga(len_x, len_y)


# Mochila 1-0


def mochila(objetos: list, capacidad: int) -> tuple:
    """Dada una capacidad y una lista de pesos y valores de n elementos,
    devuelve el valor máximo que se puede obtener sin superar la capacidad y los objetos que se deben llevar.

    Los objetos no se pueden partir.

    Args:
        objetos (list): Lista de objetos, cada objeto es una tupla (peso, valor).
        capacidad (int): Capacidad de la mochila.

    Returns:
        tuple: Valor máximo que se puede obtener y lista de objetos que se deben llevar.

    Complexity:
        O(n * capacidad)
    """
    num_objetos = len(objetos)

    # Inicializar la matriz para programación dinámica
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(num_objetos + 1)]

    # Llenar la matriz
    for indice in range(1, num_objetos + 1):
        peso, valor = objetos[indice - 1]
        for peso_actual in range(capacidad + 1):
            if peso <= peso_actual:
                dp[indice][peso_actual] = max(
                    dp[indice - 1][peso_actual],
                    dp[indice - 1][peso_actual - peso] + valor,
                )
            else:
                dp[indice][peso_actual] = dp[indice - 1][peso_actual]

    # Reconstruir la solución
    peso_restante = capacidad
    seleccionados = []
    for indice in range(num_objetos, 0, -1):
        if (
            peso_restante >= objetos[indice - 1][0]
            and dp[indice][peso_restante] != dp[indice - 1][peso_restante]
        ):
            seleccionados.append(indice - 1)
            peso_restante -= objetos[indice - 1][0]

    return dp[num_objetos][capacidad], seleccionados


# Sugerencia: Haz la función mochila con complejidad espacial O(W), siendo W la capacidad de la mochila.


def mochila_optimized(objetos: list, capacidad: int) -> int:
    """Dada una capacidad y una lista de pesos y valores de n elementos,
    devuelve el valor máximo que se puede obtener sin superar la capacidad y los objetos que se deben llevar.

    Los objetos no se pueden partir.

    Para que la complejidad espacial sea O(W), se debe de devolver solo el valor máximo, ya
    que si calculamos los objetos que se deben llevar, la complejidad espacial
    se convierte en O(n * W).

    Args:
        objetos (list): Lista de objetos, cada objeto es una tupla (peso, valor).
        capacidad (int): Capacidad de la mochila.

    Returns:
        int: Valor máximo que se puede obtener.

    Complexity:
        O(n * capacidad)
    """
    dp = [0 for _ in range(capacidad + 1)]

    for peso, valor in objetos:
        for w in range(capacidad, peso - 1, -1):
            dp[w] = max(dp[w], dp[w - peso] + valor)

    return dp[capacidad]


def mochila_optimized_profesor(objetos: list, capacidad: int) -> tuple:
    """Dada una capacidad y una lista de pesos y valores de n elementos,
    devuelve el valor máximo que se puede obtener sin superar la capacidad y los objetos que se deben llevar.

    Los objetos no se pueden partir.

    Args:
        objetos (list): Lista de objetos, cada objeto es una tupla (peso, valor).
        capacidad (int): Capacidad de la mochila.

    Returns:
        int: Valor máximo que se puede obtener.

    Complexity:
        O(n * capacidad)
    """
    dp = [(0, []) for _ in range(capacidad + 1)]

    for i, (peso, valor) in enumerate(objetos):
        for w in range(capacidad, peso - 1, -1):
            # La segunda condición evita duplicados.
            if (
                dp[w - peso][0] + valor > dp[w][0]
                and dp[w - peso][1] + [i] not in dp[w][1]
            ):
                dp[w] = (dp[w - peso][0] + valor, dp[w - peso][1] + [i])

    return dp[capacidad]
