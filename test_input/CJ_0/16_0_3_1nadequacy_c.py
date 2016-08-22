#!/usr/bin/python
import sys

def div(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return d
        d += 1
    return -1

def solve(s):
    divs = []
    for p in range(2, 11):
        x = int(s, p)
        d = div(x)
        if d == -1:
            return []
        divs.append(d)
    return divs

T = int(sys.stdin.readline().strip())
for tt in range(T):
    print 'Case #%d:' % (tt + 1)
    N, J = map(int, sys.stdin.readline().strip().split())
    for i in xrange(2**(N-3), 2**(N-2)):
        s = '1' + bin(i)[2:] + '1'
        divs = solve(s)
        if len(divs) == 9:
            print '%s %s' % (s, ' '.join(map(str, divs)))
            J -= 1
        if J == 0:
            break
