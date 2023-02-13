#!/usr/bin/python3
import json
"""Base Class"""


class Base:
    """
    class attribute initialized form 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that  generates the JSON string of dictionary:
        Returns:
            If list_dictionaries is None or empty,\
            return the string: "[]"
            else,the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes the JSON string representation \
        of list_objs to a file:

        list_objs : a list of instances who inherits of Base
        If list_objs is None, save an empty list
        If already exists overwrite the file

        """
        filename = cls.__name__ + ".json"
        list_all = []

        if list_objs is None:
            list_all = "[]"
        else:
            for obj in list_objs:
                list_all.append(obj.to_dictionary())
            list_all = cls.to_json_string(list_all)
        with open(filename, "w") as file:
            file.write(list_all)

    @staticmethod
    def from_json_string(json_string):
        """
        a static method converts a string to a list
        """
        list_json = json.loads(json_string)
        return list_json
