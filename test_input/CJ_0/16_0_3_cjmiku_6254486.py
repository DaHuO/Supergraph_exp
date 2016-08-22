#!/usr/bin/env python
# coding: utf-8

"""
* http://math.stackexchange.com/questions/104316/prove-that-n-2k-1-is-not-a-prime-number-with-k-ab-edit-a-not-1-and

n = 2^k - 1, if k = ab, then n is not prime.

For even number of 1 in binary representation, all uneven numbers sum up to an even number.
So for even number of 1, we need to check whether, 2^k + 1 is prime.
"""

import random

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def mint(length=32):
    return '1%s1' % (''.join([str(random.randint(0, 1)) for _ in range(length-2)]))

def checkrange(length=32):
    a = '1' + '0' * (length - 2) + '1'
    b = '1' * length
    print(int(a, 2), int(b, 2))

if __name__ == '__main__':
    # coin = mint(length=16)
    # for i in range(2, 11):
    #     print(i, coin, int(coin, i), isprime(int(coin, i)))
    # checkrange()
    for i in xrange(2147483649, 4294967295):
        binary = bin(i)[2:]
        if not binary.startswith('1'):
            continue
        if not binary.endswith('1'):
            continue
        if not any([isprime(int(binary, b)) for b in range(2, 11)]):
            print(i, int(bin(i)[2:]))

