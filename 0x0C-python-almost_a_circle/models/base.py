#!/usr/bin/python3
"""Base Class"""
class Base:
	"""
	class attribute initialized form 0
	"""
	__nb_objects = 0	
	def __init__(self, id=None):
		"""
		
		"""
		if id != None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects