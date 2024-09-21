import unittest
from quest_10 import get_matrix, find_best_combination


class TestFunctions(unittest.TestCase):
    def test_get_matrix_1(self):
        N = 5
        edges = [(1, 3), (2, 5), (5, 4)]
        matrix = get_matrix(N, edges)
        self.assertEqual(matrix, [[0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 1, 0]])

    def test_get_matrix_2(self):
        N = 7
        edges = [(1, 3), (2, 3), (5, 4)]
        matrix = get_matrix(N, edges)
        self.assertEqual(matrix, [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_find_best_combination_1(self):
        N = 5
        K = 3
        matrix = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 1, 0]]
        best_combination = find_best_combination(N, K, matrix)
        self.assertEqual(best_combination, "2 4 5")

    def test_find_best_combination_2(self):
        N = 7
        K = 4
        matrix = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        best_combination = find_best_combination(N, K, matrix)
        self.assertEqual(best_combination, "1 2 3 4")


if __name__ == "__main__":
    unittest.main()
