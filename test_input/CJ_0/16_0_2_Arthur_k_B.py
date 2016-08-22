#!/usr/local/bin/python3
import numpy as np
import re
c = int(input())

ns = np.array([input() for case in range(c)])


def solve(v):
    return len(v)


ns = [item.rstrip("+") for item in ns]
ns = [re.sub(r"[\-]+", "-", item) for item in ns]
ns = [re.sub(r"[\+]+", "+", item) for item in ns]

#print (ns)
vfunc = np.vectorize(solve)

for case, item in enumerate(vfunc(ns)):
    print ('Case #{}: {}'.format(case + 1, item))
