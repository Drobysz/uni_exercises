if __name__ == '__main__':
	characters = input("Enter a chain of characters : ")

	print("\naffiche cette chaîne en laissant un espace après chaque caractère :")
	for i in characters:
		print(i, end = ' ')
	print('\n')
	
	print("\naffiche cette chaîne en répétant chaque caractère 5 fois:")
	for i in characters:
		print(i * 5, end = '')
	print('\n')

	print("\naffiche cette chaîne en remplaçant toutes les voyelles par des 'e' :")
	for i in characters:
		if "auioy".count(i) > 0:
			i = 'e'
		print(i, end = '')
	print('\n')
	
	print("\naffiche cette chaîne en retirant un caractère sur deux :")
	for i in range(len(characters)):
		if (i + 1) % 2 != 0:
			print(characters[i], end = '')
	print('\n')