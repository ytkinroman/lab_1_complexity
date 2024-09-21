import unittest
from quest_6 import polynomial_values


class TestComputePolynomialValues(unittest.TestCase):
    def test_polynomial_values_1(self):
        N = 2
        M = 5
        MOD = 10
        coefficients = [1, 5, 4]
        x_values = [0, 1, 2, 3, 4]
        expected_results = [4, 0, 8, 8, 0]
        self.assertEqual(polynomial_values(coefficients, x_values, MOD), expected_results)

    def test_polynomial_values_2(self):
        N = 5
        M = 9
        MOD = 10
        coefficients = [1, 0, 0, 0, 0, 0]
        x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_results = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(polynomial_values(coefficients, x_values, MOD), expected_results)


