from typing import Union
from helpfuncs import is_alnum

def is_base_valid(bs: str) -> bool:
	ln = len(bs)

	if ln < 2:
		return False
	for i, c in enumerate(bs):
		if not is_alnum(c):
			return False
		j = i + 1
		while j < ln:
			if bs[j] == c:
				return False
			j += 1
	return True

def id_in_base(c: str, bs: str) -> Union[int, None]:
    if c in bs:
        return bs.index(c)
    return None

def convert_to_decimal(n: str, bs: str) -> int:
	bs_ln = len(bs)
	sign = 1
	start_from = 0
	res = 0
 
	if n[0] == '+' or n[0] == '-':
		start_from = 1
		if n[0] == '-':
			sign *= -1
	for i in range(start_from, len(n)):
		d = id_in_base(n[i], bs)
		if d is None:
			break
		res = res * bs_ln + d
	return res * sign

def convert_to_base(n: int, bs: str) -> str:
	res = []
	bs_ln = len(bs)
	
	if n == 0:
		return bs[0]

	n = -n if n < 0 else n

	while n:
		n, r = divmod(n, bs_ln)
		res.append(bs[r])
	if n < 0:
		res.append('-')
	return ''.join(reversed(res))
        

def ft_convert_base(
    num: str,
    bs_from: str,
    bs_to: str
) -> Union[str, None]:
	if not is_base_valid(bs_from) or not is_base_valid(bs_to):
		return None
	if len(num) < 1:
		return None

	converted = convert_to_decimal(num, bs_from)
	out = convert_to_base(converted, bs_to)

	return out