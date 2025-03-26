import unittest
import random

from src.alg_s5 import Particion, kruskal


class TestParticion(unittest.TestCase):
    
    def test_particion(self, n=100):
        """
        Función que realiza varias pruebas sobre la clase Particion, 
        siendo n el número de elementos.
        """
    
        p = Particion(range(n))
    
        # Tenemos n elementos
        self.assertEqual(p.numero(), n)        
        
        # Tenemos n subconjuntos
        self.assertEqual(len(p), n)
        
        # Los elmentos 0, 1, ... n-1 están cada uno en un subconjunto 
        for v in range(n):
            self.assertEqual(p.numero(v), 1)
            self.assertEqual(p[v], v)
    
        # Comprobamos que tenemos los valores 0, 1, ... n-1
        s = set(range(n))
        for v in p:
            self.assertEqual(p[v], v)
            self.assertIn(v, s)
            s.remove(v)
        self.assertFalse(s)
        
        # Hacemos n - 1 uniones, comprobando la situación de la partición
        for v in range(1, n):
            self.assertEqual(p.numero(0), v)
            self.assertEqual(p.numero(v), 1)
            self.assertNotEqual(p[0], p[v])
            self.assertNotEqual(p[v - 1], p[v])
            p.une(0, v)
            self.assertEqual(p[0], p[v])
            self.assertEqual(p[v - 1], p[v])
            self.assertEqual(len(p), n - v)
    
    def test_uniones_aleatorias(self, n=100, repeticiones=10, semilla=1):
        """
        Partición con n elementos, en la que hacemos varias uniones aleatorias
        sobre particiones de n elementos.
        """
       
        random.seed(semilla)
        for i in range(repeticiones):
            p = Particion(range(n))
            s = set(range(n))
            self.assertEqual(p.numero(), n)   
            while len(p) > 1:
                a, b = random.sample(list(s), 2)
                self.assertNotEqual(p[a], p[b])
                num = p.numero(a) + p.numero(b)
                p.une(a, b)
                self.assertEqual(p[a], p[b])
                self.assertEqual(num, p.numero(a))
                self.assertEqual(num, p.numero(b))
                s.remove(b)
                self.assertEqual(p.numero(), n)     


class TestArbolExtendidoKruskal(unittest.TestCase):
    
    def test_6_nodos_9_arcos(self):
            
        g = {("a", "b"): 13, 
             ("a", "c"): 8,
             ("a", "d"): 1,
             ("b", "c"): 15,
             ("c", "d"): 5,
             ("c", "e"): 3,
             ("d", "e"): 4,
             ("d", "f"): 5,
             ("e", "f"): 2}
    
        t = {("a", "b"): 13, 
             ("a", "d"): 1,
             ("c", "e"): 3,
             ("d", "e"): 4,
             ("e", "f"): 2}
        
        self.assertEqual(kruskal(g), t)
    
    def test_7_nodos_12_arcos(self):
    
        g = {("a", "b"): 2, 
             ("a", "c"): 4,
             ("a", "d"): 1,
             ("b", "d"): 3,
             ("b", "e"): 10,
             ("c", "d"): 2,
             ("c", "f"): 5,
             ("d", "e"): 7,
             ("d", "f"): 8,
             ("d", "g"): 4,
             ("e", "g"): 6,
             ("f", "g"): 1}
        
        t = {("a", "b"): 2, 
             ("a", "d"): 1,
             ("c", "d"): 2,
             ("d", "g"): 4,
             ("e", "g"): 6,
             ("f", "g"): 1}
    
        self.assertEqual(kruskal(g), t)
        
    def test_grafo_aleatorio(self, n=10, repeticiones=10, semilla=1):
        """Tests con grafos completos aleatorios de n nodos"""
        
        random.seed(semilla)
        for _ in range(repeticiones):
            
            # Creamos el grafo
            g = {(i, j): n + 1 for i in range(n - 1) for j in range(i + 1, n)}
            for i in range(1, n + 1):
                g[random.randint(0, i - 1), i] = i
            t = kruskal(g)
            
            # Comprobamos que los arcos del árbol están en el grado y 
            # que el peso total es el esperado
            total = 0
            for arco, peso in t.items():
                self.assertEqual(peso, g[arco])
                total += peso
            self.assertEqual(total, n * (n + 1) / 2)   


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)