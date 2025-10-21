from random import randrange

if __name__ == '__main__':
    n = randrange(10, 21)
    
    # a
    lst1 = []
    for i in range(n):
        lst1.append(1)
        
    # b
    lst2 = [2] * n
    
    # c
    lst_random = [randrange(0, 11) for i in range(n)] 
    
    # d
    print([el for el in lst_random if el > 5])

	# e
    lst_random10_reverse = lst_random[::-1]
    
    # а
    lst_random10_count = [lst_random.count(i) for i in range(11)]
    