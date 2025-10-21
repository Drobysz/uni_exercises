def is_pattern(s : str, pat: str):
	pat_ln = len(pat)
	cntr = 0

	for i, c in enumerate(s):
		if c == pat[cntr]:
			if cntr == pat_ln:
				return i
			cntr += 1
		else:
			cntr == 0
	return False

def n_pattern(s: str, pat: str) -> int:
	cntr = 0
	res = is_pattern(s, pat)

	while res:
		cntr += 1
		res = is_pattern(s[res:], pat)
	return cntr

def replace_car(s: str, car: str, pat: str) -> bool:
	i = is_pattern(s, car)
	car_ln = len(car)

	if i:
		s = s[:i - car_ln + 1] + pat + s[i:]
	else:
		return i
	return True

def remplace_motif(s: str, pat1: str, pat2: str):
	res = replace_car(s, pat1, pat2)

	while res:
		res = replace_car(s, pat1, pat2)

# if __name__ == "__main__":