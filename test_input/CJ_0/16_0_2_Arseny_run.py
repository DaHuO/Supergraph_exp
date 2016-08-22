#!/usr/bin/env python

import sys


def digits(k):
    result = set()
    while (k > 0):
        result.add(k % 10)
        k = k / 10
    return result


def solve(x):
    k = len(x) - 1
    flips = 0
    while True:
        good = '+' if (flips % 2 == 0) else '-'
        while (x[k] == good):
            k-= 1
            if k < 0:
                return flips
        flips+= 1


if __name__ == '__main__':
    sys.stdin.readline()
    casenum = 0
    for line in sys.stdin:
        casenum+= 1
        pancakes = line.strip()
        answer = solve(pancakes)
        print "Case #%s:" % casenum, answer
