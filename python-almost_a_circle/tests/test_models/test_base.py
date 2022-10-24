#!/usr/bin/python3
""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test(unittest.TestCase):
    ""
    def base(self):
        ""
        b1 = Base()
        self.assertEqual(b1.id(), 1)
        b2 = Base()
        self.assertEqual(b2.id(), 2)
        b3 = Base()
        self.assertEqual(b3.id(10), 10)