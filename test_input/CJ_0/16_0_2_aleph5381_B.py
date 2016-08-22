#!/usr/bin/env python3

import sys
rl = lambda: sys.stdin.readline()
T = int(rl())

def subsolve(stack):
    #print("DEBUG: ", stack, file=sys.stderr)
    n = len(stack)
    if n <= 0:
        return 0
    if n == 1:
        if stack[0] == 1:
            return 0
        else:
            stack[0] = 1 # flip
            return 1
    if stack[n-1] == 1:
        return subsolve(stack[0:n-1])
    else:
        if stack[0] == 0:
            newstack = [1^x for x in stack] # flip
            newstack = newstack[::-1]
            return 1 + subsolve(newstack)
        else:
            cnt = 1
            for i in range(n):
                if stack[i] == 0:
                    cnt = i
                    break
            stack[0:cnt] = [0] * cnt # flip
            newstack = [1^x for x in stack] # flip
            newstack = newstack[::-1]
            return 2 + subsolve(newstack)

def solve(casei):
    line = rl().split()
    mystr = str(line[0])
    mylen = len(mystr)
    stack = [0] * mylen
    for i in range(mylen):
        stack[i] = 1 if (mystr[i] == '+') else 0
    ans = subsolve(stack)
    print("Case #{}: {}".format(casei, ans))

for i in range(1, T+1):
    solve(i)
