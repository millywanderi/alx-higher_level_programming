from models.base import Base
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_to_jason_string(self):
        list_dictionaries = [{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]
        json_string = Base.to_json_string(list_dictionaries)
        
        results = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        self.assertEqual(json_string, results)

    def test_from_json_string(self):
        json_string = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        list_dictionaries = Base.from_json_string(json_string)

        results = [{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]
        self.assertEqual(list_dictionaries, results)

    def test_create(self):
        dic = {"id": 1}
        obj = Base(**dic)

        self.assertEqual(obj.id, 1)

    def test_save_to_file_csv(self):
        list_obj = [Base(1), Base(2)]
        Base.save_to_file_csv(list_obj)

        with open("Base.csv", "r") as file:
            csv_read = csv.reader(file)
            csv_content = [row for row in csv_read]

        result = [["id"], ["1"], ["2"]]
        self.assertEqual(csv_content, result)
    












