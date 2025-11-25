import unittest
from math import pi

import rectangle
import triangle
import circle


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area = rectangle.area(10, 0)
        self.assertEqual(area, 0)

        per = rectangle.perimiter(10, 0)
        self.assertEqual(per, 20)
    
    def test_square(self):
        area = rectangle.area(5, 5)
        self.assertEqual(area, 25)

        per = rectangle.perimiter(5, 5)
        self.assertEqual(per, 20)

    def test_one_mul(self):
        area = rectangle.area(1, 1000)
        self.assertEqual(area, 1000)

        per = rectangle.perimiter(1, 1000)
        self.assertEqual(per, 2002)

    def test_float(self):
        area = rectangle.area(10.01, 500)
        self.assertEqual(area, 5005)

        per = rectangle.perimiter(10.01, 500)
        self.assertAlmostEqual(per, 1020.02)


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        area = triangle.area(10, 0)
        self.assertEqual(area, 0)

        per = triangle.perimiter(10, 0, 10)
        self.assertEqual(per, 20)
    
    def test_equal_sides(self):
        per = triangle.perimiter(2, 2, 2)
        self.assertEqual(per, 6)

    def test_one_mul(self):
        area = triangle.area(50, 1)
        self.assertAlmostEqual(area, 25)

    def test_point(self):
        area = triangle.area(0, 0)
        self.assertEqual(area, 0)

        per = triangle.perimiter(0, 0, 0)
        self.assertEqual(per, 0)


class CircleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        area = circle.area(0)
        self.assertEqual(area, 0)

        per = circle.perimiter(0)
        self.assertEqual(per, 0)
    
    def test_one_radius(self):
        area = circle.area(1)
        self.assertAlmostEqual(area, pi)

        per = circle.perimiter(1)
        self.assertAlmostEqual(per, 2 * pi)

    def test_funny_radius1(self):
        area = circle.area(1 / pi)
        self.assertAlmostEqual(area, 1 / pi)

        per = circle.perimiter(1 / pi)
        self.assertAlmostEqual(per, 2)

    def test_funny_radius1(self):
        area = circle.area(1 / (pi ** 0.5))
        self.assertAlmostEqual(area, 1)

        per = circle.perimiter(1 / (pi ** 0.5))
        self.assertAlmostEqual(per, 2 * (pi ** 0.5))

