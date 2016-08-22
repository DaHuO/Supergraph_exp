from itertools import product
from primefac import *

N = 6
J = 3

#primes = set(generate_primes(1111111111))

def alln(n):
    for i in product('01', repeat=n-2):
        yield '1'+''.join(i)+'1'

def divisor(n):
    for i in xrange(2,n):
        if n%i == 0:
            return i

print 'Case #1:'
q = 0
for i in alln(N):
    div = []
    #print i
    for b in xrange(2,11):
        n = int(i,b)
        p = pollardRho_brent(n) #williams_pp1(n) #mpqs(n)
        if n == p:
            #print
            break
        else:
            div.append(str(p))
    else:
        #print i,':',
        #for b in xrange(2,11):
        #    n = int(i,b)
            #print b,n
            #div.append(str(divisor(n)))
        #    print n,divisor(n),
        print i,
        print ' '.join(div)
        #print
        q += 1
        if q == J:
            break
