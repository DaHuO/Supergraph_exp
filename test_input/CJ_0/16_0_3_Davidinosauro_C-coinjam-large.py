from __future__ import print_function

import sys
from random import random
from itertools import count

with open("./primes_2_24") as f:
    primes = [int(line.strip()) for line in f]

J = 500
j = 0

while j < J*5//4:
    line = sys.stdin.readline()
    coin, rest = line.strip().split(None, 1)
    nums = [int(coin, base=b) for b in range(2, 11)]

    factors = []
    all_factored = True
    for k, num in enumerate(nums):
        curr_factored = False
        for p in primes:
            if p >= num:
                break
            if num % p == 0:
                factors.append(p)
                curr_factored = True
                break
        if not curr_factored:
            all_factored = False
            break
    
    if all_factored:
        assert len(factors) == len(nums)
        j += 1
        print(coin + ' ' + ' '.join(str(x) for x in factors))

