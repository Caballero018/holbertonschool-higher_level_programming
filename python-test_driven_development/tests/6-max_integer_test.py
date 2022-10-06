#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 3, 4, 8]), 8)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)
        self.assertEqual(max_integer([9]), 9)