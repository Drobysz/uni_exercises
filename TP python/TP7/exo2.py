from helpers.base_convert import ft_convert_base as bs

def decimal_vers_binaire(n: int) -> str:
    """
    >>> decimal_vers_binaire(-1)
    ''
    >>> decimal_vers_binaire(0)
    '0'
    >>> decimal_vers_binaire(1)
    '1'
    >>> decimal_vers_binaire(2)
    '10'
    >>> decimal_vers_binaire(3245)
    '110010101101'
    >>> from random import randint
    >>> set(decimal_vers_binaire(randint(1,100))) <={'0','1'}
    True
    """
    if n < 0:
        return ''
    return bs(str(n), "0123456789", "01")

def decimal_vers_binaire_normalise(n: int, k: int) -> str:
    """
    >>> decimal_vers_binaire_normalise(0,8)
    '00000000'
    >>> decimal_vers_binaire_normalise(10,8)
    '00001010'
    >>> decimal_vers_binaire_normalise(10,3)
    Traceback (most recent call last):
            ...
    AssertionError
    """
    converted = decimal_vers_binaire(n)
    ln = len(converted)

    if ln > k:
        raise AssertionError

    res = '0' * (k - ln) + converted
    return res

def binaire_vers_decimal(b: str) -> int:
    """
    >>> binaire_vers_decimal('112')
    Traceback (most recent call last):
            ...
    AssertionError
    >>> binaire_vers_decimal('110')
    6
    >>> binaire_vers_decimal('0')
    0
    >>> binaire_vers_decimal('1')
    1
    >>> binaire_vers_decimal('10')
    2
    >>> binaire_vers_decimal('110010101101')
    3245
    """
    return int(bs(b, "01", "0123456789"))

def tous_binaire(k: int):
    """
    >>> tous_binaire(0)
    >>> tous_binaire(1)
    0
    1
    >>> tous_binaire(4)
    0000
    0001
    0010
    0011
    0100
    0101
    0110
    0111
    1000
    1001
    1010
    1011
    1100
    1101
    1110
    1111
    """
    if k != 0:
        for i in range(2 ** k):
            val = decimal_vers_binaire(i)
            res = '0' * (k - len(val)) + val
            print(res)

def decimal_vers_hexadecimal(n: int) -> str:
    """
    >>> decimal_vers_hexadecimal(17)
    '11'
    >>> decimal_vers_hexadecimal(161)
    'a1'
    >>> decimal_vers_hexadecimal(177)
    'b1'
    >>> decimal_vers_hexadecimal(2833)
    'b11'
    >>> decimal_vers_hexadecimal(171)
    'ab'
    >>>
    """
    return bs(str(n), "0123456789", "0123456789abcdef")

def hexadecimal_vers_binaire(h: str) -> int:
    """
    >>> hexadecimal_vers_binaire('0')
    '0'
    >>> hexadecimal_vers_binaire('1')
    '1'
    >>> hexadecimal_vers_binaire('a')
    '1010'
    >>> hexadecimal_vers_binaire('ff')
    '11111111'
    >>> hexadecimal_vers_binaire('f1')
    '11110001'
    >>> hexadecimal_vers_binaire('fg')
    Traceback (most recent call last):
            ...
    AssertionError
    """
    return bs(h, "0123456789abcdef", "01")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # print(decimal_vers_binaire_normalise(10031231, 3))