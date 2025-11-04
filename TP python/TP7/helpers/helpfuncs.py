# I'm aware that there is a built-in method len()
# but I wanted to implement lenght counting like in C
def ft_strlen(s: str) -> int:
	ln = 0

	for _ in s:
		ln += 1
	return ln

def is_alnum(c: str) -> bool:
	if (c >= '0' and c <= '9') or (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
		return True
	return False

def is_space(c: str) -> bool:
	return c == ' ' or (c >= '\t' and c <= '\r')