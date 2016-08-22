#!/bin/env python
#coding: utf8

from __future__ import generators
import sys
import time

def parse_input():
    count = int(sys.stdin.readline())
    for n in range(count):
        x, y = map(int, sys.stdin.readline().split())
        yield n + 1, x, y

def sieve_range(start, end):
    return 0

def eratosthenes(limit):
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while q < limit:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

def find_divisor(n):
    #if n in (2, 3, 5, 7):
    #    return False
    #for d in xrange(int(n**0.5), 3, -1):
    #if n % 2 == 0:
    #    return 2
    #if n % 3 == 0:
    #    return 3
    #for d in eratosthenes(int(n**0.5)):
    for d in xrange(3, int(n**0.5), 2):
        if n % d == 0:
            return d
    return False


def test_jamcoin(coin, n):
    # if len(coin) != n:
    #    return False, ['length']
    # if coin[0] != coin[-1] != '1': # this is ensured already in calling func
    #    return False, ['1s']
    divisors = []
    for b in range (2, 11):
        nx = int(coin, b)
        d = find_divisor(nx)
        if not d:
            return False, divisors
        divisors.append(d)
        #divisors.insert(0, d)
    return True, divisors


def solve_task(n, j):
    tested = 0
    last_bunch_start = time.time()
    results = []
    for x in xrange(2**(n-1) + 1, 2**(n), 2):
        coin = bin(x)[2:]
        # print "testing %s" % coin
        result, divisors = test_jamcoin(coin, n)
        # print result, divisors
        if result:
            results.append([coin] + divisors)
            if len(results) == j:
                return results
        tested += 1
        if tested % 5 == 0:
            print >> sys.stderr, "Tested %d nums in %ss, found %s results" % \
                                 (tested, time.time() - last_bunch_start, len(results))
            #last_bunch_start = time.time()
    return results

for i, n, j in parse_input():
    print "Case #%s:" % (i)
    for l in solve_task(n, j):
        print ' '.join(map(str, l))


