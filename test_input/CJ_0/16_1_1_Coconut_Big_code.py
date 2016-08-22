T = int(raw_input().strip())
for t in xrange(T):
    S = raw_input().strip()
    result = ''
    for c in S:
        if len(result) == 0 or ord(c) < ord(result[0]):
            result += c
        else:
            result = c + result
    print 'Case #%d: %s' % (t + 1, result,)
