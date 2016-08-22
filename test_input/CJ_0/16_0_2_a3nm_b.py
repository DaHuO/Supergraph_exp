#!/usr/bin/python3

import sys

T = int(sys.stdin.readline().strip())

for ncase in range(T):
    S = sys.stdin.readline().strip()
    goal = '+'
    S = S[::-1]
    cost = 0
    for i in range(len(S)):
        if S[i] != goal:
            cost += 1
            goal = '-' if goal == '+' else '+'
    print("Case #%d: %d" % (ncase + 1, cost))



