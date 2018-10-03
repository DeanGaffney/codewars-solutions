'''
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
https://www.codewars.com/kata/basic-mathematical-operations/train/python
'''

import unittest
from operator import add, sub, mul, truediv

def basic_op(operator, value1, value2):
    return {'+': add, '-': sub, '*': mul, '/': truediv}[operator](value1, value2)


class BasicMathTest(unittest.TestCase):
    def test(self):
        self.assertEqual(basic_op('+', 4, 7), 11)
        self.assertEqual(basic_op('-', 15, 18), -3)
        self.assertEqual(basic_op('*', 5, 5), 25)
        self.assertEqual(basic_op('/', 49, 7), 7)


if __name__ == '__main__':
    unittest.main()
