import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_perimeter(self):
        c = Circle(5)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 5)

    def test_perimeter_zero(self):
        c = Circle(0)
        self.assertEqual(c.perimeter(), 0)

    def test_area(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), math.pi * 25)

    def test_area_zero(self):
        c = Circle(0)
        self.assertEqual(c.area(), 0)

if __name__ == "__main__":
    unittest.main()
    