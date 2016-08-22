#!/bin/env python

# google code jam 2016 round 1A problem A
# Daniel Scharstein

import sys

def solve(s):
    r = s[0]
    for c in s[1:]:
	if c >= r[0]:
	    r = c + r
	else:
	    r += c
    return r

tests = int(raw_input())
for k in range(tests):
    s = raw_input()
    x = solve(s)
    print "Case #%d: %s" % (k+1, x)
