#!/usr/bin/python3

"""This class module defines square tests"""


import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    def test_size_setter_invalid_type(self):
        s = Square(5)

        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_setter_invalid_value(self):
        s = Square(5)

        with self.assertRaises(ValueError):
            s.size = -1

    def test_update_args(self):
        s = Square(5)

        s.update(10, 8, 2, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 2)

    def test_update_kwargs(self):
        s = Square(5)

        s.update(id=10, size=8, x=2, y=3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 10)
        dic = {
                "id": 10,
                "size": 5,
                "x": 2,
                "y": 3
                }
        self.assertEqual(s.to_dictionary(), dic)
