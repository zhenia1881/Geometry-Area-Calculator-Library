import unittest
from math import pi
from geometry import Circle, Triangle, calculate_area, is_right_angled


class TestGeometry(unittest.TestCase):
    def test_circle(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), pi * 25)
        self.assertFalse(is_right_angled(c))

        with self.assertRaises(ValueError):
            Circle(-1)

    def test_triangle(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0)
        self.assertTrue(is_right_angled(t))

        t2 = Triangle(3, 4, 6)
        self.assertFalse(is_right_angled(t2))

        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    def test_polymorphism(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [pi * 4, 6.0]
        for shape, expected in zip(shapes, areas):
            self.assertAlmostEqual(calculate_area(shape), expected)


if __name__ == '__main__':
    unittest.main()