import unittest


def prime(n: int, i=2) -> str:
    if not isinstance(n, int):
        raise TypeError('Required integer number')
    s = 0
    if n == 1:
        return ''
    while n % i == 0:
        s += 1
        n /= i
        n = int(n)
    if s == 0:
        return prime(n, i + 1)
    return (prime(n, i + 1) + f' {i}x{s}').lstrip()


class TestOne(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime(1), '')


class TestPrimes(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime(2), '2x1')
        self.assertEqual(prime(3), '3x1')
        self.assertEqual(prime(5), '5x1')
        self.assertEqual(prime(7), '7x1')
        self.assertEqual(prime(11), '11x1')


class TestNums(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime(8), '2x3')
        self.assertEqual(prime(9), '3x2')
        self.assertEqual(prime(48), '3x1 2x4')