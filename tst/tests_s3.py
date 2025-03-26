import unittest

from src.alg_s3 import dar_la_vuelta, algoritmo_mochila_voraz


class TestDarLaVuelta(unittest.TestCase):

    def setUp(self):

        self.cambios_inveros = [0.01, 0.02, 0.05, 0.1, 0.20, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]
        self.cambios_exactos = self.cambios_inveros[::-1]
        self.cambios_desordenados = [20, 5, 0.20, 200, 0.02, 2, 100, 50, 0.1, 1, 0.05, 10, 0.5, 0.01] 

    def test_dar_la_vuelta_enteros(self):
        a_probar = [10, 300, 15, 25]
        cambios_esperados = [[10], [200, 100], [10, 5], [20, 5]]
        # Se comprueba con los diversos ordenes de los cambios
        for cambio, cambio_esperado in zip(a_probar, cambios_esperados):
            self.assertEqual(list(dar_la_vuelta(cambio, self.cambios_exactos[:])), cambio_esperado)
            self.assertEqual( list(dar_la_vuelta(cambio, self.cambios_inveros[:])), cambio_esperado)
            self.assertEqual( list(dar_la_vuelta(cambio, self.cambios_desordenados[:])), cambio_esperado)

    def test_dar_la_vuelta_no_enteros(self):
        a_probar = [1.5, 0.75, 0.3, 0.15, 435.23, 123.45, 0.99]
        cambios_esperados = [[1, 0.5], [0.5, 0.20, 0.05], [0.20, 0.10], [0.1, 0.05], [200, 200, 20, 10, 5, 0.2, 0.02, 0.01], [100, 20, 2, 1, 0.2, 0.2, 0.05], [0.5, 0.2, 0.2, 0.05, 0.02, 0.02]]

        for cambio, cambio_esperado in zip(a_probar, cambios_esperados):
            self.assertEqual( list(dar_la_vuelta(cambio, self.cambios_exactos[:])), cambio_esperado)
            self.assertEqual( list(dar_la_vuelta(cambio, self.cambios_inveros[:])), cambio_esperado)
            self.assertEqual( list(dar_la_vuelta(cambio, self.cambios_desordenados[:])), cambio_esperado)

    def test_no_minimos(self):
        a_probar = [30.4, 3.6, 10.7, 0.7]
        cambios_posibles = [5, 3, 1, 0.5, 0.3, 0.1]
        cambios_esperados = [[5, 5, 5, 5, 5, 5, 0.3, 0.1], [3, 0.5, 0.1], [5, 5, 0.5, 0.1, 0.1], [0.5, 0.1, 0.1]]

        for cambio, cambio_esperado in zip(a_probar, cambios_esperados):
            self.assertEqual(list(dar_la_vuelta(cambio, cambios_posibles)), cambio_esperado)

    def test_comprueba_generador(self):
        
        for i, _ in enumerate(dar_la_vuelta(10**7, [0.01])):
            if i > 100:
                break


class TestMochilaVoraz(unittest.TestCase):
    
    def setUp(self):
        self.casos_prueba = (
            ([i for i in range(10, 60, 10)], [20, 30, 66, 40, 60], 100, 100, 156),
            ([i for i in range(10, 60, 10)], [20, 30, 66, 40, 60], 1000, 150, 216),
            ([i for i in range(10, 60, 10)], [100, 200, 300, 400, 500], 5, 0, 0),
            ([i for i in range(100,210, 20)], [i for i in range (10, 120, 20)], 500, 500, 230)
        )
        
    def test_1(self):        
        def create_dataset(pesos, valores):
            return dict(enumerate(map(lambda x,y: (x,y), pesos, valores)))


        def calcula_peso_y_valor(objetos, candidatos):
            candidatos = list(candidatos)
            peso = sum([objetos[x][0] for x in candidatos])
            valor = sum([objetos[x][1] for x in candidatos])
            return peso, valor


        for pesos, valores, peso_maximo, peso, valor in self.casos_prueba:
            objetos = create_dataset(pesos, valores)
            candidatos = algoritmo_mochila_voraz(objetos, peso_maximo)
            peso_, valor_ = calcula_peso_y_valor(objetos, candidatos)
            assert peso == peso_
            assert valor == valor_  

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)