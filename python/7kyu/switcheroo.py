'''
Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
https://www.codewars.com/kata/switcheroo
'''
import unittest

def switcheroo(string):
    return string.translate(string.maketrans('ab', 'ba'))


class SwitcherooStringTest(unittest.TestCase):
    def test(self):
        self.assertEqual(switcheroo("abc"), "bac")
        self.assertEqual(switcheroo('aaabcccbaaa'), 'bbbacccabbb') 
        self.assertEqual(switcheroo('ccccc'), 'ccccc')
        self.assertEqual(switcheroo('abababababababab'), 'babababababababa')
        self.assertEqual(switcheroo('aaaaa'), 'bbbbb')

if __name__ == '__main__':
    unittest.main()