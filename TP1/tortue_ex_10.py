from turtle import *
from math import *

if __name__ == '__main__':
	window_width = window_width()
	window_height = window_height() 
	print("taille de la fenêtre : (", window_width, ",", window_height, ")")

	#### debut de partie a modifier ####

	nbLines=int(input("Define number of sides : "))

	length=int(input("Input length of square : "))
 
	R = length / (2 * sin(pi / nbLines))

	angle = 360 / nbLines

	xInit = -length / 2

	yInit = (-R * cos(pi / nbLines))


	#### fin de partie a modifier ####

	### Ne pas modifier ce qui suit ###
	reset()
	up()
	goto(xInit, yInit)
	down()
	a=0
	while a<nbLines:
	  a+=1
	  forward(length)
	  left(angle)
	 
	exitonclick()
