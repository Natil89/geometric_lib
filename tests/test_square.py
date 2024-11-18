import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):

    def test_area_valid(self):
        self.assertAlmostEqual(area(1), 1)
        self.assertAlmostEqual(area(2), 4)

    def test_area_zero_values(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_area_negative_values(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_area_non_number(self):
        with self.assertRaises(TypeError):
            area("3")
        with self.assertRaises(TypeError):
            area(None)

    def test_perimeter_valid(self):
        self.assertAlmostEqual(perimeter(1), 4)
        self.assertAlmostEqual(perimeter(2), 8)

    def test_perimeter_zero_values(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_perimeter_non_number(self):
        with self.assertRaises(TypeError):
            perimeter("3")
        with self.assertRaises(TypeError):
            perimeter(None)


if __name__ == "__main__":
    unittest.main()
