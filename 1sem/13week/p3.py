import random
import unittest


def quicksort(a):
    if len(a) <= 1:
        return a
    else:
        q = random.choice(a)
        l = [elem for elem in a if elem < q]
        m = [q] * a.count(q)
        r = [elem for elem in a if elem > q]
        return quicksort(l) + m + quicksort(r)


class TestRandom(unittest.TestCase):
    def test_quicksort(self):
        randomlist = []
        for i in range(0, 2000):
            n = random.randint(1, 10000)
            randomlist.append(n)
        self.assertEqual(quicksort(randomlist), sorted(randomlist))


class TestEquals(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])