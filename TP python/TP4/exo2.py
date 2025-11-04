import doctest


def bonjour():
    """
    >>> bonjour()
    bonjour
    >>> bonjour(1)
    Traceback (most recent call last):
        ...
    TypeError: bonjour() takes 0 positional arguments but 1 was given
    """
    print("bonjour")


def dis_bonjour(n):
    """
    >>> dis_bonjour(-1)
    >>> dis_bonjour(0)
    >>> dis_bonjour(3)
    bonjour
    bonjour
    bonjour
    """
    for i in range(n):
        print("bonjour")


def renvoie_bonjour(n):
    """
    >>> renvoie_bonjour(-1)
    ''
    >>> renvoie_bonjour(0)
    ''
    >>> b = renvoie_bonjour(2)
    >>> b
    'bonjour bonjour'
    >>> renvoie_bonjour(3)
    'bonjour bonjour bonjour'
    """
    return (("bonjour " * (n-1)) + "bonjour") if n > 0 else ""


if __name__ == '__main__':
    # la ligne suivante active les doctests dans le programme
    doctest.testmod()

    bonjour()
    dis_bonjour(5)
    renvoie_bonjour(3)
    """
    >>> dis_bonjour(4)
    bonjour
    bonjour
    bonjour
    bonjour
    >>> test = renvoie_bonjour(6)
    >>> test
    'bonjour bonjour bonjour bonjour bonjour bonjour'
    """
    pass
