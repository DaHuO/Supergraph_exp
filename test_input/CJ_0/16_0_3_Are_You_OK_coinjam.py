#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from itertools import product
from functools32 import lru_cache

primes = """
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71
73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173
179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281
283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409
419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541
547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659
661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809
811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941
947 953 967 971 977 983 991 997""".strip().split()
primes = map(int, primes)

def int2str(p, base):
    s = []
    while p:
        x = p % base
        p /= base
        s.append(x)
    s.reverse()
    return "".join(map(str, s))

def solve2(n, j):
    invs = set()
    for base in range(2, 11):
        m = base ** (n-1) + 1
        for p in primes:
            if p < m:
                continue
            s = int2str(p, base)
            invs.add(s)
    print invs

def solve(n, j):
    factors = []
    for x in product('01', repeat=n-2):
        x = ['1'] + list(x) + ['1']
        x = "".join(x)
        del factors[:]
        for base in range(2, 11):
            isp, factor = is_prime(int(x, base))
            if isp:
                break
            factors.append(factor)
        else:
            j -= 1
            print x, " ".join(map(str, factors))
            if j <= 0:
                break

@lru_cache(None)
def is_prime(n):
    for i in xrange(2, int(n**0.5+1)):
        if n%i == 0:
            return False, i
    return True, 0

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
def test():
    assert is_prime(2)[0]
    assert is_prime(3)[0]
    assert not is_prime(4)[0]

    assert int2str(33, 10) == '33'
    assert int2str(100, 10) == '100'
    assert int2str(4, 2) == '100'
    solve(6, 3)
    solve(16, 50)
    pass

def readInt():
    return int(sys.stdin.readline().strip())

def readInts():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def readStrs():
    return [x for x in sys.stdin.readline().strip().split()]

def main():
    n = readInt()
    for i in xrange(n):
        N, J = readInts()
        print 'Case #%d:' % (i+1)
        solve(N, J)
    pass

if __name__ == '__main__':
    main()