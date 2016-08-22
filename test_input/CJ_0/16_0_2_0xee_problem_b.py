#!/bin/python

import sys


T = int(sys.stdin.readline())

lines = [sys.stdin.readline().strip() for i in range(T)]

def flip(n, stack):
    to_flip = stack[0:n].replace('-', 'x').replace('+', '-')
    to_flip = ''.join(list(reversed(to_flip.replace('x', '+'))))
    return to_flip + stack[n:]


for i, l in enumerate(lines):
    stack = l
    x = 0
#    print x, stack
    while '-' in stack:

        n = stack.find('-')
        if n != 0:
            stack = flip(n, stack)
            x = x + 1
#            print x, stack


        stack = flip(stack.rfind('-')+1, stack)
        x = x + 1
#        print x, stack


    print 'Case #%d: %d' % (i+1, x)
