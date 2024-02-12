#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):

        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_invalid_width(self):

        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_invalid_height(self):

        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            rect.height = "invalid_height"

    def test_invalid_x(self):

        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            rect.x = -2

    def test_invalid_y(self):

        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            rect.y = "invalid_y"

if __name__ == "__main__":
    unittest.main()
