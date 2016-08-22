#!/usr/bin/env python3

import sys


def simplify(s):
    result = ''
    prev = None
    for c in s:
        if c != prev:
            result += c
            prev = c
    return result.rstrip('+')


def solve(s):
    return len(simplify(s))


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(1, n + 1):
        s = sys.stdin.readline().strip()
        print('Case #{}: {}'.format(i, solve(s)))
