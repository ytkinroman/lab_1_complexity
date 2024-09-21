import unittest
from quest_1 import calculate_distances, format_distances, format_houses


class TestCalculateDistances(unittest.TestCase):
    def test_format_houses(self):
        """Проверка на правила форматирование."""
        self.assertEqual(format_houses("1 0 2 3 0 5 4"), [1, 0, 2, 3, 0, 5, 4])
        self.assertEqual(format_houses("0 2 3 4 0 1"), [0, 2, 3, 4, 0, 1])
        self.assertEqual(format_houses("5 6 7 0 1"), [5, 6, 7, 0, 1])

    def test_values_format_houses(self):
        """В последовательности должен быть ноль."""
        self.assertRaises(ValueError, format_houses, "8 4 3 1 6 7")
        self.assertRaises(ValueError, format_houses, "1 2 3 6 7 8")

    def test_number_format_houses(self):
        """Номера домов не могут превосходить 10^9."""
        self.assertRaises(ValueError, format_houses, "1 2 3 6 7 100000000000")
        self.assertRaises(ValueError, format_houses, "1 2 100000000000 6 7 8")

    def test_seen_format_houses(self):
        """Номера домов должны быть уникальными."""
        self.assertRaises(ValueError, format_houses, "1 2 3 6 7 1")
        self.assertRaises(ValueError, format_houses, "6 5 4 1 2 4")

    def test_calculate_distances(self):
        """Проверка расчёта дистанции."""
        self.assertEqual(calculate_distances(5, "0 1 4 9 0"), "0 1 2 1 0")
        self.assertEqual(calculate_distances(6, "0 7 9 4 8 20"), "0 1 2 3 4 5")
        self.assertEqual(calculate_distances(13, "0 2 3 1 11 13 14 7 9 4 8 20 19"), "0 1 2 3 4 5 6 7 8 9 10 11 12")
        self.assertEqual(calculate_distances(13, "0 2 3 1 11 13 14 7 0 4 8 20 19"), "0 1 2 3 4 3 2 1 0 1 2 3 4")
        self.assertEqual(calculate_distances(100,  "1 2 3 4 5 6 7 8 0 9 10 11 12 13 14 15 16 17 18 19 20 21 0 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 0 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 0 68 69 70 71 72 73 74 75 76 77 78 79 80 0 81 82 83 84 0 85 86 87 88 89 90 91 92 93 94 95 0 96 97 98 99 100"), "8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 6 5 4 3 2 1 0 1 2 2 1 0 1 2 3 4 5 6 5 4 3 2 1 0")

    def test_format_distances(self):
        """Проверка итогового форматирования."""
        self.assertEqual(format_distances([1, 2, 3, 1, 2, 3]), "1 2 3 1 2 3")
        self.assertEqual(format_distances([0, 1, 2, 0]), "0 1 2 0")
        self.assertEqual(format_distances([1, 3, 4, 6, 7, 10]), "1 3 4 6 7 10")

