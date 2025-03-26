import unittest

from src.alg_s4 import numero_nodos, numero_arcos, peso_total, arco, inserta_nodo, inserta_arco, grado, pesos_adyacentes, coste_camino, prim, dijkstra, obten_camino_minimo


def grafo_de_ejemplo():
    return {
        'a': {'b': 1, 'c': 2},
        'b': {'a': 3, 'd': 6},
        'c': {'a': 5, 'b': 2},
        'd': {}
    }

class TestGrafo(unittest.TestCase):
    def tests_grafo_de_ejemplo(self):
        g = grafo_de_ejemplo()
        
        self.assertEqual(numero_nodos(g), 4)
        self.assertEqual(numero_arcos(g), 6)
        self.assertEqual(peso_total(g), 19)
        
        self.assertEqual(arco(g, 'a', 'b'), 1)
        self.assertEqual(arco(g, 'b', 'a'), 3)        
        self.assertEqual(arco(g, 'b', 'd'), 6)        
        self.assertEqual(arco(g, 'd', 'b'), None)        
        self.assertEqual(arco(g, 'x', 'y'), None)

    def tests_grafo_de_ejemplo_2(self):
        g = grafo_de_ejemplo()
        
        self.assertEqual(numero_nodos(g), 4)
        self.assertEqual(numero_arcos(g), 6)
        self.assertEqual(peso_total(g), 19)
        
        inserta_nodo(inserta_nodo(g, 'd'), 'e')
        
        self.assertEqual(numero_nodos(g), 5)
        self.assertEqual(numero_arcos(g), 6)
        self.assertEqual(peso_total(g), 19) 
        
        inserta_arco(inserta_arco(g, 'a', 'b', 7), 'd', 'c', 4)
        
        self.assertEqual(numero_nodos(g), 5)
        self.assertEqual(numero_arcos(g), 7)
        self.assertEqual(peso_total(g), 29) 

        inserta_arco(inserta_arco(g, 'f', 'g', 4), 'g', 'f', 3)
        
        self.assertEqual(numero_nodos(g), 7)
        self.assertEqual(numero_arcos(g), 9)
        self.assertEqual(peso_total(g), 36)

    def tests_grado_grafo_de_ejemplo(self):
        g = grafo_de_ejemplo()
        
        for nodo, grado_salida, grado_entrada in (
                ('a', 2, 2), ('b', 2, 2), ('c', 2, 1), ('d', 0, 1)
            
        ):
            self.assertEqual(grado(g, nodo), grado_salida)
            self.assertEqual(grado(g, nodo, salida=False), grado_entrada)

    def tests_pesos_grafo_de_ejemplo(self):
        g = grafo_de_ejemplo()
        
        for nodo, pesos_salida, pesos_entrada in (
                ('a', 3, 8), ('b', 9, 3), ('c', 7, 2), ('d', 0, 6)
            
        ):
            self.assertEqual(pesos_adyacentes(g, nodo), pesos_salida)
            self.assertEqual(pesos_adyacentes(g, nodo, salida=False),
                             pesos_entrada)   

    def tests_grafo_de_ejemplo_3(self):
        g = grafo_de_ejemplo()
        
        for camino, coste in (
            (('a', 'b', 'd'), 7),           
            (('b', 'a', 'c', 'a'), 10),
            (('a', 'c', 'a', 'b', 'a'), 11), 
            (('a', 'b', 'd', 'c'), None),       
            (('c', 'a', 'b', 'c'), None)    
        ):
            self.assertEqual(coste_camino(g, camino), coste) 


