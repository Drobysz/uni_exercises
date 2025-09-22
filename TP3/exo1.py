if __name__ == '__main__':
	n = int(input("Ecrivez un nombre: "))

	cntr = 0
	print("Les n premiers entiers positifs :")
	while cntr != n:
		print(cntr, end = ' ')
		cntr += 1

	cntr = 0
	i = 0
	print("\nLes n premiers multiples de 3")
	while cntr != n:
		if i % 3 == 0:
			cntr += 1
			print(i, end = ' ')
		i += 1

	print("\nLes nombres de 1 à n ceux qui sont divisibles par 3 mais pas par 5")
	for i in range (n):
		if i % 3 == 0 and i % 5 != 0:
			print(i, end = ' ')

	print("\nLes multiples de 3 compris entre 1 et n")
	for i in range (1, n + 1):
		if i % 3 == 0:
			print(i, end = ' ')

	nums = []
	cntr = 0
	i = 0
	print("\nLes n premiers multiples de 3 en ordre décroissant ")
	while cntr != n:
		if i % 3 == 0:
			cntr += 1
			nums.append(i)
		i += 1
	# for i in reversed(nums):
	# 	print(i, end = ' ')
	while cntr != 0:
		cntr -= 1
		print(nums[cntr], end = ' ')