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
    for i in range(len(M)):
        for j in range(len(M[i])):
            if el == M[i][j]:
                return True
    return False

def somme_colonnes(M):
	sl = []
	for i in range(len(M)):
		s = 0
		for j in range(len(M[i])):
			s += M[i][j]
		sl.append(s)
	return sl
        
def annule_diagonales(M):
	new_M = M[:]
	ln = len(M)

	for i in range(ln):
		new_M[i][i] = 0
		new_M[i][ln - i - 1] = 0
	return new_M

def compacte(m1, m2):
    if m1 != m2:
        return None
    M = []
    for i in range(m1):
        row = []
        for j in range(m2):
            row.append([i, j])
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
    for i in range(len(M)):
        for j in range(len(M[i])):
            s = define_somme_voisins(M, j, i)
            if s == M[i][j]:
                return {'x': i, 'y': j}
    return None

def decalage_cyclique(M):
	shifted_M = M[:]
	lnY = len(M)
	lnX = len(M[0])
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
	pretty_matrix_print(compacte(4, 4))
 
	# h
	print('\ntask H:')
	print(cherche_somme_voisins(M))
 
	# i
	print('\ntask I:')
	pretty_matrix_print(decalage_cyclique(M))
	