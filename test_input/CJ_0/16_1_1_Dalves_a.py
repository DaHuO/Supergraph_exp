t = int(raw_input())

for i in xrange(t):
    s = raw_input()
    r = []
    for l in s:
        if not r or r[0] <= l:
            r.insert(0, l)
        else:
            r.append(l)
    print "Case #%d: %s" % (i+1, ''.join(r))
