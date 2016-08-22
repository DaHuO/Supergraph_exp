#!/usr/bin/env python2


def solve():
    S = raw_input()

    R = S[0]

    for c in S[1:]:
        if ord(c) >= ord(R[0]):
            R = c + R
        else:
            R = R + c
    print R


T = int(raw_input())

for i in xrange(1,T+1):
    print 'Case #%d:' % (i),
    solve()
