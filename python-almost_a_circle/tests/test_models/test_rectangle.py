#!/usr/bin/python3
from models import rectangle
import unittest


class RectangleTest(unittest.TestCase):

    def test_doc(self):
        self.assertTrue(len(rectangle.__doc__) > 1)
        self.assertTrue(len(rectangle.Rectangle.__doc__) > 1)
        self.assertTrue(len(rectangle.Rectangle.__init__.__doc__) > 1)
        self.assertTrue(len(rectangle.Rectangle.area.__doc__) > 1)
        self.assertTrue(len(rectangle.Rectangle.display.__doc__) > 1)
        self.assertTrue(len(rectangle.Rectangle.update.__doc__) > 1)
        self.assertTrue(len(rectangle.Rectangle.__str__.__doc__) > 1)
        self.assertTrue(len(rectangle.Rectangle.to_dictionary.__doc__) > 1)

    def test_Rectangle(self):
        self.assertRaises(TypeError, rectangle.Rectangle("2", 3))
        self.assertRaises(ValueError, rectangle.Rectangle(-2, 0))
        self.assertRaises(TypeError, rectangle.Rectangle(2, 2, "2"))
        self.assertRaises(ValueError, rectangle.Rectangle(2, 2, 2, -1))


if __name__ == "__main__":
    unittest.main()
