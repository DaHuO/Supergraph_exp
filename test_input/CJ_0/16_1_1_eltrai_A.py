#!/usr/bin/env python3
# *-* coding: utf-8 *-*

def readint():
    return int(input())

def readints():
    return map(int, input().split())

def readline():
    return str(input())

T = readint()
for case in range(T):
    S = list(readline())
    best = [S[0]]
    for s in S[1:]:
        if s >= best[0]:
            best.insert(0, s)
        else:
            best.append(s)
    result = ''.join(best)
        



    print("Case #%d: %s" % (case+1, result))
