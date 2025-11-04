if __name__ == '__main__':
	num = int(input("Input your number: "))
	# main solution
	#print("PAIR") if num % 2 == 0 else print("IMPAIR")
 
	# facultative solution
	res = "IMPAIR"
	if (num % 2 == 0):
		res = "PAIR"
	print(res)
