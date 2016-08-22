inp = open('pancakerevenge.in', 'r')
def input():
    return int(inp.readline())
raw_input = inp.readline

out = open('pancakerevenge.out', 'w')

import re

T = input()

for t in range(1, T + 1):
    msg = raw_input().strip()
    msg = msg.rstrip('+')
    if len(msg) == 0:
        out.write("Case #" + str(t) + ": 0\n")
        #print 0
        continue
    msg = ''.join(k * 2 for k in msg)
    ct = 0
    for pt in range(1, len(msg)):
        if msg[pt] != msg[pt - 1]:
            ct += 1
    out.write("Case #" + str(t) + ": " + str(ct + 1) + "\n")
    #print ct + 1

out.close()
