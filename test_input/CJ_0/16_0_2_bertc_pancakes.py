# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 08:36:44 2016

@author: BCLAES
"""

def handle_case(pcs):
    while pcs.endswith("+"):
        pcs = pcs[:-1]
    if len(pcs) > 0:
        return solve(pcs)
    else:
        return 0

def solve(pcs):
    if 1 == len(pcs):
        return 1
    pos = -1
    while "-" == pcs[pos-1]:
        pos -= 1
        if (-pos) == len(pcs):
            return 1            
    leftover = str(pcs[0:pos])
    return 2+handle_case(leftover)
    
solutions = []
with open("B-large.in") as f:
    test_cases = int(f.readline())
    for i in xrange(0,test_cases):
        m = str(f.readline())
        if m.endswith("\n"):
            m = m[:-1]
        x = handle_case(m)
        strout = str.format("Case #{}: {}\n", i+1, x)
        solutions.append(strout)
with open("output.txt", "w") as out:
        out.writelines(solutions)    