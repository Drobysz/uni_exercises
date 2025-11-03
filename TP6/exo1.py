import doctest
from random import randrange

def pretty_matrix_print(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=' ')
        print('')

def create_random_matrix(h, w):
    M = []
    
    for _ in range(h):
        row = []
        for _ in range(w):
            row.append(randrange(10))
        M.append(row)
    return M

def cherche(M, el):
    """
    >>> cherche([[]],0)
    False
    >>> cherche([[0]],0)
    True
    >>> cherche([[1]],0)
    False
    >>> cherche([[1,1,1],[2,2,2]],0)
    False
    >>> cherche([[1,1,1],[2,2,2]],2)
    True
    """
    for i in range(len(M)):
        for j in range(len(M[i])):
            if el == M[i][j]:
                return True
    return False

def somme_colonnes(M):
    """
    >>> somme_colonnes([[]])
    []
    >>> somme_colonnes([[0]])
    [0]
    >>> somme_colonnes([[1,2]])
    [1, 2]
    >>> somme_colonnes([[1,2],[3,4],[5,6]])
    [9, 12]
    >>> somme_colonnes([[1,2,3],[4,5,6]])
    [5, 7, 9]
    """
    sl = []
    for i in range(len(M[0])):
        s = 0
        for j in range(len(M)):
            s += M[j][i]
        sl.append(s)
    return sl

def annule_diagonales(M):
    """
    >>> annule_diagonales([[]])
    [[]]
    >>> annule_diagonales([[1,2],[3,4]])
    [[0, 0], [0, 0]]
    >>> annule_diagonales([[1,2,3],[4,5,6],[7,8,9]])
    [[0, 2, 0], [4, 0, 6], [0, 8, 0]]
    >>> t = [[8, 5, 1, 6, 7], [7, 1, 8, 1, 2], [3, 2, 5, 4, 8], [5, 5, 7, 4, 1], [9, 7, 4, 5, 7]]
    >>> annule_diagonales(t)
    [[0, 5, 1, 6, 0], [7, 0, 8, 0, 2], [3, 2, 0, 4, 8], [5, 0, 7, 0, 1], [0, 7, 4, 5, 0]]
    >>> t = [[8, 5, 1, 6, 7], [7, 1, 8, 1, 2], [3, 2, 5, 4, 8]]
    >>> annule_diagonales(t)
    [[8, 5, 1, 6, 7], [7, 1, 8, 1, 2], [3, 2, 5, 4, 8]]
    """
    # I erased "print(t)", since I considered that You added it accidently.
    
    new_M = M[:]
    ln = len(M)
    lnx = len(M[0])
    
    if ln == 0:
        return []
    elif lnx == 0:
        return [[]]
    elif ln != lnx:
        return M

    for i in range(ln):
        new_M[i][i] = 0
        new_M[i][ln - i - 1] = 0
    return new_M

def compacte(m1, m2):
    """
    >>> compacte([[]],[[]])
    [[]]
    >>> compacte([[1]],[[2]])
    [[[1, 2]]]
    >>> compacte([[]],[[2]])
    >>> compacte([[3, 4, 8, 7, 3], [8, 2, 2, 2, 6]],[[9, 1, 6, 1, 7], [2, 3, 9, 8, 6]])
    [[[3, 9], [4, 1], [8, 6], [7, 1], [3, 7]], [[8, 2], [2, 3], [2, 9], [2, 8], [6, 6]]]
    """
    lnx1, lnx2 = len(m1[0]), len(m2[0])
    lny1, lny2 = len(m1), len(m2)

    if (lny1 != lny2) or (lnx1 != lnx2):
        return None

    M = []
    for i in range(lny1):
        row = []
        for j in range(lnx1):
            row.append([m1[i][j], m2[i][j]])
        M.append(row)
    return M

def define_somme_voisins(M, x, y):
    s = 0
    lastX = len(M[y]) - 1
    lastY = len(M) - 1
    
    # x
    if x < lastX:
        s += M[y][x + 1]
    if x > 0:
        s += M[y][x - 1]
    # y
    if y < lastY:
        s += M[y + 1][x]
    if y > 0:
        s += M[y - 1][x]
    return s

