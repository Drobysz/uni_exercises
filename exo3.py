if __name__ == '__main__':
    # A)
    n = int(input("Enter a real positive number: "))
    
    # B)
    # version 1
    if n % 2 == 0:
        print("\nDivisible par 2, 3 ou 4")
    if n % 3 == 0:
        print("\nDivisible par 2, 3 ou 4")
    if n % 4 == 0:
        print("\nDivisible par 2, 3 ou 4")
    
    # version 2
    if n % 2 == 0 or n % 3 == 0 or n % 4 == 0:
        print("\nDivisible par 2, 3 ou 4")
        
    # C)
    if n % 2 == 0:
        print("\nDivisible par 2")
    if n % 3 == 0:
        print("\nDivisible par 3")
    if n % 4 == 0:
        print("\nDivisible par 4")
    # D + E)
    else:
        print("\nPas divisible par 2, 3 ou 4")
    # F)
    div_par_3, div_par_4 = (n % 3 == 0), (n % 4 == 0)

    if div_par_3 and div_par_4:
        print("\ndivisible par 12\n")
    elif div_par_3:
        print("\ndivisible par 3 mais pas par 12")
    elif div_par_4:
        print("\ndivisible par 4 mais pas par 12")
    else:
        print("\npas divisible par 3 ou 4")
    
    