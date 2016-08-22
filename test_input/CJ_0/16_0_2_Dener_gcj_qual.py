#!/usr/bin/python

import sys


N = int(sys.stdin.readline().strip())

for test in xrange(1, N + 1):
    print "Case #{}:".format(test),
    str = sys.stdin.readline().strip()
    #print >> sys.stderr, str

    while len(str) > 0 and str[-1] == '+':
        str = str[:-1]

    ans = 0
    cur_state = '+'
    while len(str) > 0:
        if str[-1] != cur_state:
            cur_state = str[-1]
            ans += 1
        str = str[:-1]

    print ans
