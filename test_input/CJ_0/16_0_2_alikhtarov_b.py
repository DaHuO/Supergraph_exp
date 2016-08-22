#!/usr/bin/python

import sys

for i, s in enumerate(sys.stdin.readlines()[1:]):
    s = s.strip()
    print "Case #%d:" % (i+1), sum(1 for i in range(len(s) - 1) if s[i] != s[i+1]) + (1 if s[-1] == '-' else 0)
