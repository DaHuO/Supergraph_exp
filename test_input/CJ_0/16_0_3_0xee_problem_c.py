#!/bin/python

import sys


T = int(sys.stdin.readline())

lines = [sys.stdin.readline().strip() for i in range(T)]


def is_prime(n):
    if n == 2 or n == 3:
        return None
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    m = 2

    while i <= 1000:
        if n % i == 0:
            return i

        i += m
        m = 6 - m

    return None


for i, l in enumerate(lines):

    jamcoins = {}

    N, J = (int(s) for s in l.split())

    x = 0
    while len(jamcoins) < J:
        c = '1' + ('{0:0%db}' % (N-2)).format(x) + '1'
#        print 'trying:', c
        divs = []
        for base in range(2, 11):
            interpr = int(c, base)
            div = is_prime(interpr)
            if div is None:
                break
            divs.append(div)

        if len(divs) == 9:
#            print 'found:', c, divs
            jamcoins[c] = divs

        x = x + 1



    print 'Case #%d:' % (i+1)
    for c, divs in jamcoins.items():
        print ' '.join([c] + map(str, divs))
