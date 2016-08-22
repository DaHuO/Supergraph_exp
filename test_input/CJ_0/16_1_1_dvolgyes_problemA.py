#!/usr/bin/python
from __future__ import division,print_function
import sys
import numpy as np     # http://www.numpy.org/
import scipy           # http://scipy.org/
import networkx as nx  # https://networkx.github.io/
import sympy           # http://www.sympy.org
import itertools
import operator
import string

range = xrange

sys.setrecursionlimit(5000)

def solve(s,*args,**kwargs):
    solution = ""
    for c in s:
        if len(solution)==0 or c>=solution[0]:
            solution = c+solution
        else:
            solution = solution+c
    return solution


T = int(sys.stdin.readline())
for t in range(1,T+1):
    s = sys.stdin.readline().strip()
    print("Case #%i: %s" % (t,solve(s)))
