#!/usr/bin/env python

translation = str.maketrans('+-', '-+')

T = int(input())

for i in range(1, T + 1):
    stack = input()
    s = 0

    while '-' in stack:
        s += 1
        
        lastBS = stack.rfind('-')
        stack = stack[0:lastBS+1].translate(translation) + stack[lastBS+1:]

    else:
        print('Case #{}: {}'.format(i, s))
