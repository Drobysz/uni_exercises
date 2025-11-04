if __name__ == '__main__':
    # a
    print("Question 1:")
    lst = [14, 7, 6, 12, 2, 3, 3, 10]
    print(lst)
    
    # b
    print("\nQuestion 2:")
    lst[-1] = int(lst[-1] / 2)
    print(lst[-1])
    # print(lst.pop() / 2)
    
    # c
    print("\nQuestion 3:")
    lst = [x - 1 for x in lst]
    print(lst)
    
    # d
    print("\nQuestion 4:")
    print("*--v1--*")
    for i in range(len(lst)):
        print(lst[i])
    print("*--v2--*")
    print([el for el in lst])
    print("")
    
    # e
    print("\nQuestion 5:")
    print([el for el in lst if el % 2 == 0])
    
    # f
    print("\nQuestion 6:")
    for el in lst: print((str(int(el)) + ' ') * 10)
    print("")
    
    # g
    print("\nQuestion 7:")
    for el in lst: print((str(int(el)) + ' ') * el)
    
    # h (without if)
    print("\nQuestion 8:")
    for el in lst:
        print([el + 1, el - 1][el % 2 == 0], end = ' ')
