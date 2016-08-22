#!/usr/bin/env python3
import sys
def q(l):
    l = l.strip()
    if not l:
        return str(0)
    prevchar = '+'
    k = 0
    for c in reversed(l):
        if c != prevchar:
            k += 1
            prevchar = c
    return str(k)

n = int(sys.stdin.readline())
for i in range(n):
    print("Case #%d: %s" % ((i+1), q(sys.stdin.readline())))
