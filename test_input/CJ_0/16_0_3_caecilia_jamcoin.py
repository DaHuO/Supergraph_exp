import itertools
from itertools import chain

def divisor(n):
    for i in chain([2], xrange(3,min(int(n**0.5) +1, 1000), 2)):
        if not n%i:
            return i
    return False
    
N = 32
J = 500
found = 0
print "Case #1:"
for part in itertools.product(['0', '1'], repeat=N-2):
    n = '1' + ''.join(part) + '1'
    divisors = []
    for base in xrange(2, 11):
        d = divisor(int(n,base))
        if not d:
            break
        divisors.append(d)
    if len(divisors) == 9:
        found += 1
        print n, ' '.join(map(str,divisors))
    if found >= J:
        break
        
