from random import randrange
from .model_classes import Coord
from view import view_cases
from math import sqrt

class Apples:
	def __init__(self, nb_apples, line_cs_n):
		self.nb_apples: int = nb_apples
		self.apples = [
      		(randrange(line_cs_n), randrange(line_cs_n)) for _ in range(self.nb_apples)
        ]

	def render(self, case_size): view_cases(self.apples, 'red', case_size)

	def is_apple(self, coord: Coord):
		stack = []
		isApple = False

		for apple in self.apples:
			if apple != coord:
				stack.append(apple)
			else:
				isApple = True

		self.apples = stack
		if isApple:
			self.nb_apples -= 1
			return isApple
		return False