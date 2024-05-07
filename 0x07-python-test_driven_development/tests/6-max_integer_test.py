#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_strings(self):
        self.assertEqual(max_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),                          [7, 8, 9])
        self.assertEqual(max_integer([[9, 8, 7], [6, 5, 4], [3, 2, 1]]),
                         [9, 8, 7])
