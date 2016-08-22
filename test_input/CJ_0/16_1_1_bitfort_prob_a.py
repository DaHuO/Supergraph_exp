

T = raw_input()

for t in xrange(int(T)):
    s = raw_input()

    w = ''
    for a in s:
        if len(w) == 0:
            w = a
        elif w[0] <= a:
            w = a + w
        else:
            w = w + a
    print 'Case #{}: {}'.format(t+1, w)
