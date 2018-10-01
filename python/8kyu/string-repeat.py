'''
Write a function called repeatStr which repeats the given string string exactly n times.
'''
import unittest

def repeat_str(repeat, string):
    return string * repeat

class RepeatStringTest(unittest.TestCase):
    def test(self):
        self.assertEqual(repeat_str(4, 'a'), 'aaaa')
        self.assertEqual(repeat_str(3, 'hello '), 'hello hello hello ')
        self.assertEqual(repeat_str(2, 'abc'), 'abcabc')

if __name__ == '__main__':
    unittest.main()