__author__ = 'Arwin'
import collections
fn= 'A-large.in'
f = open( fn )
ansf = open("ans.txt", "w")

def lastw(s):
    n= len(s)
    d = collections.deque()
    d.extend(s[0])
    for i in xrange(1,n):
        if s[i]<d[0]:
            d.append(s[i])
        else:
            d.appendleft(s[i])
    ans= "".join(d)
    return ans

T= int(f.next())
for i in xrange(1,T+1):
    seq= f.next().strip()
    ansf.write( 'Case #{0}: {1}\n'.format(i, lastw(seq)) )

ansf.close()
