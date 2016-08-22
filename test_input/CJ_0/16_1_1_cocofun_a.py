#!/usr/bin/python
from collections import deque

T = int(raw_input())

CASE = 1

while T > 0:
    T -= 1
    S = raw_input()

    ret = deque()

    for ch in S:
        if len(ret) == 0: 
            ret.append(ch) 
            continue

        if ord(ch) >= ord(ret[0]):
            ret.appendleft(ch)
        else:
            ret.append(ch)

    ret = ''.join(list(ret))

    print 'Case #%d:' % CASE, ret
    CASE += 1
