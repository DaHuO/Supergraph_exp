#!/usr/bin/python

import sys
from collections import deque


def encode(s):
    r = 0
    for c in s:
        r *= 2
        if c == '+':
            r += 1
    return r


FT = [chr(x) for x in xrange(256)]
FT[ord('-')] = '+'
FT[ord('+')] = '-'
FT = ''.join(FT)

def flip(s, st, end):
    return s[:st] + s[st:end + 1][::-1].translate(FT) + s[end + 1:]



def brute(s):
    D = deque()
    D.append((s, 0))
    seen = set()
    seen.add(encode(s))
    final = '+'*(len(s))
    while D:
        s, steps = D.popleft()
        if s == final:
            return steps
        for f in xrange(0, len(s) + 1):
            fs = flip(s, 0, f)
            es = encode(fs)
            if not es in seen:
                seen.add(es)
                D.append((fs, steps + 1))



T = int(sys.stdin.readline().strip())
for t in xrange(1, T + 1):
    s = sys.stdin.readline().strip()
    print 'Case #%d: %d' % (t, brute(s))
