#!/usr/local/bin/python3
import numpy as np
c = int(input())

ns = np.array([input() for case in range(c)])


def solve(v):
    t = [v[0]]

    for c in v[1:]:
        joined = "".join(t)
        if joined + c < c + joined:
            t.insert(0, c)
        else:
            t.append(c)

    return "".join(t)

vfunc = np.vectorize(solve)

for case, item in enumerate(vfunc(ns)):
    print ('Case #{}: {}'.format(case + 1, item))
