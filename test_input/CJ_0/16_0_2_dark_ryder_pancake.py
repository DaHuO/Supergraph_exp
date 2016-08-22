T = input()
for t in xrange(T):
    S = raw_input()
    S = map(lambda x: x == '+',list(S))
    I = len(S)

    flipped = False
    count = 0
    for i in range(I - 1, -1, -1):
        what = S[i]
        if flipped: what = not what
        if not what:
            count += 1
            flipped = not flipped
    print "Case #%d: %d" % (t+1, count)
