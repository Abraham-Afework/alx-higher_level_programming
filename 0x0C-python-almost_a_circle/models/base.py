#!/usr/bin/python3
"""Define Base class model"""
import json
import csv


class Base:
    """
    Represents Base Model

    class attribute __nb_objects initialized form 0

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize a new base.
        Args:
            -id(int):The identity of Base
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
        if json_string is None:
            return []
        list_json = json.loads(json_string)
        return list_json

    @classmethod
    def create(cls, **dictionary):
        """" class method that creates an instance of class with pre-defined\
         attirbutes passed as key word arguments(kwargs)

         Returns:
                new instance of a class

         """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ Method that loads form the json file
                -opens the file name related to the class name
                -parses the the fetched string from the file to a list using
                - created empty list
                -append the each list after a class instance\
                 is created using create method
            Return:
                list of the fetched file

        """
        filename = str(cls.__name__+".json")
        all_list = []
        try:
            with open(filename) as file:
                fetched_string = file.read()

                fetched_list = cls.from_json_string(fetched_string)

                for data in fetched_list:
                    all_list.append(cls.create(**data))

        except FileNotFoundError:
            pass
        return all_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This method takes a list of objects and saves\
        it to a csv file with the name of the class.

        -param cls: the class that this method is called from
        -param list_objs: a list of objects of the class type
        Return:
             None
        """
        filename = str(cls.__name__) + ".csv"
        with open(filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            if cls.__name__ == "Rectangle":
                csv_writer.writerow(["id", "width", "height", "x", "y"])

                for obj in list_objs:
                    csv_writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])

            elif cls.__name__ == "Square":
                csv_writer.writerow(["id", "size", "x", "y"])
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        This method loads the objects of the class type\
         from a csv file with the name of the class.

        :param cls: the class that this method is called from
        :return: a list of objects of the class type
        """
        filename = str(cls.__name__) + ".csv"
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(reader)
            all_objs = []
            for row in csv_reader:
                if cls.__name__ == "Rectangle":
                    all_objs.append(cls(int(row[0]), int(row[1]), int(
                        row[2]), int(row[3]), int(row[4])))
                elif cls.__name__ == "Square":
                    all_objs.append(cls(int(row[0]), int(
                        row[1]), int(row[2]), int(row[3])))
            return all_objs
