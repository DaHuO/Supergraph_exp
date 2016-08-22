#!/usr/bin/python

import sys
import random

PR = []
N = (16000000)
ISPR = [True] * N
ISPR[0] = ISPR[1] = False
for c in range(2, N):
    if ISPR[c]:
        PR.append(c)
        for j in range(c * c, N, c):
            ISPR[j] = False

def get_divs(bx):
    b = []
    divs = []
    for base in range(2, 10):
        y = int(bx, base)
        b.append(y)
        for p in PR:
            if p * p > y:
                return None, None
            if y % p == 0:
                divs.append(p)
                break
    return b, divs

s = sys.stdin.readlines()
n, j = [int(x) for x in s[1].split()]

print "Case #1:"

used = set()

for i in range(j):
    while True:
        x = (1<<(n-1)) | 1 | (random.randint(0, (1<<(n-2)) - 1) << 1)
        bx = bin(x)[2:]
        if sum(1 for c in bx if c == '1') % 3:
            continue
        if x in used:
            continue
        b, d = get_divs(bx)
        if d is not None:
#            print bx
#            print b
#            print d
#            print [b[i] % d[i] for i in range(len(b))]
            d.append(3)
            print bx, " ".join(str(c) for c in d)
            used.add(x)
            break
