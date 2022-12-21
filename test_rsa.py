import unittest
import number_theory_functions
from rsa_functions import RSA
from random import sample


class TestNumberTheory(unittest.TestCase):
    def test_extended_gcd(self):
        values = [(119952, 34425, 153),
                  (428848, 123075, 547)
                  ]
        for (a, b, d) in values:
            (gcd, x, y) = number_theory_functions.extended_gcd(a, b)
            self.assertEqual(d, gcd)
            self.assertEqual(gcd, a * x + b * y)

    def test_modular_inverse(self):
        values = [(17, 81),
                  (50, 137)
                  ]
        for (a, n) in values:
            x = number_theory_functions.modular_inverse(a, n)
            self.assertEqual(1, (a * x) % n)
            self.assertEqual((x % n), x)

        self.assertIsNone(number_theory_functions.modular_inverse(119952, 34425))

    def test_modular_exponent(self):
        values = [
            [(0, 0, 1), 0], [(0, 1, 1), 0], [(0, 1, 123), 0], [(0, 0, 123), 1], [(241, 0, 3213), 1],
            [(969003984405, 969003984405, 12321), 10683], [(547358786569, 29948725249, 279730978816), 91612218377]
        ]

        for val in values:
            base, exp, n = val[0]
            self.assertEqual(number_theory_functions.modular_exponent(base, exp, n), val[1])


class TestRSA(unittest.TestCase):
    def test_encrypt_decrypt(self):
        for i in range(10, 100):
            rsa = RSA.generate(i)
            plaintexts = [123456789, 17, 9999, 102930]
            for M in plaintexts:
                C = rsa.encrypt(M)
                MM = rsa.decrypt(C)
                self.assertEqual(M, MM)


if __name__ == '__main__':
    unittest.main()
