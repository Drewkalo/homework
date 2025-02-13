import numpy as np
import unittest

def mnk(x, y):
    x, y = np.array(x), np.array(y)

    if len(x) < 2 or len(x) != len(y) or np.all(x == x[0]): 
        return None
    
    b = ((x*y).mean() - (x.mean() * y.mean())) / ((x**2).mean() - (x.mean())**2)

    a = y.mean() - b * x.mean()

    k = ((x*y).mean()) / ((x**2).mean())

    return [a, b, k]

x = [1, 2, 3, 4, 5]
y = [2, 3.2, 3.9, 4.5, 5.1]
print(mnk(x, y))


class TestMNK(unittest.TestCase):
    def test_valid_data(self):
        self.assertTrue(isinstance(mnk([1, 2, 3], [1, 2, 3]),list))

    def test_empty_input(self):
        self.assertIsNone(mnk([], []))

    def test_mismatched_lengths(self):
        self.assertIsNone(mnk([1, 2, 3], [1, 2]))
        
    def test_constant_x(self):
        self.assertIsNone(mnk([1, 1, 1], [1, 2, 3]))

unittest.main()