#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_constructor_without_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_constructor_with_id(self):
        obj = Base(id=2)
        self.assertEqual(obj.id, 2)

    def test_multiple_instances(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()

        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj2.id, obj3.id)
        self.assertNotEqual(obj1.id, obj3.id)
        
if __name__ == "__main__":
    unittest.main()