#!/usr/bin/python3
import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
	def test_base(self):
		first = Base()
		second = Base()
		self.assertEqual(first.id, second.id-1)
	
if __name__ == '__main__':
	unittest.main()