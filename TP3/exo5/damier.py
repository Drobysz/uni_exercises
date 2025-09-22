from fltk import *

if __name__ == '__main__':
	largeurFenetre = 400
	hauteurFenetre = 400
	length = 400/12
	x = 0
	y = 0
	clr1 = 'black'
	clr2 = 'white'
 
	cree_fenetre(largeurFenetre, hauteurFenetre)
	for i in range(12):
		for j in range(12):
			clr_fin = clr1 if j % 2 == 0 else clr2
			rectangle(x, y, x + length, y + length, clr_fin, clr_fin)
			x += length
		x = 0
		y += length
		tmp = clr1
		clr1 = clr2
		clr2 = tmp

	attend_clic_gauche()
	ferme_fenetre()