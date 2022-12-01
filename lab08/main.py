import time
import random
import math
import sys
import threading

sys.setrecursionlimit(10 ** 9)
suma = 0


def sum_all(a: [int]):
    global suma
    local = 0
    for i in a:
        local += i

    with lockSuma:
        suma += local


def sum_all_threaded(a: [int], g):
    if g > 0:
        if len(a) > 1:
            q = len(a) // 2
            t1 = threading.Thread(target=sum_all_threaded, args=(a[:q], g - 1))
            t2 = threading.Thread(target=sum_all_threaded, args=(a[q:], g - 1))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
    else:
        sum_all(a)


M = 1000  # rozmiar tablicy
G = 5 # ograniczenie poziomów rekursji realizowanych wielowątkowo
lockSuma = threading.Lock()
a = [random.randint(0, 100) for i in range(M)]

sum_all_threaded(a, G)

if suma == sum(a):
    print("Suma poprawna")
else:
    print("Suma niepoprawna")

print("Suma: ", suma)
print("Suma kontrolna: ", sum(a))