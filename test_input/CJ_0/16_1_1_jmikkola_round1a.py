T = int(raw_input())
for x in xrange(T):
    S = raw_input()
    '''
    maxOut = ""
    for i in xrange(2 ** (len(S) - 1)):
        out = S[0]
        for c in S[1:]:
            if i & 1 == 1:
                out = out + c
            else:
                out = c + out
            i = i >> 1
        maxOut = max(out, maxOut)
    '''

    out2 = S[0]
    for c in S[1:]:
        out2 = max(out2 + c, c + out2)
    print 'Case #{}: {}'.format(x+1, out2)
