import string
from typing import Dict

def is_alphabet(c):
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
        return True
    return False


def chiffre_lettre(lettre, cle):
    """
    >>> chiffre_lettre('a',10), chiffre_lettre('a',26)
    ('k', 'a')
    >>> chiffre_lettre('z',1), chiffre_lettre('a',260)
    ('a', 'a')
    >>> chiffre_lettre('A',10), chiffre_lettre('A',26)
    ('K', 'A')
    >>> chiffre_lettre('w',10), chiffre_lettre('W',10)
    ('g', 'G')
    """
    
    if not is_alphabet(lettre):
        return lettre
    
    cle = cle % 26
    lettre_id = ord(lettre)
    total = lettre_id + cle
    id = 0
    
    if (65 <= lettre_id <= 90):
        if total > 90:
            id = 64 + (total - 90)
        else:
            id = total
    elif (97 <= lettre_id <= 122):
        if total > 122:
            id = 96 + (total - 122)
        else:
            id = total
            
    return chr(id)


def chiffre(en_clair, cle):
    """
    >>> import string
    >>> chiffre(string.ascii_lowercase,10)
    'klmnopqrstuvwxyzabcdefghij'
    >>> chiffre(string.ascii_uppercase,100)
    'WXYZABCDEFGHIJKLMNOPQRSTUV'
    >>> chiffre('Toto est une girafe, avec des petites jambes.',12)
    'Fafa qef gzq sudmrq, mhqo pqe bqfufqe vmynqe.'
    """
    hashed = ''
    
    for c in en_clair:
        if is_alphabet(c):
            hashed += chiffre_lettre(c, cle)
        else:
            hashed += c
    return hashed


def dechiffre_lettre(lettre, cle):
    if not is_alphabet(lettre):
        return lettre

    cle = cle % 26
    lettre_id = ord(lettre)
    total = lettre_id - cle
    
    if (65 <= lettre_id <= 90):
        if total < 65:
            id = 91 - (65 - total)
        else:
            id = total
    elif (97 <= lettre_id <= 122):
        if total < 97:
            id = 123 - (97 - total)
        else:
            id = total
            
    return chr(id)


def dechiffre(texte_cache, cle):
    """
    >>> import string; cle = 12
    >>> dechiffre(chiffre(string.ascii_lowercase,cle),cle) == string.ascii_lowercase
    True
    >>> dechiffre(chiffre(string.ascii_uppercase,cle),cle) == string.ascii_uppercase
    True
    >>> dechiffre('Fafa qef gzq sudmrq, mhqo pqe bqfufqe vmynqe.',12)
    'Toto est une girafe, avec des petites jambes.'
    """
    hashed = ''

    for c in texte_cache:        
        if is_alphabet(c):
            hashed += dechiffre_lettre(c, cle)
        else:
            hashed += c
    return hashed


def devine_cle(texte_cache):
    """
    >>> devine_cle('a e dd e eeee d')
    0
    >>> devine_cle('x b aa b bbbb a')
    23
    """
    e_sum_list = [dechiffre(texte_cache, i).count('e') for i in range(26)]
    return e_sum_list.index(max(e_sum_list))

        
def max_dict(d: Dict) -> str:
    mx_val = max([val for val in d.values()])
    for key in d.keys():
        if d[key] == mx_val:
            return key


def unique_chars(s: str) -> Dict:
    c_n = dict()

    for c in s:
        if c not in c_n.keys():
           c_n[c] = s.count(c)
    return c_n    


def devine_cle2(texte_cache):
    """
    >>> devine_cle2('a e dd e eeee d')
    0
    >>> devine_cle2('x b aa b bbbb a')
    23
    """
    most_repeated_char = max_dict(unique_chars(texte_cache))
    # 97 - premier index dans ASCII de lettre lowercase d'alphabet
    # methode lower() a été utilisé pour obtenir index de lettre lowercase dans ASCII tableau
    pos = ord(most_repeated_char.lower()) - 97 
    return int((pos + ord('a') - ord('e')) % 26)


def chiffre_mieux(texte, cle, decal = 1):
    """
    >>> chiffre_mieux('abc de f ghijk lmnopqrstuvw xyz',3)
    'def hi k mnopq stuvwxyzabcd fgh'
    """
    hashed = ''
    i = 0
    
    for c in texte:
        if c == ' ':
            i += decal
        if is_alphabet(c):
            hashed += chiffre_lettre(c, cle + i)
        else:
            hashed += c
    return hashed


def dechiffre_mieux(texte, cle, decal = 1):
    """
    >>> dechiffre_mieux('def hi k mnopq stuvwxyzabcd fgh',3)
    'abc de f ghijk lmnopqrstuvw xyz'
    """
    hashed = ''
    i = 0
    
    for c in texte:
        if c == ' ':
            i += decal
        if is_alphabet(c):
            hashed += dechiffre_lettre(c, cle + i)
        else:
            hashed += c
    return hashed
        

def chiffre_encore_mieux(texte, cle, decal = 0):
    """
    >>> chiffre_encore_mieux('abc de f ghijk lmnopqrstuvw xyz',3,7)
    'def no w efghi qrstuvwxyzab jkl'
    """
    if decal > 0:
        return chiffre_mieux(texte, cle, decal)
    return chiffre(texte, cle)


def dechiffre_encore_mieux(texte, cle, decal):
    """
    >>> dechiffre_encore_mieux('def no w efghi qrstuvwxyzab jkl',3,7)
    'abc de f ghijk lmnopqrstuvw xyz'
    """
    if decal > 0:
        return dechiffre_mieux(texte, cle, decal)
    return dechiffre(texte, cle)


def tests(s1, s2):
    print(chiffre_encore_mieux(s1, 4))
    print(chiffre_encore_mieux(s2, 3, 5))

def main():
    import doctest

    doctest.testmod()

    premier_essai = """Cdzm, e'vd hvibz piz kjhhz. 
    Vkmzn, e'vd zp yzn cvggpxdivodjin, kgzdi y'cvggpxdivodjin. 
    Ez qjtvdn yzn zgzkcvion, yzn gdxjmizn zo yzn kviyvn. Zo dgn zovdzio mjnzn, ojpn mjnzn.
    """

    deuxieme_essai = """Jli c'rsrkkrek ul mrjzjkrj, le rezdrc rl kyfiro zeuzxf, r c'rzxlzccfe jrwire, ez le trwriu, 
    ez le tyriretfe, drzj gclkfk le rikzjfe, j'rmretrzk, kirzerek le size u'rcwr. 
    Zc j'rggiftyr, mflcrek c'rgcrkzi u'le tflg mzw, drzj c'rezdrc gizk jfe mfc, uzjgrirzjjrek 
    urej cr elzk rmrek hl'zc rzk gl c'rjjrzcczi.
    """
    
    tests(premier_essai, deuxieme_essai)


if __name__ == '__main__':
    main()
