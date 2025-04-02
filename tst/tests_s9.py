import unittest

from src.alg_s9 import es_subsecuencia, subsecuencia_comun_mas_larga, subsecuencias_comunes_mas_largas, mochila


class TestEsSubsecuencia(unittest.TestCase):

    def test_positivos(self):
        
        for subsecuencia, secuencia in (
                ("GTTC", "GTTCCTAATA"),
                ("CCTA", "GTTCCTAATA"),
                ("AATA", "GTTCCTAATA"),
                ("GTCAT", "GTTCCTAATA"),
                ("TCTAA", "GTTCCTAATA"),
                ("GTTCCTAATA", "GTTCCTAATA"),
        ):
            self.assertTrue(es_subsecuencia(subsecuencia, secuencia))
            
    def test_negativos(self):
        
        for subsecuencia, secuencia in (
                ("GTTCCTTATA", "GTTCCTAATA"),
                ("GGTTCCTAATA", "GTTCCTAATA"),            
                ("GTTCCTAATAA", "GTTCCTAATA"),
                ("GG", "GTTCCTAATA"), 
                ("AC", "GTTCCTAATA"), 
                ("TGTCCTAATA", "GTTCCTAATA"),
                ("ATAA", "GTTCCTAATA"), 

        ):
            self.assertFalse(es_subsecuencia(subsecuencia, secuencia))                 



class TestSubsecuenciaComunMasLarga(unittest.TestCase):

    def test_subsecuencia_comun_mas_larga(self):
        
        for s1, s2, longitud in (
            ("GTTCCTAATA", "CGATAATTGAGA", 6),
            ("ACDAADDADDDDCCBCBCAD", "ADBDBBCDBDAABBDDDCBB", 11),
            ("BBDABCCADCCADADDCACAACBA", "DBCBBDCBADABBBCCCDCACAADDACADD", 17),
            ("01111000000111100011", "10010100000100101111", 14),
            ('TTTATTTCGTCTAACTTATGACGTCCCTTCACGATCCAA',
             'TGGCCGGTTATTCAAGAGCGATATGTGCTATAAAGTGCC', 23)
        ):    
            for x, y in ((s1, s2), (s2, s1)):
                subsecuencia = subsecuencia_comun_mas_larga(x, y)
                self.assertEqual(len(subsecuencia), longitud)
                for secuencia in x, y:
                    self.assertTrue(es_subsecuencia(subsecuencia, secuencia))                 


class TestSubsecuenciasComunesMasLarga(unittest.TestCase):

    def test_subsecuencias_comunes_mas_largas(self):
        
        for s1, s2, longitud, numero in ( 
                ("GTTCCTAATA", "CGATAATTGAGA", 6, 3),
                ("ACDAADDADDDDCCBCBCAD", "ADBDBBCDBDAABBDDDCBB", 11, 4),
                ("BBDABCCADCCADADDCACAACBA", "DBCBBDCBADABBBCCCDCACAADDACADD", 
                 17, 1),
                ("01111000000111100011", "10010100000100101111", 14, 10),
                ('TTTATTTCGTCTAACTTATGACGTCCCTTCACGATCCAA',
                 'TGGCCGGTTATTCAAGAGCGATATGTGCTATAAAGTGCC', 23, 20)
            
        ):    
            for x, y in ((s1, s2), (s2, s1)):
                subsecuencias = subsecuencias_comunes_mas_largas(x, y)
                self.assertTrue(isinstance(subsecuencias, set))
                self.assertEqual(len(subsecuencias), numero)
                for subsecuencia in subsecuencias:
                    self.assertEqual(len(subsecuencia), longitud)
                    for secuencia in x, y:
                        self.assertTrue(es_subsecuencia(subsecuencia, secuencia))               


class TestMochila10(unittest.TestCase):

    def setUp(self):
        self.objetos = [
            [(1,1), (2,6), (5, 18), (6, 22), (7, 28)],
            [(1,1), (2,6), (5, 18), (6, 22), (7, 28), (9, 35)],
            [(1,1), (2,6), (5, 18), (6, 22), (7, 28), (9, 35), (10, 40)],
            [(1,1), (2,6), (5, 18), (6, 22), (7, 28), (9, 35), (10, 40), (11, 44)],
            [(1,1), (2,6), (5, 18), (6, 22), (7, 28), (9, 35), (10, 40), (11, 44), (12, 50)],
            [(1,1), (2,6), (5, 18), (6, 22), (7, 28), (9, 35), (10, 40), (11, 44), (12, 50), (13, 55)]
        ]
        self.capacidades = [11, 12, 13, 14, 15, 16]
        self.soluciones = [(40, [2, 3]), (46, [2, 4]), (50, [3, 4]), (53, [2, 5]), (55, [2,6]), (55, [4, 5])]

    def test_generico_mochila(self):
        
        for objetos, capacidad, (valor, solucion) in zip(self.objetos, self.capacidades, self.soluciones):
            valor, seleccionados = mochila(objetos, capacidad)
            self.assertEqual(valor, valor)
            self.assertEqual(set(seleccionados), set(solucion))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)