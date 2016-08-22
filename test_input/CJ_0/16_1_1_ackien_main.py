#!/usr/bin/python

from sys import stdin, stdout

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    S = stdin.readline().strip()
    P = []
    for c in S:
        if not len(P):
            P.append(c)
        else:
            if c >= P[0]:
                P.insert(0,c)
            else:
                P.append(c)
    answer = ''.join(P)
    stdout.write("Case #{:d}: {:s}\n".format(case_num, answer))
