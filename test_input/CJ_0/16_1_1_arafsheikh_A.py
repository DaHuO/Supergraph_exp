from itertools import permutations

def get(s, ch):
    return [str(s)+ch, ch+str(s)]
    
def func(l, ch):
    n = []
    for elm in l:
        n.append(get(elm, ch))
    n = [item for sublist in n for item in sublist]
    return n

_t = int(raw_input())
for t in xrange(_t):
    
    s = raw_input()
    curr = []
    curr.append(s[0])
    for x in xrange(len(s)-1):
        curr = func(curr, s[x+1])
    
    curr.sort()
    print "Case #%i:"%(t+1), curr[-1]
        
