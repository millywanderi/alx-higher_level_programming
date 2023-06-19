#!/usr/bin/python3

""""This is a class module defining Rectangle tests"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
from unittest import mock
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):

    def test__constructor(self):
        r = Rectangle(4, 6)

        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)

        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_area(self):
        r = Rectangle(4, 6)

        self.assertEqual(r.area(), 24)

    def test_display(self):
        r = Rectangle(4, 6)

        exp_output = "####\n####\n####\n####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), exp_output)

    def test_update(self):
        r = Rectangle(4, 6)

        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        r = Rectangle(4, 6, 2, 3, 1)

        dic = {
                "id": 1,
                "width": 4,
                "height": 6,
                "x": 2,
                "y": 3
                }
        self.assertEqual(r.to_dictionary(), dic)

    def test_str(self):
        r = Rectangle(4, 6, 2, 3, 1)

        exp_output = "[Rectangle] (1) 2/3 - 4/6"
        self.assertEqual(str(r), exp_output)

    def test_setter(self):
        r = Rectangle(4, 6)

        r.y = 3

        self.assertEqual(r.y, 3)

    def test_setter_invalid(self):
        r = Rectangle(4, 6)

        with self.assertRaises(TypeError):
            r.y = "invalid"

    def test__set_negative(self):
        r = Rectangle(4, 6)

        with self.assertRaises(ValueError):
            r.y = -2
