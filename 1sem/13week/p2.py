import numpy as np
import unittest


def mnk_factors(x, y) -> tuple:
    x = np.array(x)
    y = np.array(y)
    xxx = np.ones(len(x))
    matrix = np.vstack([x, xxx]).T
    a, b = np.linalg.lstsq(matrix, y, rcond=None)[0]
    # y = ax + b
    return round(a, 6), round(b, 6)


class TestOne(unittest.TestCase):
    def test_mnk_factors(self):
        self.assertEqual(mnk_factors([1, 2], [1, 2]), (1.0, 0.0))


class TestTwo(unittest.TestCase):
    def test_mnk_factors(self):
        self.assertEqual(mnk_factors([1, 2], [3, 5]), (2.0, 1.0))


class TestHalf(unittest.TestCase):
    def test_mnk_factors(self):
        self.assertEqual(mnk_factors([1, 2, 3], [1.5, 2, 2.5]), (0.5, 1.0))