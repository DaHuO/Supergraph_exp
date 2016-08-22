#!/usr/bin/env python

from sys import stdin, stderr

T = int(stdin.readline())

def Solve(S):
    if len(S) == 0: return ''
    bi = 0
    bc = S[0]
    for i, c in enumerate(S):
        if bc <= c: bi, bc = i, c
        pass

    search = bi
    last = 0
    while search > 0:
        search -= 1
        if S[search] != bc: break
        last += 1
        pass
    
    return S[bi-last:bi+1] + Solve(S[:bi-last]) + S[bi+1:]

# for i in range(100):
#     print Solve('A' * 1000)
# exit(0)


for t in range(T):
    S = stdin.readline().strip()

    print "Case #%d:" % (t+1),
    print Solve(S)
