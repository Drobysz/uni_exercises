def check_dividers(n, divider):
	if divider < 2:
		return True
	if n % divider != 0:
		return check_dividers(n, divider - 1)
	return False

def is_prime(n):
	if n < 3:
		return False
	return check_dividers(n, n-1)

if __name__ == '__main__':
    n = int(input("Enter a number : "))
    cntr = 0
    
    if is_prime(n):
        print("You entered a prime number")
    
    print(f"Prime numbers less then {n} or equal to it : ")
    for i in range(1, n + 1):
        if is_prime(i):
            print(i, end = ' ')
            cntr += 1
            
    print(f"\nQuantity of prime numbers less then {n} or equal to it : \n{cntr}")
    