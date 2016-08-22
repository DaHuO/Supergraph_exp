#!/usr/bin/env python2

import sys

count = int(sys.stdin.readline().strip())
case = 1


def solve(seq):
    sys.stderr.write('Processing {}\n'.format(seq))

    seq = list(seq)

    if len(seq) == 1:
        if seq[0] == '+':
            return 0
        return 1

    target = ['+'] * len(seq)

    flips = 0

    while seq != target:
        flip = -1

        for i, c in enumerate(seq[:-1]):
            c2 = seq[i + 1]
            if c != c2:
                flip = i + 1
                break

        sys.stderr.write('Flip at {}\n'.format(flip))

        if flip != -1:
            picked = seq[:flip]
            remaining = seq[flip:]
        else:
            picked = seq
            remaining = []

        seq = [('+' if x == '-' else '-') for x in reversed(picked)] + remaining

        sys.stderr.write('New value: {}\n'.format(seq))

        flips += 1

    return flips

while case <= count:
    arg = sys.stdin.readline().strip()
    print 'Case #{}: {}'.format(case, solve(arg))
    case += 1
