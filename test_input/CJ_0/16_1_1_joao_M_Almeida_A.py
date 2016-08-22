def probAsolve(N):
    state = N[0]
    lst  = [N[0]]
    for c in N[1:]:
        if c > state:
            lst.insert(0,c)
            state = c
        else:
            lst.append(c)
    return ''.join(lst)


with open("A-small-attempt2.in") as f:
    T = int(f.next())
    for i in xrange(T):
        N = str(f.next())
        R = probAsolve(N)
        print "Case #%d: %s" % (i+1,R[:-1])
