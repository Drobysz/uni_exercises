from fltk import *

if __name__ == '__main__':
    lst = [100, 200, 350, 40, 160, 210, 130, 80, 170, 300, 280, 210, 320, 30, 70]
    largeurs = [20, 19, 18, 24, 30, 12, 29, 30, 26, 15, 22, 26, 21, 27, 13]
    largeurFenetre = 400
    hauteurFenetre = 400
    cree_fenetre(largeurFenetre, hauteurFenetre)
    x = 0
    y = hauteurFenetre
    
    for i in range(len(lst)):
        color = "blue" if i % 2 else "black"
        rectangle(x, y, x + largeurs[i], y - lst[i], color, color)
        x += largeurs[i]

    attend_clic_gauche()
    ferme_fenetre()
