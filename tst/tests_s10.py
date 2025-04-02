import unittest

from src.alg_s10 import CaminosMinimosFloyd, multiplicacion_encadenada_matrices


class TestCaminosMinimosFloyd(unittest.TestCase):
    """Tests para la clase CaminosMinimosFloyd."""

    def test_7_nodos_12_arcos(self):       
        
        grafo = {
            ("a", "b"): 2, 
            ("a", "d"): 1, 
            ("b", "d"): 3, 
            ("b", "e"): 10,
            ("c", "a"): 4,
            ("c", "f"): 5,
            ("d", "c"): 2,
            ("d", "e"): 7,
            ("d", "f"): 8,
            ("d", "g"): 4,
            ("e", "g"): 6,
            ("g", "f"): 1
        }
        
        caminos = CaminosMinimosFloyd(grafo)
        
        for origen, destino, distancia, camino in (
            ("a", "a", 0, ["a"]),
            ("a", "b", 2, ["a", "b"]),
            ("a", "c", 3, ["a", "d", "c"]),
            ("a", "d", 1, ["a", "d"]),
            ("a", "e", 8, ["a", "d", "e"]),
            ("a", "f", 6, ["a", "d", "g", "f"]),
            ("a", "g", 5, ["a", "d", "g"]),
            ("b", "a", 9, ["b", "d", "c", "a"]),
            ("c", "e", 12, ["c", "a", "d", "e"]),
            ("d", "b", 8, ["d", "c", "a", "b"]),
            ("e", "f", 7, ["e", "g", "f"]),
            ("e", "a", None, None),
            ("f", "d", None, None)
        ):
            self.assertEqual(caminos.distancia(origen, destino), distancia)
            self.assertEqual(caminos.camino(origen, destino), camino)


class TestMultiplicacionMatricesEncadenadas(unittest.TestCase):

    def test_orden_multiplicacion_matrices(self):
        """Casos de prueba para multiplicacion_encadenada_matrices."""
        
        for dimensiones, multiplicaciones, formula in (
            ([13, 5, 89], 13 * 5 * 89, "M_1*M_2"),
            ([13, 5, 89, 3, 34], 2856, "(M_1*(M_2*M_3))*M_4"), 
            ([2, 3, 5, 2, 4, 3], 78, "(M_1*(M_2*M_3))*(M_4*M_5)"),
            ([66, 87, 71, 43, 18, 19, 33, 98, 54], 498402, 
            "(M_1*(M_2*(M_3*M_4)))*(((M_5*M_6)*M_7)*M_8)")
        ):
            multiplicacion_encadenada_matrices(dimensiones)
            self.assertEqual(multiplicacion_encadenada_matrices(dimensiones),
                    (multiplicaciones, formula))
            

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)