class TestPrimDijkstra(unittest.TestCase):

    def setUp(self):

        self.grafo1 = {
            'A': {'B': 3, 'D': 1},
            'B': {'A': 3, 'C': 4},
            'C': {'B': 4, 'D': 2},
            'D': {'A': 1, 'C': 2}
        }

        self.grafo2 = {
            'X': {'Y': 5, 'Z': 2},
            'Y': {'X': 5, 'Z': 8, 'W': 3},
            'Z': {'X': 2, 'Y': 8, 'W': 4},
            'W': {'Y': 3, 'Z': 4}
        }

        self.grafo3 = {
            'A': {'B': 7, 'C': 5},
            'B': {'A': 7, 'D': 8},
            'C': {'A': 5, 'D': 6},
            'D': {'B': 8, 'C': 6}
        }

        self.grafo4 = {
            'P': {'Q': 4, 'R': 3},
            'Q': {'P': 4, 'S': 2},
            'R': {'P': 3, 'S': 7, 'T': 6},
            'S': {'Q': 2, 'R': 7, 'T': 5},
            'T': {'R': 6, 'S': 5}
        }

        self.grafo5 = {
            'M': {'N': 9, 'O': 10},
            'N': {'M': 9, 'P': 2},
            'O': {'M': 10, 'P': 3, 'Q': 7},
            'P': {'N': 2, 'O': 3, 'Q': 1},
            'Q': {'O': 7, 'P': 1}
        }

        self.grafo6 = {
            '1': {'2': 4, '3': 1},
            '2': {'1': 4, '3': 2, '4': 6},
            '3': {'1': 1, '2': 2, '4': 3},
            '4': {'2': 6, '3': 3}
        }

        self.grafo7 = {
            'U': {'V': 3, 'W': 8},
            'V': {'U': 3, 'W': 4, 'X': 6},
            'W': {'U': 8, 'V': 4, 'X': 7},
            'X': {'V': 6, 'W': 7}
        }

        self.grafo_completo = {
            'a': {'b': 1, 'c': 2},
            'b': {'a': 1, 'c': 2},
            'c': {'a': 2, 'b': 2}
        }

        self.grafo_dirigido_1 = {
            'A': {'B': 3, 'D': 1},
            'B': {'C': 4},
            'C': {'D': 2},
            'D': {'A': 1}
        }

        self.grafo_dirigido_2 = {
            'A': {'B': 3, 'D': 1},
            'B': {'C': 4},
            'C': {'D': 2},
            'D': {}
        }    
    def test_prim(self):
        soluciones = [
            (self.grafo1, {'A': {'D': 1, 'B': 3}, 'B': {'A': 3}, 'C': {'D': 2}, 'D': {'A': 1, 'C': 2}}),
            (self.grafo2, {
                'X': {'Z': 2}, 'Y': {'W': 3}, 'Z': {'W': 4, 'X': 2}, 'W': {'Y': 3, 'Z': 4}
            }),
            (self.grafo3, {
                'A': {'C': 5, 'B': 7},
                'B': {'A': 7},
                'C': {'D': 6, 'A': 5},
                'D': {'C': 6}
            }),
            (self.grafo4, {
                'P': {'R': 3, 'Q': 4},
                'Q': {'S': 2, 'P': 4},
                'R': {'P': 3},
                'T': {'S': 5},
                'S': {'Q': 2, 'T': 5}
            }),
            (self.grafo5, {
                'M': {'N': 9},
                'N': {'M': 9, 'P': 2},
                'O': {'P': 3},
                'P': {'N': 2, 'O': 3, 'Q': 1},
                'Q': {'P': 1}
            }),
            (self.grafo6, {
                '1': {'3': 1},
                '2': {'3': 2},
                '3': {'2': 2, '1': 1, '4': 3},
                '4': {'3': 3}
            }),
            (self.grafo7,{
            'U': {'V': 3},
            'V': {'W': 4, 'U': 3, 'X': 6},
            'W': {'V': 4,},
            'X': {'V': 6}
            })
        ]

        for grafo, solucion in soluciones:
            self.assertEqual(prim(grafo), solucion)
        
        self.assertEqual(prim(self.grafo_completo, 'c'), {'a': {'c': 2, 'b': 1}, 'b': {'a': 1}, 'c': {'a': 2}})

    def test_dijkstra(self):

        soluciones = [
            (self.grafo1, 'A', {'A': (None, 0), 'B': ('A', 3), 'C': ('D', 3), 'D': ('A', 1)}),
            (self.grafo1, 'B', {'A': ('B', 3), 'B': (None, 0), 'C': ('B', 4), 'D': ('A', 4)}),
            (self.grafo1, 'C', {'A': ('D', 3), 'B': ('C', 4), 'C': (None, 0), 'D': ('C', 2)}),
            (self.grafo1, 'D', {'A': ('D', 1), 'B': ('A', 4), 'C': ('D', 2), 'D': (None, 0)}),
            (self.grafo_dirigido_1, 'A', {'A': (None, 0), 'B': ('A', 3), 'C': ('B', 7), 'D': ('A', 1)}),
            (self.grafo_dirigido_1, 'B', {'A': ('D', 7), 'B': (None, 0), 'C': ('B', 4), 'D': ('C', 6)}),
            (self.grafo_dirigido_1, 'C', {'A': ('D', 3), 'B': ('A', 6), 'C': (None, 0), 'D': ('C', 2)}),
            (self.grafo_dirigido_1, 'D', {'A': ('D', 1), 'B': ('A', 4), 'C': ('B', 8), 'D': (None, 0)}),
            (self.grafo_dirigido_2, 'A', {'A': (None, 0), 'B': ('A', 3), 'C': ('B', 7), 'D': ('A', 1)}),
            (self.grafo_dirigido_2, 'B', {'A': (None, float("inf")), 'B': (None, 0), 'C': ('B', 4), 'D': ('C', 6)}),
            (self.grafo_dirigido_2, 'C', {'A': (None, float("inf")), 'B':  (None, float("inf")), 'C': (None, 0), 'D': ('C', 2)}),
            (self.grafo_dirigido_2, 'D', {'A':  (None, float("inf")), 'B':  (None, float("inf")), 'C':  (None, float("inf")), 'D': (None, 0)})
        ]

        for grafo, origen, solucion in soluciones:
            self.assertEqual(dijkstra(grafo, origen), solucion)


    def test_caminos_dijkstra(self):

        caminos_pre_calculado1 = {'A': (None, 0), 'B': ('A', 3), 'C': ('D', 3), 'D': ('A', 1)}
        caminos_pre_calculado2 = {'A': ('B', 3), 'B': (None, 0), 'C': ('B', 4), 'D': ('A', 4)}
        caminos_pre_calculado3 = {'A': ('D', 3), 'B': ('C', 4), 'C': (None, 0), 'D': ('C', 2)}
        caminos_pre_calculado4 = {'A': ('D', 1), 'B': ('A', 4), 'C': ('D', 2), 'D': (None, 0)}
        caminos_pre_calculado5 = {'A': (None, 0), 'B': ('A', 3), 'C': ('B', 7), 'D': ('A', 1)}
        caminos_pre_calculado6 = {'A': ('D', 7), 'B': (None, 0), 'C': ('B', 4), 'D': ('C', 6)}
        caminos_pre_calculado7 = {'A': ('D', 3), 'B': ('A', 6), 'C': (None, 0), 'D': ('C', 2)}
        caminos_pre_calculado8 = {'A': ('D', 1), 'B': ('A', 4), 'C': ('B', 8), 'D': (None, 0)}
        caminos_pre_calculado9 = {'A': (None, 0), 'B': ('A', 3), 'C': ('B', 7), 'D': ('A', 1)}
        caminos_pre_calculado10 = {'A': (None, float("inf")), 'B': (None, 0), 'C': ('B', 4), 'D': ('C', 6)}
        caminos_pre_calculado11 = {'A': (None, float("inf")), 'B':  (None, float("inf")), 'C': (None, 0), 'D': ('C', 2)}
        caminos_pre_calculado12 = {'A':  (None, float("inf")), 'B':  (None, float("inf")), 'C':  (None, float("inf")), 'D': (None, 0)}
                    # Inicial, Final, Caminos, Resultado
        soluciones = [
            ('A', 'D', caminos_pre_calculado1, ['A', 'D']),
            ('B', 'D', caminos_pre_calculado2, ['B', 'A', 'D']),
            ('C', 'C', caminos_pre_calculado3, ['C']),
            ('D', 'A', caminos_pre_calculado4, ['D', 'A']),
            ('A', 'C', caminos_pre_calculado5, ['A', 'B', 'C']),
            ('B', 'D', caminos_pre_calculado6, ['B', 'C', 'D']),
            ('C', 'D', caminos_pre_calculado7, ['C', 'D']),
            ('D', 'B', caminos_pre_calculado8, ['D', 'A', 'B']),
            ('A', 'C', caminos_pre_calculado9, ['A', 'B', 'C']),
            ('B', 'D', caminos_pre_calculado10, ['B', 'C', 'D']),
            ('C', 'A', caminos_pre_calculado11, None),
            ('D', 'A', caminos_pre_calculado12, None)
        ]

        for origen, destino, caminos, resultado in soluciones:
            self.assertEqual(obten_camino_minimo(origen, destino, caminos), resultado)

        self.assertRaises(Exception, obten_camino_minimo, 'A', 'B', caminos_pre_calculado2)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)