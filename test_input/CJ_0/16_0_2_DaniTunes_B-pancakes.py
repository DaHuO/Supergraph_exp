#!/bin/env python

# google code jam 2016 qualifiers problem 2
# Daniel Scharstein

import sys

def solve(s):
    prev = '+'
    n = 0
    for c in s[::-1]:
	if c != prev:
	    prev = c
	    n += 1
    return n

tests = int(raw_input())
for k in range(tests):
    s = raw_input()
    x = solve(s)
    print "Case #%d: %s" % (k+1, x)
