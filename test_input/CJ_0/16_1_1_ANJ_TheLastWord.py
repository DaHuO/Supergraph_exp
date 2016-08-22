T = input()

for i in xrange(1, T+1):
    s = raw_input()
    r = ''
    for c in s:
        if r:
            if c >= r[0]:
                r = c + r
            else:
                r += c
        else:
            r += c

    print "case #" + str(i) + ": " + r