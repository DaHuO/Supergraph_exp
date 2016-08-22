#! /usr/bin/env python
"""
Name: Sravan Bhamidipati
Date: 8th April, 2016
Purpose: https://code.google.com/codejam/contest/6254486/dashboard#s=p1
"""

import sys


def flip(sequence, n):
    return [not sequence[i] if i < n else sequence[i] for i in xrange(len(sequence))]


def booleanize(sequence):
    return [True if s == '+' else False for s in sequence]


def find_next_break(sequence):
    for i in xrange(len(sequence)):
        if sequence[i] != sequence[0]:
            return i
    else:
        return None


def create_happiness(str):
    sequence = booleanize(str)
    flips = 0
    while True:
        next_break = find_next_break(sequence)
        if next_break is None:
            if True in sequence:
                return flips
            else:
                return flips + 1
        else:
            sequence = flip(sequence, next_break)
            flips += 1


with open(sys.argv[1]) as fd:
    for line_no, line in enumerate(fd):
        if line_no == 0:
            continue
        else:
            print 'Case #%s: %s' % (line_no, create_happiness(line.strip()))
