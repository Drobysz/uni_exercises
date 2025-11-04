from helpers.random_list import random_num_list
from helpers.chrono import chrono
from helpers.complexite_matplotlib import tracer
from random import randrange

#---------------------------------------------1

def custom_count(lst: list[int], n):
    cntr = 0

    for el in lst:
        if el == n:
            cntr += 1
    return cntr

def enumerate1(lst: list[int]):
	mx = max(lst)
	stack = []

	for i in range(mx + 1):
		stack.append(lst.count(i))
	return stack

def enumerate2(lst: list[int]):
	mx = max(lst)
	stack = []

	for i in range(mx + 1):
		stack.append(custom_count(lst, i))
	return stack

#---------------------------------------------2

def sort_listA(n, mx):
    lst = random_num_list(n, mx)
    lst.sort()
    return lst

def sort_listB(lst: list[int], el):
    lst_copy = lst[:]
    lst_copy.append(el)
    lst_copy.sort()
    return lst_copy

def sort_listC(lst: list[int], el):
    lst_copy = lst[:]
    lst_copy.insert(0, el)
    ln = len(lst_copy)
    
    for i in range(ln - 1):
        if lst_copy[i] > lst_copy[i + 1]:
            tmp = lst_copy[i]
            lst_copy[i] = lst_copy[i + 1]
            lst_copy[i + 1] = tmp
        else:
            break
    return lst_copy

def sort_listD(lst: list[int], el):
    ln = len(lst)
    lst_copy = lst[:]
    isAdded = False

    for i in range(ln):
        if lst_copy[i] > el:
            lst_copy.insert(i, el)
            isAdded = True
            break
    if not isAdded:
        lst_copy.insert(ln, el)
    return lst_copy

#---------------------------------------------3

def remove_pairA(lst: list):
    ln = len(lst)
    i = 0

    while i < ln:
        if lst[i] % 2 == 0:
            del lst[i]
            ln -=1
        i += 1
    return lst

def remove_pairB(lst: list):
    modified_list = []
    
    for el in lst:
        if el % 2 != 0:
            modified_list.append(el)

    lst[:] = modified_list
    return lst

def remove_pairC(lst: list):
    ln = len(lst)
    i = ln - 1

    while i > 0 :
        if lst[i] % 2 == 0:
            del lst[i]
        i -= 1
    return lst
         

if __name__ == '__main__':
    lst = random_num_list(9, 5)

    # EXERCISE 1

    t_enum1, t_enum2 = [], []
    
    for i in range(20):
        n = randrange(1, 30)
        mx = randrange(1, 20)
        lst = random_num_list(n, mx)

        t_enum1.append(chrono(enumerate1, lst))
        t_enum2.append(chrono(enumerate2, lst))

    tracer("comparaison of enumerate functions",
           t_enum1, "system count",
           t_enum2, "custom count")

    
    #EXERCISE 2
        
    t_sort1, t_sort2, t_sort3, t_sort4 = [], [], [], []
    
    for i in range(20):
        n = randrange(1, 30)
        mx = randrange(1, 20)
        lst = random_num_list(n, mx)
        lst.sort()
        rand_num = randrange(30)

        t_sort1.append(chrono(sort_listA, n, mx))
        t_sort2.append(chrono(sort_listB, lst, rand_num))
        t_sort3.append(chrono(sort_listC, lst, rand_num))
        t_sort4.append(chrono(sort_listD, lst, rand_num))
        

    tracer("comparaison of sort functions",
           t_sort1, "sorting A",
           t_sort2, "sorting B",
           t_sort3, "sorting C",
           t_sort4, "sorting D")
    
    # EXERCISE 3
    
    t_rm1, t_rm2, t_rm3 = [], [], []
    
    for i in range(20):
        n = randrange(1, 30)
        mx = randrange(1, 20)
        lst = random_num_list(n, mx)

        t_rm1.append(chrono(remove_pairA, lst))
        t_rm2.append(chrono(remove_pairB, lst))
        t_rm3.append(chrono(remove_pairC, lst))
        

    tracer("comparaison of remove functions",
           t_rm1, "remove A",
           t_rm2, "remove B",
           t_rm3, "remove C")
    
