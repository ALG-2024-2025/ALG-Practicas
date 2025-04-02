import unittest
import networkx as nx

from src.alg_s12 import FormaNormalConjuntiva, reduccion_a_clique

def grafo_de_prueba():
    """
    Devuelve un grafo como los que se pueden obtener con reduccion_a_clique().
    """
    
    return nx.Graph([
        ('0:x_2', '2:!x_1'), ('0:x_2', '1:!x_1'), ('0:x_2', '1:x_3'), 
        ('0:x_2', '1:x_2'), ('0:x_2', '2:x_3'), ('1:!x_1', '2:!x_1'), 
        ('1:!x_1', '2:x_3'), ('2:!x_1', '1:x_3'), ('2:!x_1', '1:x_2'), 
        ('0:x_1', '1:x_3'), ('0:x_1', '1:x_2'), ('0:x_1', '2:x_3'), 
        ('2:x_3', '1:x_3'), ('2:x_3', '1:x_2')])


class TestFormaNormalConjuntiva(unittest.TestCase):
    """Tests para la clase ArbolBusquedaOptimo"""
    
    def test_forma_normal_conjuntiva_1(self):
        """Primer test para la clase FormaNormalConjuntiva."""
        
        fnc = FormaNormalConjuntiva()
        self.assertEqual(fnc.num_variables(), 0)
        self.assertEqual(len(fnc), 0)
    
        fnc.inserta_clausulas([["x_1", "x_4"], ["x_3"]])
        self.assertEqual(fnc.num_variables(), 3)
        self.assertEqual(len(fnc), 1)
    
        fnc.inserta_clausulas([["x_3"], ["x_2", "x_4"]])
        self.assertEqual(fnc.num_variables(), 4)
        self.assertEqual(len(fnc), 2)
    
        self.assertTrue(fnc.evalua([]))
        self.assertTrue(fnc.evalua(("x_1", "x_2", "x_3", "x_4")))
        self.assertFalse(fnc.evalua(("x_3",)))
        self.assertFalse(fnc.evalua(("x_2", "x_4")))
    
        asignacion = fnc.asignacion_satisfacible()
        self.assertIsNotNone(asignacion)
        self.assertTrue(fnc.evalua(asignacion))
        
    def test_forma_normal_conjuntiva_2(self):
        """Segundo test para la clase FormaNormalConjuntiva."""
        
        fnc = FormaNormalConjuntiva([["x_1", "x_2", "x_3"], []])
        self.assertEqual(fnc.num_variables(), 3)
        self.assertEqual(len(fnc), 1)
    
        fnc.inserta_clausulas(
            [["x_2"], ["x_1", "x_3"]],
            [["x_1", "x_3"], ["x_2"]],
            [[], ["x_1", "x_2", "x_3"]])
    
        self.assertEqual(fnc.num_variables(), 3)
        self.assertEqual(len(fnc), 4)
        
        self.assertTrue(fnc.evalua(["x_1"]))
        self.assertFalse(fnc.evalua([]))
        self.assertFalse(fnc.evalua(["x_1", "x_2", "x_3"]))
    
        asignacion = fnc.asignacion_satisfacible()
        self.assertIsNotNone(asignacion)
        self.assertTrue(fnc.evalua(asignacion))   
 
    def test_forma_normal_conjuntiva_3(self):
        """Tercer test para la clase FormaNormalConjuntiva."""
        
        fnc = FormaNormalConjuntiva(        
            [["x_1", "x_2", "x_3"], []],
            [["x_2", "x_3"], ["x_1"]])
        self.assertEqual(fnc.num_variables(), 3)
        self.assertEqual(len(fnc), 2)
    
        fnc.inserta_clausulas(
            [["x_1", "x_3"], ["x_2"]],
            [["x_3"], ["x_1", "x_2"]],
            [[], ["x_3"]])
        
        self.assertEqual(fnc.num_variables(), 3)
        self.assertEqual(len(fnc), 5)
        
        self.assertFalse(fnc.evalua([]))
        self.assertFalse(fnc.evalua(["x_1", "x_2", "x_3"]))
        
        asignacion = fnc.asignacion_satisfacible()
        self.assertIsNone(asignacion) 
    
    def test_forma_normal_conjuntiva_4(self):
        """Cuarto test para la clase FormaNormalConjuntiva."""
        
        fnc = FormaNormalConjuntiva()
        self.assertEqual(fnc.num_variables(),  0)
        self.assertEqual(len(fnc), 0)
    
        fnc.inserta_clausulas(
            [["x_1", "x_2"], []],
            [["x_2", "x_3"], []],
            [["x_3", "x_4"], []],
            [["x_4", "x_5"], []],
            [["x_5", "x_6"], []])
        
        self.assertEqual(fnc.num_variables(), 6)
        self.assertEqual(len(fnc), 5)
        
        self.assertFalse(fnc.evalua([]))
        self.assertFalse(fnc.evalua(["x_1", "x_2", "x_3"]))
        self.assertTrue(fnc.evalua(["x_2", "x_4", "x_6"]))
        self.assertTrue(fnc.evalua(["x_1", "x_3", "x_5"]))
        
        asignacion = fnc.asignacion_satisfacible()
        self.assertIsNotNone(asignacion)
        self.assertTrue(fnc.evalua(asignacion))

def grafos_iguales(g1, g2):
    """
    Devuelve un booleano indicando si dos grafos son iguales: tienen los
    mismos nodos y arcos.
    """
    
    if set(g1.nodes()) != set(g2.nodes()):
        return False
  
    # No funciona comparar g1.edges() con g2.edges() porque en los arcos los 
    # nodos puede aparecer en distinto orden.
    
    for a, b in [(g1, g2), (g2, g1)]:
        for u, v in a.edges():
            if not b.has_edge(u, v):
                return False
    return True


class TestReduccionAClique(unittest.TestCase):
    """Tests para la función reduccion_a_clique()"""
        
    def test_reduccion_a_clique(self):
        
        fnc = FormaNormalConjuntiva(
            [["x_1", "x_2"], []],
            [["x_2", "x_3"], ["x_1"]],
            [["x_3"], ["x_1"]]
        )    
        
        g1 = reduccion_a_clique(fnc)
        g2 = grafo_de_prueba()
        
        self.assertTrue(grafos_iguales(g1, g2))  
        self.assertTrue(grafos_iguales(g2, g1))



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)