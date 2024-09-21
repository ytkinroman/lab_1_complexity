import unittest
from quest_8 import count_mag


class TestCountMag(unittest.TestCase):
    def test_count_mag(self):
        self.assertEqual(count_mag(3, 1), 9)
        self.assertEqual(count_mag(4, 2), 20)
        self.assertEqual(count_mag(5, 3), 48)
