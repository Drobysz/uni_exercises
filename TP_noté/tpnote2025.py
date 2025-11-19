"""
Attention : aucune fonction ne doit modifier les éventuelles listes qu'elle reçoit en paramètre.
"""
def positions_lettre(chaine, lettre):
    """
    >>> positions_lettre("programmation", "a")
    [5, 8]
    >>> positions_lettre("programmation", "z")
    []
    >>> positions_lettre("programmation", "on")
    []
    """
    pst = []
    
    for i in range(len(chaine)):
        if chaine[i] == lettre:
            pst.append(i)
    return pst

def nombre_caracteres_differents(chaine):
    """
    >>> nombre_caracteres_differents("programmation")
    9
    >>> nombre_caracteres_differents("")
    0
    >>> nombre_caracteres_differents("aaaaa")
    1
    """
    ln = len(chaine)
    isNotUnique = False
    cntr = 0
    
    for i in range(ln):
        for j in range(i):
            isNotUnique = chaine[i] == chaine[j]
            if isNotUnique:
                break
        if not isNotUnique:
            cntr += 1
            isNotUnique = False
    return cntr
        
def mot_le_plus_long(phrase):
    """
    >>> mot_le_plus_long("Ceci est une phrase qui n'est pas très longue")
    'phrase'
    >>> mot_le_plus_long("bonjour")
    'bonjour'
    >>> mot_le_plus_long("bon jour")
    'jour'
    """
    words = phrase.split(' ')
    lens = [len(x) for x in words]
    
    return words[lens.index(max(lens))]
    
def est_adn(chaine):
    """
    >>> est_adn("")
    True
    >>> est_adn("ACGT")
    True
    >>> est_adn("ABCD")
    False
    """
    dnk_symbols = "ACGT"
    
    for smbl in chaine:
        if not smbl in dnk_symbols:
            return False
    return True

def composition(chaine):
    """
    >>> composition("CAACATCACAAGAAGT")
    50.0 % de A
    25.0 % de C
    12.5 % de G
    12.5 % de T
    """
    total = len(chaine)
    total_char = 0
    dnk_symbols = "ACGT"
    
    for char in dnk_symbols:
        for chain_char in chaine:
            if char == chain_char:
                total_char += 1
        print(f"{(total_char/total) * 100} % de {char}")
        # Probably it worths to wrap percent number with round(num, 1)
        total_char = 0
        
def complement(chaine):
    """
    >>> complement("GACT")
    'AGTC'
    >>> complement("CAACATCACAAGAAGT")
    'ACTTCTTGTGATGTTG'
    >>> complement("ACGT")
    'ACGT'
    """
    reversed_chain = chaine[::-1]
    dnk_symbols = "ACGT"
    rev_dnk_symbols = dnk_symbols[::-1]
    sequence = ''
    
    for char in reversed_chain:
        sequence += rev_dnk_symbols[dnk_symbols.index(char)]
    return sequence

def isbn_vers_donnees(chaine):
    """
    >>> isbn_vers_donnees("0262367505")
    ['02', '6236', '750']
    """
    isbn = []
    
    isbn.append(chaine[0:2])
    isbn.append(chaine[2:6])
    isbn.append(chaine[6:9])
    return isbn

def est_isbn_correct(chaine):
	"""
	>>> est_isbn_correct("0262367505")
	True
	>>> est_isbn_correct("038518915X")
	True
	>>> est_isbn_correct("3141592653")
	False
	"""
	nums = []
	ln = len(chaine)

	for i in range(ln):
		nums.append(10 if chaine[i] == 'X' else int(chaine[i]) * (ln-i))
	return sum(nums) % 11 == 0

def plus_long_suffixe_croissant(valeurs):
    # """
    # >>> plus_long_suffixe_croissant([])
    # 0
    # >>> plus_long_suffixe_croissant([3, 1, 4, 1, 5, 9])
    # 3
    # >>> plus_long_suffixe_croissant([3, 2, 1, 2, 2, 3])
    # 4
    # >>> plus_long_suffixe_croissant([3, 2, 1, 2, 2, 3])
    # 4
    # """
    line_lns = []
    cntr = 0
    ln = len(valeurs)
    
    for i in range(ln - 1):
        if valeurs[i] <= valeurs[i + 1]:
            cntr += 1 
        else:
            line_lns.append(cntr)
            cntr = 0
    line_lns.append(cntr + 1 if ln > 1 and valeurs[ln - 2] <= valeurs[ln - 1] else cntr)
    print(valeurs[ln - 2] <= valeurs[ln - 1])
    return max(line_lns)
        
# def gains_potentiels(achat, actuel, nombre):
#     """
#     >>> gains_potentiels(100, 150, 1)
#     50
#     >>> gains_potentiels(100, 50, 2)
#     -100
#     """
#     pass

def achat_interessant(valeurs):
	"""
	>>> achat_interessant([3, 2, 4, 2, 8, 5, 6])
	[False, 6, 4.0]
	>>> achat_interessant([10, 9, 8, 7, 6, 5])
	[True, 5, 8.0]
	"""

	ln = len(valeurs)
	avrg = round(sum(valeurs) / ln, 0)  
	is_more = valeurs[ln - 1] >= avrg

	return [not is_more, valeurs[ln - 1], avrg]
    

# def gains_et_pertes_max(valeurs):
#     """
#     >>> gains_et_pertes_max([4, 1, 4, 2, 8, 5, 6])
#     [700.0, -75.0]
#     """
#     pass
    
if __name__ == "__main__":
	from doctest import testmod
	testmod()
	print(achat_interessant([10, 9, 8, 7, 6, 5]))
