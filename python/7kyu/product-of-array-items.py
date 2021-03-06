'''
Calculate the product of all elements in an array.

If the array is empty or None, return None.
'''
import unittest
from operator import mul
from functools import reduce

def product(numbers):
    return reduce(mul, numbers) if numbers else None

class ProductTest(unittest.TestCase):
    def test(self):
        self.assertEqual(product([5, 4, 1, 3, 9]), 540)
        self.assertEqual(product([-2, 6, 7, 8]), -672)
        self.assertEqual(product([10]), 10)
        self.assertEqual(product([0, 2, 9, 7]), 0)
        self.assertEqual(product(None), None)
        self.assertEqual(product([]), None)

if __name__ == '__main__':
    unittest.main()