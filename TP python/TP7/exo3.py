from typing import Union

def is_pattern(s : str, pat: str) -> bool:
	"""
	>>> chaine = "supercalifragilisticexpialidocious"
	>>> is_pattern(chaine, 'super')
	True
	>>> is_pattern(chaine, 'superb')
	False
	>>> is_pattern(chaine, 'docious')
	True
	>>> is_pattern(chaine, 'dociouss')
	False
	"""
	pat_ln = len(pat)
	cntr = 0

	for c in s:
		if c == pat[cntr]:
			if cntr == pat_ln - 1:
				return True
			cntr += 1
		else:
			cntr == 0
	return False

def define_idx(
    s: str,
    pat: str,
    since: int
) -> Union[str, bool]:
	pat_ln = len(pat)
	s_ln = len(s)
	cntr = 0

	for i in range(since, s_ln):
		if s[i] == pat[cntr]:
			if cntr == pat_ln - 1:
				return i
			cntr += 1
		else:
			cntr = 0
	return False

def n_pattern(s: str, pat: str) -> int:
	"""
	>>> chaine = "supercalifragilisticexpialidocious"
	>>> n_pattern(chaine, 's')
	3
	>>> n_pattern(chaine, 'sf')
	0
	>>> n_pattern(chaine, 'li')
	3
	>>> n_pattern(chaine, 'ali')
	2
	"""
	cntr = 0
	res = define_idx(s, pat, 0)

	while res is not False:
		cntr += 1
		res = define_idx(s, pat, res + 1)
	return cntr

def replace_car(
    s: str,
    car: str,
    pat: str
) -> str:
	"""
	>>> chaine = "supercalifragilisticexpialidocious"
	>>> replace_car(chaine, 's', 'ff')
	'ffupercalifragiliffticexpialidociouff'
	>>> replace_car(chaine, 'z', 'ff')
	'supercalifragilisticexpialidocious'
	"""
	i = -1
	car_ln = len(car)

	while i is not False:
		i = define_idx(s, car, i + 1)
		if i is not False:
			s = s[:i - car_ln + 1] + pat + s[i + 1:]
	return s

def remplace_motif(s: str, pat1: str, pat2: str) -> str:
	"""
	>>> chaine = "supercalifragilisticexpialidocious"
	>>> remplace_motif(chaine, 's', 'ff')
	'ffupercalifragiliffticexpialidociouff'
	>>> remplace_motif(chaine, 'li', 'titi')
	'supercatitifragititisticexpiatitidocious'
	>>> remplace_motif(chaine, 'docious', 'dodo')
	'supercalifragilisticexpialidodo'
	>>> remplace_motif(chaine, 'dociouss', 'dodo')
	'supercalifragilisticexpialidocious'
	"""
	return replace_car(s, pat1, pat2)

if __name__ == "__main__":
	import doctest
	doctest.testmod()