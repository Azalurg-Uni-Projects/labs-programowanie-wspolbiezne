import math
import time
from multiprocessing import Pool


def if_prime(k):
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


def create_mlp(r):
    mlp = []
    s = math.ceil(math.sqrt(r))
    for i in range(2, s + 1):
        if if_prime(i):
            mlp.append(i)
    return mlp


def find_primes(l, r, mlp):
    primes = set()
    s = math.ceil(math.sqrt(r))
    for i in range(l, r + 1):
        for p in mlp:
            if i % p == 0:
                break
            if p * p > i:
                primes.add(i)
                break
        primes.add(i)
    return primes


if __name__ == '__main__':
    left = 1000000
    right = 2000000
    mlp = create_mlp(right)
    processes = 4

    print("Start straightforward")
    start1 = time.time()
    solution1 = find_primes(left, right, mlp)
    end1 = time.time() - start1
    print("Straightforward time: ", end1)

    print("Start multiprocessing")
    with Pool(processes) as p:
        components = []
        part = (right - left) // processes
        for i in range(processes):
            components.append([left + i * part, left + (i + 1) * part, mlp])
        start2 = time.time()
        solution2 = p.starmap(find_primes, components)
        end2 = time.time() - start2

    print("Multiprocessing time: ", end2)
    print("Speedup: ", end1 / end2)
    print("Solution is correct: ", solution1 == set.union(*solution2))

