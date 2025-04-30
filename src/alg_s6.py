# # Algoritmia
# ## Práctica 6
# En esta práctica se resolverá el problema de las Torres de Hanoi, con dos añadidos: el número de postes puede ser mayor que 3, los discos pueden estar en cualquiera de los postes.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.


from typing import Optional, Sequence, Union


class Hanoi:
    """Clase para representar las torres de Hanoi."""

    def __init__(
        self, discos: Union[int, Sequence[int]], num_postes: Optional[int] = None
    ):
        """El parámetro discos es un entero o una secuencia.
        Si es un entero se refiere al número de discos en el primer poste.
        Si es una secuencia, cada elemento indica en qué poste está el disco.
        Los postes se identifican como 1, 2, 3...
        El primer elemento de la secuencia se refiere al disco más pequeño,
        el último al más grande.
        El parámetro num_postes es el número de postes.
        Si num_postes es None, será el máximo de 3 y el mayor valor que aparezca
        en discos.

        Args:
            discos (int): Discos en el primer poste o secuencia de postes.
            num_postes (int, optional): Número de postes. Defaults to None.
        """

        if isinstance(discos, int):
            discos = [1] * discos  # todos los discos en el poste 1
        else:
            discos = list(discos)
        self._discos = discos

        if num_postes is None:
            num_postes = max(3, max(discos))

        self._num_postes = num_postes

        # Almacenamos los postes como una lista de listas
        self._postes = [[] for _ in range(num_postes)]
        i = len(discos)
        for d in discos[::-1]:
            self._postes[d - 1].append(i)
            i -= 1

    def __len__(self) -> int:
        """Devuelve el número de discos.

        Returns:
            int: Número de discos.
        """

        return len(self._discos)

    def mueve(self, origen: int, destino: int):
        """Mueve el disco superior del poste origen al poste destino.

        Args:
            origen (int): Disco de origen.
            destino (int): Disco de destino.
        """

        assert 1 <= origen <= self._num_postes
        assert 1 <= destino <= self._num_postes

        poste_origen = self._postes[origen - 1]
        poste_destino = self._postes[destino - 1]

        assert len(poste_origen) > 0  # hay discos en el poste origen
        disco = poste_origen[-1]

        # comprobamos si podemos mover el disco:
        assert (
            len(poste_destino) == 0  # el destino está vacío
            or disco < poste_destino[-1]
        )  # contiene un disco mayor

        # movemos:
        self._discos[disco - 1] = destino
        poste_origen.pop()
        poste_destino.append(disco)

    def __str__(self) -> str:
        """Devuelve una representación de las torres.

        Returns:
            str: Representación de las torres.
        """
        return str(self._discos)

    def realiza_movimientos(self, movimientos: list, imprime: bool = False):
        """Realiza varios movimientos, cada movimiento se indica como un par
        (origen, destino).

        Args:
            movimientos (list): Movimientos a realizar.
            imprime (Boolean, optional): Indica si se imprime el estado de las torresdespués de cada movimiento. Defaults to False.
        """
        if imprime:
            self.imprime()
        for origen, destino in movimientos:
            self.mueve(origen, destino)
            if imprime:
                print("\n", origen, "->", destino, sep="")
                self.imprime()

    def imprime(self):
        """Imprime una representación gráfica de las torres."""

        n = len(self)
        for nivel in range(len(self) - 1, -1, -1):
            for poste in self._postes:
                if nivel >= len(poste):
                    print("|", " " * (n - 1), sep="", end=" ")
                else:
                    disco = poste[nivel]
                    print("X" * disco, " " * (n - disco), sep="", end=" ")
            print()
        for _ in self._postes:
            print("=" * n, sep=" ", end=" ")
        print()

    def resuelve(self, destino: Optional[int] = None) -> list:
        """Resuelve el problema, moviendo todos los discos al poste destino,
        partiendo de cualquier configuración inicial.
        Si el argumento destino es None, el poste destino es el último.
        Devuelve una secuencia con los movimientos, cada movimiento es un par
        (origen, destino).
        Si hay más de 3 postes, el resto también se deberían utilizar en algunos
        casos.

        Args:
            destino (int, optional): Poste destino. Defaults to None.

        Returns:
            list: Movimientos realizados.
        """
        if destino is None:
            destino = self._num_postes

        self._movimientos = []
        self.hanoi_generalizado(len(self), destino)

        return self._movimientos

    def hanoi_generalizado(self, tamano: int, destino: int):
        """Resuelve el problema, moviendo todos los discos al poste destino,
        partiendo de cualquier configuración inicial.
        Si el argumento destino es None, el poste destino es el último.
        Devuelve una secuencia con los movimientos, cada movimiento es un par
        (origen, destino).

        Args:
            tamano (int): Tamaño de la torre.
            destino (int): Poste destino.

        Complexity:
            O(2^n)
        """
        if tamano <= 0:
            return

        # Obtenemos el poste de origen donde se encuentra el disco de mayor tamaño.
        origen = self._discos[tamano - 1]

        if origen != destino:
            # Seleccionamos los postes candidatos (excluyendo origen y destino).
            candidatos = [
                poste
                for poste in range(1, self._num_postes + 1)
                if poste not in (origen, destino)
            ]
            # Si existe un poste vacío lo usamos; en caso contrario, seleccionamos aquel con el disco superior mayor.
            auxiliar = next(
                (poste for poste in candidatos if not self._postes[poste - 1]), None
            ) or max(candidatos, key=lambda poste: self._postes[poste - 1][-1])

            self.hanoi_generalizado(tamano - 1, auxiliar)
            self.mueve(origen, destino)
            self._movimientos.append((origen, destino))

        self.hanoi_generalizado(tamano - 1, destino)

    def hanoi_generalizado_profesor(self, tamano: int, destino: int):
        """Resuelve el problema, moviendo todos los discos al poste destino,
        partiendo de cualquier configuración inicial.
        Si el argumento destino es None, el poste destino es el último.
        Devuelve una secuencia con los movimientos, cada movimiento es un par
        (origen, destino).
        Si hay más de 3 postes, el resto también se deberían utilizar en algunos
        casos.

        Args:
            tamano (int): Tamaño de la torre.
            destino (int): Poste destino.
        """

        if tamano <= 0:
            return

        origen = self._discos[tamano - 1]

        if origen == destino:
            self.hanoi_generalizado_profesor(tamano - 1, destino)
            return

        auxiliar = None

        for poste in range(1, self._num_postes + 1):
            if poste == origen or poste == destino:
                continue

            if not self._postes[poste - 1]:
                auxiliar = poste
                break

            if (
                not auxiliar
                or self._postes[poste - 1][-1] > self._postes[auxiliar - 1][-1]
            ):
                auxiliar = poste

        assert auxiliar is not None, "No auxiliary post found"
        self.hanoi_generalizado_profesor(tamano - 1, auxiliar)
        self.mueve(origen, destino)
        self._movimientos.append((origen, destino))
        self.hanoi_generalizado_profesor(tamano - 1, destino)


def main():
    """Para ejecutar el juego de pruebas y visualizar las torres."""
    h = Hanoi(3)
    movimientos = h.resuelve()
    h = Hanoi(3)
    h.realiza_movimientos(movimientos, True)


if __name__ == "__main__":
    main()
