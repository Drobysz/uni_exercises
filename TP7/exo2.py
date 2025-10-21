from helpers.base_convert import ft_convert_base as bs

def decimal_vers_binaire(n: int) -> str:
    return bs(str(n), "0123456789", "01")

def decimal_vers_binaire_normalise(n: int, k: int) -> str:
	converted = decimal_vers_binaire(n)
	cond = len(converted) <= k

	assert cond
	return converted

def binaire_vers_decimal(b: str) -> int:
	return int(bs(b, "01", "0123456789"))

def tous_binaire(k: int):
    for i in range(2 ** k):
        print(decimal_vers_binaire(i))

def decimal_vers_hexadecimal(n: int) -> str:
    return bs(str(n), "0123456789", "0123456789ABCDEF")

def hexadecimal_vers_binaire(h: str) -> int:
    return int(bs(h, "0123456789ABCDEF", "0123456789"))

if __name__ == "__main__":
    print(decimal_vers_binaire_normalise(10031231, 3))