#!/usr/bin/python

import sys

def solve(s):
    sign = '+'
    cnt = 0
    for c in s[::-1]:
        if c != sign:
            sign = '+' if sign == '-' else '-'
            cnt += 1
    return cnt

T = int(input())
for t in range(T):
    print('Case #{}: {}'.format(t + 1,  solve(input())))

