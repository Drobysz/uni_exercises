from .model_classes import *
from view import view_case

def define_cell_coordinates(l_c, dir):
	match dir:
		case "Down":
			return (l_c[0], l_c[1] + 1)
		case "Up":
			return (l_c[0], l_c[1] - 1)
		case "Left":
			return (l_c[0] + 1, l_c[1])
		case "Right":
			return (l_c[0] - 1, l_c[1])

def define_next_coordinates(c, dir):
	match dir:
		case "Down":
			return (c[0], c[1] - 1)
		case "Up":
			return (c[0], c[1] + 1)
		case "Left":
			return (c[0] - 1, c[1])
		case "Right":
			return (c[0] + 1, c[1])

dirs = {'Up': 'Down', 'Down': 'Up', 'Left': 'Left', 'Right': 'Right'}
opposite = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}

class Snake:
	def __init__(s, size):
		s.size: int = size
		s.dir: Direction = 'Right'
		s.body: Body = [(i + 5, 20) for i in range(s.size)]

	@property
	def ln(s): return len(s.body)

	def render(s, case_size):
		for i in range(s.ln):
			view_case(s.body[i], 'green' if i < s.ln - 1 else 'blue', case_size)
 
	def isEncountered(s, w, cs):
		head = s.body[-1]
		rest_of_body = s.body[:s.ln-1]
		
		if head in rest_of_body:
			return True

		x_px = head[0] * cs
		y_px = head[1] * cs

		if x_px < cs or x_px >= w - cs or y_px < cs or y_px >= w - cs:
			return True
		return False

	def current_coordinates(s):
		return s.body[-1]

	def change_dir(s, key):
		if key in ('Up', 'Down', 'Left', 'Right'):
			dir = dirs[key] 
			if opposite[dir] != s.dir:
				s.dir = dirs[key]    
	def body_positive(s):
		for _ in range(3):
			l_c: Coord = s.body[0]
			n_c = define_cell_coordinates(l_c, s.dir)
			s.body = [n_c] + s.body[:]

	def shift_snake(s):
		for id in range(s.ln - 1):
			next_coord = s.body[id + 1]
			s.body[id] = next_coord
		s.body[s.ln - 1] = define_next_coordinates(s.body[s.ln - 1], s.dir)