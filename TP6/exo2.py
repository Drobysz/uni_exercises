def separe(lst):
    impairs = lst[0::2]
    pairs = lst[1::2]
    return [impairs, pairs]

def combine(lst1, lst2):
    res = []
    n1, n2 = len(lst1), len(lst2)
    m = max(n1, n2)

    for i in range(m):
        if i < n1:
            res.append(lst1[i])
        if i < n2:
            res.append(lst2[i])
    return res

def debut_croissant(lst):
    if not lst:
        return []
    
    res = [lst[0]]
    
    for x in lst[1:]:
        if x < res[-1]:
            break
        res.append(x)
    return res


def decoupage_croissant(lst):
    if not lst:
        return []
    
    runs = []
    cur = [lst[0]]
    
    for x in lst[1:]:
        if x < cur[-1]: 
            runs.append(cur)
            cur = [x]
        else:
            cur.append(x)
    runs.append(cur)
    return runs

if __name__ == '__main__':
	print("123")