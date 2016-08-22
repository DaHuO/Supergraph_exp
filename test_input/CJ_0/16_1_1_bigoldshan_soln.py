import sys
from collections import deque
inp = sys.stdin
inp = open("A-large.in","r")
outp = open("out","w")
#outp = sys.stdout

def read_inp():
    return inp.readline().strip()

T = int(read_inp())

for t in xrange(1,T+1):
    S = read_inp()
    
    lw = deque()
    for a in S:
        if len(lw) == 0:
            lw.append(a)
        elif a >= lw[0]:
            lw.appendleft(a)
        else:
            lw.append(a)
    
    outp.write("Case #%d: %s\n"%(t,''.join(lw)))

outp.close()