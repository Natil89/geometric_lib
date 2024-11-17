import unittest
import math
from calculate import calc


class TestCalcFunction(unittest.TestCase):
    def test_valid_circle_area(self):
        self.assertEqual(calc('circle', 'area', [5]), f'area of circle is {math.pi * 25}')

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('hexagon', 'area', [5])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [5])

    def test_invalid_sizes(self):
        with self.assertRaises(TypeError):
            calc('circle', 'area', [3, 'a', 5])

    def test_invalid_size_count(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', [5, 6])

if __name__ == "__main__":
    unittest.main()
