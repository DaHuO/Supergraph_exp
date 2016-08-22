#!/usr/bin/env python

import sys, random, sympy
from math import pow


def get_factor(n):
    lim = int(pow(n, 0.2))
    for i in xrange(2, lim + 1):
        if n % i == 0:
            return i
    return None


def test(bits):
    nums = [int(bits, b) for b in xrange(2, 11)]
    if any(sympy.ntheory.primetest.isprime(n) for n in nums):
        return None
    ans = []
    for b in xrange(2, 11):
        factor = get_factor(nums[b - 2])
        if factor is None:
            return None
        ans.append(factor)
    return ans


def main():
    n, j = map(int, sys.stdin.readlines()[1].split())
    print 'Case #1:'
    tried = set()
    while j > 0:
        bits = '1' + '{0:b}'.format(random.getrandbits(n - 2)).zfill(n - 2) + '1'
        if bits in tried:
            continue
        tried.add(bits)
        res = test(bits)
        if res is not None:
            j -= 1
            print >> sys.stderr, 'found', j
            print bits, ' '.join(map(str, res))


if __name__ == '__main__':
    main()
