#!/usr/bin/python

T = int(raw_input())

CASE = 1

while T > 0:
    T -= 1
    S = raw_input()
    ret = 0

    while '-' in S:
        start = S[0]

        if start == '+':
            opposite = '-'
        else:
            opposite = '+'

        x = S.find(opposite)
        if x != -1:
            S = opposite * x + S[x:] # flip
        elif start == '-':
            ret += 1
            break
        ret += 1

    print 'Case #%d:' % CASE, ret
    CASE += 1
