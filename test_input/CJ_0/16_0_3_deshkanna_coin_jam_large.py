import gmpy2
import math
import random
from fractions import gcd

def pollardRho(N):
        if N%2==0:
                return 2
        x = random.randint(1, N-1)
        y = x
        c = random.randint(1, N-1)
        g = 1
        while g==1:
                x = ((x*x)%N+c)%N
                y = ((y*y)%N+c)%N
                y = ((y*y)%N+c)%N
                g = gcd(abs(x-y),N)
        return g


def brent(N):
        if N%2==0:
                return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break

        #if g == N: brent(N)
        #return g
        if g!=N: return g
        else: return brent(N)


print "Case #1: "
count = 0
#for i in range(9, 100, 2):
for i in xrange(2147483649, 4294967296, 2):
    #print i
    l = []
    for j in xrange(2,11):
        b = gmpy2.digits(i,2)
        a = int(b,j)
        if gmpy2.is_prime(a): break
        l.append(a)
    if len(l)==9:
        ll = []
        #print i, l
        for i in xrange(len(l)):
            ll.append(brent(l[i]))
            #ll.append(brent(1029))
            # for j in xrange(2,int(math.sqrt(l[i]))):
            #     if l[i] % j == 0:
            #         ll.append(j)
            #         break
        print b, ' '.join(str(x) for x in ll)
        count += 1
        if count == 500: break
        #print "Case #{}: {}".format(i, o)
