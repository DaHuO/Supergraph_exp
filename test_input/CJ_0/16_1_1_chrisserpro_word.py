#!/usr/bin/python27

import sys

def get_all(prevstr, tot):
    if len(tot) == 0:
        return [prevstr]
    nowstr1 = prevstr + tot[0]
    nowstr2 = tot[0] + prevstr
    return get_all(nowstr1, tot[1:]) + get_all(nowstr2, tot[1:]) 

def find_last(tot):
    fin =  get_all('', tot)
    fin.sort()
    return fin[-1]

c = int(sys.stdin.readline())

results = []
for cn in range(c):
    nx = sys.stdin.readline().strip()
    last = find_last(nx)
    results.append(last)

for r in range(len(results)):
    print "Case #%d: %s" % (r + 1, results[r])
