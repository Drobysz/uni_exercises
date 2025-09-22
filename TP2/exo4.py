if __name__ == '__main__':
	print("Enter a set consisting of 3 numbers and the program will show\nthe maximal number among them")
	a = int(input('Premier nombre: '))
	b = int(input('Deuxième nombre: '))
	c = int(input('Troisieme nombre: '))

	# A)

	# i
	
	max_val = a
	if a < b:
		max_val = b
	if b < c:
		max_val = c
	print("\nMaximal value: " + str(max_val) + '\n')

	# ii
	# 1] (3,2,1)
	# 2] (1,3,2)
	# 3] (1,2,3)
	# 4] (3,3,1)
	# 5] (3,1,3)
	# 6] (1,3,3)
	# 7] (2,2,2)
	#
	# Total: 7
 
	# iii
	min_val = a
	if a > b:
		min_val = b
	if b > c:
		min_val = c
	print("Minimal value: "+ str(min_val) + '\n')
 
	# iv
	avg_val = b
	if a < b:
		if a > c:
			avg_val = a
	else:
		if a < c:
			avg_val = a
	if a >= c:
		if b < c:
			avg_val = c
	else:
		if b > c:
			avg_val = c
	print("Average value: " + str(avg_val) + '\n')
 
	# v 
	# My 1st solution (Approach №2) at the beginning already corresponds to the condition
	
	# B)
	# Bubble sorting
	s_num = [a, b, c]
	for i in range (3):
		for j in range(2):
			if [a, b, c][j] > s_num[j + 1]:
				temp = s_num[j + 1]
				s_num[j + 1] = s_num[j]
				s_num[j] = temp
	print("Sorted set:", " ".join(str(num) for num in s_num))