#!/usr/bin/env python3

import math

def calc(N, J):
    r = []
    for x in range(2 ** (N-2)):
        divisors = []
        for p in range(2, 11):
            n = 1 + p**(N-1)
            y = x
            z = p
            while y:
                if y % 2:
                    n += z
                y //= 2
                z *= p
            d = divisor(n)
            if d > 0:
                divisors.append(str(d))
            else:
                divisors = None
                break

        if divisors:
            r.append('{0:b} {1}'.format(1 + 2**(N-1) + x*2, ' '.join(divisors)))
            if len(r) == J:
                return r

d = {}
def divisor(n):
    def f(n):
        if n <= 3:
            return 0
        if n % 2 == 0:
            return 2
        for k in range(3, int(math.sqrt(n)) + 1, 2):
            if n % k == 0:
                return k
        return 0

    if n not in d:
        d[n] = f(n)
    return d[n]

T = int(input())
for t in range(T):
    N, J = [int(x) for x in input().split()]
    r = calc(N, J)
    print("Case #{}:".format(t + 1))
    for rr in r:
        print(rr)
