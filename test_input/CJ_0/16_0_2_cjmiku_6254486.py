#!/usr/bin/env python
# coding: utf-8

"""
--+-
++-+
--++
++++

+-
-+
++

-+-+-+++
+-+-++++
-+-+++++
+-++++++
-+++++++
++++++++
"""

from __future__ import print_function
import math
import sys

def flip(pancakes, k):
    flipped = []
    for i, p in enumerate(pancakes):
        if i < k:
            if p == '+':
                flipped.append('-')
            else:
                flipped.append('+')
        else:
            flipped.append(p)
    return ''.join(flipped)

def solve(pancakes):
    i = 0
    while '-' in pancakes:
        b = pancakes.rfind('-')
        pancakes = flip(pancakes, b + 1)
        i += 1
    return i

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: %s FILE' % sys.argv[0])
        sys.exit(1)
    fn = sys.argv[1]
    with open(fn) as handle:
        _ = handle.next()
        for i, line in enumerate(handle, start=1):
            line = line.strip()
            if line == "":
                continue
            # print(line, flip(line, 0), solve(line))
            print("Case #%s: %s" % (i, solve(line)))
