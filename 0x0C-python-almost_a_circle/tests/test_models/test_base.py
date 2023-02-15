#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit testsing for instantiating of the Base class"""

    def test_base(self):
        first = Base()
        second = Base()
        self.assertEqual(first.id, second.id-1)

    def test_base_saves_id(self):
        first = Base(89)
        self.assertEqual(first.id, 89)


class TestBase_to_json_string(unittest.TestCase):
    """ Unittest for testing to_jason_string method"""

    def test_base_to_json_string_none(self):
        first = Base.to_json_string(None)
        self.assertEqual(first, "[]")

    def test_base_to_json_string_empty(self):

        second = Base.to_json_string([])
        self.assertEqual(second, "[]")

    def test_base_to_json_string_id(self):

        second = Base.to_json_string([{"id": 12}])
        self.assertEqual(second, "[{\"id\": 12}]")


if __name__ == '__main__':
    unittest.main()
