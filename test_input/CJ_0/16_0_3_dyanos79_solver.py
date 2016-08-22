#!/usr/bin/env python
import os,sys,string

import math
def _xrange(s, v):
    num = s
    while num <= v:
        yield num
        num += 1

def expand_x_1(n): 
# This version uses a generator and thus less computations
    c =1
    for i in _xrange(0, n/2+1):
        c = c*(n-i)/(i+1)
        yield c
 
def aks(p):
    if p==2:
        return True
 
    for i in expand_x_1(p):
        if i % p:
# we stop without computing all possible solutions
            return False
    return True

def getDivisor(p, i):
    for n in _xrange(3, math.floor(math.sqrt(p))):
        #v = int(bin(n)[2:], i)
        #print p, v, n, bin(n)
        #if v > p:
        #    break
        v = n    
        if p % v == 0:
            return v
        
    return -1

problem = open(sys.argv[1], 'rt').readlines()
T = int(problem[0].strip())
p = problem[1].strip().split()
N, J = int(p[0]), int(p[1])

import fractions

startval = "".join(['1', '0'*(N-2), '1'])
endval = '1' * N

db, found = set([]), 0
print "Case #1:"
for v in range(int(startval, 2), int(endval, 2)+1):
    if v % 2 == 0:
        continue

    if found == J:
        break

    t = bin(v)[2:]
    sol = []
    for i in range(2, 11):
        pv = int(t, i)
        oo = getDivisor(pv, i)
        if oo != -1:
            sol.append(str(oo))
        else:
            break

    if len(sol) == 9:
        prevn = len(db)
        db |= set(sol)
        nextn = len(db)
        if prevn != nextn:
            print " ".join([t] + sol)
            found += 1

