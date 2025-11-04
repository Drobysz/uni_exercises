from time import time

if __name__ == '__main__':
    n = 100000

    t0 = time()
    r0 = []
    for i in range(n):
        r0 = r0 + [i]
    t1 = time()
    print('Temps de construction de la liste avec + :', t1 - t0, 's', sep='')

    t0 = time()
    r1 = []
    for i in range(n):
        r1.append(i)
    t1 = time()
    print('Temps de construction de la liste avec append :', t1 - t0, 's', sep='')

    print()

    t0 = time()
    for i in range(n):
        r0.pop()
    t1 = time()
    print('Temps de destruction de la liste avec pop() ', t1 - t0, 's')

    t0 = time()
    for i in range(n):
        r1.pop(0)
    t1 = time()
    print('Temps de destruction de la liste avec pop(0) ', t1 - t0, 's')
