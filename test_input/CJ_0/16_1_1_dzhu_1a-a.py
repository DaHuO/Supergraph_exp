def go(s):
    if len(s) <= 1: return s

    c = max(s)
    i = s.index(c)
    sub = s[i:]
    sub2 = sub.translate(None, c)
    n = len(sub) - len(sub2)

    return c * n + go(s[:i]) + sub2

import sys
ln = sys.stdin.readline
N = int(ln())
for i in xrange(N):
    print 'Case #%d: %s' % (i + 1, go(ln().strip()))

# import random, string
# s = ''.join(random.choice(string.lowercase) for _ in xrange(1000))
# print s
# print go(s)
