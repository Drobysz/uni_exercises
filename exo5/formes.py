############# Ne pas modifier ##################
from fltk import *

################################################

# C)
rect1_width, rect1_height = int(input("Width (rectangle blue): ")), int(input("Height (rectangle blue): "))
rect2_width, rect2_height = int(input("Width (rectangle red): ")), int(input("Height (rectangle red): "))


############# Ne pas modifier ##################
if __name__ == '__main__':
    cree_fenetre(400, 400)
    x1, y1 = attend_clic_gauche()
    rectangle(x1, y1, x1 + rect1_width, y1 + rect1_height, "blue", "blue")
    x2, y2 = attend_clic_gauche()
    rectangle(x2, y2, x2 + rect2_width, y2 + rect2_height, "red", "red")
    mise_a_jour()
    print("Coin supérieur gauche rectangle bleu : (" + str(x1) + "," + str(y1) + ")")
    print("Coin supérieur gauche rectangle bleu : (" + str(x2) + "," + str(y2) + ")")
    ############################################

    # A)
    
    intersection = ((x2 >= x1 and x2 <= x1 + rect1_width) or (x2 + rect2_width >= x1 and x2 + rect2_width <= x1 + rect1_width)) and ((y2 >= y1 and y2 <= y1 + rect1_height) or (y2 + rect2_height >= y1 and y2 + rect2_height <= y1 + rect1_height))
    inside = (x2 >= x1 and (x2 + rect2_width) <= (x1 + rect1_width)) and (y2 >= y1 and y2 + rect2_height <= y1 + rect1_width)
    
    if intersection:
        if inside:
            print("Rouge contenu dans Bleu")
        else:
            print("Intersection")
    else:
        print("Pas d'intersection")

    # B) 2 test
    ############# Ne pas modifier ##############
    attend_clic_gauche()
    ferme_fenetre()
