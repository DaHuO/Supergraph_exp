#!/usr/bin/env python
# -*- Encoding: utf-8 -*-

from __future__ import print_function, unicode_literals

import sys

f = sys.stdin
T = int(f.readline())


def solve(word):
    if len(word) == 1:
        return word
    s = [word[0]]
    for c in word[1:]:
        if ord(c) < ord(s[0]):
            s.append(c)
        else:
            s = [c] + s
    return "".join(s)

if __name__ == '__main__':
    for t in range(1, T + 1):
        word = f.readline().strip()
        ans = solve(word)
        print("Case #{}: {}".format(t, ans))
