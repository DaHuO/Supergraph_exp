#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def pack(cakes):
    packed = []
    prev_c = None
    for c in cakes:
        if c != prev_c:
            packed.append(c)
        prev_c = c
    if prev_c == '+':
        # remove it
        packed.pop()

    return packed

def solve(cakes):
    cakes = pack(cakes)
    if len(cakes) == 0:
        return 0
    if len(cakes) == 1 and cakes[0] == '-':
        return 1

    if cakes[0] == '+':
        # +-...+-
        return len(cakes)

    # -+...+-
    return len(cakes)

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        cakes = f.readline().rstrip()
        answer = solve(cakes)
        print "Case #%d: %d" % (i+1, answer)

# sort by key
# for k,v in sorted(d.items())
# sort by value
# for k,v in sorted(d.items(), key=lambda x:x[1])
# items() return tapple, tapple[0] is k, tapple[1] is v
#
# import copy
# copy.copy()
# copy.deepcopy()
#
# a = [0]*100
#
# for tc in xrange(1, int(sys.stdin.readline())+1):
#   A, B = [int(w) for w in sys.stdin.readline().split()]
#   p = [float(w) for w in sys.stdin.readline().split()]
#
# array = [[0 for j in range(m)] for i in range(n)]

