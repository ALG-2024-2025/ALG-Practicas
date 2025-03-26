import unittest

from src.alg_s2 import RecurrenciaMaestra, generador_recurrencia


class TestGeneradorRecurrencia(unittest.TestCase):
    
    @staticmethod
    def comprueba_recurrencia(coeficientes, funcion_adicional, iniciales,
                              funcion_alternativa, numero_comprobaciones=100, 
                              epsilon=0.1):
        """
        Dada una recurrencia (definida en términos de sus coeficientes,
        condiciones inciales y la función_adicional) comprueba si los valores
        generados son (aproximadamente) los mismos que los definidos por una función
        alternativa, para un determinado número de comprobaciones.
        """
    
        iterador = generador_recurrencia(coeficientes, funcion_adicional, 
                                         iniciales)
        for n in range(numero_comprobaciones):
            if abs(next(iterador) - funcion_alternativa(n)) > epsilon:
                return False
        return True
    
    """
    Nomenclatura de los tests: test_X_Y_Z.
        X representa los coeficientes. Usamos "n" para valores negativos.
        Y representa la función. Usamos "d" para la división, "p" para la 
        potencia.
        Z representa las condiciones inciales.
    """
          
    def test_1_1_0(self):
        # Recurrencia f(0)=0, f(n)=f(n-1)+1, que se corresponde con f(n)=n
        self.assertTrue(self.comprueba_recurrencia([1], lambda n: 1, [0], lambda n: n))
        
    def test_2_0_1(self):        
        # Recurrencia f(0)=1, f(n)=2*f(n-1), que se corresponde con f(n)=2**n
        self.assertTrue(self.comprueba_recurrencia([2], lambda n: 0, [1], lambda n: 2**n))

    def test_1_n_0(self):        
        # Recurrencia f(0)=0, f(n)=f(n-1)+n, que se corresponde con 
        # f(n)=n*(n+1)/2
        self.assertTrue(self.comprueba_recurrencia([1], lambda n: n, [0],
                                                   lambda n: n * (n + 1) / 2))
        
    def test_1_nd2_0(self):        
        # Recurrencia f(0)=0, f(n)=f(n-1)+n/2, que se corresponde con
        # f(n)=n*(n+1)/4
        self.assertTrue(self.comprueba_recurrencia([1], lambda n: n / 2, [0], 
                                                   lambda n: n * (n + 1) / 4))
        
    def test_1_2pn_1(self):        
        # Recurrencia f(0)=1, f(n)=f(n-1)+2**n, que se corresponde con
        # f(n)=2**(n+1)-1
        self.assertTrue(self.comprueba_recurrencia([1], lambda n: 2 ** n, [1],
                                                   lambda n: 2 ** (n + 1) - 1))

    def test_4n4_0_01(self):        
        # Recurrencia f(0)=0, f(1)=1, f(n)=4f(n-1)-4f(n-2), que se corresponde
        # con f(n)=2**(n-1)*n
        self.assertTrue(self.comprueba_recurrencia([4, -4], lambda n: 0, [0, 1],
                                                   lambda n: 2 ** (n - 1) * n))

    def test_2n1_1_01(self):        
        # Recurrencia f(0)=0, f(1)=1, f(n)=2f(n-1)-f(n-2)+1, que se corresponde
        # con f(n)=n*(n+1)/2
        self.assertTrue(self.comprueba_recurrencia([2, -1], lambda n: 1, [0, 1], 
                                                   lambda n: n * (n + 1) / 2))
        
    def test_11n1_0_012(self):        
        # Recurrencia f(0)=0, f(1)=1, f(2)=2, f(n)=f(n-1)+f(n-2)-f(n-3), que se
        # corresponde con f(n)=n
        self.assertTrue(self.comprueba_recurrencia([1, 1, -1], 
                                                   lambda n: 0, [0, 1, 2], 
                                                   lambda n: n))    
        

class TestRecurrenciaMaestra(unittest.TestCase):
           
    def test_teorema_3_2_2(self):
        # Recurrencia T(n)=3T(n/2)+O(n^2)
        resultado = RecurrenciaMaestra(3, 2, 2).metodo_maestro()
        self.assertEqual(resultado, "O(n^2)")

    def test_teorema_2_2_1(self):
        # Recurrencia T(n)=2T(n/2)+O(n)
        resultado = RecurrenciaMaestra(2, 2, 1).metodo_maestro()
        self.assertEqual(resultado, "O(n^1*log(n))")

    def test_teorema_3_2_1(self):
        # Recurrencia T(n)=3T(n/2)+O(n)
        resultado = RecurrenciaMaestra(3, 2, 1).metodo_maestro()
        # esperamos algo parecido a "O(n^1.5849625007211563)"
        self.assertTrue("O(n^1.58" in resultado)
        self.assertTrue("log" not in resultado)
        
    def test_operador_eq(self):
        # Tests para los operadores == y !=

        r = RecurrenciaMaestra(2, 2, 2)

        self.assertTrue(r == RecurrenciaMaestra(2, 2, 2))
        self.assertFalse(r != RecurrenciaMaestra(2, 2, 2))
        for a, b, k in ((1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1) ):
            self.assertTrue(r != RecurrenciaMaestra(a, b, k))
            self.assertFalse(r == RecurrenciaMaestra(a, b, k))

    def test_operador_str(self):
        # Tests para str()
        self.assertEqual(str(RecurrenciaMaestra(2, 2, 2)), "2T(n/2)+n^2")
        self.assertEqual(str(RecurrenciaMaestra(7, 4, 3)), "7T(n/4)+n^3")

    # Tests para []        
    
    def test_operador_getitem_222(self):        
       
        r = RecurrenciaMaestra(2, 2, 2)
        for n, valor in enumerate((0, 1, 6, 11, 28, 37, 58, 71, 120, 137, 174, 
                                   195, 260, 285, 338, 367, 496, 529, 598, 635)):
            self.assertEqual(r[n], valor)

    def test_operador_getitem_1201(self):        

        r = RecurrenciaMaestra(1, 2, 0, 1) 
        for n, valor in enumerate((1, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 
                                   5, 6, 6, 6, 6)):
            self.assertEqual(r[n], valor)

    def test_operador_getitem_431(self):        
        
        r = RecurrenciaMaestra(4, 3, 1)
        for n, valor in enumerate((0, 1, 2, 7, 8, 9, 14, 15, 16, 37, 38, 39, 44,
                                   45, 46, 51, 52, 53, 74, 75)):
            self.assertEqual(r[n], valor)
            
    # Casos de prueba para la generación sobre RecurrenciaMaestra.
    
    def comprueba_generacion(self, recurrencia, valores):
        it = iter(recurrencia)
        for v in valores:
            self.assertEqual(v, next(it))
            
    def test_generacion_222(self):
        self.comprueba_generacion(
            RecurrenciaMaestra(2, 2, 2), 
            (0, 1, 6, 11, 28, 37, 58, 71, 120, 137, 174, 195, 260, 285, 338, 
             367, 496, 529, 598, 635))
            
    def test_generacion_1201(self):            
        self.comprueba_generacion(
            RecurrenciaMaestra(1, 2, 0, 1), 
            (1, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6))

    def test_generacion_431(self):            
        self.comprueba_generacion(
            RecurrenciaMaestra(4, 3, 1),
            (0, 1, 2, 7, 8, 9, 14, 15, 16, 37, 38, 39, 44, 45, 46, 51, 52, 53,
             74, 75))
        
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)