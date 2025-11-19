from fltk import *

def view_case(cell, color, size):
		b1, b2 = (cell[0] * size) + size, (cell[1] * size) + size
		e1, e2 = b1 + size, b2 + size,

		rectangle(
			b1, b2,
			e1, e2,
			color,
			color
		)

def view_cases(lst, color, size):
	for cell in lst:
		view_case(cell, color, size)