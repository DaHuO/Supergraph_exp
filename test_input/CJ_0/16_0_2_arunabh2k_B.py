#!/usr/bin/python

def getCount(ix, sc, ct):
    if ix == 0:
        if sc[ix] == "-":
            return ct+1
        return ct
    if sc[ix] == "+":
        return getCount(ix-1, sc, ct)
    if sc[0] == '+':
        ct += 1
        sc[0] = "-"
        idx = 1
        while sc[idx] == "+":
            sc[idx] = "-"
            idx += 1
    #reset the string
    tx = 0
    csc = []
    csc +=  sc
    while tx <= ix:
        if sc[ix-tx] == "-":
            csc[tx] = "+"
        else:
            csc[tx] = "-"
        tx += 1

    return getCount(ix-1, csc, ct+1)

f = open('B.small.txt', 'r')
tc = int(f.readline())
#print tc
for index in range(tc):
    st = f.readline().rstrip()
    sl = len(st)
    sc = []
    sc += st
    print "Case #" + str(index+1) + ": " + str(getCount(sl-1, sc, 0))
