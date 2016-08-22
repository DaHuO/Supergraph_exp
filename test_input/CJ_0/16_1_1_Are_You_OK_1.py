#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint

def solve1(s):
    l = [s[0]]
    for i in range(1, len(s)):
        l = sum([[x+s[i], s[i]+x] for x in l], [])
    return max(l)

def solve(s):
    out = s[0]
    for i in range(1, len(s)):
        x = s[i]
        if out[0] > x:
            out = out + x
        else:
            out = x + out
    return out

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