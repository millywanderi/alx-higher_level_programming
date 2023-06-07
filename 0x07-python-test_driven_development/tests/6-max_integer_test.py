#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger class"""

    def test_mod_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_docstr_func(self):
        functDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functDoc) > 1)

    def test_signed_ints_floats(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([4, 5, 6]), 6)
        self.assertEqual(max_integer([4, 5, 6, -1]), 6)
        self.assertEqual(max_integer([1.1, 0.2]), 1.1)
        self.assertEqual(max_integer([-1.1, -0.2]), -1.1)
        self.assertEqual(max_integer([{1, 8}, {1}]), {1, 8})

    def test_str(self):
        self.assertEqual(max_integer("987"), '9')
        self.assertEqual(max_integer("abct"), 't')
        self.assertEqual(max_integer(["b", "v", "a"]), 'v')
        self.assertEqual(max_integer(["efg", "z"]), 'z')

    def test_list(self):
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])

    def test_err(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2}, {1, 2, 3})
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4})
        with self.assertRaises(TypeError):
            max_integer([-2, 1.1, "mine", {2, 6})
