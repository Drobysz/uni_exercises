from random import randrange

def random_num_list(n, mx):
    return [randrange(n) for _ in range(mx)]