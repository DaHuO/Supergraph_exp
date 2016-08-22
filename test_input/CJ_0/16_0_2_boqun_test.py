#!/usr/bin/env python3

import sys

def reverse(s):
    return '-' if s == '+' else '+'

def flip(s, to):
    l = len(s)
   
    if l == 1:
        if s[0] == to:
            return 0
        else:
            return 1

    if s[l-1] == to:
        return flip(s[:-1], to)
    else:
        return flip(s[:-1], reverse(to)) + 1

n = []
for line in sys.stdin:
    n.append(line.strip())

for i in range(1, len(n)):
    print("Case #%d: %d" % (i, flip(n[i], '+')))
