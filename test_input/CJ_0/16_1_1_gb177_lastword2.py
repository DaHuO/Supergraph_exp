#!/usr/bin/python

import sys

def Ni(): return tuple(map(int, sys.stdin.readline().split()))
def Nil(): return map(int, sys.stdin.readline().split())
def Ns(): return tuple(sys.stdin.readline().split())

T = Ni()[0]

for c in range(1, T+1):
    w = Ns()[0]
    word = ""
    for l in w:
        if word + l < l + word:
            word = l + word
        else:
            word = word + l

    print "Case #%d: %s" % (c, word)

