import unittest

# import collections
from itertools import chain, count, cycle, repeat, zip_longest

from src.alg_s1 import iter_mezcla, iter_repetido, iterador_incluido, iterador_anidado, fibonacci_generalizado, iterador_con_sustitucion, generador_media_movil

num_iteraciones_test = 10**5

class TestS1(unittest.TestCase):
    
    def test_iterador_con_sustitucion(self):
        for iterable, cambios, iterable_sustituido in (
            ([1, 2, 3, 4, 1, 2], {2: 1, 1: 2, 3: 5}, [2, 1, 5, 4, 2, 1]),
            ([1, 2, 3, 4, 1, 2] * 100, {2: 1, 1: 2, 3: 5}, 
                [2, 1, 5, 4, 2, 1] * 100),
            ("abcdb" * 100, {'a': 'z', 'b': 'a', 'd': 'y'},
                ['z', 'a', 'c', 'y', 'a'] * 100)
        ):
            self.assertEqual(list(iterador_con_sustitucion(iterable, cambios)), iterable_sustituido)
            it = iterador_con_sustitucion(iterable, cambios)
            for e in iterable_sustituido:
                self.assertEqual(next(it), e)

        for v in iterador_con_sustitucion(range(10**100), {0: 0}):
            if v > 100:
                break
    
    def test_iterador_anidado(self):

        self.assertEqual(list(iterador_anidado(4)), [4])
        self.assertEqual(list(iterador_anidado([4])), [4])
        self.assertEqual(list(iterador_anidado((4,))), [4])
        self.assertEqual(list(iterador_anidado([[4]])), [4])
        self.assertEqual(list(iterador_anidado([1, [2, [3], 4]])), [1, 2, 3, 4])

        l1 = []
        l2 = []
        l3 = []
        for i in range(100):
            l1 += [i]
            l2 = [l2, i]
            self.assertEqual(l1, list(iterador_anidado(l2)))
            l3 = [(l3, [i])]
            self.assertEqual(l1, list(iterador_anidado(l3)))
            
        for v in iterador_anidado(range(10**100)):
            if v > 100:
                break

    def test_generador_media_movil(self): 
        
        for secuencia in (list(range(10)), tuple(range(10)), range(10)):
            self.assertEqual(list(generador_media_movil(secuencia, 1)), list([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]))
            self.assertEqual(list(generador_media_movil(secuencia, 2)), list([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]))
            self.assertEqual(list(generador_media_movil(secuencia, 3)), list([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]))
            self.assertEqual(list(generador_media_movil(secuencia, 4)), list([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]))
            self.assertEqual(list(generador_media_movil(secuencia, 5)), list([2.0, 3.0, 4.0, 5.0, 6.0, 7.0]))

        self.assertEqual(list(generador_media_movil(range(100), 1)), list(range(100)))
        self.assertEqual(list(generador_media_movil(range(100), 3)), list(range(1, 99)))
        self.assertEqual(list(generador_media_movil(range(100), 5)), list(range(2, 98)))

        self.assertEqual(list(generador_media_movil(range(100), 2)), [x + 0.5 for x in range(99)])
        self.assertEqual(list(generador_media_movil(range(100), 4)), [x + 1.5 for x in range(97)])

        self.assertEqual(list(generador_media_movil(range(100, 0, -1), 1)), list(range(100, 0, -1)))
        self.assertEqual(list(generador_media_movil(range(100, 0, -1), 3)), list(range(99, 1, -1)))
        self.assertEqual(list(generador_media_movil(range(100, 0, -1), 5)), list(range(98, 2, -1)))
        
        it = generador_media_movil(range(1000),4)
        for v in range(997):
            self.assertEqual(next(it), v + 1.5)
            
        self.assertEqual(list(generador_media_movil([1, 2] * 1000, 2)), [1.5] * 1999)
        self.assertEqual(list(generador_media_movil([1, 2] * 1000, 3)), [4/3, 5/3] * 999)
        
        for v in generador_media_movil(range(10**100), 10):
            if v >= 100:
                break

    def test_iterador_incluido(self):
        """
        Casos de prueba para iterador_incluido().
        """
        
        self.assertTrue(iterador_incluido(range(100), range(100)))
        self.assertTrue(iterador_incluido(range(99), range(100)))
        self.assertTrue(iterador_incluido(range(1,100), range(100)))

        self.assertFalse(iterador_incluido(range(100), range(99)))
        self.assertFalse(iterador_incluido(range(100), range(1, 100)))

        self.assertTrue(iterador_incluido(range(10, 90, 3), range(100)))
        self.assertFalse(iterador_incluido(range(10, 110, 3), range(100)))
        
        range_list = list(range(10, 90, 3))
        self.assertTrue(iterador_incluido(range_list, range(100)))
        lista_incluido = list(range(10, 90, 3))
        self.assertTrue(iterador_incluido(lista_incluido, range(100)))
        lista_incluido[20] = 11
        self.assertFalse(iterador_incluido(lista_incluido, range(100)))
        self.assertFalse(iterador_incluido(iter(lista_incluido), range(100)))
        self.assertFalse(iterador_incluido(range(10**100), range(1000)))

    def test_fibonacci(self):

        casos_prueba = (
            (2, None, [1, 1, 2, 3, 5, 8, 13, 21, 34]),
            (2, [2, 2], [2, 2, 4, 6, 10, 16, 26, 42]),
            (3, None, [1, 1, 1, 3, 5, 9, 17, 31, 57]),
            (4, None, [1, 1, 1, 1, 4, 7, 13, 25, 49]),
        )

        for k, iniciales, secuencia in casos_prueba:
            i = 0
            for v in fibonacci_generalizado(k, iniciales):
                if i >= len(secuencia):
                    break
                self.assertEqual(v, secuencia[i])
                i += 1
            assert i == len(secuencia)

        for k, iniciales, secuencia in casos_prueba:
            for v, w in zip(fibonacci_generalizado(k, iniciales), secuencia):
                self.assertEqual(v, w)

        for k, iniciales, secuencia in casos_prueba: 
            generador = fibonacci_generalizado(k, iniciales)
            for v in secuencia:
                self.assertEqual(v, next(generador))

        generador = fibonacci_generalizado(4, [0, 0, 0, 0])
        for _ in range(num_iteraciones_test):
            self.assertEqual(next(generador), 0)

    def test_iter_repetido(self):
        casos_prueba = (
            ("abc", [3, 0, 2], ['a', 'a', 'a', 'c', 'c']),
            ("abcd", [3, 0, 2], ['a', 'a', 'a', 'c', 'c']),
            ("abc", [3, 0, 2, 4], ['a', 'a', 'a', 'c', 'c']),
            (range(3), range(1, 4), [0, 1, 1, 2, 2, 2])
        )

        for iterable, repeticiones, lista in casos_prueba:
            self.assertEqual(list(iter_repetido(iterable, repeticiones)), 
                             lista)

        for iterable, repeticiones, lista in casos_prueba:
            for v, w in zip_longest(iter_repetido(iterable, repeticiones), 
                                    lista):
                self.assertEqual(v, w)

        for iterable, repeticiones, lista in casos_prueba:
            generador = iter_repetido(iterable, repeticiones)
            for v in lista:
                self.assertEqual(v, next(generador))
                        
        generador = iter_repetido(count(), repeat(1))
        for i in range(num_iteraciones_test):
            self.assertEqual(i, next(generador))

        repeticiones = [3, 0, 1]
        generador = iter_repetido(count(), cycle(repeticiones))
        r = 0
        for i in range(num_iteraciones_test):
            for _ in range(repeticiones[r]):
                self.assertEqual(i, next(generador))
            r = r + 1 
            if r == len(repeticiones): 
                r = 0    

    def test_iter_mezcla(self):

        casos_prueba = (
            (range(100), range(100, 200), range(200)),
            (range(0, 100, 2), range(1, 100, 2), range(100)),
            (range(0, 100, 4), range(2, 100, 4), range(0, 100, 2)),
            (range(0, 100), range(200, 300), 
             chain(range(0, 100), range(200, 300))),
            (range(100), range(100), (x for x in range(100) for _ in range(2))),
            (range(0, 100, 3), range(0, 100, 5), 
             sorted(chain(range(0, 100, 3), range(0, 100, 5)))),
            (range(num_iteraciones_test), 
             range(num_iteraciones_test, 2*num_iteraciones_test),
             range(2*num_iteraciones_test)),
            (range(0, num_iteraciones_test, 2), 
             range(1, num_iteraciones_test, 2), 
             range(num_iteraciones_test)),
            (range(num_iteraciones_test), range(num_iteraciones_test), 
             (x for x in range(num_iteraciones_test) for _ in range(2)))
        )

        for it_1, it_2, it_resultado in casos_prueba:
            for v, w in zip_longest(iter_mezcla(it_1, it_2), it_resultado):
                self.assertEqual(v, w) 

        casos_prueba = (
            (range(100), range(100, 200), range(200)),
            (range(0, 100, 2), range(1, 100, 2), range(100)),
            (range(0, 100, 4), range(2, 100, 4), range(0, 100, 2)),
            (range(0, 100), range(200, 300), 
             chain(range(0, 100), range(200, 300))),
            (range(100), range(100), (x for x in range(100) for _ in range(2))),
            (range(0, 100, 3), range(0, 100, 5), 
             sorted(chain(range(0, 100, 3), range(0, 100, 5)))),
            (range(num_iteraciones_test), 
             range(num_iteraciones_test, 2*num_iteraciones_test),
             range(2*num_iteraciones_test)),
            (range(0, num_iteraciones_test, 2), 
             range(1, num_iteraciones_test, 2), 
             range(num_iteraciones_test)),
            (range(num_iteraciones_test), range(num_iteraciones_test), 
             (x for x in range(num_iteraciones_test) for _ in range(2)))
        )

        for it_1, it_2, it_resultado in casos_prueba:
            for v, w in zip_longest(iter_mezcla(it_2, it_1), it_resultado):
                self.assertEqual(v, w) 

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)