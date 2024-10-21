import unittest
import logging

logging.basicConfig(
    level=logging.NOTSET,
    filemode='w',
    format='%(asctime)s - %(name)s  - %(filename)s - %(lineno)s - %(funcName)s - %(levelname)s:  %(message)s'
)

info = logging.info
error = logging.error

def is_ord_char_even(*, char):
    
    return ord(char) % 2 == 0

result = is_ord_char_even(char = input('Ant char: '))
info(result)



class TestIsOrdCharEven(unittest.TestCase):
    def testEven(self):
        for char in ['d', 'b', '6', '2', 'a']:
            with self.subTest(char = char):
                self.assertIsInstance(is_ord_char_even(char = char), bool)
    def testOdd(self):
        self.assertFalse(is_ord_char_even(char = '3'))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)