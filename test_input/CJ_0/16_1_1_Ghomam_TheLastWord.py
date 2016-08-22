# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 01:54:52 2016

@author: Ghomam
"""
import sys

print sys.argv[1]
inp = open(sys.argv[1]).readlines()


def raw_input():
    return inp.pop(0).strip()

# Read input data
T = int(raw_input())
tests = []
for i in xrange(T):
    S = raw_input().strip()
    tests.append(S)


O = ['' for s in tests]
for i,S in enumerate(tests):
    O [i] = S[0]
    for s in S[1:]:
        if s >= O[i][0]:
            O[i] = s + O[i]
        else:
            O[i] = O[i] + s



# output
output = open('output.out', 'w')
for i,o in enumerate(O):
    out = 'Case #{}: {}'.format(i+1, "".join(list(o) ))
    print out
    if i > 0 : out = '\n'+out
    output.write(out)
output.close()