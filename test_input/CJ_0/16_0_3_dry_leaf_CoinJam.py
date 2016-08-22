#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def CoinJam():
    T = 1

    out = open("C-small-attempt0.out", "w")
    for n in range(T):

        N = 16
        J = 50

        jams = set()
        i = 0
        out.write("case #{}:\n".format(n+1))
        while i != range(J):
            jamcoin = '1'
            arr = np.random.choice([0, 1], size=((N-2),))
            mid = ''.join(str(x) for x in arr.tolist())
            jamcoin += mid + '1'
            num = [int(jamcoin, n) for n in range(2, 11)]
            if not isPrime(num):
                if jamcoin not in jams:
                    res = list(divisorGenerator(num))
                    if len(res) == 9:
                        # print num, isPrime(num)
                        jams.add(jamcoin)
                        print "{} {}".format(jamcoin, res)
                        out.write("{} {}\n".format(jamcoin, ' '.join(str(k) for k in res)))
                        i += 1
            if i == J:
                break
    out.close()

def divisorGenerator(n):

    for x in n:
        large_divisors = []
        flag = False
        for i in xrange(2, int(x**0.5) + 1):
            if x % i == 0:
                yield i
                flag = True
                if i*i != x:
                    large_divisors.append(x / i)
                break
        for divisor in reversed(large_divisors):
            if not flag:
                yield divisor
                break

def isPrime(numbers):
    for x in numbers:
        if x >= 2:
            for y in xrange(2, x):
                if not (x % y):
                    return False
        else:
            return False
    return True

if __name__ == '__main__':
    CoinJam()
