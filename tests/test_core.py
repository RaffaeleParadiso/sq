# import sys
# sys.path.append('C:/Users/raffy/Desktop/temp/sqr/sq')
import unittest

from core import square

class TestCore(unittest.TestCase):
    """Unittest for core module"""

    def test_float(self):
        ''' test with floats'''
        self.assertAlmostEqual(square(2.), 4.)

if __name__ == '__main__':
    unittest.main()
