import unittest

from src.alg_s6 import Hanoi


class TestHanoi(unittest.TestCase):
    
    @staticmethod
    def postes_usados(movimientos: list) -> int:
        """Devuelve el número de postes usados en una secuencia de movimientos.

        Args:
            movimientos (list): Lista de movimientos.

        Returns:
            int: Número de postes usados.
        """
        return len(set((y for x in movimientos for y in x)))
    
    def test_3_3_3(self):
        # 3 discos en el poste 1, mover al poste 3
        h = Hanoi(3)
        movimientos = h.resuelve()
        self.assertEqual(str(h), "[3, 3, 3]")
        h = Hanoi(3)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), "[3, 3, 3]")
        
    def test_7_3_2(self):
        # 7 discos en el poste 1, mover al poste 2
        h = Hanoi(7)
        movimientos = h.resuelve(2)
        self.assertEqual(str(h), str([2] * 7))
        h = Hanoi(7)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), str([2] * 7))
        
    def test_3_4_4(self):
        # 3 discos en el poste 1, 4 postes
        h = Hanoi(3, 4)
        movimientos = h.resuelve()
        self.assertEqual(str(h), str([4] * 3))
        h = Hanoi(3, 4)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), str([4] * 3))    
        self.assertEqual(self.postes_usados(movimientos), 4)
 
    def test_10_5_5(self):
        # 10 discos en el poste 1, 5 postes
        h = Hanoi(10, 5)
        movimientos = h.resuelve()
        self.assertEqual(str(h), str([5] * 10))
        h = Hanoi(10, 5)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), str([5] * 10))  
        self.assertEqual(self.postes_usados(movimientos), 5)
        
    def test_132_3_3(self):
        # 3 discos repartidos en los 3 postes
        discos = [1, 3, 2]
        h = Hanoi(discos)
        movimientos = h.resuelve()
        self.assertEqual(str(h), str([3] * 3))
        h = Hanoi(discos)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), str([3] * 3))     

    def test_233122_3_3(self):
        # 6 discos repartidos en los 3 postes
        discos = [2, 3, 3, 1, 1, 2]
        h = Hanoi(discos)
        movimientos = h.resuelve()
        self.assertEqual(str(h), str([3] * 6))
        h = Hanoi(discos)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), str([3] * 6)) 

    def test_233112312_3_3(self):
        # 9 discos repartidos en los 3 postes
        discos = [2, 3, 3, 1, 1, 2, 3, 1, 2]
        h = Hanoi(discos)
        movimientos = h.resuelve()
        self.assertEqual(str(h), str([3] * 9))
        h = Hanoi(discos)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), str([3] * 9))
        
    def test_3341344221_4_4(self):
        # 10 discos repartidos en 4 postes
        discos = [3, 3, 4, 1, 3, 4, 4, 2, 2, 1]
        h = Hanoi(discos)
        movimientos = h.resuelve()
        self.assertEqual(str(h), str([4] * 10))
        h = Hanoi(discos)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), str([4] * 10))
        self.assertEqual(self.postes_usados(movimientos), 4)
        
    def test_3341344221_6_6(self):
        # 10 discos repartidos en los primeros 4 postes de 6
        discos = [3, 3, 4, 1, 3, 4, 4, 2, 2, 1]
        h = Hanoi(discos, 6)
        movimientos = h.resuelve()
        self.assertEqual(str(h), str([6] * 10))
        h = Hanoi(discos, 6)
        h.realiza_movimientos(movimientos)
        self.assertEqual(str(h), str([6] * 10))
        self.assertEqual(self.postes_usados(movimientos), 6)        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)