from fltk import *

if __name__ == '__main__':
    n = int(input("Enter the number of circles to draw: "))
    largeurFenetre = 400
    hauteurFenetre = 400
    cree_fenetre(largeurFenetre, hauteurFenetre)
    
    # 1 + 2
    
    D = 400/n
    x_shift = D/2
    y_shift = D/2
    
    # for i in range(n):
    #     cercle(x_shift, y_shift, D/2, "red")
    #     x_shift += D
        
    # 3
    
    for i in range(n):
        for j in range(n):
            cercle(x_shift, y_shift, D/2, "red")
            x_shift += D
        y_shift += D
        x_shift = D/2
            

    attend_clic_gauche()
    ferme_fenetre()
