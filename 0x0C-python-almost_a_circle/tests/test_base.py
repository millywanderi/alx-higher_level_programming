from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):

    def test_to_jason_string(self):
        list_dict = [{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]
        json_string = Base.to_json_string(list_dict)

        results = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        self.assertEqual(json_string, results)

    def test_from_json_string(self):
        json_string = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        list_dictionaries = Base.from_json_string(json_string)

        results = [{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]
        self.assertEqual(list_dictionaries, results)

    def test_save_to_file(self):
        r1 = Rectangle(4, 6)
        r2 = Rectangle(1, 2)
        s1 = Square(5)
        s2 = Square(6)

        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1, s2])

        assert os.path.exists("Rectangle.json")
        assert os.path.exists("Square.json")

    def test_create(self):
        dic = {"id": 1}
        obj = Base(**dic)

        self.assertEqual(obj.id, 1)

    def test_load_from_file(self):
        r1 = Rectangle(4, 6)
        r2 = Rectangle(1, 2)
        s1 = Square(5)
        s2 = Square(6)

        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1, s2])

        rect = Rectangle.load_from_file()
        squr = Square.load_from_file()

        assert len(rect) == 2
        assert isinstance(rect[0], Rectangle)
        assert isinstance(rect[1], Rectangle)

        assert len(squr) == 2
        assert isinstance(squr[0], Square)
        assert isinstance(squr[1], Square)

    def test_csv_method(self):
        r1 = Rectangle(4, 6)
        r2 = Rectangle(1, 2)
        s1 = Square(5)
        s2 = Square(6)

        Rectangle.save_to_file_csv([r1, r2])
        Square.save_to_file_csv([s1, s2])

        load_rectangle = Rectangle.load_from_file_csv()
        load_square = Square.load_from_file_csv()

        assert len(load_rectangle) == 2
        assert len(load_square) == 2

    def test_to_load_csv(self):
        load_rectangle = Rectangle.load_from_file_csv()
        load_square = Square.load_from_file_csv()

        assert isinstance(load_rectangle[0], Rectangle)
        assert isinstance(load_rectangle[1], Rectangle)

        assert isinstance(load_square[0], Square)
        assert isinstance(load_square[1], Square)

    def test_load_object(self):
        load_rectangle = Rectangle.load_from_file_csv()
        load_square = Square.load_from_file_csv()

        assert load_square[0].size == 5
        assert load_square[1].size == 6

        assert load_rectangle[0].width == 4
        assert load_rectangle[0].height == 6

        assert load_rectangle[1].width == 1
        assert load_rectangle[1].height == 2
