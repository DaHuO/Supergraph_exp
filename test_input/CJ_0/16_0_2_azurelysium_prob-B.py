#!/bin/python
#
# Google Codejam 2016
# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
#
import sys
def rl(): return sys.stdin.readline().strip()

def pancakes(pile, goal=True, flips=0):
    if len(pile) == 0:
        return flips
    return pancakes(pile[:-1], goal, flips) if pile[-1] == goal else pancakes(pile[:-1], not goal, flips+1)

CASES = int(rl())
for case in xrange(CASES):
    pile = map(lambda x: x=='+', rl())
    print 'Case #%d: %s' % (case+1, pancakes(pile))
