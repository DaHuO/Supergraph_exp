T=int(raw_input())

for i in xrange(T):
    S = raw_input()
    firstC = S[0]
    nS = ''
    for c in S:
        if c>=firstC:
            nS = c+nS
            firstC=c
        else:
            nS = nS+c
    print "Case #%d: %s"%(i+1,nS)