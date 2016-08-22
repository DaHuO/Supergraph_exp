#!/usr/bin/env python3
# this is greedy. let's hope it works.

from collections import deque

def solve(S):
    r = deque()
    for c in S:
        if r:
            if c < r[0]:
                r.append(c)
            else:
                r.appendleft(c)
        else:
            r.append(c)
    return ''.join(r)

def main():
    T = int(input())
    for x in range(1, T+1):
        print('Case #%d: %s' % (x, solve(input())))

if __name__ == "__main__":
    main()
