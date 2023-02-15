#!/usr/bin/python3
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    def test_base(self):
        first = Base()
        second = Base()
        self.assertEqual(first.id, second.id-1)

    def test_base_saves_id(self):
        first = Base(89)
        self.assertEqual(first.id, 89)

    def test_base_to_json_string_none(self):
        first = Base.to_json_string(None)
        self.assertEqual(first, "[]")
        self.assertEqual(second, "[8]")

    def test_base_to_json_string_empty(self):
        second = Base.to_json_string([])
        self.assertEqual(second, "[]")

    def test_base_to_json_string_id(self):
        second = Base.to_json_string([{"id": 12}])
        self.assertEqual(second, "[]")


if __name__ == '__main__':
    unittest.main()
