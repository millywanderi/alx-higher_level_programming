#!/usr/bin/python3

"""This class module defines square tests"""


import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test for the Square class"""
    def test_size_setter_invalid_type(self):
        """Tests validation of size setter"""
        s = Square(5)

        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_setter_invalid_value(self):
        """Test validation of the setter value"""
        s = Square(5)

        with self.assertRaises(ValueError):
            s.size = -1

    def test_update_args(self):
        """Test the update using argument args"""
        s = Square(5)

        s.update(10, 8, 2, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 2)

    def test_update_kwargs(self):
        """Test the update using argument kwargs"""
        s = Square(5)

        s.update(id=10, size=8, x=2, y=3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        """Tests for ditionary representation of Square"""
        s = Square(5, 2, 3, 10)
        dic = {
                "id": 10,
                "size": 5,
                "x": 2,
                "y": 3
                }
        self.assertEqual(s.to_dictionary(), dic)


if __name__ == "__main__":
    unittest.main()
