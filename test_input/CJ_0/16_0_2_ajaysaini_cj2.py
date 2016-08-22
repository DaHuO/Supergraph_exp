import sys

t = int(sys.stdin.readline())
for i in range(1,1+t):
    s = sys.stdin.readline().strip() + '+'
    k = len(s)
    c = s.count('-+') + s.count('+-')
    print('Case #%d: %d'%(i,c))
