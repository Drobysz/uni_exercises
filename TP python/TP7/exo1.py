import re	
from helpers.helpfuncs import is_alnum, ft_strlen
import random
import string

def is_palindrome(s: str) -> bool:
	"""
	>>> is_palindrome('')
	True
	>>> is_palindrome('a')
	True
	>>> is_palindrome('radar')
	True
	>>> is_palindrome('elle')
	True
	>>> is_palindrome('snobons')
	True
	>>> is_palindrome('snoberons')
	False
	"""
	# if I was writing it on C
	# ln = ft_strlen(s)

	# for i in range(round(ln/2)):
	#     if s[i] != s[ln-i-1]:
	#         return False
	# return True
	# a shorter way
	copied_s = s.lower()
	return copied_s == copied_s[::-1]

def is_palindrome2(s: str) -> bool:
	"""
	>>> chaine = 'God ! A red nugget! A fat egg under a dog !'
	>>> is_palindrome2(chaine)
	True
	>>> is_palindrome2(chaine+'g')
	False
	"""
	handled_string = ''

	for c in s:
		if is_alnum(c):
			handled_string += c

	handled_string = handled_string.lower()
	return handled_string == handled_string[::-1]

# decoupe
def ft_split(s: str) -> list[str]:
	"""
	>>> ft_split('')
	[]
	>>> ft_split('a')
	['a']
	>>> ft_split('aaa')
	['aaa']
	>>> ft_split("aaa b   cc \\naaa ")
	['aaa', 'b', 'cc', 'aaa']
	>>> ft_split('  aaa b   cc aaa')
	['aaa', 'b', 'cc', 'aaa']
	"""
	ws: list[str] = []
	w = ''

	for c in s:
		if (c >= '\t' and c <= '\r') or (c == ' '):
			if w != '':
				ws.append(w)
				w = ''
		else:
			w += c
	if w != '':
		ws.append(w)
	return ws

# decoupe2
def ft_split2(s: str) -> list[str]:
	"""
	>>> chaine = "".join([random.choice(string.whitespace+'abc') for i in range(100)])
	>>> ft_split(chaine) == ft_split2(chaine)
	True
	"""
	return re.split(r"[\t-\r ]+", s.strip())

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	# 1
	s = 'Bonjour\n' + '''le "Monde"
et l'Univers'''
	print(s)

	# 2
	print(is_palindrome('tenet'))

	# 3
	print(ft_split("test1 estgeerwg	gergerg !k"))

	# 4
	print(ft_split2("test1 estgeerwg	gergerg !k"))

	# 5
	print(is_palindrome2(" tenet tenet "))

    