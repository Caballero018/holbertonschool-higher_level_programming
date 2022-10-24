#!/usr/bin/python3
import unittest
from models import base


class BaseTest(unittest.TestCase):

    def test_doc(self):
        self.assertTrue(len(base.__doc__) > 1)
        self.assertTrue(len(base.Base.__doc__) > 1)
        self.assertTrue(len(base.Base.__init__.__doc__) > 1)
        self.assertTrue(len(base.Base.to_json_string.__doc__) > 1)
        self.assertTrue(len(base.Base.save_to_file.__doc__) > 1)
        self.assertTrue(len(base.Base.from_json_string.__doc__) > 1)
        self.assertTrue(len(base.Base.create.__doc__) > 1)
        self.assertTrue(len(base.Base.load_from_file.__doc__) > 1)

    def test_Base(self):
        b1 = base.Base()
        b2 = base.Base(98)
        self.assertNotEqual(b1, b2)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 98)


if __name__ == "__main__":
    unittest.main()
