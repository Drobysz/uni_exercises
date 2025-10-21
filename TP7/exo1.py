import re

# I'm aware that there is a built-in method len()
# but I wanted to implement lenght counting like in C
def ft_strlen(s: str) -> int:
	ln = 0

	for _ in s:
		ln += 1
	return ln	

def is_palindrome(s: str) -> bool:
    # if I was writing it on C
    ln = ft_strlen(s)

    for i in range(round(ln/2)):
        if s[i] != s[ln-i-1]:
            return False
    return True
	# a shorter way
	# return s == s[::-1]

def is_alnum(c: str) -> bool:
	if (c >= '0' and c <= '9') or (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
		return True
	return False

def is_palindrome2(s: str) -> bool:
	handled_string = ''
 
	for c in s:
		if is_alnum(c):
			handled_string += c
	return handled_string == handled_string[::-1]

def ft_split(s: str) -> list[str]:
	ws: list[str] = []
	w = ''

	for c in s:
		if c >= '\t' and c <= '\r':
			if w != '':
				ws.append(w)
				w = ''
		else:
			w += c
	if w != '':
		ws.append(w)
	return ws

def ft_split2(s: str) -> list[str]:
	i = 9
	seps = ''

	while i <= 13:
		seps += chr(i) + '|'
		i += 1
	seps += ' '
	return re.split(seps, s.strip())

if __name__ == "__main__":
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

    