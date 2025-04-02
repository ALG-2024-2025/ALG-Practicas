import unittest

from src.alg_s8 import subvector_suma_maxima_fuerza_bruta as fb
from src.alg_s8 import subvector_suma_maxima_divide_y_venceras as dyv


class TestS8(unittest.TestCase):

    def setUp(self):
        
        self.datos = (([-6, 27, 83, 75, -19, -1, 48, -7, 41, -26], 247),
                 ([-55, -97, -47, -100, 24, 87, 58, -51, -1, 22], 169),
                 ([40, -69, -73, 39, -38, 45, 53, 41, -26, -24, 28, -96, -68, 54, 24, 93, -71, -23, -36, -34], 171),
                 ([61, 7, 97, -3, 34, 19, -64, 58, 32, -16, -77, -42, 13, 38, -90, -44, -36, -61, 59, 96], 241))

    def test_fb(self):
        for d in self.datos:
            self.assertEqual(fb(d[0]), d[1])

    def test_dyv(self):
        for d in self.datos:
            self.assertEqual(dyv(d[0]), d[1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)