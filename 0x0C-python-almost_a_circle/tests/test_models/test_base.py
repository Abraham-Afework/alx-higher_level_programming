#!/usr/bin/python3
import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
	def test_base(self):
		first = Base()
		second = Base()
		self.assertEqual(first.id, second.id-1)

	def test_multiplebase(self):
		first = Base()
		second = Base(5)
		third = Base()
		self.assertEqual(first.id, third.id-1)

	def test_nonebase(self):
		first = Base(None)
		second = Base(None)
		self.assertEqual(first.id, second.id - 1)

	def test_base_nbobjects(self):
		first = Base(None)
		second = Base(None)
		self.assertEqual(2, Base.__nb_objects)
		
if __name__ == '__main__':
	unittest.main()