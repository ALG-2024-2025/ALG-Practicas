import unittest
import random

from src.alg_s7 import ordena


class SortTest(unittest.TestCase):

    def setUp(self):
        # Crear conjuntos de prueba.
        self.listas_ordenadas = [
            list(range(10**i)) for i in range(1, 3)
        ]
        self.listas_inversas = [
            list(range(10**i, 0, -1)) for i in range(1, 3)
        ]
        self.listas_aleatorias = [
            [random.randint(0, 10**i) for _ in range(10**i)] for i in range(1, 5)
        ]
        self.listas_de_pares = [
            [(i, -i) for i in range(10**i)] for i in range(1, 3)
        ]

    def test_mergesort(self):
        for lista in self.listas_ordenadas:
            self.assertEqual(ordena(lista.copy(), tipo="mergesort"), sorted(lista))
        for lista in self.listas_inversas:
            self.assertEqual(ordena(lista.copy(), tipo="mergesort"), sorted(lista))
        for lista in self.listas_aleatorias:
            self.assertEqual(ordena(lista.copy(), tipo="mergesort"), sorted(lista))

    def test_quicksort(self):
        for lista in self.listas_ordenadas:
            self.assertEqual(ordena(lista.copy(), tipo="quicksort"), sorted(lista))
        for lista in self.listas_inversas:
            self.assertEqual(ordena(lista.copy(), tipo="quicksort"), sorted(lista))
        for lista in self.listas_aleatorias:
            self.assertEqual(ordena(lista.copy(), tipo="quicksort"), sorted(lista))

    def test_mergesort_reverse(self):
        for lista in self.listas_ordenadas:
            self.assertEqual(ordena(lista.copy(), reverse=True, tipo="mergesort"), sorted(lista, reverse=True))
        for lista in self.listas_inversas:
            self.assertEqual(ordena(lista.copy(), reverse=True, tipo="mergesort"), sorted(lista, reverse=True))
        for lista in self.listas_aleatorias:
            self.assertEqual(ordena(lista.copy(), reverse=True, tipo="mergesort"), sorted(lista, reverse=True))

    def test_quicksort_reverse(self):
        for lista in self.listas_ordenadas:
            self.assertEqual(ordena(lista.copy(), reverse=True, tipo="quicksort"), sorted(lista, reverse=True))
        for lista in self.listas_inversas:
            self.assertEqual(ordena(lista.copy(), reverse=True, tipo="quicksort"), sorted(lista, reverse=True))
        for lista in self.listas_aleatorias:
            self.assertEqual(ordena(lista.copy(), reverse=True, tipo="quicksort"), sorted(lista, reverse=True))

    def test_mergesort_key(self):
        for lista in self.listas_de_pares:
            self.assertEqual(ordena(lista.copy(), key_function=lambda x: x[1], tipo="mergesort"), sorted(lista, key=lambda x: x[1]))
        for lista in self.listas_de_pares:
            self.assertEqual(ordena(lista.copy(), key_function=lambda x: x[1], reverse=True, tipo="mergesort"), sorted(lista, key=lambda x: x[1], reverse=True))

        for lista in self.listas_de_pares:
            self.assertEqual(ordena(lista.copy(), key_function=lambda x: x[0], tipo="mergesort"), sorted(lista, key=lambda x: x[0]))
        for lista in self.listas_de_pares:
            self.assertEqual(ordena(lista.copy(), key_function=lambda x: x[0], reverse=True, tipo="mergesort"), sorted(lista, key=lambda x: x[0], reverse=True))

    def test_quicksort_key(self):
        for lista in self.listas_de_pares:
            self.assertEqual(ordena(lista.copy(), key_function=lambda x: x[1], tipo="quicksort"), sorted(lista, key=lambda x: x[1]))
        for lista in self.listas_de_pares:
            self.assertEqual(ordena(lista.copy(), key_function=lambda x: x[1], reverse=True, tipo="quicksort"), sorted(lista, key=lambda x: x[1], reverse=True))

        for lista in self.listas_de_pares:
            self.assertEqual(ordena(lista.copy(), key_function=lambda x: x[0], tipo="quicksort"), sorted(lista, key=lambda x: x[0]))
        for lista in self.listas_de_pares:
            self.assertEqual(ordena(lista.copy(), key_function=lambda x: x[0], reverse=True, tipo="quicksort"), sorted(lista, key=lambda x: x[0], reverse=True))

    

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)