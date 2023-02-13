#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

	def test_no_args(self):
		with self.assertRaises(TypeError):
			Square()

	def test_one_args(self):
		first = Square(1)
		second = Square(2)
		self.assertEqual(first.id, second.id - 1)

	def test_two_args(self):
		first = Square(1, 2)
		second = Square(1, 2)
		self.assertEqual(first.id, second.id - 1)

	def test_three_args(self):
		first = Square(1, 2, 3)
		second = Square(1, 2, 3)
		self.assertEqual(first.id, second.id - 1)

	def test_morethan_four_args(self):
		with self.assertRaises(TypeError):
			Square(1, 2, 3, 4, 5, 6)