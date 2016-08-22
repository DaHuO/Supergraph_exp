#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from functools32 import lru_cache

def solve(s):
    n = len(s)
    @lru_cache(None)
    def f(i, c):
        if i < 0:
            return 0
        if s[i] == c:
            r = f(i-1, c)
        else:
            r = f(i-1, c == '+' and '-' or '+') + 1
        return r
    return f(n-1, '+')

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
def test():
    pass

def readInt():
    return int(sys.stdin.readline().strip())

def readInts():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def readStrs():
    return [x for x in sys.stdin.readline().strip().split()]

def main():
    n = readInt()
    for i in xrange(n):
        s = readStrs()[0]
        print 'Case #%d: %s' % (i+1, solve(s))
    pass

if __name__ == '__main__':
    main()