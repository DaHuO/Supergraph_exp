#!/usr/bin/python3

import sys

sys.setrecursionlimit(1000000)

beta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

from functools import partial
from operator import add

flip = lambda f: lambda x, y: f(y, x)
rev = partial(reduce, flip(add))

def recurse(start, last, bits, nxt):
    n = nxt[-1]
    i = beta.index(n)
    if len(nxt) == 1:
        if i >= last:
            return bits + n
        else:
            return n + bits

    elif i >= last:
        bits = recurse(start, i, bits + n, nxt[:-1])
    else:
        bits = recurse(i, last, n + bits, nxt[:-1])

    return bits

T = int(input())
for _ in range(T):
    s = rev(input()[:-1])
    i = beta.index(s[-1])
    if len(s) == 1:
        print("Case #" + str(_+1) + ": " + s)
    else:
        print("Case #" + str(_+1) + ": " + rev(recurse(i,i,s[-1],s[:-1])))

"""
def determine(meta, times):
    pass

T = int(input())
for _ in range(T):
    obj = (lambda x: {'N':int(x[0]),'K':int(x[1])})(input().split(' '))
    print(determine(obj, [int(x) for x in input().split(' ')]))

# Data structures from input
# Array
[int(x) for x in input().split(' ')]
# Dict
(lambda x: {'N':int(x[0]),'K':int(x[1])})(input().split(' '))
# Class
class X:
    def __init__(self, attrs):
        puts = [int(x) for x in input().split(' ')]
        i = 0
        for attr in attrs:
            setattr(self,attr,puts[i])
            i += 1
"""