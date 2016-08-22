import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(10000)

class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
    def clear(self):
        self.cache = {}

def modPow(b, e, mod):
    res = 1
    b = b % mod
    while e > 0:
        if e%2 == 1:
            res = (res * b) % mod
        e = e // 2
        b = (b * b) % mod
    return res

def inputInts():
    return map(int, raw_input().split())


T = int(raw_input())
for testId in range(T):
    S = raw_input()

    res = [S[0]]
    S = S[1:]
    for c in S:
        if c >= res[0]:
            res.insert(0, c)
        else:
            res.append(c)

    print "Case #{:d}: {:s}".format(testId+1, ''.join(res))
