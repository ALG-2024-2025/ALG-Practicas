# ## Algoritmia
# ### Práctica 2
# El objetivo de esta práctica es trabajar con recurrencias


# Se pide la implementación de las funciones que aparecen a continuación.
#
# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada.
#
# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# Importaciones
from math import log
from collections import deque
from typing import Callable, Generator


def generador_recurrencia(
    coeficientes: list, funcion_adicional: Callable, iniciales: list
) -> Callable:
    """Generador de valores de acuerdo a una recurrencia:
    F(n) = coeficientes[0]*F(n-1) + coeficientes[1]*F(n-2) + ...
         + funcion_adicional(n)
    Los valores iniciales son F(0) = iniciales[0], F(1) = iniciales[1],...
    Los valores que se generan son F(0), F(1), F(2),...
    Se deben generar los valores de uno en uno, no hay que devolver varios.
    Debe generar valores indefinidamente, no hay que poner límites.
    Aunque sea una recurrencia, los valores *no* deben calcularse recursivamente.

    Args:
        coeficientes (list): Lista de coeficientes.
        funcion_adicional (callable):  Función adicional. Será utilizada para calcular el valor de la recurrencia.
        iniciales (list): Lista de valores iniciales.

    Returns:
        callable: Generador de valores de la recurrencia.
    """

    def generador():
        """Generador de valores de la recurrencia."""
        # Se usa un deque para almacenar solo los últimos len(coeficientes) valores.
        ventana = deque(iniciales[-len(coeficientes) :], maxlen=len(coeficientes))
        # Emitir todos los valores iniciales.
        for valor in iniciales:
            yield valor

        indice = len(iniciales)
        while True:
            # Se invierte la ventana para que coincida con el orden de los coeficientes.
            rev_ventana = list(reversed(ventana))
            valor = sum(
                c * v for c, v in zip(coeficientes, rev_ventana)
            ) + funcion_adicional(indice)
            yield valor
            ventana.append(valor)
            indice += 1

    return generador


def generador_recurrencia_profesor(
    coeficientes: list, funcion_adicional: Callable, iniciales: list
) -> Callable:
    """Generador de valores de acuerdo a una recurrencia:
    F(n) = coeficientes[0]*F(n-1) + coeficientes[1]*F(n-2) + ...
         + funcion_adicional(n)
    Los valores iniciales son F(0) = iniciales[0], F(1) = iniciales[1],...
    Los valores que se generan son F(0), F(1), F(2),...
    Se deben generar los valores de uno en uno, no hay que devolver varios.
    Debe generar valores indefinidamente, no hay que poner límites.
    Aunque sea una recurrencia, los valores *no* deben calcularse recursivamente.

    Args:
        coeficientes (list): Lista de coeficientes.
        funcion_adicional (callable):  Función adicional. Será utilizada para calcular el valor de la recurrencia.
        iniciales (list): Lista de valores iniciales.

    Returns:
        callable: Generador de valores de la recurrencia.
    """

    def generador():
        yield from iniciales
        coeficientes_rev = coeficientes[::-1]
        lista_recurrencia = deque(iniciales)
        indice = len(iniciales)
        while True:
            valor_adicional = funcion_adicional(indice)
            indice += 1

            valor = (
                sum(
                    coeficientes_rev[i] * lista_recurrencia[i]
                    for i in range(len(coeficientes_rev))
                )
                + valor_adicional
            )
            yield valor

            lista_recurrencia.append(valor)
            lista_recurrencia.popleft()

    return generador


