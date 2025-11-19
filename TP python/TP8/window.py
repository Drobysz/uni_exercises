from fltk import *
from view import *
from models.apples import *
from models.snake import *

class Window: 
	def __init__(self, case_size, width):	
		self.case_size: int = case_size
		self.width: int = width
		self.nb_cases: int = (int(self.width / self.case_size) - 2) ** 2

		# assert (self.width % self.nb_cases == 0)
		cree_fenetre(self.width, self.width)
		texte(
			self.width // 2, self.width // 2,
			"Tapez sur une touche !", "red", "center"
		)

		attend_ev()
	
	def render_border(s):
		# Up
		rectangle(
			0, 0,
			s.width, s.case_size,
			'violet', 'violet'
		)

		# Down
		rectangle(
			0, s.width - s.case_size,
			s.width, s.width,
			'violet', 'violet'
		)
  
		# Left
		rectangle(
			0, 0,
			s.case_size, s.width,
			'violet', 'violet'
		)
  
		# Right
		rectangle(
			s.width - s.case_size, 0,
			s.width, s.width,
			'violet', 'violet'
		)

	def render(s, snake, apples):
		efface_tout()
		s.render_border()
		snake.render(s.case_size)
		apples.render(s.case_size)
		mise_a_jour()
 
	def win(s):
		efface_tout()
		texte(
			s.width // 2, s.width // 2,
			"Gagné! pour continuer clicker ou Esc pour finir", "green", "center"
		)

	def loss(s):
		efface_tout()
		texte(
			s.width // 2, s.width // 2,
			"Perdu! pour continuer clicker ou Esc pour finir", "red", "center"
		)