#!/usr/bin/env python

import sys

def groups(n):
    if n == ():
        return 0
    c = n[0]
    for i in xrange(1, len(n)):
        if n[i] != c:
            return 1 + groups(n[i:])
    return 1

def solvePancakes(n):
    res = groups(n)
    if n[len(n)-1]:
        res -= 1

    return res

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    for i in xrange(n):
        pancakes = tuple(c == "+" for c in [x for x in sys.stdin.readline() if x in ('-', '+')])
        print "Case #%d: %s" % (i + 1, solvePancakes(pancakes))
