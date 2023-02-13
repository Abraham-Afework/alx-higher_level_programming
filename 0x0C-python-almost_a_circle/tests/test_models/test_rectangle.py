#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

	def test_no_args(self):
		with self.assertRaises(TypeError):
			Rectangle()

	def test_one_args(self):
		with self.assertRaises(TypeError):
			Rectangle(1)

	def test_two_args(self):
		first = Rectangle(1, 2)
		second = Rectangle(1, 2)
		self.assertEqual(first.id, second.id - 1)

	def test_three_args(self):
		first = Rectangle(1, 2, 3)
		second = Rectangle(1, 2, 3)
		self.assertEqual(first.id, second.id - 1)

	def test_morethan_five_args(self):
		with self.assertRaises(TypeError):
			Rectangle(1, 2, 3, 4, 5, 6)
		
