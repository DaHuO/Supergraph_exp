#!/usr/bin/env python

import sys

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input()
    leng = len(s)
    
    #print "#%d input : %d(%s)" %(i, leng, s)
    if s[leng-1] == '-':
        cnt = 1
        #print "1"
    else:
        cnt = 0

    if leng > 1:
        for j in range(leng-1):
            if s[j] != s[j+1]:
                cnt = cnt+1
                #print "+1"
    
    print "Case #%d: %d" %(i, cnt)


