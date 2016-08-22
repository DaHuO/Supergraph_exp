#!/usr/bin/python

import os
import math

inf = open('input.in','r')
inp = inf.read().split('\n')
inf.close()
T = int(inp.pop(0))

def last_word(s):
    last = s[0]
    for i in range(1,len(s)):
        if s[i] >= last[0]:
            last = s[i] + last
        else:
            last = last + s[i]
    return last

outf = open('output','w')
for i in range(T):
    S = inp.pop(0)
    outf.write('Case #%d: %s\n'%(i+1, last_word(S)))

outf.close()