def cherche_somme_voisins(M):
    """
    >>> cherche_somme_voisins([[]])
    >>> cherche_somme_voisins([[1]])
    >>> cherche_somme_voisins([[1,1]])
    (0, 0)
    >>> cherche_somme_voisins([[8, 3, 3, 3], [5, 6, 1, 5], [8, 7, 9, 1]])
    (0, 0)
    >>> cherche_somme_voisins([[7, 3, 3, 3], [5, 6, 1, 5], [0, 7, 9, 1]])
    (1, 3)
    >>> cherche_somme_voisins([[3, 4, 8, 7, 3], [1, 8, 2, 2, 6], [9, 1, 6, 1, 7], [2, 3, 9, 8, 6]])
    (1, 1)
    >>> cherche_somme_voisins([[3, 4, 8, 7, 3], [1, 7, 2, 2, 6], [9, 1, 6, 1, 7], [2, 3, 9, 8, 6]])
    """
    for i in range(len(M)):
        for j in range(len(M[i])):
            s = define_somme_voisins(M, j, i)
            if s == M[i][j]:
                return (i, j)
    return None

def decalage_cyclique(M):
    """
    >>> decalage_cyclique([[]])
    [[]]
    >>> decalage_cyclique([[1]])
    [[1]]
    >>> decalage_cyclique([[1,2]])
    [[2, 1]]
    >>> decalage_cyclique([[1,2,3],[8,0,4],[7,6,5]])
    [[8, 1, 2], [7, 0, 3], [6, 5, 4]]
    >>> decalage_cyclique([[1,2,3],[6,5,4]])
    [[6, 1, 2], [5, 4, 3]]
    """
    shifted_M = M[:]
    lnY = len(M)
    lnX = len(M[0])

    if lnY == 0:
        return []
    elif lnX == 0:
        return [[]]

    replace_by = M[0][0]

    for i in range(lnX - 1):
        temp = M[0][i + 1]
        M[0][i + 1] = replace_by
        replace_by = temp

    for i in range(lnY - 1):
        temp = M[i + 1][lnX - 1]
        M[i + 1][lnX - 1] = replace_by
        replace_by = temp

    for i in range(lnX - 1, 0, -1):
        temp = M[lnY - 1][i - 1]
        M[lnY - 1][i - 1] = replace_by
        replace_by = temp

    for i in range(lnY - 1, 0, -1):
        temp = M[i - 1][0]
        M[i - 1][0] = replace_by
        replace_by = temp
	
    return shifted_M

if __name__ == '__main__':
    # la ligne suivante active les doctests dans le programme
    doctest.testmod()

    M = [
		[8, 3, 3, 3],
		[5, 6, 1, 5],
		[0, 7, 9, 1],
	]
	# a
    print('task A:')
    pretty_matrix_print(M)

    # b
    print('\ntask B:')
    ln_b = len(M)
    M[ln_b - 1][0] = randrange(10)

    for el in M[ln_b - 1]:
        print(el, end=' ')
    print(' ')

    # c
    print('\ntask C:')
    pretty_matrix_print(create_random_matrix(5, 7))

    # d
    print('\ntask D:')
    print(cherche(M, 2))

    # e
    print('\ntask E:')
    print(somme_colonnes(M))

    # f
    print('\ntask F:')
    rndm_M = create_random_matrix(5, 5)
    pretty_matrix_print(annule_diagonales(rndm_M))

    # g
    print('\ntask G:')
    rndm_M1 = create_random_matrix(5, 5)
    rndm_M2 = create_random_matrix(5, 5)
    pretty_matrix_print(compacte(rndm_M1, rndm_M2))

    # h
    print('\ntask H:')
    print(cherche_somme_voisins(M))

    # i
    print('\ntask I:')
    pretty_matrix_print(decalage_cyclique(M))
