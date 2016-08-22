T = int(raw_input().strip())

for t in xrange(T):
    S = raw_input().strip()
    result = 0
    start = None
    for c in S:
        if not start:
            start = c
        if c != start:
            result += 1
            start = c
    if start == '-':
        result += 1
    print 'Case #%d: %d' % (t + 1, result,)

