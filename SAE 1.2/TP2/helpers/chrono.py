from time import perf_counter

def chrono(f, *args):
    start = perf_counter()
    f(*args)
    end = perf_counter()
    return end - start