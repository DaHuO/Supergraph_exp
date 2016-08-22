#!/usr/bin/python2

import random

MAX = 10000


def convert(t, b):
    return int(format(t, 'b'), b)
    x = 0
    while t > 0:
        x = x*b+(t & 1)
        t >>= 1
    return x


def check(t):
    c = []
    for b in xrange(2, 11):
        x = convert(t, b)
        success = False
        for p in xrange(2, MAX):
            if p != x and x % p == 0:
                success = True
                c.append(p)
                break
        if not success:
            return False
    return c


def verify(s, f):
    for b, x in zip(xrange(2, 11), f):
        if int(s, b) % x != 0:
            print "Error ", [s, f, b, x]
        return False
    return True


n = 32
target = 500
a = set()

print "Case #1:"
while len(a) < target:
    t = random.randint(2**(n-1), 2**n-1) | 1
    c = check(t)
    if c and (t not in a):
        a.add(t)
        s = format(t, '0>32b')
        verify(s, c)
        print s, ' '.join(map(str, c))
