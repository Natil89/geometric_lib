import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):

    def test_area_valid(self):

        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)

    def test_area_zero_vaiues(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_area_negative_vaiues(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_area_non_number(self):
	with self.assertRaises(ValueError):
            area("abc")

	with self.assertRaises(ValueError):
            area(None)

    def test_perimeter_valid(self):

        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero_vaiues(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_vaiues(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_perimeter_non_number(self):
	with self.assertRaises(ValueError):
            perimeter("abc")

	with self.assertRaises(ValueError):
            perimeter(None)


if __name__ == '__main__':
    unittest.main()

