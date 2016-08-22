from collections import deque
from heapq import heappush,heappop
import numpy as np

t = int(input())

from math import sqrt;

import math

# n > 2
def is_prime(n):
    if n % 2 == 0:
        return 2

    sqr = int(pow(n, 0.5)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return divisor

    return 0


def is_good(vec):
    divisors = []
    for jk in vec:
        div = is_prime(jk)
        #print(jk, div)
        if div == 0:
            return None
        divisors.append(div)

    return divisors



for i in range(t):

    print("Case #{0}:".format(i+1))

    n,j = input().split(' ')
    n = int(n)
    j = int(j)

    bi = np.ndarray((9))
    pm = np.ndarray((9,n-2))
    for base in range(2,11):
        powers = [base**power for power in range(1, n-1)]
        pm[base-2] = powers
        bi[base-2] = (1 + base**(n-1))

    # print(pm)
    # print(bi)
    
    seen = [0] * (2 ** (n-2))

    mid_jc = np.random.choice(2, n-2)
    count = 0
    while(True):
        mid_jc = np.random.choice(2, n-2)
        key = int(np.array_str(mid_jc)[1:-1].replace(' ', ''), 2)
        if seen[key]:
            continue

        seen[key] = 1
        
        vec = np.dot(pm, mid_jc) + bi
        # print(mid_jc)
        # print(vec)
        div = is_good(vec)
        if div is not None:
            key = np.array_str(mid_jc)[1:-1].replace(' ', '')
            div = str(div)[1:-1].replace(',', '')
            print('1{0}1 {1}'.format(key[::-1], div))
            j -= 1

        if j == 0:
            break