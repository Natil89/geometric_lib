import unittest
import math
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):

    def test_area_valid_triangle(self):
        self.assertAlmostEqual(area(3, 4, 5), 6.0, places=2)
        self.assertAlmostEqual(area(2, 2, 2), math.sqrt(3), places=2)

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 2, 10)

    def test_area_zero_values(self):
        with self.assertRaises(ValueError):
            area(0, 4, 5)
        with self.assertRaises(ValueError):
            area(3, 0, 5)
        with self.assertRaises(ValueError):
            area(3, 4, 0)

    def test_area_negative_values(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)
        with self.assertRaises(ValueError):
            area(3, -4, 5)
        with self.assertRaises(ValueError):
            area(3, 4, -5)

    def test_area_non_number(self):
        with self.assertRaises(TypeError):
            area("3", 4, 5)
        with self.assertRaises(TypeError):
            area(3, None, 5)
        with self.assertRaises(TypeError):
            area(3, 4, "a")

    def test_perimeter_valid_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(2, 2, 2), 6)

    def test_perimeter_zero_values(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 0, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, 0)

    def test_perimeter_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)

    def test_perimeter_non_number(self):
        with self.assertRaises(TypeError):
            perimeter("3", 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, None, 5)
        with self.assertRaises(TypeError):
            perimeter(3, 4, "a")


if __name__ == "__main__":
    unittest.main()
