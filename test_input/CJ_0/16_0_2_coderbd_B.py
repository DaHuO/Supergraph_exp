#!/usr/bin/python

t = int(raw_input())
for case_no in xrange(1, t+1):
    s = raw_input()
    pre, cur, ans = None, None, 0
    for c in s:
        cur = c
        if pre is not None and pre != cur:
            ans += 1
        pre = cur
    if cur == '-':
        ans += 1
    print 'Case #%d: %d' % (case_no, ans)
