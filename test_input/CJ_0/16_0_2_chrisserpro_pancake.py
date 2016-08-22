#!/usr/bin/python27

import sys

def flip(fl, n):
    flnew = ""
    if n == 0:
        if fl[0] == '-':
            flnew = '+'
        else:
            flnew = '-'
        return flnew + fl[1:]
    for f in fl[:n]:
        if f == '-':
            flnew += '+'
        else:
            flnew += '-'
    return flnew[::-1] + fl[n:]

c = int(sys.stdin.readline())

results = []
for cn in range(c):
    fl = sys.stdin.readline().strip()
    cnt = 0
    while '-' in fl:
        ind = fl.find('-')
        if len(fl) == 1 and ind == 0:
            fl = flip(fl, 0)
        elif ind == 0:
            indp = fl.find('+')
            if indp == -1: # no positives, flip all
                fl = flip(fl, len(fl))
            elif fl[-1] == '-':
                fl = flip(fl, len(fl))
            elif fl.rfind('-') > fl.find('+') and fl.rfind('-') < len(fl):
                fl = flip(fl, fl.rfind('-')+1)
            elif not '-' in fl[indp:] and indp > -1:
                fl = flip(fl, indp)
        elif ind > 0:
            fl = flip(fl, ind )
        else:
            ind = fl.find('+')
            fl = flip(fl, ind - 1)
        cnt += 1
    results.append(cnt)

for i in range(len(results)):
    print "Case #%d: %d" % (i+1, results[i])
