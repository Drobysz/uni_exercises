import doctest


def separe(lst):
    """
    >>> separe([1, 0])
    [[1], [0]]
    >>> separe([1,1,1,2,9,4,2,2,1,1,1,9,1,2,9,4,2,3])
    [[1, 1, 9, 2, 1, 1, 1, 9, 2], [1, 2, 4, 2, 1, 9, 2, 4, 3]]
    >>> separe([1,1,1,2,9,4,2,2,1,1,1,9,1,2,9,4,2,2,1])
    [[1, 1, 9, 2, 1, 1, 1, 9, 2, 1], [1, 2, 4, 2, 1, 9, 2, 4, 2]]
    >>> separe([1])
    [[1], []]
    >>> separe([])
    [[], []]
    >>> len(separe([0]*1000000)[0])
    500000
    """
    impairs = lst[0::2]
    pairs = lst[1::2]
    return [impairs, pairs]


def combine(lst1, lst2):
    """
    >>> combine([1], [0])
    [1, 0]
    >>> combine([1, 2, 3, 4], [0])
    [1, 0, 2, 3, 4]
    >>> combine([1], [2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> combine([1, 1, 9, 2, 1, 1, 1, 9, 2], [1, 2, 4, 2, 1, 9, 2, 4, 3])
    [1, 1, 1, 2, 9, 4, 2, 2, 1, 1, 1, 9, 1, 2, 9, 4, 2, 3]
    >>> combine([1, 1, 9, 2, 1, 1, 1, 9, 2, 1], [1, 2, 4, 2, 1, 9, 2, 4, 2])
    [1, 1, 1, 2, 9, 4, 2, 2, 1, 1, 1, 9, 1, 2, 9, 4, 2, 2, 1]
    >>> combine([1], [])
    [1]
    >>> combine([], [])
    []
    >>> len(combine([0]*1000000,[0]*1000000))
    2000000
    """
    res = []
    n1, n2 = len(lst1), len(lst2)
    m = max(n1, n2)

    for i in range(m):
        if i < n1:
            res.append(lst1[i])
        if i < n2:
            res.append(lst2[i])
    return res


def debut_croissant(lst):
    """
    >>> lst = [1,1,1,2,9,4,2,2,1,1,1,9,1,2,9,4,2,2,1]
    >>> debut_croissant(lst)
    [1, 1, 1, 2, 9]
    >>> lst
    [1, 1, 1, 2, 9, 4, 2, 2, 1, 1, 1, 9, 1, 2, 9, 4, 2, 2, 1]
    >>> debut_croissant([1, 1, 1, 2, 9])
    [1, 1, 1, 2, 9]
    >>> debut_croissant([1])
    [1]
    >>> debut_croissant([1, 0])
    [1]
    >>> debut_croissant([])
    []
    >>> print(len(debut_croissant([0]*1000000)))
    1000000
    """
    if not lst:
        return []
    
    res = [lst[0]]
    
    for x in lst[1:]:
        if x < res[-1]:
            break
        res.append(x)
    return res


def decoupage_croissant(lst):
    """
    >>> lst = [1,1,1,2,9,4,2,2,1,1,1,9,1,2,9,4,2,2,1]
    >>> decoupage_croissant(lst)
    [[1, 1, 1, 2, 9], [4], [2, 2], [1, 1, 1, 9], [1, 2, 9], [4], [2, 2], [1]]
    >>> lst
    [1, 1, 1, 2, 9, 4, 2, 2, 1, 1, 1, 9, 1, 2, 9, 4, 2, 2, 1]
    >>> decoupage_croissant([])
    []
    >>> decoupage_croissant([1])
    [[1]]
    >>> decoupage_croissant([1,1])
    [[1, 1]]
    >>> decoupage_croissant([1,0])
    [[1], [0]]
    >>> len(decoupage_croissant([0]*1000000))
    1
    """
    if not lst:
        return []
    
    runs = []
    cur = [lst[0]]
    
    for x in lst[1:]:
        if x < cur[-1]: 
            runs.append(cur)
            cur = [x]
        else:
            cur.append(x)
    runs.append(cur)
    return runs


if __name__ == '__main__':
    # la ligne suivante active les doctests dans le programme
    doctest.testmod()

    print(separe([1,1,1,2,9,4,2,2,1,1,1,9,1,2,9,4,2,3]))
    pass
