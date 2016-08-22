#!/usr/bin/env python

for cas in xrange(input()):
    ans = 0
    x=list(raw_input().strip())
    for i in xrange(len(x)-1):
        ans += x[i] != x[i+1]
    if x[-1]=='-':
        ans += 1
    print "Case #%d: %d" % (cas+1, ans)
