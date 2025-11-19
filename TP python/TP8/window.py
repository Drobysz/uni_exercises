from fltk import *
from view import *
from models.apples import *
from models.snake import *

class Window: 
	def __init__(self, case_size, width):	
		self.case_size: int = case_size
		self.width: int = width
		self.nb_cases: int = int(self.width / self.case_size)

		assert (self.width % self.nb_cases == 0)
		cree_fenetre(self.width, self.width)
		texte(
			self.width // 2, self.width // 2,
			"Tapez sur une touche !", "red", "center"
		)

		attend_ev()
 
	def render(self, snake, apples):
		efface_tout()
		snake.render(self.case_size)
		apples.render(self.case_size)
		mise_a_jour()
 
	def win(self):
		efface_tout()
		texte(
			self.width // 2, self.width // 2,
			"Gagné! pour continuer clicker ou Esc pour finir", "green", "center"
		)

	def loss(self):
		efface_tout()
		texte(
			self.width // 2, self.width // 2,
			"Perdu! pour continuer clicker ou Esc pour finir", "red", "center"
		)