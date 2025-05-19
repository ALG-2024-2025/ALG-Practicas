import unittest

from src.alg_s11 import ArbolBusquedaOptimo


class TestArbolBusquedaOptimo(unittest.TestCase):
    """Tests para la clase ArbolBusquedaOptimo"""
    
    def test_arbol_busqueda_1(self):
        """Tests para la clase ArbolBusquedaOptimo"""
        
        claves = ["k1", "k2", "k3", "k4", "k5"]
        arbol = ArbolBusquedaOptimo(
            claves, [0.15, 0.10, 0.05, 0.10, 0.20], 
            [0.05, 0.10, 0.05, 0.05, 0.05, 0.10])
       
        self.assertEqual(len(arbol), 5)
                              
        for clave in claves:
            self.assertTrue(clave in arbol)
        self.assertTrue("k0" not in arbol)
        self.assertTrue("k6" not in arbol)
        
        for i, clave in enumerate(claves):
            self.assertEqual(arbol[i], clave)
        
        for i, clave in enumerate(arbol):
            self.assertEqual(claves[i], clave)
            
        self.assertEqual(arbol.raiz(), "k2")
        
        self.assertEqual(arbol.profundidad(), 3)
        profundidades = [1, 0, 3, 2, 1]
        for clave, profundidad in zip(claves, profundidades):
            self.assertEqual(arbol.profundidad(clave), profundidad)
            
        lista_hijos = [(None, None), ("k1", "k5"), (None, None), ("k3", None), 
                 ("k4", None)]
        for clave, hijos in zip(claves, lista_hijos):
            self.assertEqual(arbol.hijos(clave), hijos)
            
        self.assertEqual(round(arbol.coste_esperado(), 2), 2.75)
        self.assertEqual(str(arbol), "((k1)k2(((k3)k4)k5))")
        
    def test_arbol_busqueda_2(self):
        """Tests para la clase ArbolBusquedaOptimo"""
        
        claves = ["k" + str(i) for i in range(1, 11)]
        arbol = ArbolBusquedaOptimo(
            claves, 
            [0.21, 0.2, 0.04, 0.06, 0.08, 0.04, 0.04, 0.11, 0.19, 0.03])
    
        self.assertEqual(len(arbol), 10)
                              
        for clave in claves:
            assert clave in arbol
        assert "k0" not in arbol
        assert "k11" not in arbol
        
        for i, clave in enumerate(claves):
            self.assertEqual(arbol[i], clave)
        
        for i, clave in enumerate(arbol):
            self.assertEqual(claves[i], clave)
            
        self.assertEqual(arbol.raiz(), "k2")
        
        self.assertEqual(arbol.profundidad(), 4)
        profundidades = [1, 0, 4, 3, 2, 3, 4, 1, 2, 3]
        for clave, profundidad in zip(claves, profundidades):
            self.assertEqual(arbol.profundidad(clave), profundidad)
        
        lista_hijos = [(None, None), ('k1', 'k8'), (None, None), ('k3', None), 
                       ('k4', 'k6'), (None, 'k7'), (None, None), ('k5', 'k9'), 
                       (None, 'k10'), (None, None)]
        for clave, hijos in zip(claves, lista_hijos):
            self.assertEqual(arbol.hijos(clave), hijos)
            
        self.assertEqual(round(arbol.coste_esperado(), 2), 2.57)
        self.assertEqual(str(arbol), "((k1)k2((((k3)k4)k5(k6(k7)))k8(k9(k10))))")        
            

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)