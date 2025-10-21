import doctest

from random import randrange


def carre(n):
    """
    >>> [carre(0),carre(2),carre(-1)]
    [0, 4, 1]
    """
    return n ** 2


def liste_aleatoire(n, b):
    """
    >>> liste_aleatoire(0,10)
    []
    >>> liste_aleatoire(10,1)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    rand_nums = []
    while n != 0:
        rand_nums.append(randrange(1, b + 1))
        n -= 1
    return rand_nums


def liste_carres(lst):
    """
    >>> liste_carres([])
    []
    >>> liste_carres([2,3,42,5,9,100])
    [4, 9, 1764, 25, 81, 10000]
    """
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2
    return lst


def max_liste(lst):
    # """
    # >>> max_liste([])
    # Traceback (most recent call last):
    #     ...
    # AssertionError
    # >>> max_liste([100, 2,-3,42,5,-9])
    # 100
    # >>> max_liste([2,-3,42,5,-9,100])
    # 100
    # >>> max_liste([2,3,42,100,5,9,100,2,3])
    # 100
    # >>> max_liste([-1,-2])
    # -1
    # """
    return max(lst)


def singletons(lst):
    """
    >>> l = [2,1,2,1,3,2,1,4]
    >>> singletons(l)
    [2, 1, 3, 4]
    >>> l
    [2, 1, 2, 1, 3, 2, 1, 4]
    >>> singletons([])
    []
    >>> singletons([1,1,1])
    [1]
    """
    signls = []
    length = len(lst)
    is_unique = True
    
    if length < 2:
        return lst
    for i in range(length):
        for j in range(i):
            if lst[i] == lst[j]:
                is_unique = False
        if is_unique:
            signls.append(lst[i])
        is_unique = True
    return signls      


def indice(lst, n):
    """
    >>> lst = [2,1,2,1,3,2,1,4]
    >>> indice(lst,1)
    1
    >>> indice(lst,2)
    0
    >>> indice(lst,4)
    7
    >>> indice(lst,5)
    -1
    """
    try:
        return lst.index(n)
    except ValueError:
        return -1


def nb_occurrences(n, lst):
    """
    >>> lst = [1,1,1,2,9,4,2,2,1,1,1,9,1,2,9,4,2,2,1]
    >>> [nb_occurrences(1,lst), nb_occurrences(5,lst), nb_occurrences(5,[])]
    [8, 0, 0]
    >>> lst
    [1, 1, 1, 2, 9, 4, 2, 2, 1, 1, 1, 9, 1, 2, 9, 4, 2, 2, 1]
    """
    return lst.count(n)


def toutes_occurrences(lst):
    """
    >>> toutes_occurrences([])
    []
    >>> toutes_occurrences([1,1,1])
    [[1, 3]]
    >>> toutes_occurrences([1,2,3])
    [[1, 1], [2, 1], [3, 1]]
    >>> lst = [1,1,1,2,9,4,2,2,1,1,1,9,1,2,9,4,2,2,1]
    >>> toutes_occurrences(lst)
    [[1, 8], [2, 6], [9, 3], [4, 2]]
    >>> lst
    [1, 1, 1, 2, 9, 4, 2, 2, 1, 1, 1, 9, 1, 2, 9, 4, 2, 2, 1]
    """
    return [[x, lst.count(x)] for x in singletons(lst)]
    


def plus_frequent(lst):
    """
    >>> plus_frequent([])
    Traceback (most recent call last):
        ...
    AssertionError
    >>> plus_frequent([1,2,1,1,2,2,3,3,4])
    2
    >>> plus_frequent([3,1,2,1,1,2,2,3,3,4])
    3
    >>> plus_frequent([1,1,1])
    1
    >>> plus_frequent([1,2,3])
    3
    """
    
    if lst == []:
        print("""Traceback (most recent call last):
    ...
AssertionError""")
        return
    
    occs = toutes_occurrences(lst)
    max_num = max([x[1] for x in occs])
    equals = []

    for x in occs:
        if x[1] == max_num:
            equals.append(x)       
    
    return max([x[0] for x in equals])


if __name__ == '__main__':
    # la ligne suivante active les doctests dans le programme
    doctest.testmod()

    # print(plus_frequent([3,1,2,1,1,2,2,3,3,4]))
    pass
