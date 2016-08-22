import re

T = int(raw_input())

def sol1(s):
    m = len(re.findall('\-+', s))
    return (m - 1) * 2 + 1 + int(s[0] == '+')

for i in xrange(1, T + 1):
    print 'Case #%s: %s' % (i, sol1(raw_input()))