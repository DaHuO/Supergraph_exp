#!/usr/bin/env python

import sys


def invert(s):
    return ''.join('+' if c == '-' else '-' for c in s)


def reverse(s):
    return ''.join(reversed(s))


def flip(s):
    return reverse(invert(s))


def solve(s):
    n = len(s)

    cache = {}
    def get_min(s, m):
        n = len(s)

        if n == 0:
            return 0

        if all(c == m for c in s):
            return 0

        if all(c != m for c in s):
            return 1

        if (s, m) in cache:
            return cache[(s, m)]

        ans = 999999
        for div_point in xrange(1, n):
            top = s[:div_point]
            bottom = s[div_point:]
            if all(c == m for c in bottom):
                ans = min(ans, get_min(top, m))
            ans = min(ans, get_min(top, invert(m)) + 1 + get_min(flip(bottom), m))
            ans = min(ans, 1 + get_min(flip(bottom), invert(m)) + 1 + get_min(top, m))

        cache[(s, m)] = ans
        return ans

    return get_min(s, '+')


def main():
    cases = sys.stdin.readlines()[1:]
    for i, s in enumerate(cases):
        print 'Case #%d: %d' % (i + 1, solve(s.strip()))


if __name__ == '__main__':
    main()
