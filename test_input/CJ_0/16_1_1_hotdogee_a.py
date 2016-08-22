#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(s):
    l = s[0]
    for c in s[1:]:
        if c >= l[0]:
            l = c + l
        else:
            l = l + c
    return l
    

if __name__ == "__main__":
	for case in xrange(1, 1+input()):
		print "Case #{0}: {1}".format(case, solve(raw_input())) # one string