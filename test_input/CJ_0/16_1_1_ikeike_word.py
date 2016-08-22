import sys
from collections import deque

stream = sys.stdin

t = int(stream.readline().strip())

for i in range(t):
    s = stream.readline().strip()
    res = deque()
    res.append(s[0])
    for k in s[1:]:
        if ord(k)>=ord(res[0]):
            res.appendleft(k)
        else:
            res.append(k)
    print 'Case #' + str(i+1) + ':', ''.join(res)
