def lastword(S):
    r = ""
    first = 'Z'
    for c in S:
        if ord(c) >= ord(first):
            r = c + r
        else:
            r = r + c
        first = r[0]
        #print "c : ", c
        #print "f : ", first        
    return r

N = int(raw_input ())
for i in range(N):
    S = raw_input()
    print "Case #%d: %s" %  (i+1, lastword(S))