class RecurrenciaMaestra:
    """
    Clase que representa una recurrencia de las que se consideran en el
    teorema maestro, de la forma T(n)=aT(n/b)+n^k. Se interpreta que en n/b
    la división es entera.
    Además de los métodos que aparecen a continuación, tienen que funcionar
    los siguientes operadores:
        ==, !=,
        str(): la representación como cadena debe ser 'aT(n/b)+n^k'
        []: el parámetro entre corchetes es el valor de n para calcular T(n).
    """

    def __init__(self, a: int, b: int, k: int, inicial: int = 0):
        """Constructor de la clase, los parámetros a, b, y k son los que
        aparecen en la fórmula aT(n/b)+n^k. El parámetro inicial es el valor
        para T(0).

        Args:
            a (int): constante a.
            b (int): constante b.
            k (int): constante k.
            inicial (int, optional): Valor por defecto para la función recursiva. Defaults to 0.
        """
        self.a = a
        self.b = b
        self.k = k
        self.inicial = inicial

    def metodo_maestro(self) -> str:
        """Devuelve una cadena con el tiempo de la recurrencia de acuerdo al
        método maestro. La salida está en el formato "O(n^x)" o "O(n^x*log(n))",
        siendo x un número.

        Returns:
            str: Cadena con el tiempo de la recurrencia.
        """
        if self.a > self.b**self.k:
            return f"O(n^{log(self.a, self.b)})"
        elif self.a == self.b**self.k:
            return f"O(n^{self.k}*log(n))"

        return f"O(n^{self.k})"

    def metodo_maestro_profesor(self) -> str:
        """Devuelve una cadena con el tiempo de la recurrencia de acuerdo al
        método maestro. La salida está en el formato "O(n^x)" o "O(n^x*log(n))",
        siendo x un número.

        Returns:
            str: Cadena con el tiempo de la recurrencia.
        """
        if log(self.a, self.b) > self.k:
            return f"O(n^{log(self.a, self.b)})"
        elif log(self.a, self.b) == self.k:
            return f"O(n^{self.k}*log(n))"

        return f"O(n^{self.k})"

    def __iter__(self) -> "Generator[int, None, None]":
        """Generador de valores de la recurrencia: T(0), T(1), T(2), T(3)...,
        indefinidamente.
        Se calcula iterativamente apoyándose en los valores previamente calculados.

        Returns:
            Generator[int, None, None]: Un generador que devuelve valores de la recurrencia.
        """
        values = [self.inicial]
        yield self.inicial
        n = 1
        while True:
            next_val = self.a * values[n // self.b] + n**self.k
            values.append(next_val)
            yield next_val
            n += 1

    def __iter__Profesor(self) -> "Generator[int, None, None]":
        """Generador de valores de la recurrencia: T(0), T(1), T(2), T(3)...,
        indefinidamente.
        Se calcula iterativamente apoyándose en los valores previamente calculados.

        Returns:
            Generator[int, None, None]: Generador de valores de la recurrencia.
        """
        lista_recurrencia = deque([self.inicial])
        indice = 1
        yield self.inicial
        while True:
            valor = self.a * lista_recurrencia[indice // self.b] + indice**self.k
            yield valor
            lista_recurrencia.append(valor)

            indice += 1
            if indice % self.b == 0:
                lista_recurrencia.popleft()

    def __eq__(self, x: object) -> bool:
        """Operador de igualdad."""
        if not isinstance(x, RecurrenciaMaestra):
            return False
        return (
            self.a == x.a
            and self.b == x.b
            and self.k == x.k
            and self.inicial == x.inicial
        )

    def __ne__(self, x: object) -> bool:
        """Operador de desigualdad."""
        return not self.__eq__(x)
        # return not self == other es lo mismo que lo de arriba gracias a '=='.

    def __str__(self) -> str:
        """Operador str.

        Returns:
            str: Representación de la recurrencia como cadena.
        """
        return f"{self.a}T(n/{self.b})+n^{self.k}"

    def __getitem__(self, n: int) -> int:
        """Operador [].

        Args:
            n (int): Índice para calcular el valor de la recurrencia.

        Raises:
            IndexError: Si el índice es negativo.

        Returns:
            int: Valor de la recurrencia en el índice n.
        """
        if n < 0:
            raise IndexError("Index cannot be negative")
        values = [self.inicial]
        for i in range(1, n + 1):
            next_val = self.a * values[i // self.b] + i**self.k
            values.append(next_val)
        return values[n]

    def __getitem__Profesor(self, n: int) -> int:
        """Operador [].

        Args:
            n (int): Índice para calcular el valor de la recurrencia.

        Raises:
            IndexError: Si el índice es negativo.

        Returns:
            int: Valor de la recurrencia en el índice n.
        """
        if n == 0:
            return self.inicial

        return self.a * self[n // self.b] + n**self.k
