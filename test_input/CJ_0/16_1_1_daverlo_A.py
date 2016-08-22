T = input()

for t in xrange(1, T+1):
    S = raw_input()
    out = S[0]
    for i in range(1, len(S)):
        if S[i] >= out[0]:
            out = S[i] + out
        else:
            out = out + S[i]

    print "Case #"+str(t)+":", out