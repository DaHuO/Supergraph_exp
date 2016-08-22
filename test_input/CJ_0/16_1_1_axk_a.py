#!/usr/bin/env python3

def calc(s):
    r = ''
    for c in s:
        if not r or c >= r[0]:
            r = c + r
        else:
            r = r + c
    return r

T = int(input())
for t in range(T):
    S = input()
    r = calc(S)
    print("Case #{}: {}".format(t + 1, r))
